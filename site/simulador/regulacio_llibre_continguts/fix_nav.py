with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

nav_old = """      <li class="pt-2"><a href="#sec-preguntes-2" class="block hover:text-teal-600 transition-colors font-semibold text-teal-700">Preguntes Capítol 2</a></li>
    </ul>"""

nav_new = """      <li class="pt-2"><a href="#sec-preguntes-2" class="block hover:text-teal-600 transition-colors font-semibold text-teal-700">Preguntes Capítol 2</a></li>
    </ul>

    <ul class="space-y-3 text-sm text-slate-600 hidden chapter-nav" id="nav-menu-3">
      <li><a href="#sec-3-1" class="block hover:text-teal-600 transition-colors" onclick="if(window.innerWidth < 1024) toggleSidebar()">3.1 Motors i variadors</a></li>
      <li><a href="#sec-3-2" class="block hover:text-teal-600 transition-colors" onclick="if(window.innerWidth < 1024) toggleSidebar()">3.2 Vàlvules de procés</a></li>
      <li><a href="#sec-3-3" class="block hover:text-teal-600 transition-colors" onclick="if(window.innerWidth < 1024) toggleSidebar()">3.3 Resistències elèctriques</a></li>
      <li><a href="#sec-3-4" class="block hover:text-teal-600 transition-colors" onclick="if(window.innerWidth < 1024) toggleSidebar()">3.4 Actuació pneumàtica</a></li>
      <li class="pt-2"><a href="#sec-preguntes-3" class="block hover:text-teal-600 transition-colors font-semibold text-teal-700" onclick="if(window.innerWidth < 1024) toggleSidebar()">Preguntes Capítol 3</a></li>
    </ul>"""

if nav_old in html:
    html = html.replace(nav_old, nav_new)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Nav added!")
else:
    print("Nav old NOT FOUND")

