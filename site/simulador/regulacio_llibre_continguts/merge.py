import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('/tmp/chapter2.html', 'r', encoding='utf-8') as f:
    chap2 = f.read()

# 1. Update <style>
style_add = """
    .hidden { display: none !important; }
"""
html = html.replace('</style>', style_add + '</style>')

# 2. Update sidebar
sidebar_old = """    <ul class="space-y-3 text-sm text-slate-600" id="nav-menu">
      <li><a href="#sec-1-1" class="block hover:text-teal-600 transition-colors">1.1 Problemes de control</a></li>
      <li><a href="#sec-1-2" class="block hover:text-teal-600 transition-colors">1.2 Dinàmiques i models</a></li>
      <li><a href="#sec-1-3" class="block hover:text-teal-600 transition-colors">1.3 Definició de sistema</a></li>
      <li><a href="#sec-1-4" class="block hover:text-teal-600 transition-colors">1.4 Aplicacions</a></li>
      <li><a href="#sec-1-5" class="block hover:text-teal-600 transition-colors">1.5 Elements d'un bucle</a></li>
      <li><a href="#sec-1-6" class="block hover:text-teal-600 transition-colors">1.6 Tipologia de variables</a></li>
      <li><a href="#sec-1-7" class="block hover:text-teal-600 transition-colors">1.7 Modelatge matemàtic</a></li>
      <li><a href="#sec-1-8" class="block hover:text-teal-600 transition-colors">1.8 Transformada de Laplace</a></li>
      <li><a href="#sec-1-9" class="block hover:text-teal-600 transition-colors">1.9 Funció de Transferència</a></li>
      <li class="pt-2"><a href="#sec-preguntes" class="block hover:text-teal-600 transition-colors font-semibold text-teal-700">Preguntes</a></li>
    </ul>"""

sidebar_new = """    <div class="mb-6">
      <select id="chapterSelect" onchange="switchChapter(this.value)" class="w-full p-2 border border-slate-300 rounded text-sm text-slate-800 focus:ring-teal-500 focus:border-teal-500 bg-slate-50 cursor-pointer font-bold">
        <option value="1">Capítol 1: Introducció...</option>
        <option value="2">Capítol 2: Sensors i senyals...</option>
      </select>
    </div>
    
    <ul class="space-y-3 text-sm text-slate-600 chapter-nav" id="nav-menu-1">
      <li><a href="#sec-1-1" class="block hover:text-teal-600 transition-colors">1.1 Problemes de control</a></li>
      <li><a href="#sec-1-2" class="block hover:text-teal-600 transition-colors">1.2 Dinàmiques i models</a></li>
      <li><a href="#sec-1-3" class="block hover:text-teal-600 transition-colors">1.3 Definició de sistema</a></li>
      <li><a href="#sec-1-4" class="block hover:text-teal-600 transition-colors">1.4 Aplicacions</a></li>
      <li><a href="#sec-1-5" class="block hover:text-teal-600 transition-colors">1.5 Elements d'un bucle</a></li>
      <li><a href="#sec-1-6" class="block hover:text-teal-600 transition-colors">1.6 Tipologia de variables</a></li>
      <li><a href="#sec-1-7" class="block hover:text-teal-600 transition-colors">1.7 Modelatge matemàtic</a></li>
      <li><a href="#sec-1-8" class="block hover:text-teal-600 transition-colors">1.8 Transformada de Laplace</a></li>
      <li><a href="#sec-1-9" class="block hover:text-teal-600 transition-colors">1.9 Funció de Transferència</a></li>
      <li class="pt-2"><a href="#sec-preguntes-1" class="block hover:text-teal-600 transition-colors font-semibold text-teal-700">Preguntes Capítol 1</a></li>
    </ul>

    <ul class="space-y-3 text-sm text-slate-600 hidden chapter-nav" id="nav-menu-2">
      <li><a href="#sec-2-1" class="block hover:text-teal-600 transition-colors">2.1 Instrumentació industrial</a></li>
      <li><a href="#sec-2-2" class="block hover:text-teal-600 transition-colors">2.2 Senyals estàndard</a></li>
      <li><a href="#sec-2-3" class="block hover:text-teal-600 transition-colors">2.3 Classificació de sensors</a></li>
      <li><a href="#sec-2-4" class="block hover:text-teal-600 transition-colors">2.4 Tractament de senyals</a></li>
      <li><a href="#sec-2-5" class="block hover:text-teal-600 transition-colors">2.5 Tècniques de calibratge</a></li>
      <li class="pt-2"><a href="#sec-preguntes-2" class="block hover:text-teal-600 transition-colors font-semibold text-teal-700">Preguntes Capítol 2</a></li>
    </ul>"""
