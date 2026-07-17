with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

old_export = re.search(r'function exportarHTML\(\) \{.*?\n    \}', html, re.DOTALL)
if old_export:
    new_export = """function exportarHTML() {
      let activeChap = '1';
      if (!document.getElementById('chapter-2').classList.contains('hidden')) {
        activeChap = '2';
      }
      
      const docClone = document.documentElement.cloneNode(true);
      
      const chapterContents = docClone.querySelectorAll('.chapter-content');
      chapterContents.forEach(chap => {
         const id = chap.getAttribute('id');
         if (id !== `chapter-${activeChap}`) {
            chap.remove();
         } else {
            const sections = chap.querySelectorAll('section');
            sections.forEach(sec => {
               if (!sec.id.startsWith('sec-preguntes')) {
                  sec.remove();
               }
            });
         }
      });
      
      const noPrints = docClone.querySelectorAll('.no-print, .sidebar, header');
      noPrints.forEach(el => el.remove());

      const textareas = docClone.querySelectorAll('textarea');
      textareas.forEach(ta => ta.remove());
      const fallbacks = docClone.querySelectorAll('.print-textarea-fallback');
      fallbacks.forEach(fb => {
         fb.style.display = 'block';
         fb.classList.remove('print-textarea-fallback');
      });

      const printHeaders = docClone.querySelectorAll('.print-header');
      printHeaders.forEach(ph => {
         ph.classList.remove('hidden');
         ph.style.display = 'block';
      });
      const studentGrids = docClone.querySelectorAll('.print-student-grid');
      studentGrids.forEach(grid => {
          grid.classList.remove('hidden');
          grid.style.display = 'grid';
          grid.style.gridTemplateColumns = 'repeat(3, 1fr)';
          grid.style.gap = '20px';
          grid.style.marginBottom = '24px';
      });

      const content = "<!DOCTYPE html>\\n" + docClone.outerHTML;
      const blob = new Blob([content], { type: 'text/html;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `Respostes_Capitol_${activeChap}.html`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }"""
    html = html.replace(old_export.group(0), new_export)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
