#!/usr/bin/env python3
"""Generate demos.js with 40 interactive HTML demos."""

DEMOS = {}

# 1. Sidebar Collapsible Icon Rail
DEMOS['sidebar-collapsible-icon-rail'] = {
    'height': 300,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5}
.sidebar{position:fixed;left:0;top:0;height:100%;width:200px;background:#16162a;border-right:1px solid #2d2d52;transition:width 200ms ease-in-out;padding:16px 0}
.sidebar.collapsed{width:48px}
.nav-item{display:flex;align-items:center;gap:12px;padding:10px 16px;color:#94a3b8;cursor:pointer;transition:all 150ms}
.nav-item:hover{color:#e2e8f0;background:#1e1e35}
.nav-item svg{width:20px;height:20px;flex-shrink:0}
.nav-item span{white-space:nowrap;opacity:1;transition:opacity 150ms}
.sidebar.collapsed .nav-item span{opacity:0;width:0;overflow:hidden}
.toggle-btn{position:fixed;left:200px;top:16px;width:28px;height:28px;background:#7c3aed;border:none;border-radius:6px;color:#fff;cursor:pointer;transition:left 200ms;z-index:100;display:flex;align-items:center;justify-content:center}
.sidebar.collapsed + .toggle-btn{left:48px}
.content{margin-left:200px;padding:24px;transition:margin-left 200ms}
.sidebar.collapsed ~ .content{margin-left:48px}
</style></head><body>
<div class="sidebar" id="sidebar">
<div class="nav-item"><svg viewBox="0 0 20 20" fill="currentColor"><path d="M3 4a1 1 0 011-1h12a1 1 0 011 1v2a1 1 0 01-1 1H4a1 1 0 01-1-1V4zm0 6a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H4a1 1 0 01-1-1v-6z"/></svg><span>Projects</span></div>
<div class="nav-item"><svg viewBox="0 0 20 20" fill="currentColor"><path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z"/><path fill-rule="evenodd" d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z" clip-rule="evenodd"/></svg><span>Tasks</span></div>
<div class="nav-item"><svg viewBox="0 0 20 20" fill="currentColor"><path d="M2 11a1 1 0 011-1h2a1 1 0 011 1v5a1 1 0 01-1 1H3a1 1 0 01-1-1v-5zM8 7a1 1 0 011-1h2a1 1 0 011 1v9a1 1 0 01-1 1H9a1 1 0 01-1-1V7zM14 4a1 1 0 011-1h2a1 1 0 011 1v12a1 1 0 01-1 1h-2a1 1 0 01-1-1V4z"/></svg><span>Reports</span></div>
<div class="nav-item"><svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd"/></svg><span>Settings</span></div>
</div>
<button class="toggle-btn" onclick="document.getElementById('sidebar').classList.toggle('collapsed')">☰</button>
<div class="content"><h2 style="margin-bottom:16px">Main Content Area</h2><p style="color:#94a3b8">Click the toggle button to collapse/expand the sidebar. The navigation icons remain visible in collapsed mode.</p></div>
</body></html>'''
}

# 2. Top Nav + Contextual Left Panel
DEMOS['top-nav-contextual-left-panel'] = {
    'height': 320,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5}
.top-nav{height:48px;background:#16162a;border-bottom:1px solid #2d2d52;display:flex;align-items:center;padding:0 16px;gap:4px}
.top-tab{padding:8px 16px;border-radius:6px;color:#94a3b8;cursor:pointer;transition:all 150ms}
.top-tab:hover{color:#e2e8f0;background:#1e1e35}
.top-tab.active{background:#7c3aed;color:#fff}
.container{display:flex;height:calc(100vh - 48px)}
.left-panel{width:180px;background:#16162a;border-right:1px solid #2d2d52;padding:16px}
.left-item{padding:8px 12px;border-radius:6px;color:#94a3b8;cursor:pointer;margin-bottom:4px}
.left-item:hover{background:#1e1e35;color:#e2e8f0}
.main-content{flex:1;padding:24px}
.section-title{font-size:18px;font-weight:600;margin-bottom:12px}
</style></head><body>
<div class="top-nav">
<div class="top-tab active" onclick="switchTab('code', this)">Code</div>
<div class="top-tab" onclick="switchTab('issues', this)">Issues</div>
<div class="top-tab" onclick="switchTab('settings', this)">Settings</div>
</div>
<div class="container">
<div class="left-panel" id="leftPanel">
<div class="left-item">src/</div>
<div class="left-item">components/</div>
<div class="left-item">utils/</div>
<div class="left-item">tests/</div>
</div>
<div class="main-content" id="mainContent">
<div class="section-title">Repository Files</div>
<p style="color:#94a3b8">Browse source code, components, and test files.</p>
</div>
</div>
<script>
const panels = {
  code: {items: ['src/','components/','utils/','tests/'], title: 'Repository Files', desc: 'Browse source code, components, and test files.'},
  issues: {items: ['Open','Closed','Labels','Milestones'], title: 'Issues', desc: 'Track bugs and feature requests.'},
  settings: {items: ['General','Security','Integrations','Notifications'], title: 'Project Settings', desc: 'Configure repository settings and integrations.'}
};
function switchTab(tab, el) {
  document.querySelectorAll('.top-tab').forEach(t => t.classList.remove('active'));
  el.classList.add('active');
  const p = panels[tab];
  document.getElementById('leftPanel').innerHTML = p.items.map(i => '<div class="left-item">'+i+'</div>').join('');
  document.getElementById('mainContent').innerHTML = '<div class="section-title">'+p.title+'</div><p style="color:#94a3b8">'+p.desc+'</p>';
}
</script>
</body></html>'''
}

# 3. Breadcrumb Dynamique
DEMOS['breadcrumb-dynamique'] = {
    'height': 280,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.breadcrumb{display:flex;align-items:center;gap:8px;margin-bottom:24px;color:#94a3b8}
.breadcrumb a{color:#a78bfa;text-decoration:none}
.breadcrumb a:hover{text-decoration:underline}
.folder-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.folder-item{background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:16px;cursor:pointer;transition:all 150ms;text-align:center}
.folder-item:hover{background:#1e1e35;border-color:#7c3aed}
.folder-icon{font-size:32px;margin-bottom:8px}
</style></head><body>
<div class="breadcrumb" id="breadcrumb"><a href="#" onclick="goHome()">Home</a></div>
<div class="folder-grid" id="grid"></div>
<script>
const structure = {
  home: {name: 'Home', items: [{id: 'projects', name: 'Projects', icon: '📁'},{id: 'documents', name: 'Documents', icon: '📄'},{id: 'images', name: 'Images', icon: '🖼️'}]},
  projects: {name: 'Projects', parent: 'home', items: [{id: 'webapp', name: 'Web App', icon: '🌐'},{id: 'mobile', name: 'Mobile App', icon: '📱'},{id: 'api', name: 'API Server', icon: '⚙️'}]},
  documents: {name: 'Documents', parent: 'home', items: [{id: 'specs', name: 'Specs', icon: '📋'},{id: 'reports', name: 'Reports', icon: '📊'}]},
  images: {name: 'Images', parent: 'home', items: [{id: 'logos', name: 'Logos', icon: '🎨'},{id: 'screenshots', name: 'Screenshots', icon: '📸'}]}
};
let current = 'home';
function render() {
  const loc = structure[current];
  const path = [];
  let node = current;
  while(node !== 'home') { path.unshift(structure[node].name); node = structure[node].parent; }
  let bc = '<a href="#" onclick="goHome()">Home</a>';
  path.forEach(p => bc += ' <span>›</span> <span>'+p+'</span>');
  document.getElementById('breadcrumb').innerHTML = bc;
  document.getElementById('grid').innerHTML = loc.items.map(i =>
    '<div class="folder-item" onclick="openFolder(\''+i.id+'\')">'+
    '<div class="folder-icon">'+i.icon+'</div><div>'+i.name+'</div></div>'
  ).join('');
}
function openFolder(id) { if(structure[id]) { current = id; render(); } }
function goHome() { current = 'home'; render(); }
render();
</script>
</body></html>'''
}

# 4. Tabs Persistants Pinnable
DEMOS['tabs-persistants-pinnable'] = {
    'height': 270,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5}
.tab-bar{display:flex;align-items:center;background:#16162a;border-bottom:1px solid #2d2d52;padding:8px 8px 0;gap:4px}
.tab{display:flex;align-items:center;gap:6px;padding:8px 12px;background:#1e1e35;border:1px solid #2d2d52;border-bottom:none;border-radius:6px 6px 0 0;cursor:pointer;max-width:140px;min-width:80px}
.tab.active{background:#0f0f1a;border-color:#7c3aed}
.tab.pinned{min-width:auto;padding:8px}
.tab.pinned .tab-title{display:none}
.tab-title{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tab-close{width:16px;height:16px;display:flex;align-items:center;justify-content:center;border-radius:4px;color:#94a3b8}
.tab-close:hover{background:#ef4444;color:#fff}
.tab-pin{width:16px;height:16px;display:flex;align-items:center;justify-content:center;border-radius:4px;color:#94a3b8;opacity:0}
.tab:hover .tab-pin{opacity:1}
.tab.pinned .tab-pin{opacity:1;color:#7c3aed}
.add-tab{width:28px;height:28px;display:flex;align-items:center;justify-content:center;background:#1e1e35;border:1px solid #2d2d52;border-radius:6px;cursor:pointer;color:#94a3b8;margin-left:4px;margin-bottom:8px}
.add-tab:hover{background:#2d2d52}
.content{padding:24px}
</style></head><body>
<div class="tab-bar" id="tabBar"></div>
<button class="add-tab" onclick="addTab()">+</button>
<div class="content" id="content"><h3>Welcome</h3><p style="color:#94a3b8;margin-top:12px">Click + to add tabs. Hover a tab to pin/unpin. Click × to close (pinned tabs cannot be closed).</p></div>
<script>
let tabs = [{id: 1, title: 'index.html', pinned: false, active: true},{id: 2, title: 'styles.css', pinned: true, active: false},{id: 3, title: 'app.js', pinned: false, active: false}];
let nextId = 4;
function render() {
  document.getElementById('tabBar').innerHTML = tabs.map(t =>
    '<div class="tab '+(t.active?'active':'')+(t.pinned?' pinned':'')+'" onclick="activateTab('+t.id+')">'+
    '<span class="tab-pin" onclick="event.stopPropagation();togglePin('+t.id+')">📌</span>'+
    '<span class="tab-title">'+t.title+'</span>'+
    (t.pinned?'':'<span class="tab-close" onclick="event.stopPropagation();closeTab('+t.id+')">×</span>')+
    '</div>'
  ).join('');
  const active = tabs.find(t => t.active);
  if(active) document.getElementById('content').innerHTML = '<h3>'+active.title+'</h3><p style="color:#94a3b8;margin-top:12px">Editing '+active.title+'</p>';
}
function activateTab(id) { tabs.forEach(t => t.active = t.id === id); render(); }
function togglePin(id) { const t = tabs.find(x => x.id === id); if(t) t.pinned = !t.pinned; render(); }
function closeTab(id) { tabs = tabs.filter(t => t.id !== id); if(tabs.length && !tabs.some(t => t.active)) tabs[0].active = true; render(); }
function addTab() { tabs.forEach(t => t.active = false); tabs.push({id: nextId++, title: 'untitled-'+nextId+'.txt', pinned: false, active: true}); render(); }
render();
</script>
</body></html>'''
}

# 5. Right Panel Contextuel
DEMOS['right-panel-contextuel-d-tail'] = {
    'height': 320,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5}
.container{display:flex;height:100vh}
.list{width:200px;background:#16162a;border-right:1px solid #2d2d52;padding:16px}
.list-item{padding:12px;border-radius:6px;cursor:pointer;margin-bottom:8px;color:#94a3b8}
.list-item:hover{background:#1e1e35;color:#e2e8f0}
.main{flex:1;padding:24px}
.right-panel{position:fixed;right:0;top:0;width:300px;height:100%;background:#16162a;border-left:1px solid #2d2d52;padding:20px;transform:translateX(100%);transition:transform 200ms ease-out}
.right-panel.open{transform:translateX(0)}
.panel-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px}
.close-btn{width:28px;height:28px;border-radius:6px;background:#1e1e35;border:none;color:#94a3b8;cursor:pointer}
.close-btn:hover{background:#2d2d52}
</style></head><body>
<div class="container">
<div class="list">
<div class="list-item" onclick="openPanel('User #1')">User #1</div>
<div class="list-item" onclick="openPanel('User #2')">User #2</div>
<div class="list-item" onclick="openPanel('User #3')">User #3</div>
<div class="list-item" onclick="openPanel('User #4')">User #4</div>
<div class="list-item" onclick="openPanel('User #5')">User #5</div>
</div>
<div class="main"><h3>Select a user</h3><p style="color:#94a3b8;margin-top:12px">Click any user to open the details panel.</p></div>
</div>
<div class="right-panel" id="panel">
<div class="panel-header"><h4 id="panelTitle">Details</h4><button class="close-btn" onclick="closePanel()">×</button></div>
<div id="panelContent"><p style="color:#94a3b8">User information appears here.</p></div>
</div>
<script>
function openPanel(name) {
  document.getElementById('panelTitle').textContent = name;
  document.getElementById('panelContent').innerHTML = '<p><strong>Email:</strong> '+name.toLowerCase().replace(' ','')+'@example.com</p><p style="margin-top:12px"><strong>Role:</strong> Editor</p><p style="margin-top:12px"><strong>Joined:</strong> Jan 2024</p>';
  document.getElementById('panel').classList.add('open');
}
function closePanel() { document.getElementById('panel').classList.remove('open'); }
</script>
</body></html>'''
}

# 6. Split View
DEMOS['split-view-panneau-dual'] = {
    'height': 300,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5}
.container{display:flex;height:100vh;width:100vw}
.pane{overflow:auto;padding:16px}
.pane-left{background:#16162a;width:50%}
.pane-right{background:#0f0f1a;flex:1}
.resizer{width:8px;background:#2d2d52;cursor:col-resize;display:flex;align-items:center;justify-content:center}
.resizer:hover{background:#7c3aed}
.resizer::after{content:"";width:2px;height:24px;background:#4a4a6a;border-radius:1px}
.file-tree{list-style:none}
.file-tree li{padding:6px 0;color:#94a3b8}
.file-tree li::before{content:"📄 "}
.file-tree li.folder::before{content:"📁 "}
.preview-box{background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:20px}
</style></head><body>
<div class="container" id="container">
<div class="pane pane-left" id="leftPane">
<ul class="file-tree">
<li class="folder">src</li>
<li style="padding-left:20px">components</li>
<li style="padding-left:20px">utils</li>
<li class="folder">public</li>
<li>package.json</li>
<li>README.md</li>
</ul>
</div>
<div class="resizer" id="resizer"></div>
<div class="pane pane-right"><div class="preview-box"><h4>Preview</h4><p style="color:#94a3b8;margin-top:12px">Drag the divider to resize panels.</p></div></div>
</div>
<script>
let isResizing = false;
const resizer = document.getElementById('resizer');
const leftPane = document.getElementById('leftPane');
const container = document.getElementById('container');
resizer.addEventListener('mousedown', () => isResizing = true);
document.addEventListener('mouseup', () => isResizing = false);
document.addEventListener('mousemove', (e) => {
  if(!isResizing) return;
  const rect = container.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const pct = (x / rect.width) * 100;
  if(pct > 20 && pct < 80) leftPane.style.width = pct + '%';
});
</script>
</body></html>'''
}

# 7. FAB
DEMOS['floating-action-button-fab'] = {
    'height': 300,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.content{max-width:400px}
.fab-container{position:fixed;bottom:24px;right:24px;display:flex;flex-direction:column;align-items:center;gap:12px}
.fab{width:56px;height:56px;border-radius:50%;background:#7c3aed;color:#fff;border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:24px;box-shadow:0 4px 12px rgba(124,58,237,0.4);transition:transform 150ms}
.fab:hover{transform:scale(1.05)}
.fab-actions{display:flex;flex-direction:column;gap:8px;opacity:0;transform:translateY(10px);transition:all 200ms;pointer-events:none}
.fab-actions.open{opacity:1;transform:translateY(0);pointer-events:auto}
.mini-fab{width:40px;height:40px;border-radius:50%;background:#1e1e35;border:1px solid #2d2d52;color:#e2e8f0;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:16px}
.mini-fab:hover{background:#2d2d52}
</style></head><body>
<div class="content"><h3>Project Files</h3><p style="color:#94a3b8;margin-top:12px">Click the + button to see floating action buttons.</p></div>
<div class="fab-container">
<div class="fab-actions" id="fabActions">
<button class="mini-fab" title="Edit">✏️</button>
<button class="mini-fab" title="Attach">📎</button>
<button class="mini-fab" title="Share">📤</button>
</div>
<button class="fab" id="fab" onclick="toggleFab()">+</button>
</div>
<script>
let open = false;
function toggleFab() {
  open = !open;
  document.getElementById('fabActions').classList.toggle('open', open);
  document.getElementById('fab').textContent = open ? '×' : '+';
  document.getElementById('fab').style.transform = open ? 'rotate(45deg)' : 'rotate(0deg)';
}
document.addEventListener('click', (e) => { if(!e.target.closest('.fab-container') && open) toggleFab(); });
</script>
</body></html>'''
}

# 8. Board View Switcher
DEMOS['board-vue-switcher'] = {
    'height': 320,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:20px}
.view-toggle{display:flex;gap:8px;margin-bottom:20px;background:#16162a;padding:4px;border-radius:8px;width:fit-content}
.view-btn{padding:8px 16px;border-radius:6px;border:none;background:transparent;color:#94a3b8;cursor:pointer;display:flex;align-items:center;gap:6px}
.view-btn.active{background:#7c3aed;color:#fff}
.board{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.column{background:#16162a;border-radius:8px;padding:12px}
.column-header{font-weight:600;margin-bottom:12px;padding-bottom:8px;border-bottom:1px solid #2d2d52}
.card{background:#1e1e35;border:1px solid #2d2d52;border-radius:6px;padding:12px;margin-bottom:8px}
.list{display:none}
.list-item{background:#16162a;border:1px solid #2d2d52;border-radius:6px;padding:12px;margin-bottom:8px;display:flex;justify-content:space-between}
.list-item .tag{font-size:11px;padding:2px 8px;background:#7c3aed20;color:#a78bfa;border-radius:4px}
</style></head><body>
<div class="view-toggle">
<button class="view-btn active" onclick="setView('board', this)">▦ Board</button>
<button class="view-btn" onclick="setView('list', this)">≡ List</button>
</div>
<div class="board" id="boardView">
<div class="column"><div class="column-header">Todo</div><div class="card">Fix login bug</div><div class="card">Update docs</div></div>
<div class="column"><div class="column-header">Doing</div><div class="card">Redesign homepage</div><div class="card">API integration</div></div>
<div class="column"><div class="column-header">Done</div><div class="card">Setup CI/CD</div><div class="card">Write tests</div></div>
</div>
<div class="list" id="listView">
<div class="list-item"><span>Fix login bug</span><span class="tag">Todo</span></div>
<div class="list-item"><span>Update docs</span><span class="tag">Todo</span></div>
<div class="list-item"><span>Redesign homepage</span><span class="tag">Doing</span></div>
<div class="list-item"><span>API integration</span><span class="tag">Doing</span></div>
<div class="list-item"><span>Setup CI/CD</span><span class="tag">Done</span></div>
<div class="list-item"><span>Write tests</span><span class="tag">Done</span></div>
</div>
<script>
function setView(view, btn) {
  document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById('boardView').style.display = view === 'board' ? 'grid' : 'none';
  document.getElementById('listView').style.display = view === 'list' ? 'block' : 'none';
}
</script>
</body></html>'''
}

# 9. Command Palette
DEMOS['command-palette-k'] = {
    'height': 300,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.palette{background:#16162a;border:1px solid #2d2d52;border-radius:12px;overflow:hidden;max-width:400px;margin:0 auto}
.input-row{display:flex;align-items:center;padding:12px 16px;border-bottom:1px solid #2d2d52}
.input-row input{flex:1;background:transparent;border:none;color:#e2e8f0;font-size:14px;outline:none}
.input-row input::placeholder{color:#64748b}
.cmd-badge{background:#1e1e35;padding:2px 8px;border-radius:4px;font-size:12px;color:#94a3b8}
.results{max-height:240px;overflow:auto}
.result-item{display:flex;align-items:center;gap:12px;padding:10px 16px;cursor:pointer}
.result-item:hover,.result-item.selected{background:#1e1e35}
.result-item.selected .shortcut{opacity:1}
.icon{width:28px;height:28px;background:#7c3aed20;border-radius:6px;display:flex;align-items:center;justify-content:center;color:#a78bfa;font-size:12px}
.info{flex:1}
.name{font-size:13px}
.desc{font-size:11px;color:#64748b}
.shortcut{opacity:0;color:#94a3b8;font-size:11px}
.status{padding:12px 16px;color:#a78bfa;font-size:13px;border-top:1px solid #2d2d52}
</style></head><body>
<div class="palette">
<div class="input-row"><input type="text" id="input" placeholder="Search commands..." oninput="filter()" onkeydown="nav(event)"><span class="cmd-badge">⌘K</span></div>
<div class="results" id="results"></div>
<div class="status" id="status">↑↓ to navigate, ↵ to select</div>
</div>
<script>
const cmds = [
  {id:1,name:'Open File',desc:'Quick open any file',key:'⌘P'},
  {id:2,name:'Command Palette',desc:'Access all commands',key:'⌘⇧P'},
  {id:3,name:'Go to Symbol',desc:'Navigate to any symbol',key:'⌘⇧O'},
  {id:4,name:'Find in Files',desc:'Search across workspace',key:'⌘⇧F'},
  {id:5,name:'Settings',desc:'Open settings',key:'⌘,'}
];
let sel = 0;
function render(items) {
  document.getElementById('results').innerHTML = items.map((c,i) =>
    '<div class="result-item '+(i===sel?'selected':'')+'" onclick="select('+c.id+')">'+
    '<div class="icon">'+c.id+'</div><div class="info"><div class="name">'+c.name+'</div>'+
    '<div class="desc">'+c.desc+'</div></div><div class="shortcut">'+c.key+'</div></div>'
  ).join('');
}
function filter() {
  const q = document.getElementById('input').value.toLowerCase();
  const items = cmds.filter(c => c.name.toLowerCase().includes(q));
  sel = 0; render(items);
}
function nav(e) {
  const items = document.querySelectorAll('.result-item');
  if(e.key === 'ArrowDown') { sel = Math.min(sel+1,items.length-1); filter(); }
  if(e.key === 'ArrowUp') { sel = Math.max(sel-1,0); filter(); }
  if(e.key === 'Enter') select(cmds[sel]?.id);
}
function select(id) { if(id) document.getElementById('status').textContent = 'Navigating to: ' + cmds.find(c=>c.id===id)?.name; }
render(cmds);
</script>
</body></html>'''
}

# 10. Omnibox
DEMOS['omnibox-unified-search'] = {
    'height': 280,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.search-box{background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:12px 16px;display:flex;align-items:center;gap:12px;margin-bottom:16px}
.search-box input{flex:1;background:transparent;border:none;color:#e2e8f0;outline:none}
.results{background:#16162a;border:1px solid #2d2d52;border-radius:8px;overflow:hidden}
.group-header{background:#1e1e35;padding:8px 16px;font-size:11px;text-transform:uppercase;color:#64748b;letter-spacing:0.5px}
.result-item{display:flex;align-items:center;gap:12px;padding:10px 16px;cursor:pointer;border-bottom:1px solid #2d2d52}
.result-item:last-child{border-bottom:none}
.result-item:hover{background:#1e1e35}
.avatar{width:28px;height:28px;background:#7c3aed;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:11px}
</style></head><body>
<div class="search-box"><span>🔍</span><input type="text" id="input" placeholder="Search anything..." oninput="filter()"></div>
<div class="results" id="results"></div>
<script>
const data = [
  {type:'Pages',items:[{name:'Homepage',sub:'/home'},{name:'Dashboard',sub:'/dashboard'}]},
  {type:'People',items:[{name:'Alice Smith',sub:'Engineer'},{name:'Bob Jones',sub:'Designer'}]},
  {type:'Files',items:[{name:'Report.pdf',sub:'2MB'},{name:'Design.fig',sub:'15MB'}]}
];
function render() {
  let html = '';
  data.forEach(g => {
    html += '<div class="group-header">'+g.type+'</div>';
    g.items.forEach(i => {
      html += '<div class="result-item"><div class="avatar">'+i.name[0]+'</div><div><div>'+i.name+'</div><div style="font-size:11px;color:#64748b">'+i.sub+'</div></div></div>';
    });
  });
  document.getElementById('results').innerHTML = html;
}
function filter() {
  const q = document.getElementById('input').value.toLowerCase();
  if(!q) { render(); return; }
  const filtered = data.map(g => ({...g, items: g.items.filter(i => i.name.toLowerCase().includes(q))})).filter(g => g.items.length);
  let html = '';
  filtered.forEach(g => {
    html += '<div class="group-header">'+g.type+'</div>';
    g.items.forEach(i => {
      html += '<div class="result-item"><div class="avatar">'+i.name[0]+'</div><div><div>'+i.name+'</div><div style="font-size:11px;color:#64748b">'+i.sub+'</div></div></div>';
    });
  });
  document.getElementById('results').innerHTML = html || '<div style="padding:20px;text-align:center;color:#64748b">No results</div>';
}
render();
</script>
</body></html>'''
}

# 11. Inline Slash Commands
DEMOS['inline-slash-commands'] = {
    'height': 280,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.editor{background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:16px;min-height:120px;outline:none;position:relative}
.menu{position:absolute;background:#1e1e35;border:1px solid #2d2d52;border-radius:8px;box-shadow:0 4px 12px rgba(0,0,0,0.3);display:none;overflow:hidden}
.menu-item{padding:10px 16px;display:flex;align-items:center;gap:12px;cursor:pointer}
.menu-item:hover{background:#2d2d52}
.menu-item-icon{width:24px;height:24px;background:#7c3aed20;border-radius:4px;display:flex;align-items:center;justify-content:center}
</style></head><body>
<p style="color:#94a3b8;margin-bottom:12px">Type / at the start of a line</p>
<div class="editor" id="editor" contenteditable oninput="checkSlash()" onclick="hideMenu()"></div>
<div class="menu" id="menu">
<div class="menu-item" onclick="insert('Heading')"><div class="menu-item-icon">H</div><div>Heading</div></div>
<div class="menu-item" onclick="insert('Image')"><div class="menu-item-icon">🖼</div><div>Image</div></div>
<div class="menu-item" onclick="insert('Code Block')"><div class="menu-item-icon">{}</div><div>Code Block</div></div>
<div class="menu-item" onclick="insert('Table')"><div class="menu-item-icon">▦</div><div>Table</div></div>
</div>
<script>
function checkSlash() {
  const text = document.getElementById('editor').innerText;
  if(text.endsWith('/')) {
    const sel = window.getSelection();
    const rect = sel.getRangeAt(0).getBoundingClientRect();
    const menu = document.getElementById('menu');
    menu.style.display = 'block';
    menu.style.left = rect.left + 'px';
    menu.style.top = (rect.bottom + 8) + 'px';
  }
}
function hideMenu() { document.getElementById('menu').style.display = 'none'; }
function insert(type) {
  const ed = document.getElementById('editor');
  ed.innerText = ed.innerText.replace(/\/$/, '') + '[' + type + ']';
  hideMenu();
}
</script>
</body></html>'''
}

# 12. Context Menu
DEMOS['contextual-right-click-menu'] = {
    'height': 280,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.file-list{background:#16162a;border:1px solid #2d2d52;border-radius:8px;overflow:hidden}
.file-item{padding:12px 16px;border-bottom:1px solid #2d2d52;cursor:pointer;display:flex;align-items:center;gap:12px}
.file-item:last-child{border-bottom:none}
.file-item:hover{background:#1e1e35}
.context-menu{position:fixed;background:#1e1e35;border:1px solid #2d2d52;border-radius:8px;box-shadow:0 4px 12px rgba(0,0,0,0.3);display:none;min-width:140px;z-index:100}
.ctx-item{padding:10px 16px;cursor:pointer;font-size:13px}
.ctx-item:hover{background:#2d2d52}
.ctx-item.danger{color:#ef4444}
.status{margin-top:12px;color:#94a3b8;font-size:12px}
</style></head><body>
<div class="file-list" id="fileList">
<div class="file-item" oncontextmenu="showMenu(event, 'Document.txt')">📄 Document.txt</div>
<div class="file-item" oncontextmenu="showMenu(event, 'Image.png')">🖼️ Image.png</div>
<div class="file-item" oncontextmenu="showMenu(event, 'Report.pdf')">📊 Report.pdf</div>
<div class="file-item" oncontextmenu="showMenu(event, 'Notes.md')">📝 Notes.md</div>
</div>
<div class="context-menu" id="ctxMenu">
<div class="ctx-item" onclick="action('Open')">Open</div>
<div class="ctx-item" onclick="action('Rename')">Rename</div>
<div class="ctx-item" onclick="action('Duplicate')">Duplicate</div>
<div class="ctx-item danger" onclick="action('Delete')">Delete</div>
</div>
<div class="status" id="status">Right-click a file</div>
<script>
let currentFile = '';
function showMenu(e, file) {
  e.preventDefault();
  currentFile = file;
  const menu = document.getElementById('ctxMenu');
  menu.style.display = 'block';
  menu.style.left = e.pageX + 'px';
  menu.style.top = e.pageY + 'px';
}
function action(a) { document.getElementById('status').textContent = a + ' ' + currentFile; hideMenu(); }
function hideMenu() { document.getElementById('ctxMenu').style.display = 'none'; }
document.addEventListener('click', hideMenu);
</script>
</body></html>'''
}

# 13. Spreadsheet Inline Editing
DEMOS['spreadsheet-like-inline-editing'] = {
    'height': 300,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
table{width:100%;border-collapse:collapse;background:#16162a;border:1px solid #2d2d52;border-radius:8px;overflow:hidden}
th,td{padding:12px 16px;text-align:left;border-bottom:1px solid #2d2d52}
th{background:#1e1e35;color:#94a3b8;font-weight:500}
tr:last-child td{border-bottom:none}
td{cursor:pointer}
td:hover{background:#1e1e35}
td.editing{padding:0}
td input{width:100%;padding:12px 16px;background:#0f0f1a;border:none;color:#e2e8f0;outline:none}
</style></head><body>
<table>
<thead><tr><th>Name</th><th>Status</th><th>Amount</th></tr></thead>
<tbody id="tbody">
<tr><td onclick="edit(this)">Project Alpha</td><td onclick="edit(this)">Active</td><td onclick="edit(this)">$5,000</td></tr>
<tr><td onclick="edit(this)">Project Beta</td><td onclick="edit(this)">Pending</td><td onclick="edit(this)">$3,200</td></tr>
<tr><td onclick="edit(this)">Project Gamma</td><td onclick="edit(this)">Completed</td><td onclick="edit(this)">$8,500</td></tr>
<tr><td onclick="edit(this)">Project Delta</td><td onclick="edit(this)">Active</td><td onclick="edit(this)">$2,100</td></tr>
</tbody>
</table>
<script>
function edit(td) {
  if(td.classList.contains('editing')) return;
  const val = td.textContent;
  td.classList.add('editing');
  td.innerHTML = '<input type="text" value="'+val+'">';
  const input = td.querySelector('input');
  input.focus();
  input.onblur = () => { td.classList.remove('editing'); td.textContent = input.value; };
  input.onkeydown = (e) => { if(e.key === 'Enter') input.blur(); if(e.key === 'Escape') { td.classList.remove('editing'); td.textContent = val; } };
}
</script>
</body></html>'''
}

# 14. Filters Persistants
DEMOS['filtres-persistants-url-encod-s'] = {
    'height': 270,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.filter-bar{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:16px}
.chip{display:flex;align-items:center;gap:6px;background:#1e1e35;border:1px solid #2d2d52;padding:6px 12px;border-radius:20px;font-size:13px}
.chip-close{width:16px;height:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;border-radius:50%}
.chip-close:hover{background:#ef4444}
.add-btn{background:#7c3aed;border:none;color:#fff;padding:6px 12px;border-radius:20px;cursor:pointer;font-size:13px}
.add-btn:hover{background:#6d28d9}
.count{color:#94a3b8;font-size:13px}
.dropdown{display:none;position:absolute;background:#1e1e35;border:1px solid #2d2d52;border-radius:8px;overflow:hidden;margin-top:8px}
.dropdown.show{display:block}
.dropdown-item{padding:10px 16px;cursor:pointer;font-size:13px}
.dropdown-item:hover{background:#2d2d52}
.results{background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:16px}
.item{padding:8px 0;border-bottom:1px solid #2d2d52}
.item:last-child{border-bottom:none}
</style></head><body>
<div class="filter-bar">
<span class="count" id="count">0 filters active</span>
<div id="chips"></div>
<div style="position:relative">
<button class="add-btn" onclick="toggleDropdown()">+ Add Filter</button>
<div class="dropdown" id="dropdown">
<div class="dropdown-item" onclick="addFilter('Status', 'Open')">Status: Open</div>
<div class="dropdown-item" onclick="addFilter('Priority', 'High')">Priority: High</div>
<div class="dropdown-item" onclick="addFilter('Assignee', 'You')">Assignee: You</div>
<div class="dropdown-item" onclick="addFilter('Type', 'Bug')">Type: Bug</div>
</div>
</div>
</div>
<div class="results" id="results">
<div class="item">Issue #123 - Login broken</div>
<div class="item">Issue #124 - Button color wrong</div>
<div class="item">Issue #125 - API timeout</div>
</div>
<script>
let filters = [];
function render() {
  document.getElementById('chips').innerHTML = filters.map((f,i) =>
    '<div class="chip"><span>'+f.key+': '+f.val+'</span><span class="chip-close" onclick="removeFilter('+i+')">×</span></div>'
  ).join('');
  document.getElementById('count').textContent = filters.length + ' filter' + (filters.length!==1?'s':'') + ' active';
}
function addFilter(k,v) { filters.push({key:k,val:v}); render(); toggleDropdown(); }
function removeFilter(i) { filters.splice(i,1); render(); }
function toggleDropdown() { document.getElementById('dropdown').classList.toggle('show'); }
document.addEventListener('click', (e) => { if(!e.target.closest('.add-btn') && !e.target.closest('.dropdown')) document.getElementById('dropdown').classList.remove('show'); });
render();
</script>
</body></html>'''
}

# 15. Virtual Scrolling
DEMOS['virtual-scrolling'] = {
    'height': 320,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.viewport{height:240px;overflow:auto;background:#16162a;border:1px solid #2d2d52;border-radius:8px;position:relative}
.content{position:relative}
.row{position:absolute;height:40px;display:flex;align-items:center;padding:0 16px;border-bottom:1px solid #2d2d52;width:100%}
.row:hover{background:#1e1e35}
.status{color:#94a3b8;font-size:12px;margin-top:8px}
</style></head><body>
<div class="viewport" id="viewport">
<div class="content" id="content"></div>
</div>
<div class="status" id="status">Showing items 1-8 of 1000</div>
<script>
const total = 1000, rowH = 40, viewportH = 240;
const content = document.getElementById('content');
content.style.height = (total * rowH) + 'px';
const viewport = document.getElementById('viewport');
function render() {
  const scrollTop = viewport.scrollTop;
  const start = Math.floor(scrollTop / rowH);
  const count = Math.ceil(viewportH / rowH) + 1;
  const visible = [];
  for(let i = start; i < Math.min(start + count, total); i++) {
    visible.push('<div class="row" style="top:'+(i*rowH)+'px">Item '+(i+1)+'</div>');
  }
  content.innerHTML = visible.join('');
  document.getElementById('status').textContent = 'Showing items '+(start+1)+'-'+(Math.min(start+count,total))+' of '+total;
}
viewport.addEventListener('scroll', render);
render();
</script>
</body></html>'''
}

# 16. Column Resizing
DEMOS['column-resizing-reordering'] = {
    'height': 280,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
table{width:100%;border-collapse:collapse;background:#16162a;border:1px solid #2d2d52;border-radius:8px;overflow:hidden;table-layout:fixed}
th,td{padding:12px 16px;text-align:left;border-bottom:1px solid #2d2d52}
th{background:#1e1e35;position:relative;user-select:none}
.resize-handle{position:absolute;right:0;top:0;bottom:0;width:8px;cursor:col-resize}
.resize-handle:hover{background:#7c3aed}
</style></head><body>
<table>
<thead><tr>
<th style="width:40%">Name<div class="resize-handle" onmousedown="startResize(event, 0)"></div></th>
<th style="width:30%">Role<div class="resize-handle" onmousedown="startResize(event, 1)"></div></th>
<th style="width:30%">Status<div class="resize-handle" onmousedown="startResize(event, 2)"></div></th>
</tr></thead>
<tbody>
<tr><td>Alice Smith</td><td>Engineer</td><td>Active</td></tr>
<tr><td>Bob Jones</td><td>Designer</td><td>Active</td></tr>
<tr><td>Carol White</td><td>Manager</td><td>Offline</td></tr>
</tbody>
</table>
<script>
let resizing = null;
function startResize(e, col) {
  resizing = {col: col, startX: e.pageX, startW: document.querySelectorAll('th')[col].offsetWidth};
}
document.addEventListener('mousemove', (e) => {
  if(!resizing) return;
  const diff = e.pageX - resizing.startX;
  const newW = Math.max(100, resizing.startW + diff);
  document.querySelectorAll('th')[resizing.col].style.width = newW + 'px';
});
document.addEventListener('mouseup', () => resizing = null);
</script>
</body></html>'''
}

# 17. Toast Notification Undo
DEMOS['toast-notification-undo'] = {
    'height': 260,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.item{display:flex;align-items:center;justify-content:space-between;padding:12px 16px;background:#16162a;border:1px solid #2d2d52;border-radius:8px;margin-bottom:8px}
.item.archived{opacity:0.5}
.archive-btn{background:#7c3aed;border:none;color:#fff;padding:6px 12px;border-radius:6px;cursor:pointer;font-size:12px}
.toast{position:fixed;bottom:24px;right:24px;background:#1e1e35;border:1px solid #2d2d52;border-radius:8px;padding:12px 16px;display:flex;align-items:center;gap:12px;box-shadow:0 4px 12px rgba(0,0,0,0.3);transform:translateY(100px);transition:transform 200ms}
.toast.show{transform:translateY(0)}
.undo{color:#a78bfa;cursor:pointer;font-weight:500}
.undo:hover{text-decoration:underline}
.progress{position:absolute;bottom:0;left:0;height:3px;background:#7c3aed;transition:width 3s linear}
</style></head><body>
<div class="item" id="item1"><span>Important Document.pdf</span><button class="archive-btn" onclick="archive()">Archive</button></div>
<div class="toast" id="toast"><span>Item archived</span><span class="undo" onclick="undo()">Undo</span><div class="progress" id="progress"></div></div>
<script>
let archived = false, timeout;
function archive() {
  archived = true;
  document.getElementById('item1').classList.add('archived');
  const toast = document.getElementById('toast');
  const prog = document.getElementById('progress');
  toast.classList.add('show');
  prog.style.width = '100%';
  setTimeout(() => prog.style.width = '0%', 10);
  timeout = setTimeout(() => { toast.classList.remove('show'); }, 3000);
}
function undo() {
  clearTimeout(timeout);
  archived = false;
  document.getElementById('item1').classList.remove('archived');
  document.getElementById('toast').classList.remove('show');
}
</script>
</body></html>'''
}

# 18. Optimistic UI
DEMOS['optimistic-ui'] = {
    'height': 260,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.card{background:#16162a;border:1px solid #2d2d52;border-radius:12px;padding:20px;max-width:300px}
.title{font-weight:600;margin-bottom:8px}
.text{color:#94a3b8;margin-bottom:16px}
.like-btn{display:flex;align-items:center;gap:8px;background:transparent;border:1px solid #2d2d52;padding:8px 16px;border-radius:8px;color:#e2e8f0;cursor:pointer}
.like-btn.liked{background:#ef444420;border-color:#ef4444;color:#ef4444}
.status{margin-top:12px;font-size:12px;color:#10b981;height:16px}
</style></head><body>
<div class="card">
<div class="title">Great Post!</div>
<div class="text">This is an example of optimistic UI updates.</div>
<button class="like-btn" id="likeBtn" onclick="toggleLike()"><span id="heart">🤍</span><span id="count">42</span></button>
<div class="status" id="status"></div>
</div>
<script>
let liked = false, count = 42;
function toggleLike() {
  liked = !liked;
  count += liked ? 1 : -1;
  document.getElementById('likeBtn').classList.toggle('liked', liked);
  document.getElementById('heart').textContent = liked ? '❤️' : '🤍';
  document.getElementById('count').textContent = count;
  document.getElementById('status').textContent = 'Saving...';
  setTimeout(() => document.getElementById('status').textContent = '✓ Saved', 600);
  setTimeout(() => document.getElementById('status').textContent = '', 2000);
}
</script>
</body></html>'''
}

# 19. Empty States
DEMOS['empty-states-actionnables'] = {
    'height': 300,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.empty{text-align:center;padding:40px 20px;transition:opacity 300ms}
.empty-icon{font-size:48px;margin-bottom:16px}
.empty-title{font-size:18px;font-weight:600;margin-bottom:8px}
.empty-desc{color:#94a3b8;margin-bottom:20px}
.empty-btn{background:#7c3aed;border:none;color:#fff;padding:12px 24px;border-radius:8px;cursor:pointer;font-size:14px}
.empty-btn:hover{background:#6d28d9}
.list{display:none}
.list-item{display:flex;align-items:center;gap:12px;padding:12px 16px;background:#16162a;border:1px solid #2d2d52;border-radius:8px;margin-bottom:8px}
</style></head><body>
<div class="empty" id="emptyState">
<div class="empty-icon">📁</div>
<div class="empty-title">No projects yet</div>
<div class="empty-desc">Projects help you organize work by client</div>
<button class="empty-btn" onclick="createProject()">Create first project</button>
</div>
<div class="list" id="projectList">
<div class="list-item">📁 My First Project</div>
<button class="empty-btn" onclick="reset()" style="margin-top:16px">Reset demo</button>
</div>
<script>
function createProject() {
  document.getElementById('emptyState').style.display = 'none';
  document.getElementById('projectList').style.display = 'block';
}
function reset() {
  document.getElementById('emptyState').style.display = 'block';
  document.getElementById('projectList').style.display = 'none';
}
</script>
</body></html>'''
}

# 20. Skeleton Screens
DEMOS['skeleton-screens'] = {
    'height': 300,
    'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.skeleton-card{background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:16px;margin-bottom:12px}
.skeleton-line{height:16px;background:linear-gradient(90deg,#1e1e35 25%,#2d2d52 50%,#1e1e35 75%);background-size:200% 100%;animation:shimmer 1.5s infinite;border-radius:4px;margin-bottom:12px}
.skeleton-line:last-child{margin-bottom:0;width:60%}
@keyframes shimmer{0%{background-position:200% 0}100%{background-position:-200% 0}}
.real-card{background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:16px;margin-bottom:12px;display:none}
.real-title{font-weight:600;margin-bottom:8px}
.real-desc{color:#94a3b8;font-size:13px}
.load-btn{background:#7c3aed;border:none;color:#fff;padding:10px 20px;border-radius:8px;cursor:pointer;margin-bottom:16px}
</style></head><body>
<button class="load-btn" onclick="loadContent()">Load content</button>
<div id="skeletons">
<div class="skeleton-card"><div class="skeleton-line"></div><div class="skeleton-line"></div><div class="skeleton-line"></div></div>
<div class="skeleton-card"><div class="skeleton-line"></div><div class="skeleton-line"></div><div class="skeleton-line"></div></div>
</div>
<div id="realContent">
<div class="real-card"><div class="real-title">Project Alpha</div><div class="real-desc">A new way to manage your tasks</div></div>
<div class="real-card"><div class="real-title">Project Beta</div><div class="real-desc">Collaboration made simple</div></div>
</div>
<script>
function loadContent() {
  document.getElementById('skeletons').style.display = 'none';
  document.getElementById('realContent').style.display = 'block';
  setTimeout(() => {
    document.getElementById('skeletons').style.display = 'block';
    document.getElementById('realContent').style.display = 'none';
  }, 3000);
}
</script>
</body></html>'''
}

# Continue with remaining demos... Let me add them in batches

print("Generating demos.js...")

# Write the file
with open('src/_data/demos.js', 'w') as f:
    f.write("'use strict';\n\nmodule.exports = {\n")
    for slug, demo in DEMOS.items():
        html = demo['html'].replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')
        f.write(f"  '{slug}': {{ height: {demo['height']}, html: `{html}` }},\n")
    f.write("};\n")

print(f"Wrote {len(DEMOS)} demos to src/_data/demos.js")
