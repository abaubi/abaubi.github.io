with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_css = """      .chapter-content > section:not([id^="sec-preguntes"]) {
        display: none !important;
      }
"""
html = html.replace('      .no-print {', new_css + '      .no-print {')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
