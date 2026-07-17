with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_js = """      if (chap === '1') {
        title.textContent = 'Capítol 1: Introducció als sistemes de mesura i regulació';
        desc.textContent = "Sistemes de mesura, models i principis de l'automàtica";
      } else if (chap === '2') {
        title.textContent = 'Capítol 2: Sensors i condicionadors de senyal';
        desc.textContent = "Instrumentació industrial, senyals estàndard, classificació de sensors i calibratge";
      } else if (chap === '3') {
        title.textContent = 'Capítol 3: Actuadors i preactuadors';
        desc.textContent = "Motors elèctrics, vàlvules de procés, resistències i elements hidràulics/pneumàtics";
      }
      window.scrollTo(0, 0);"""

new_js = """      if (chap === '1') {
        title.textContent = 'Capítol 1: Introducció als sistemes de mesura i regulació';
        desc.textContent = "Sistemes de mesura, models i principis de l'automàtica";
      } else if (chap === '2') {
        title.textContent = 'Capítol 2: Sensors i condicionadors de senyal';
        desc.textContent = "Instrumentació industrial, senyals estàndard, classificació de sensors i calibratge";
      } else if (chap === '3') {
        title.textContent = 'Capítol 3: Actuadors i preactuadors';
        desc.textContent = "Motors elèctrics, vàlvules de procés, resistències i elements hidràulics/pneumàtics";
      }
      document.title = title.textContent;
      window.scrollTo(0, 0);"""

if old_js in html:
    html = html.replace(old_js, new_js)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced!")
else:
    print("Not found!")
