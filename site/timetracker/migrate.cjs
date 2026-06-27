const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

html = html.replace('<body>', '<body>\n  <div id="login-screen" style="display:flex; height:100vh; align-items:center; justify-content:center; flex-direction:column; text-align:center;">\n    <h1>TimeTracker</h1>\n    <p style="margin-bottom:20px;">Inicia sessió per continuar</p>\n    <button onclick="loginWithGoogle()" style="padding:12px 24px; font-size:16px;">Iniciar Sessió amb Google</button>\n  </div>\n  <div id="app-container" style="display:none;">');

html = html.replace('</body>', '  </div>\n</body>');

html = html.replace('Agustí Baubí - abaubi@gmail.com', '<span id="user-email"></span> | <a href="#" onclick="logout(); return false;" style="color:var(--text-muted); text-decoration:underline;">Surt</a>');

const firebaseConfig = require('./firebase-applet-config.json');

const fbCode = [
  '<script type="module">',
  '  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";',
  '  import { getAuth, signInWithPopup, GoogleAuthProvider, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js";',
  '  import { getFirestore, collection, getDocs, setDoc, doc, deleteDoc, writeBatch } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js";',
  '',
  '  const firebaseConfig = ' + JSON.stringify(firebaseConfig) + ';',
  '',
  '  const app = initializeApp(firebaseConfig);',
  '  const auth = getAuth(app);',
  '  const db = getFirestore(app, firebaseConfig.firestoreDatabaseId || "(default)");',
  '  const provider = new GoogleAuthProvider();',
  '',
  '  window.currentUser = null;',
  '',
  '  window.loginWithGoogle = () => {',
  '    signInWithPopup(auth, provider).catch(error => console.error("Error logging in:", error));',
  '  };',
  '',
  '  window.logout = () => {',
  '    signOut(auth).catch(error => console.error("Error logging out:", error));',
  '  };',
  '',
  '  onAuthStateChanged(auth, async (user) => {',
  '    if (user) {',
  '      window.currentUser = user;',
  '      document.getElementById("login-screen").style.display = "none";',
  '      document.getElementById("app-container").style.display = "block";',
  '      document.getElementById("user-email").textContent = user.email;',
  '      ',
  '      await window.loadFirebaseData();',
  '    } else {',
  '      window.currentUser = null;',
  '      document.getElementById("login-screen").style.display = "flex";',
  '      document.getElementById("app-container").style.display = "none";',
  '    }',
  '  });',
  '',
  '  window.syncToFirebase = async (collectionName, dataArray) => {',
  '    if (!window.currentUser) return;',
  '    try {',
  '      const batch = writeBatch(db);',
  '      const snapshot = await getDocs(collection(db, collectionName));',
  '      snapshot.forEach(docSnap => {',
  '        if (docSnap.data().uid === window.currentUser.uid) {',
  '          batch.delete(docSnap.ref);',
  '        }',
  '      });',
  '      for (const item of dataArray) {',
  '        const docData = { ...item, uid: window.currentUser.uid };',
  '        const docRef = doc(db, collectionName, item.id || Math.random().toString(36).substr(2, 9));',
  '        batch.set(docRef, docData);',
  '      }',
  '      await batch.commit();',
  '    } catch(e) {',
  '      console.error("Error syncing " + collectionName + " to Firebase:", e);',
  '    }',
  '  };',
  '  ',
  '  window.loadFirebaseData = async () => {',
  '    if (!window.currentUser) return;',
  '    try {',
  '      const loadColl = async (collName) => {',
  '        const snap = await getDocs(collection(db, collName));',
  '        const arr = [];',
  '        snap.forEach(d => {',
  '          const data = d.data();',
  '          if (data.uid === window.currentUser.uid) arr.push(data);',
  '        });',
  '        return arr;',
  '      };',
  '      ',
  '      const projects = await loadColl("projects");',
  '      const tasks = await loadColl("tasks");',
  '      const activeTimers = await loadColl("activeTimers");',
  '      const records = await loadColl("records");',
  '      ',
  '      window.updateLocalVariables(projects, tasks, activeTimers, records);',
  '      ',
  '      if(window.render) window.render();',
  '    } catch(e) {',
  '      console.error("Error loading from Firebase:", e);',
  '    }',
  '  };',
  '</script>'
].join('\n');

html = html.replace('</head>', fbCode + '\n</head>');

const oldSaveStateRegex = /const saveState = \(\) => \{[\s\S]*?render\(\);\s*\};/;
const newSaveStateCode = [
  'const saveState = () => {',
  '  if(window.syncToFirebase && window.currentUser) {',
  '    window.syncToFirebase("projects", projects);',
  '    window.syncToFirebase("tasks", tasks);',
  '    window.syncToFirebase("activeTimers", activeTimers);',
  '    window.syncToFirebase("records", records);',
  '  } else {',
  '    localStorage.setItem("projects", JSON.stringify(projects));',
  '    localStorage.setItem("tasks", JSON.stringify(tasks));',
  '    localStorage.setItem("activeTimers", JSON.stringify(activeTimers));',
  '    localStorage.setItem("records", JSON.stringify(records));',
  '  }',
  '  if(typeof render !== "undefined") render();',
  '};',
  '',
  'window.updateLocalVariables = (p, t, a, r) => {',
  '  projects = p;',
  '  tasks = t;',
  '  activeTimers = a;',
  '  records = r;',
  '};',
  '',
  'window.render = render;'
].join('\n');

html = html.replace(oldSaveStateRegex, newSaveStateCode);

fs.writeFileSync('index.html', html);
console.log("Migration complete.");
