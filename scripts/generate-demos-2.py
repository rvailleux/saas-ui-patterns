#!/usr/bin/env python3
"""Append demos 21-40 to demos.js."""

DEMOS = {}

# 21. AI Sidebar Persistante
DEMOS['ai-sidebar-persistante'] = {'height': 340, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5}
.container{display:flex;height:100vh}
.main-content{flex:1;padding:24px}
.sidebar{width:280px;background:#16162a;border-left:1px solid #2d2d52;display:flex;flex-direction:column}
.sidebar-header{padding:16px;border-bottom:1px solid #2d2d52;display:flex;align-items:center;gap:8px}
.sidebar-header .star{color:#a78bfa}
.messages{flex:1;overflow:auto;padding:16px;display:flex;flex-direction:column;gap:12px}
.message{max-width:85%;padding:10px 14px;border-radius:12px;font-size:13px}
.message.user{align-self:flex-end;background:#7c3aed;color:#fff}
.message.ai{align-self:flex-start;background:#1e1e35}
.input-area{padding:16px;border-top:1px solid #2d2d52;display:flex;gap:8px}
.input-area input{flex:1;background:#0f0f1a;border:1px solid #2d2d52;border-radius:8px;padding:10px 14px;color:#e2e8f0;outline:none}
.input-area button{background:#7c3aed;border:none;color:#fff;padding:10px 16px;border-radius:8px;cursor:pointer}
</style></head><body>
<div class="container">
<div class="main-content"><h3>Document Editor</h3><p style="color:#94a3b8;margin-top:12px">Your main content here. The AI sidebar persists across navigation.</p></div>
<div class="sidebar">
<div class="sidebar-header"><span class="star">✦</span><span>AI Assistant</span></div>
<div class="messages" id="messages">
<div class="message user">Summarize this doc</div>
<div class="message ai">This document covers project planning, implementation strategies, and deployment timelines.</div>
</div>
<div class="input-area"><input type="text" id="msgInput" placeholder="Ask anything..."><button onclick="send()">Send</button></div>
</div>
</div>
<script>
function send() {
  const input = document.getElementById('msgInput');
  const text = input.value.trim();
  if(!text) return;
  const msgs = document.getElementById('messages');
  msgs.innerHTML += '<div class="message user">'+text+'</div>';
  input.value = '';
  setTimeout(() => {
    msgs.innerHTML += '<div class="message ai">Here is a helpful response about: '+text.substring(0,30)+'...</div>';
    msgs.scrollTop = msgs.scrollHeight;
  }, 600);
}
</script>
</body></html>'''}

# 22. K AI Intent
DEMOS['k-ai-intent'] = {'height': 300, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.palette{background:#16162a;border:1px solid #2d2d52;border-radius:12px;overflow:hidden;max-width:400px;margin:0 auto}
.input-row{display:flex;align-items:center;padding:12px 16px;border-bottom:1px solid #2d2d52}
.input-row input{flex:1;background:transparent;border:none;color:#e2e8f0;font-size:14px;outline:none}
.results{max-height:200px;overflow:auto}
.result-item{display:flex;align-items:center;gap:12px;padding:10px 16px;cursor:pointer}
.result-item:hover,.result-item.selected{background:#1e1e35}
.result-item.ai-first{background:#7c3aed15;border-left:3px solid #7c3aed}
.icon{width:28px;height:28px;background:#7c3aed20;border-radius:6px;display:flex;align-items:center;justify-content:center;color:#a78bfa;font-size:12px}
.name{font-size:13px}
.desc{font-size:11px;color:#64748b}
.ai-badge{font-size:10px;background:#7c3aed;color:#fff;padding:2px 6px;border-radius:4px;margin-left:8px}
</style></head><body>
<div class="palette">
<div class="input-row"><input type="text" id="input" placeholder="Type a command or question..." oninput="filter()"></div>
<div class="results" id="results"></div>
</div>
<p style="text-align:center;color:#94a3b8;margin-top:16px;font-size:12px">Try typing "how to" or a question with "?"</p>
<script>
const cmds = [
  {name:'Open File',key:'⌘P'},
  {name:'Go to Symbol',key:'⌘⇧O'},
  {name:'Command Palette',key:'⌘⇧P'},
  {name:'Find in Files',key:'⌘⇧F'}
];
function filter() {
  const q = document.getElementById('input').value.toLowerCase();
  const isQuestion = q.includes('?') || q.includes('how') || q.includes('what') || q.includes('why');
  let html = '';
  if(q.length > 0 && isQuestion) {
    html += '<div class="result-item ai-first"><div class="icon">✦</div><div><div class="name">Ask AI: "'+q+'"<span class="ai-badge">AI</span></div></div></div>';
  }
  cmds.filter(c => c.name.toLowerCase().includes(q)).forEach(c => {
    html += '<div class="result-item"><div class="icon">⌘</div><div><div class="name">'+c.name+'</div><div class="desc">'+c.key+'</div></div></div>';
  });
  document.getElementById('results').innerHTML = html;
}
filter();
</script>
</body></html>'''}

# 23. Floating AI Button
DEMOS['floating-ai-button-contextuel'] = {'height': 300, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:32px}
.content{line-height:1.8;color:#cbd5e1}
.highlight{background:#7c3aed30;padding:2px 4px;border-radius:4px}
.float-toolbar{position:absolute;display:none;gap:8px;background:#1e1e35;border:1px solid #2d2d52;border-radius:8px;padding:8px;box-shadow:0 4px 12px rgba(0,0,0,0.3)}
.float-btn{background:#7c3aed;border:none;color:#fff;padding:6px 12px;border-radius:6px;cursor:pointer;font-size:12px}
.result-card{display:none;background:#16162a;border:1px solid #2d2d52;border-radius:12px;padding:16px;margin-top:16px;position:relative}
.result-card.show{display:block}
.close-x{position:absolute;top:12px;right:12px;cursor:pointer;color:#64748b}
</style></head><body>
<p class="content" id="text">Select any text in this paragraph to see the floating AI toolbar appear. The <span class="highlight">quick brown fox</span> jumps over the lazy dog. This is a demonstration of contextual AI assistance that appears when you select text, offering options to explain, rewrite, or translate.</p>
<div class="float-toolbar" id="toolbar">
<button class="float-btn" onclick="explain()">Explain</button>
<button class="float-btn" onclick="rewrite()">Rewrite</button>
<button class="float-btn" onclick="translate()">Translate</button>
</div>
<div class="result-card" id="result"><span class="close-x" onclick="closeResult()">×</span><div id="resultText"></div></div>
<script>
document.addEventListener('mouseup', () => {
  const sel = window.getSelection();
  const toolbar = document.getElementById('toolbar');
  if(sel.toString().length > 0) {
    const r = sel.getRangeAt(0).getBoundingClientRect();
    toolbar.style.display = 'flex';
    toolbar.style.left = (r.left + r.width/2 - 60) + 'px';
    toolbar.style.top = (r.top - 50) + 'px';
  } else { toolbar.style.display = 'none'; }
});
function explain() { showResult('Explanation: This phrase is a pangram containing every letter of the alphabet.'); }
function rewrite() { showResult('Rewritten: The speedy auburn fox leaps across the indolent canine.'); }
function translate() { showResult('French: Le renard brun rapide saute par-dessus le chien paresseux.'); }
function showResult(t) { document.getElementById('resultText').textContent = t; document.getElementById('result').classList.add('show'); document.getElementById('toolbar').style.display = 'none'; }
function closeResult() { document.getElementById('result').classList.remove('show'); }
</script>
</body></html>'''}

# 24. Inline Slash AI Commands
DEMOS['inline-slash-ai-commands'] = {'height': 280, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.editor{background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:16px;min-height:120px;outline:none;position:relative}
.menu{position:absolute;background:#1e1e35;border:1px solid #2d2d52;border-radius:8px;box-shadow:0 4px 12px rgba(0,0,0,0.3);display:none;overflow:hidden}
.menu-item{padding:10px 16px;display:flex;align-items:center;gap:12px;cursor:pointer}
.menu-item:hover{background:#2d2d52}
.ai-icon{color:#a78bfa;font-weight:bold}
</style></head><body>
<p style="color:#94a3b8;margin-bottom:12px">Type /ai at the start of a line</p>
<div class="editor" id="editor" contenteditable oninput="checkSlash()"></div>
<div class="menu" id="menu">
<div class="menu-item" onclick="insertAI('summarize')"><span class="ai-icon">✦</span><span>Summarize</span></div>
<div class="menu-item" onclick="insertAI('translate')"><span class="ai-icon">✦</span><span>Translate to English</span></div>
<div class="menu-item" onclick="insertAI('improve')"><span class="ai-icon">✦</span><span>Improve writing</span></div>
</div>
<script>
function checkSlash() {
  const text = document.getElementById('editor').innerText;
  const menu = document.getElementById('menu');
  if(text.endsWith('/ai')) {
    const sel = window.getSelection();
    const rect = sel.getRangeAt(0).getBoundingClientRect();
    menu.style.display = 'block';
    menu.style.left = rect.left + 'px';
    menu.style.top = (rect.bottom + 8) + 'px';
  }
}
function insertAI(type) {
  const ed = document.getElementById('editor');
  const texts = {summarize:'This is a concise summary of your document.',translate:'This is the translated text.',improve:'This is the improved version with better clarity.'};
  let i = 0;
  const txt = texts[type];
  ed.innerText = ed.innerText.replace('/ai', '');
  document.getElementById('menu').style.display = 'none';
  const interval = setInterval(() => {
    ed.innerText += txt[i];
    i++;
    if(i >= txt.length) clearInterval(interval);
  }, 30);
}
</script>
</body></html>'''}

# 25. Streaming Text
DEMOS['streaming-text-typewriter'] = {'height': 280, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.input-row{display:flex;gap:8px;margin-bottom:16px}
input{flex:1;background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:10px 14px;color:#e2e8f0;outline:none}
button{background:#7c3aed;border:none;color:#fff;padding:10px 20px;border-radius:8px;cursor:pointer}
button:disabled{opacity:0.5}
.output{background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:16px;min-height:100px;line-height:1.6}
.cursor{display:inline-block;width:8px;height:16px;background:#a78bfa;animation:blink 1s infinite;margin-left:2px}
@keyframes blink{0%,50%{opacity:1}51%,100%{opacity:0}}
</style></head><body>
<div class="input-row"><input type="text" id="prompt" placeholder="Ask something..." value="Explain quantum computing"><button id="btn" onclick="generate()">Generate</button></div>
<div class="output" id="output"></div>
<script>
let interval;
function generate() {
  const btn = document.getElementById('btn');
  const out = document.getElementById('output');
  btn.disabled = true;
  out.innerHTML = '';
  const text = 'Quantum computing leverages quantum mechanics to process information in ways classical computers cannot. Using qubits that can exist in superposition, quantum computers perform certain calculations exponentially faster.';
  let i = 0;
  interval = setInterval(() => {
    out.innerHTML += text[i];
    i++;
    if(i >= text.length) {
      clearInterval(interval);
      out.innerHTML += '<span class="cursor"></span>';
      btn.disabled = false;
      btn.textContent = 'Stop';
      btn.onclick = () => { clearInterval(interval); btn.textContent = 'Generate'; btn.onclick = generate; };
    }
  }, 30);
}
</script>
</body></html>'''}

# 26. Diff View
DEMOS['diff-view-accept-reject'] = {'height': 340, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:16px}
.toolbar{display:flex;gap:8px;margin-bottom:12px}
.toolbar button{background:#1e1e35;border:1px solid #2d2d52;color:#e2e8f0;padding:6px 12px;border-radius:6px;cursor:pointer;font-size:12px}
.toolbar button:hover{background:#2d2d52}
.diff{background:#16162a;border:1px solid #2d2d52;border-radius:8px;font-family:monospace;font-size:12px;line-height:1.6}
.line{padding:6px 16px;display:flex}
.line.ctx{color:#64748b}
.line.rem{background:#ef444410;color:#ef4444}
.line.add{background:#10b98110;color:#10b981}
.line-num{width:40px;color:#64748b}
.hunk-actions{display:flex;gap:8px;padding:8px 16px;border-bottom:1px solid #2d2d52;background:#1e1e35}
.hunk-btn{font-size:11px;padding:4px 10px;border-radius:4px;cursor:pointer;border:none}
.accept{background:#10b98120;color:#10b981}
.reject{background:#ef444420;color:#ef4444}
</style></head><body>
<div class="toolbar">
<button onclick="acceptAll()">Accept All</button>
<button onclick="rejectAll()">Reject All</button>
</div>
<div class="diff" id="diff">
<div class="hunk-actions"><button class="hunk-btn accept" onclick="acceptHunk(1)">✓ Accept</button><button class="hunk-btn reject" onclick="rejectHunk(1)">✗ Reject</button></div>
<div class="line ctx"><span class="line-num">1</span>function calculateTotal(items) {</div>
<div class="line rem" id="h1-1"><span class="line-num">-</span>  return items.reduce((a,b) => a + b.price, 0);</div>
<div class="line add" id="h1-2"><span class="line-num">+</span>  return items.reduce((a,b) => a + (b.price * b.quantity), 0);</div>
<div class="line ctx"><span class="line-num">4</span>}</div>
</div>
<script>
function acceptHunk(n) { document.getElementById('h1-1').style.opacity='0.3'; document.getElementById('h1-1').style.textDecoration='line-through'; }
function rejectHunk(n) { document.getElementById('h1-2').style.opacity='0.3'; document.getElementById('h1-2').style.textDecoration='line-through'; }
function acceptAll() { acceptHunk(1); }
function rejectAll() { rejectHunk(1); }
</script>
</body></html>'''}

# 27. Ghost Text
DEMOS['ghost-text-inline-autocomplete'] = {'height': 260, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:32px}
.input-wrap{position:relative}
input{width:100%;background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:12px 16px;color:#e2e8f0;font-size:14px;outline:none}
.ghost{position:absolute;left:16px;top:12px;color:#64748b;pointer-events:none;font-size:14px;display:none}
.hint{color:#94a3b8;margin-top:12px;font-size:12px}
</style></head><body>
<div class="input-wrap">
<input type="text" id="input" placeholder="Start typing..." oninput="onInput()" onkeydown="onKey(event)">
<span class="ghost" id="ghost"></span>
</div>
<p class="hint">Type "The quick brown fox" then wait... Press Tab to accept</p>
<script>
const completions = {'The quick brown fox': ' jumps over the lazy dog', 'Machine learning is': ' a subset of artificial intelligence', 'To be or not to be': ' that is the question'};
let currentGhost = '';
let timeout;
function onInput() {
  clearTimeout(timeout);
  document.getElementById('ghost').style.display = 'none';
  const val = document.getElementById('input').value;
  for(let k in completions) {
    if(k.startsWith(val) && val.length > 5) {
      timeout = setTimeout(() => {
        currentGhost = completions[k].substring(val.length - k.length + k.length);
        document.getElementById('ghost').textContent = val + completions[k].substring(val.length);
        document.getElementById('ghost').style.display = 'block';
        document.getElementById('ghost').style.paddingLeft = (val.length * 8.5) + 'px';
      }, 700);
      break;
    }
  }
}
function onKey(e) {
  if(e.key === 'Tab' && currentGhost) {
    e.preventDefault();
    document.getElementById('input').value += currentGhost;
    document.getElementById('ghost').style.display = 'none';
    currentGhost = '';
  }
}
</script>
</body></html>'''}

# 28. Canvas Artifact
DEMOS['canvas-artifact-panel'] = {'height': 340, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5}
.container{display:flex;height:100vh}
.editor{width:50%;display:flex;flex-direction:column}
.editor-header{padding:12px 16px;background:#16162a;border-bottom:1px solid #2d2d52;font-size:12px;color:#94a3b8}
textarea{flex:1;background:#0f0f1a;border:none;padding:16px;color:#e2e8f0;font-family:monospace;font-size:13px;outline:none;resize:none}
.resizer{width:8px;background:#2d2d52;cursor:col-resize}
.resizer:hover{background:#7c3aed}
.preview{flex:1;background:#fff;padding:20px}
.preview iframe{width:100%;height:100%;border:none;background:#fff}
</style></head><body>
<div class="container" id="container">
<div class="editor" id="leftPane">
<div class="editor-header">HTML</div>
<textarea id="code" oninput="updatePreview()"><h1>Hello World</h1>
<p>Edit this HTML to see live preview.</p>
<button>Click me</button></textarea>
</div>
<div class="resizer" id="resizer"></div>
<div class="preview"><iframe id="preview"></iframe></div>
</div>
<script>
let timeout;
function updatePreview() {
  clearTimeout(timeout);
  timeout = setTimeout(() => {
    document.getElementById('preview').srcdoc = document.getElementById('code').value;
  }, 300);
}
updatePreview();
let isResizing = false;
document.getElementById('resizer').addEventListener('mousedown', () => isResizing = true);
document.addEventListener('mouseup', () => isResizing = false);
document.addEventListener('mousemove', (e) => {
  if(!isResizing) return;
  const pct = (e.clientX / window.innerWidth) * 100;
  if(pct > 20 && pct < 80) document.getElementById('leftPane').style.width = pct + '%';
});
</script>
</body></html>'''}

# 29. Mentions
DEMOS['mentions-pour-le-contexte'] = {'height': 280, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.composer{background:#16162a;border:1px solid #2d2d52;border-radius:12px;padding:16px}
textarea{width:100%;background:transparent;border:none;color:#e2e8f0;outline:none;resize:none;height:80px;font-family:inherit}
.mention{color:#a78bfa;background:#7c3aed20;padding:2px 6px;border-radius:4px}
.dropdown{background:#1e1e35;border:1px solid #2d2d52;border-radius:8px;margin-top:8px;overflow:hidden;display:none}
.dropdown.show{display:block}
.user-item{display:flex;align-items:center;gap:12px;padding:10px 16px;cursor:pointer}
.user-item:hover{background:#2d2d52}
.avatar{width:32px;height:32px;background:#7c3aed;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:bold}
</style></head><body>
<div class="composer">
<textarea id="input" placeholder="Type @ to mention someone..." oninput="checkMention()"></textarea>
</div>
<div class="dropdown" id="dropdown">
<div class="user-item" onclick="mention('Alice Smith')"><div class="avatar">AS</div><div><div>Alice Smith</div><div style="font-size:11px;color:#64748b">Engineer</div></div></div>
<div class="user-item" onclick="mention('Bob Jones')"><div class="avatar">BJ</div><div><div>Bob Jones</div><div style="font-size:11px;color:#64748b">Designer</div></div></div>
<div class="user-item" onclick="mention('Carol White')"><div class="avatar">CW</div><div><div>Carol White</div><div style="font-size:11px;color:#64748b">Manager</div></div></div>
</div>
<script>
function checkMention() {
  const val = document.getElementById('input').value;
  document.getElementById('dropdown').classList.toggle('show', val.endsWith('@'));
}
function mention(name) {
  const input = document.getElementById('input');
  input.value = input.value.replace(/@$/, '') + '@' + name + ' ';
  document.getElementById('dropdown').classList.remove('show');
}
</script>
</body></html>'''}

# 30. Conversation Thread
DEMOS['fil-de-conversation-persistant'] = {'height': 340, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5}
.chat{display:flex;flex-direction:column;height:100vh}
.messages{flex:1;overflow:auto;padding:16px;display:flex;flex-direction:column;gap:12px}
.msg{max-width:80%;padding:12px 16px;border-radius:16px;font-size:13px}
.msg.user{align-self:flex-end;background:#7c3aed;color:#fff;border-bottom-right-radius:4px}
.msg.ai{align-self:flex-start;background:#16162a;border:1px solid #2d2d52;border-bottom-left-radius:4px}
.ai-header{display:flex;align-items:center;gap:8px;margin-bottom:6px;color:#a78bfa;font-size:11px}
.input-area{padding:16px;border-top:1px solid #2d2d52;display:flex;gap:8px}
.input-area input{flex:1;background:#16162a;border:1px solid #2d2d52;border-radius:20px;padding:10px 16px;color:#e2e8f0;outline:none}
.input-area button{background:#7c3aed;border:none;color:#fff;padding:10px 20px;border-radius:20px;cursor:pointer}
</style></head><body>
<div class="chat">
<div class="messages" id="messages">
<div class="msg user">What are the key benefits?</div>
<div class="msg ai"><div class="ai-header">✦ AI Assistant</div>The key benefits include improved efficiency, cost reduction, and enhanced user experience.</div>
</div>
<div class="input-area">
<input type="text" id="msgInput" placeholder="Type a message..." onkeydown="if(event.key==='Enter')send()">
<button onclick="send()">Send</button>
</div>
</div>
<script>
function send() {
  const input = document.getElementById('msgInput');
  const text = input.value.trim();
  if(!text) return;
  const msgs = document.getElementById('messages');
  msgs.innerHTML += '<div class="msg user">'+text+'</div>';
  input.value = '';
  msgs.scrollTop = msgs.scrollHeight;
  setTimeout(() => {
    msgs.innerHTML += '<div class="msg ai"><div class="ai-header">✦ AI Assistant</div>That is an interesting question. Here is my response about that topic.</div>';
    msgs.scrollTop = msgs.scrollHeight;
  }, 800);
}
</script>
</body></html>'''}

# 31. Memory Preferences
DEMOS['memory-pr-f-rences-utilisateur'] = {'height': 300, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.memory-list{display:flex;flex-direction:column;gap:12px;margin-bottom:16px}
.memory-card{background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:12px 16px;display:flex;align-items:center;justify-content:space-between}
.memory-content{display:flex;align-items:center;gap:12px}
.delete-btn{color:#64748b;cursor:pointer;padding:4px}
.delete-btn:hover{color:#ef4444}
.add-row{display:flex;gap:8px}
.add-row input{flex:1;background:#16162a;border:1px solid #2d2d52;border-radius:6px;padding:10px 14px;color:#e2e8f0;outline:none}
.add-row button{background:#7c3aed;border:none;color:#fff;padding:10px 16px;border-radius:6px;cursor:pointer}
</style></head><body>
<div class="memory-list" id="memories">
<div class="memory-card"><div class="memory-content"><span>🌙</span><span>Prefers dark mode</span></div><span class="delete-btn" onclick="remove(this)">×</span></div>
<div class="memory-card"><div class="memory-content"><span>🇫🇷</span><span>Responds in French</span></div><span class="delete-btn" onclick="remove(this)">×</span></div>
<div class="memory-card"><div class="memory-content"><span>📝</span><span>Detailed explanations</span></div><span class="delete-btn" onclick="remove(this)">×</span></div>
</div>
<div class="add-row">
<input type="text" id="newMem" placeholder="Add new memory...">
<button onclick="add()">Add</button>
</div>
<script>
function remove(btn) { btn.parentElement.remove(); }
function add() {
  const input = document.getElementById('newMem');
  const text = input.value.trim();
  if(!text) return;
  const list = document.getElementById('memories');
  const card = document.createElement('div');
  card.className = 'memory-card';
  card.innerHTML = '<div class="memory-content"><span>💡</span><span>'+text+'</span></div><span class="delete-btn" onclick="remove(this)">×</span>';
  list.appendChild(card);
  input.value = '';
}
</script>
</body></html>'''}

# 32. Sources Cited
DEMOS['sources-cit-es-grounding'] = {'height': 300, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.content{line-height:1.8;margin-bottom:24px}
.citation{display:inline-block;background:#7c3aed20;color:#a78bfa;padding:0 6px;border-radius:4px;font-size:11px;cursor:pointer;position:relative}
.citation:hover .tooltip{display:block}
.tooltip{display:none;position:absolute;bottom:100%;left:50%;transform:translateX(-50%);background:#1e1e35;border:1px solid #2d2d52;border-radius:8px;padding:12px;width:220px;margin-bottom:8px;box-shadow:0 4px 12px rgba(0,0,0,0.3);z-index:10}
.tooltip-title{font-weight:500;margin-bottom:4px}
.tooltip-url{font-size:11px;color:#64748b}
.references{margin-top:24px;padding-top:24px;border-top:1px solid #2d2d52}
.ref-title{font-size:11px;text-transform:uppercase;color:#64748b;margin-bottom:12px;letter-spacing:0.5px}
.ref-item{margin-bottom:8px;padding-left:20px;position:relative}
.ref-num{position:absolute;left:0;color:#64748b}
</style></head><body>
<div class="content">
Research shows that sleep quality directly impacts cognitive performance
<span class="citation">[1]<span class="tooltip"><div class="tooltip-title">Sleep and Cognition Study</div><div class="tooltip-url">nature.com/sleep-study</div></span></span>.
Optimal sleep duration is 7-9 hours for adults
<span class="citation">[2]<span class="tooltip"><div class="tooltip-title">WHO Sleep Guidelines</div><div class="tooltip-url">who.int/health-topics</div></span></span>.
</div>
<div class="references">
<div class="ref-title">References</div>
<div class="ref-item"><span class="ref-num">1.</span>Sleep and Cognition: A Meta-Analysis. Nature Neuroscience, 2023.</div>
<div class="ref-item"><span class="ref-num">2.</span>WHO Guidelines on Sleep Health. World Health Organization, 2024.</div>
</div>
</body></html>'''}

# 33. Thinking Reasoning
DEMOS['thinking-reasoning-visible'] = {'height': 280, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.ask-btn{background:#7c3aed;border:none;color:#fff;padding:12px 24px;border-radius:8px;cursor:pointer;font-size:14px;margin-bottom:16px}
.ask-btn:disabled{opacity:0.5}
.thinking{background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:16px;margin-bottom:16px;display:none}
.thinking.show{display:block}
.thinking-header{color:#94a3b8;font-size:12px;margin-bottom:8px;display:flex;align-items:center;gap:8px}
.dot{width:8px;height:8px;background:#7c3aed;border-radius:50%;animation:pulse 1.4s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.3}}
.toggle{color:#a78bfa;cursor:pointer;font-size:12px;margin-top:8px}
.reasoning{display:none;margin-top:12px;padding-top:12px;border-top:1px solid #2d2d52;color:#94a3b8}
.reasoning.show{display:block}
.answer{display:none;line-height:1.6}
.answer.show{display:block}
</style></head><body>
<button class="ask-btn" id="askBtn" onclick="ask()">Ask</button>
<div class="thinking" id="thinking">
<div class="thinking-header"><div class="dot"></div>Thinking...</div>
<div class="toggle" onclick="toggleReasoning()">▶ View reasoning</div>
<div class="reasoning" id="reasoning">1. Analyzing the question... 2. Retrieving relevant facts... 3. Formulating response...</div>
</div>
<div class="answer" id="answer">Here is the answer after careful consideration of all relevant factors.</div>
<script>
function ask() {
  document.getElementById('askBtn').disabled = true;
  document.getElementById('thinking').classList.add('show');
  document.getElementById('answer').classList.remove('show');
  setTimeout(() => {
    document.getElementById('thinking').classList.remove('show');
    document.getElementById('answer').classList.add('show');
    document.getElementById('askBtn').disabled = false;
  }, 2000);
}
function toggleReasoning() { document.getElementById('reasoning').classList.toggle('show'); }
</script>
</body></html>'''}

# 34. Regenerate Variants
DEMOS['regenerate-variantes'] = {'height': 280, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.response-card{background:#16162a;border:1px solid #2d2d52;border-radius:12px;padding:20px;margin-bottom:16px;line-height:1.6}
.variants{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px}
.variant-btn{background:#1e1e35;border:1px solid #2d2d52;color:#e2e8f0;padding:8px 16px;border-radius:6px;cursor:pointer;font-size:12px}
.variant-btn:hover{background:#2d2d52}
.regen-btn{background:#7c3aed;border:none;color:#fff;padding:10px 20px;border-radius:6px;cursor:pointer}
</style></head><body>
<div class="response-card" id="response">The project implementation should prioritize user feedback and iterative development cycles to ensure product-market fit.</div>
<div class="variants">
<button class="variant-btn" onclick="changeVariant('shorter')">↺ Shorter</button>
<button class="variant-btn" onclick="changeVariant('formal')">↺ More formal</button>
<button class="variant-btn" onclick="changeVariant('casual')">↺ More casual</button>
</div>
<button class="regen-btn" onclick="regenerate()">↺ Regenerate</button>
<script>
const variants = {
  shorter: 'Prioritize user feedback and iterate quickly for product-market fit.',
  formal: 'The implementation strategy ought to emphasize user feedback acquisition and iterative developmental methodologies to ascertain optimal product-market alignment.',
  casual: 'Focus on what users say and keep iterating until you find the sweet spot!'
};
function changeVariant(type) { document.getElementById('response').textContent = variants[type]; }
function regenerate() { document.getElementById('response').textContent = 'Here is a fresh take on the project approach with new insights and perspectives.'; }
</script>
</body></html>'''}

# 35. Agentic Step Tracker
DEMOS['agentic-step-tracker'] = {'height': 320, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.stepper{display:flex;flex-direction:column;gap:16px}
.step{display:flex;align-items:flex-start;gap:12px}
.step-icon{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0}
.step.done{background:#10b981}
.step.active{background:#7c3aed;animation:pulse 2s infinite}
.step.pending{background:#2d2d52;color:#64748b}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(124,58,237,0.4)}50%{box-shadow:0 0 0 8px rgba(124,58,237,0)}}
.step-content{flex:1}
.step-title{font-weight:500;margin-bottom:4px}
.step-desc{font-size:12px;color:#94a3b8}
.continue-btn{background:#7c3aed;border:none;color:#fff;padding:12px 24px;border-radius:8px;cursor:pointer;margin-top:16px}
.continue-btn:disabled{opacity:0.5}
</style></head><body>
<div class="stepper" id="stepper">
<div class="step"><div class="step-icon done">✓</div><div class="step-content"><div class="step-title">Searching the web</div><div class="step-desc">Found 15 relevant sources</div></div></div>
<div class="step"><div class="step-icon done">✓</div><div class="step-content"><div class="step-title">Reading documents</div><div class="step-desc">Processed 3 PDFs</div></div></div>
<div class="step"><div class="step-icon active">⟳</div><div class="step-content"><div class="step-title">Analyzing results</div><div class="step-desc">Extracting key insights...</div></div></div>
<div class="step"><div class="step-icon pending">○</div><div class="step-content"><div class="step-title">Writing summary</div></div></div>
<div class="step"><div class="step-icon pending">○</div><div class="step-content"><div class="step-title">Formatting output</div></div></div>
</div>
<button class="continue-btn" id="continueBtn" onclick="advance()">Continue</button>
<script>
let currentStep = 2;
const steps = document.querySelectorAll('.step');
function advance() {
  if(currentStep < steps.length - 1) {
    steps[currentStep].querySelector('.step-icon').classList.remove('active');
    steps[currentStep].querySelector('.step-icon').classList.add('done');
    steps[currentStep].querySelector('.step-icon').textContent = '✓';
    currentStep++;
    steps[currentStep].querySelector('.step-icon').classList.remove('pending');
    steps[currentStep].querySelector('.step-icon').classList.add('active');
    steps[currentStep].querySelector('.step-icon').textContent = '⟳';
  }
  if(currentStep === steps.length - 1) document.getElementById('continueBtn').textContent = 'Complete';
}
</script>
</body></html>'''}

# 36. Confidence Signal
DEMOS['confidence-uncertainty-signal'] = {'height': 260, 'html': '''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.answer{margin-bottom:20px;line-height:1.6}
.confidence{background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:16px}
.conf-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}
.conf-label{font-size:12px;color:#94a3b8}
.conf-value{font-weight:600}
.conf-bar{height:8px;background:#2d2d52;border-radius:4px;overflow:hidden}
.conf-fill{height:100%;transition:width 300ms,background 300ms}
.conf-desc{margin-top:12px;font-size:13px;color:#94a3b8}
.toggle-btn{background:#7c3aed;border:none;color:#fff;padding:8px 16px;border-radius:6px;cursor:pointer;margin-top:16px}
</style>
</head>
<body>
<div class="answer">
The Earth orbits the Sun at an average distance of approximately 93 million miles.
</div>
<div class="confidence">
<div class="conf-header">
<span class="conf-label">Confidence</span>
<span class="conf-value" id="confValue">High</span>
</div>
<div class="conf-bar"><div class="conf-fill" id="confFill" style="width:92%;background:#10b981"></div></div>
<div class="conf-desc" id="confDesc">This is well-established scientific fact.</div>
</div>
<button class="toggle-btn" onclick="toggleConfidence()">Toggle confidence level</button>
<script>
const levels = [
  {value:'High',pct:'92%',color:'#10b981',desc:'This is well-established scientific fact.'},
  {value:'Medium',pct:'61%',color:'#f59e0b',desc:'This is generally accurate but some details may vary.'},
  {value:'Low',pct:'28%',color:'#ef4444',desc:'Please verify this information independently.'}
];
let current = 0;
function toggleConfidence() {
  current = (current + 1) % levels.length;
  const l = levels[current];
  document.getElementById('confValue').textContent = l.value;
  document.getElementById('confFill').style.width = l.pct;
  document.getElementById('confFill').style.background = l.color;
  document.getElementById('confDesc').textContent = l.desc;
}
</script>
</body>
</html>'''
}

# 37. Suggested Prompts
DEMOS['suggested-prompts-quick-actions'] = {'height': 270, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:20px}
.chip{background:#1e1e35;border:1px solid #2d2d52;padding:10px 16px;border-radius:20px;cursor:pointer;font-size:13px;transition:all 150ms}
.chip:hover{background:#2d2d52;border-color:#7c3aed}
.input-area{display:flex;gap:8px}
.input-area input{flex:1;background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:12px 16px;color:#e2e8f0;outline:none}
.input-area button{background:#7c3aed;border:none;color:#fff;padding:12px 20px;border-radius:8px;cursor:pointer}
</style></head><body>
<div class="chips" id="chips">
<div class="chip" onclick="useChip('Summarize this document')">Summarize this</div>
<div class="chip" onclick="useChip('Find action items')">Find action items</div>
<div class="chip" onclick="useChip('Translate to French')">Translate to French</div>
<div class="chip" onclick="useChip('Generate report')">Generate report</div>
</div>
<div class="input-area">
<input type="text" id="input" placeholder="Or type your own...">
<button onclick="send()">Send</button>
</div>
<script>
const suggestions = ['What are the key points?','Compare options','Create timeline','Draft email'];
let sugIdx = 0;
function useChip(text) { document.getElementById('input').value = text; }
function send() {
  const input = document.getElementById('input');
  if(input.value) {
    input.value = '';
    const chips = document.getElementById('chips');
    const chipDivs = chips.querySelectorAll('.chip');
    chipDivs.forEach((c,i) => {
      c.textContent = suggestions[(sugIdx + i) % suggestions.length];
    });
    sugIdx = (sugIdx + 1) % suggestions.length;
  }
}
</script>
</body></html>'''}

# 38. Prompt Templates
DEMOS['prompt-templates'] = {'height': 320, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:20px}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-bottom:16px}
.template-card{background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:16px;cursor:pointer;transition:all 150ms}
.template-card:hover,.template-card.active{background:#1e1e35;border-color:#7c3aed}
.template-icon{font-size:24px;margin-bottom:8px}
.template-name{font-weight:500}
.preview{background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:16px;display:none}
.preview.show{display:block}
.preview-title{font-size:12px;color:#94a3b8;margin-bottom:8px}
.preview-text{font-family:monospace;font-size:12px;line-height:1.6;color:#cbd5e1}
.placeholder{color:#7c3aed;background:#7c3aed20;padding:2px 6px;border-radius:4px}
.use-btn{background:#7c3aed;border:none;color:#fff;padding:10px 20px;border-radius:6px;cursor:pointer;margin-top:12px}
</style></head><body>
<div class="grid">
<div class="template-card" onclick="select(this,'meeting')"><div class="template-icon">📝</div><div class="template-name">Meeting notes</div></div>
<div class="template-card" onclick="select(this,'weekly')"><div class="template-icon">📊</div><div class="template-name">Weekly report</div></div>
<div class="template-card" onclick="select(this,'bug')"><div class="template-icon">🐛</div><div class="template-name">Bug report</div></div>
<div class="template-card" onclick="select(this,'feature')"><div class="template-icon">🚀</div><div class="template-name">Feature spec</div></div>
</div>
<div class="preview" id="preview">
<div class="preview-title">Preview</div>
<div class="preview-text" id="previewText"></div>
<button class="use-btn" onclick="useTemplate()">Use template</button>
</div>
<script>
const templates = {
  meeting: 'Meeting: <span class="placeholder">{title}</span>\nDate: <span class="placeholder">{date}</span>\nAttendees: <span class="placeholder">{names}</span>\n\nAgenda:\n- <span class="placeholder">{item}</span>',
  weekly: 'Weekly Report - <span class="placeholder">{week}</span>\n\nAccomplishments:\n- <span class="placeholder">{ accomplishment }</span>\n\nBlockers:\n- <span class="placeholder">{blocker}</span>',
  bug: 'Bug Report\n\nTitle: <span class="placeholder">{title}</span>\nSeverity: <span class="placeholder">{level}</span>\nSteps to reproduce:\n1. <span class="placeholder">{step}</span>',
  feature: 'Feature Spec: <span class="placeholder">{name}</span>\n\nProblem:\n<span class="placeholder">{description}</span>\n\nSolution:\n<span class="placeholder">{approach}</span>'
};
let selected = null;
function select(card, type) {
  document.querySelectorAll('.template-card').forEach(c => c.classList.remove('active'));
  card.classList.add('active');
  selected = type;
  document.getElementById('previewText').innerHTML = templates[type];
  document.getElementById('preview').classList.add('show');
}
function useTemplate() { alert('Template applied!'); }
</script>
</body></html>'''}

# 39. Multimodal Drop Zone
DEMOS['multimodal-drop-zone'] = {'height': 280, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;padding:24px}
.dropzone{border:2px dashed #2d2d52;border-radius:12px;padding:40px;text-align:center;transition:all 200ms}
.dropzone.dragover{border-color:#7c3aed;background:#7c3aed10}
.dropzone-icon{font-size:48px;margin-bottom:12px}
.dropzone-text{color:#94a3b8;margin-bottom:16px}
.browse-btn{background:#7c3aed;border:none;color:#fff;padding:10px 20px;border-radius:6px;cursor:pointer}
.file-list{margin-top:16px}
.file-item{display:flex;align-items:center;justify-content:space-between;background:#16162a;border:1px solid #2d2d52;border-radius:8px;padding:12px 16px;margin-bottom:8px}
.file-info{display:flex;align-items:center;gap:12px}
.remove{color:#64748b;cursor:pointer}
.remove:hover{color:#ef4444}
</style></head><body>
<div class="dropzone" id="dropzone">
<div class="dropzone-icon">☁️</div>
<div class="dropzone-text">Drop files here or click to browse</div>
<button class="browse-btn" onclick="addFile()">Browse</button>
</div>
<div class="file-list" id="fileList"></div>
<script>
const dropzone = document.getElementById('dropzone');
const files = [{name:'document.pdf',size:'2.3 MB'},{name:'image.png',size:'1.1 MB'}];
['dragenter','dragover','dragleave','drop'].forEach(e => {
  dropzone.addEventListener(e, (ev) => {
    ev.preventDefault();
    if(e === 'dragenter' || e === 'dragover') dropzone.classList.add('dragover');
    else dropzone.classList.remove('dragover');
  });
});
dropzone.addEventListener('drop', (e) => {
  addFile('dropped-file.txt','0.5 MB');
});
function renderFiles() {
  document.getElementById('fileList').innerHTML = files.map((f,i) =>
    '<div class="file-item"><div class="file-info">📄 '+f.name+' <span style="color:#64748b">· '+f.size+'</span></div>'+
    '<span class="remove" onclick="removeFile('+i+')">×</span></div>'
  ).join('');
}
function addFile(name,size) {
  files.push({name:name||'new-file-'+files.length+'.txt',size:size||'0.8 MB'});
  renderFiles();
}
function removeFile(i) { files.splice(i,1); renderFiles(); }
renderFiles();
</script>
</body></html>'''}

# 40. Voice Mode
DEMOS['mode-voix-natif'] = {'height': 300, 'html': '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}body{font-family:system-ui,-apple-system,sans-serif;background:#0f0f1a;color:#e2e8f0;height:100vh;overflow:hidden;font-size:13px;line-height:1.5;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px}
.mic-btn{width:72px;height:72px;border-radius:50%;background:#7c3aed;border:none;color:#fff;font-size:32px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all 200ms;position:relative}
.mic-btn:hover{transform:scale(1.05)}
.mic-btn.recording{background:#ef4444;animation:pulse-ring 2s infinite}
@keyframes pulse-ring{0%{box-shadow:0 0 0 0 rgba(239,68,68,0.4)}70%{box-shadow:0 0 0 20px rgba(239,68,68,0)}100%{box-shadow:0 0 0 0 rgba(239,68,68,0)}}
.waveform{display:flex;align-items:center;gap:4px;height:40px;margin:24px 0;opacity:0;transition:opacity 200ms}
.waveform.show{opacity:1}
.bar{width:4px;background:#7c3aed;border-radius:2px;animation:wave 1s ease-in-out infinite}
.bar:nth-child(2){animation-delay:0.1s}
.bar:nth-child(3){animation-delay:0.2s}
.bar:nth-child(4){animation-delay:0.3s}
.bar:nth-child(5){animation-delay:0.4s}
@keyframes wave{0%,100%{height:20%}50%{height:100%}}
.transcript{max-width:300px;text-align:center;color:#cbd5e1;min-height:60px}
.processing{color:#94a3b8;font-size:12px;margin-top:16px;opacity:0}
.processing.show{opacity:1}
</style></head><body>
<button class="mic-btn" id="micBtn" onclick="toggleRecording()">🎤</button>
<div class="waveform" id="waveform"><div class="bar" style="height:40%"></div><div class="bar" style="height:70%"></div><div class="bar" style="height:100%"></div><div class="bar" style="height:60%"></div><div class="bar" style="height:80%"></div></div>
<div class="transcript" id="transcript">Tap the microphone to start</div>
<div class="processing" id="processing">Processing...</div>
<script>
let recording = false, interval;
const texts = ['The','quick','brown','fox','jumps','over','the','lazy','dog'];
function toggleRecording() {
  recording = !recording;
  document.getElementById('micBtn').classList.toggle('recording', recording);
  document.getElementById('waveform').classList.toggle('show', recording);
  if(recording) {
    document.getElementById('transcript').textContent = '';
    document.getElementById('processing').classList.remove('show');
    let i = 0;
    interval = setInterval(() => {
      if(i < texts.length) {
        document.getElementById('transcript').textContent += (i>0?' ':'') + texts[i];
        i++;
      } else {
        clearInterval(interval);
        document.getElementById('processing').classList.add('show');
      }
    }, 400);
  } else {
    clearInterval(interval);
    document.getElementById('processing').classList.remove('show');
  }
}
</script>
</body></html>'''}

print("Appending demos 21-40...")

# Read existing file, remove closing brace, append new demos
with open('src/_data/demos.js', 'r') as f:
    content = f.read()

# Remove the closing `};`
content = content.rstrip()
if content.endswith('};'):
    content = content[:-2]

# Add comma after last entry if needed
content = content.rstrip()
if not content.endswith(','):
    content += ','

# Append new demos
for slug, demo in DEMOS.items():
    html = demo['html'].replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')
    content += f"\n  '{slug}': {{ height: {demo['height']}, html: `{html}` }},"

# Close the object
content += "\n};\n"

with open('src/_data/demos.js', 'w') as f:
    f.write(content)

print(f"Appended {len(DEMOS)} more demos. Total: 40")
