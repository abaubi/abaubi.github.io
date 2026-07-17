with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

old_link = 'class="block hover:text-teal-600 transition-colors"'
new_link = 'class="block hover:text-teal-600 transition-colors" onclick="if(window.innerWidth < 1024) toggleSidebar()"'
html = html.replace(old_link, new_link)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