html = html.replace(sidebar_old, sidebar_new)

# 3. Update header
header_old = """          <div>
            <span class="text-xs font-semibold uppercase tracking-wider text-teal-400">Llibre Digital Interactiu</span>
            <h1 class="text-2xl sm:text-3xl font-bold tracking-tight mt-2">Capítol 1: Introducció als sistemes de mesura i regulació</h1>
            <p class="text-slate-400 text-sm mt-2">Sistemes de mesura, models i principis de l'automàtica</p>
          </div>"""
header_new = """          <div>
            <span class="text-xs font-semibold uppercase tracking-wider text-teal-400">Llibre Digital Interactiu</span>
            <h1 id="header-title" class="text-2xl sm:text-3xl font-bold tracking-tight mt-2">Capítol 1: Introducció als sistemes de mesura i regulació</h1>
            <p id="header-desc" class="text-slate-400 text-sm mt-2">Sistemes de mesura, models i principis de l'automàtica</p>
          </div>"""
html = html.replace(header_old, header_new)

# Update sec-preguntes id to sec-preguntes-1
html = html.replace('id="sec-preguntes"', 'id="sec-preguntes-1"')

# 4. Wrap chap 1 in <div id="chapter-1" class="chapter-content space-y-10">
html = html.replace('<main class="max-w-4xl w-full mx-auto p-6 sm:p-10 space-y-10 flex-grow">\n      \n      <!-- 1.1 -->', '<main class="max-w-4xl w-full mx-auto p-6 sm:p-10 flex-grow">\n      <div id="chapter-1" class="chapter-content space-y-10">\n      <!-- 1.1 -->')

# 5. Insert chap 2 after chap 1
chap1_end = "      </section>\n\n    </main>"
chap2_insert = "      </section>\n      </div>\n" + chap2 + "\n    </main>"
html = html.replace(chap1_end, chap2_insert)

# 6. Update JS
js_old = "const navLinks = document.querySelectorAll('#nav-menu a');"
js_new = "const navLinks = document.querySelectorAll('.chapter-nav a');"
html = html.replace(js_old, js_new)

js_add = """
    // Funció per canviar de capítol
    function switchChapter(chap) {
      document.querySelectorAll('.chapter-content').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.chapter-nav').forEach(el => el.classList.add('hidden'));
      
      document.getElementById('chapter-' + chap).classList.remove('hidden');
      document.getElementById('nav-menu-' + chap).classList.remove('hidden');
      
      const title = document.getElementById('header-title');
      const desc = document.getElementById('header-desc');
      
      if (chap === '1') {
        title.textContent = 'Capítol 1: Introducció als sistemes de mesura i regulació';
        desc.textContent = "Sistemes de mesura, models i principis de l'automàtica";
      } else if (chap === '2') {
        title.textContent = 'Capítol 2: Sensors i condicionadors de senyal';
        desc.textContent = "Instrumentació industrial, senyals estàndard, classificació de sensors i calibratge";
      }
      window.scrollTo(0, 0);
    }
"""
html = html.replace('// Funció per amagar o mostrar el menú lateral', js_add + '\n    // Funció per amagar o mostrar el menú lateral')

export_old = "a.download = 'Capitol1_Regulacio_Automatica.html';"
export_new = "a.download = 'Llibre_Regulacio_Automatica.html';"
html = html.replace(export_old, export_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
