with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS
old_css = """    .sidebar { width: 280px; transition: transform 0.3s ease; }
    .sidebar.collapsed { transform: translateX(-100%); }
    @media (min-width: 1024px) {
      .main-content { margin-left: 280px; transition: margin-left 0.3s ease; }
      .main-content.expanded { margin-left: 0; }
    }"""
new_css = """    .sidebar { width: 280px; transition: transform 0.3s ease; transform: translateX(-100%); }
    .sidebar.open { transform: translateX(0); }
    @media (min-width: 1024px) {
      .sidebar { transform: translateX(0); }
      .sidebar.collapsed { transform: translateX(-100%); }
      .main-content { margin-left: 280px; transition: margin-left 0.3s ease; }
      .main-content.expanded { margin-left: 0; }
    }"""
html = html.replace(old_css, new_css)

# 2. Update sidebar nav classes
old_nav = 'class="sidebar fixed inset-y-0 left-0 bg-white border-r border-slate-200 p-6 hidden lg:block overflow-y-auto z-20 no-print shadow-sm"'
new_nav = 'class="sidebar fixed inset-y-0 left-0 bg-white border-r border-slate-200 p-6 overflow-y-auto z-20 no-print shadow-sm"'
html = html.replace(old_nav, new_nav)

# 3. Update hamburger button classes
old_btn = 'class="text-white hover:text-teal-400 focus:outline-none transition-colors hidden lg:block" title="Amaga/Mostra el menú"'
new_btn = 'class="text-white hover:text-teal-400 focus:outline-none transition-colors" title="Amaga/Mostra el menú"'
html = html.replace(old_btn, new_btn)

# 4. Update JS toggleSidebar
old_js = """    function toggleSidebar() {
      const sidebar = document.getElementById('sidebar');
      const mainContent = document.getElementById('main-content');
      
      sidebar.classList.toggle('collapsed');
      mainContent.classList.toggle('expanded');
    }"""
new_js = """    function toggleSidebar() {
      const sidebar = document.getElementById('sidebar');
      const mainContent = document.getElementById('main-content');
      
      sidebar.classList.toggle('open');
      sidebar.classList.toggle('collapsed');
      mainContent.classList.toggle('expanded');
    }"""
html = html.replace(old_js, new_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
