with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('/tmp/chapter3.html', 'r', encoding='utf-8') as f:
    chap3 = f.read()

# 1. Update the Select dropdown
select_old = """      <select id="chapterSelect" onchange="switchChapter(this.value)" class="w-full p-2 border border-slate-300 rounded text-sm text-slate-800 focus:ring-teal-500 focus:border-teal-500 bg-slate-50 cursor-pointer font-bold">
        <option value="1">Capítol 1: Introducció...</option>
        <option value="2">Capítol 2: Sensors i senyals...</option>
      </select>"""
select_new = """      <select id="chapterSelect" onchange="switchChapter(this.value)" class="w-full p-2 border border-slate-300 rounded text-sm text-slate-800 focus:ring-teal-500 focus:border-teal-500 bg-slate-50 cursor-pointer font-bold">
        <option value="1">Capítol 1: Introducció...</option>
        <option value="2">Capítol 2: Sensors i senyals...</option>
        <option value="3">Capítol 3: Actuadors...</option>
      </select>"""
html = html.replace(select_old, select_new)

# 2. Add nav-menu-3
nav_old = """      <li class="pt-2"><a href="#sec-preguntes-2" class="block hover:text-teal-600 transition-colors" onclick="if(window.innerWidth < 1024) toggleSidebar()">Preguntes Capítol 2</a></li>
    </ul>"""
nav_new = """      <li class="pt-2"><a href="#sec-preguntes-2" class="block hover:text-teal-600 transition-colors" onclick="if(window.innerWidth < 1024) toggleSidebar()">Preguntes Capítol 2</a></li>
    </ul>

    <ul class="space-y-3 text-sm text-slate-600 hidden chapter-nav" id="nav-menu-3">
      <li><a href="#sec-3-1" class="block hover:text-teal-600 transition-colors" onclick="if(window.innerWidth < 1024) toggleSidebar()">3.1 Motors i variadors</a></li>
      <li><a href="#sec-3-2" class="block hover:text-teal-600 transition-colors" onclick="if(window.innerWidth < 1024) toggleSidebar()">3.2 Vàlvules de procés</a></li>
      <li><a href="#sec-3-3" class="block hover:text-teal-600 transition-colors" onclick="if(window.innerWidth < 1024) toggleSidebar()">3.3 Resistències elèctriques</a></li>
      <li><a href="#sec-3-4" class="block hover:text-teal-600 transition-colors" onclick="if(window.innerWidth < 1024) toggleSidebar()">3.4 Actuació pneumàtica</a></li>
      <li class="pt-2"><a href="#sec-preguntes-3" class="block hover:text-teal-600 transition-colors font-semibold text-teal-700" onclick="if(window.innerWidth < 1024) toggleSidebar()">Preguntes Capítol 3</a></li>
    </ul>"""
html = html.replace(nav_old, nav_new)

# 3. Update switchChapter function
js_old = """      if (chap === '1') {
        title.textContent = 'Capítol 1: Introducció als sistemes de mesura i regulació';
        desc.textContent = "Sistemes de mesura, models i principis de l'automàtica";
      } else if (chap === '2') {
        title.textContent = 'Capítol 2: Sensors i condicionadors de senyal';
        desc.textContent = "Instrumentació industrial, senyals estàndard, classificació de sensors i calibratge";
      }"""
js_new = """      if (chap === '1') {
        title.textContent = 'Capítol 1: Introducció als sistemes de mesura i regulació';
        desc.textContent = "Sistemes de mesura, models i principis de l'automàtica";
      } else if (chap === '2') {
        title.textContent = 'Capítol 2: Sensors i condicionadors de senyal';
        desc.textContent = "Instrumentació industrial, senyals estàndard, classificació de sensors i calibratge";
      } else if (chap === '3') {
        title.textContent = 'Capítol 3: Actuadors i preactuadors';
        desc.textContent = "Motors elèctrics, vàlvules de procés, resistències i elements hidràulics/pneumàtics";
      }"""
html = html.replace(js_old, js_new)

# 4. Insert Chapter 3 HTML
chap2_end = "      </section>\n\n      </div>\n"
chap3_insert = "      </section>\n\n      </div>\n" + chap3 + "\n"
html = html.replace(chap2_end, chap3_insert)

# 5. Update activeChap logic
export_js_old = """      let activeChap = '1';
      if (!document.getElementById('chapter-2').classList.contains('hidden')) {
        activeChap = '2';
      }"""
export_js_new = """      let activeChap = '1';
      if (!document.getElementById('chapter-2').classList.contains('hidden')) {
        activeChap = '2';
      } else if (!document.getElementById('chapter-3').classList.contains('hidden')) {
        activeChap = '3';
      }"""
html = html.replace(export_js_old, export_js_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

