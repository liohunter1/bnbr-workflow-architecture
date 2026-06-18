import os, glob

folder = r'C:\Users\le\OneDrive\Desktop\hanns docs\BNBR_Workflow_Architecture'
files = sorted(glob.glob(os.path.join(folder, '*.md')))

diagrams = []
for f in files:
    name = os.path.basename(f)
    with open(f, encoding='utf-8') as fh:
        content = fh.read()
    parts = content.split('```mermaid')
    for idx, part in enumerate(parts[1:], 1):
        end = part.find('```')
        if end != -1:
            code = part[:end].strip()
            title = name.replace('.md','').replace('_',' ').strip()
            # Get first H1 or H2 from file as friendly title
            for line in content.split('\n'):
                if line.startswith('# '):
                    title = line.replace('# ','').strip()
                    break
            label = f"{title} (Diagram {idx})" if len(parts) > 2 else title
            diagrams.append((label, code))

nav_items = ''
for i, (title, _) in enumerate(diagrams):
    short = title[:42] + '…' if len(title) > 42 else title
    nav_items += f'<li><a href="#diag{i}" onclick="setActive(this)">{short}</a></li>\n'

cards = ''
for i, (title, code) in enumerate(diagrams):
    cards += f'''<section class="card" id="diag{i}">
  <div class="card-header">
    <span class="card-icon">&#x25A6;</span>
    <h2>{title}</h2>
    <button class="zoom-btn" onclick="toggleZoom(this)" title="Toggle fit/scroll">&#x26F6; Fit</button>
  </div>
  <div class="diagram-wrap">
    <div class="mermaid">{code}</div>
  </div>
</section>\n'''

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BNBR ApprovalMax Workflow Architecture</title>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

  :root {{
    --bg: #0d0f18;
    --surface: #151824;
    --surface2: #1c2033;
    --border: #252840;
    --accent: #4f8ef7;
    --accent2: #f0c040;
    --text: #dde3f0;
    --text-muted: #6b7494;
    --success: #2ecc71;
    --danger: #e74c3c;
    --sidebar-w: 260px;
    --header-h: 58px;
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    font-family: 'Inter', -apple-system, sans-serif;
    background: var(--bg);
    color: var(--text);
    display: flex;
    flex-direction: column;
    height: 100vh;
    overflow: hidden;
  }}

  /* ── TOP HEADER ── */
  header {{
    height: var(--header-h);
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    padding: 0 20px;
    gap: 14px;
    flex-shrink: 0;
    z-index: 100;
  }}
  .logo {{
    width: 32px; height: 32px;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; font-weight: 700; color: #fff; flex-shrink: 0;
  }}
  .header-title {{ flex: 1 }}
  .header-title h1 {{ font-size: .95em; font-weight: 600; color: var(--text); }}
  .header-title p {{ font-size: .72em; color: var(--text-muted); margin-top: 1px; }}
  .header-meta {{
    display: flex; gap: 10px; align-items: center;
  }}
  .badge {{
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 3px 10px;
    font-size: .7em;
    color: var(--text-muted);
  }}
  .badge span {{ color: var(--accent2); font-weight: 600; }}

  /* ── LAYOUT ── */
  .layout {{
    display: flex;
    flex: 1;
    overflow: hidden;
  }}

  /* ── SIDEBAR ── */
  aside {{
    width: var(--sidebar-w);
    background: var(--surface);
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
    overflow: hidden;
  }}
  .sidebar-search {{
    padding: 12px;
    border-bottom: 1px solid var(--border);
  }}
  .sidebar-search input {{
    width: 100%;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 7px 10px;
    color: var(--text);
    font-size: .78em;
    font-family: inherit;
    outline: none;
  }}
  .sidebar-search input:focus {{ border-color: var(--accent); }}
  .sidebar-search input::placeholder {{ color: var(--text-muted); }}

  .sidebar-label {{
    padding: 10px 14px 6px;
    font-size: .65em;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: .08em;
    border-bottom: 1px solid var(--border);
  }}

  nav ul {{
    list-style: none;
    overflow-y: auto;
    flex: 1;
    padding: 6px 0;
  }}
  nav ul li a {{
    display: block;
    padding: 8px 14px;
    font-size: .75em;
    color: var(--text-muted);
    text-decoration: none;
    border-left: 3px solid transparent;
    transition: all .15s;
    line-height: 1.4;
  }}
  nav ul li a:hover {{
    color: var(--text);
    background: var(--surface2);
    border-left-color: var(--accent);
  }}
  nav ul li a.active {{
    color: var(--accent);
    background: rgba(79,142,247,.08);
    border-left-color: var(--accent);
    font-weight: 500;
  }}
  .sidebar-counter {{
    padding: 10px 14px;
    border-top: 1px solid var(--border);
    font-size: .68em;
    color: var(--text-muted);
    text-align: center;
  }}

  /* ── MAIN CONTENT ── */
  main {{
    flex: 1;
    overflow-y: auto;
    padding: 24px;
    scroll-behavior: smooth;
  }}

  .welcome {{
    background: linear-gradient(135deg, rgba(79,142,247,.12), rgba(240,192,64,.08));
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 16px;
  }}
  .welcome-icon {{ font-size: 2em; }}
  .welcome-text h2 {{ font-size: .95em; font-weight: 600; color: var(--accent2); }}
  .welcome-text p {{ font-size: .78em; color: var(--text-muted); margin-top: 4px; line-height: 1.5; }}

  /* ── DIAGRAM CARDS ── */
  .card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    margin-bottom: 24px;
    overflow: hidden;
    scroll-margin-top: 20px;
  }}
  .card:hover {{
    border-color: rgba(79,142,247,.4);
    box-shadow: 0 4px 24px rgba(79,142,247,.08);
    transition: all .2s;
  }}
  .card-header {{
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 14px 18px;
    background: var(--surface2);
    border-bottom: 1px solid var(--border);
  }}
  .card-icon {{
    font-size: 1.1em;
    color: var(--accent);
    flex-shrink: 0;
  }}
  .card-header h2 {{
    flex: 1;
    font-size: .85em;
    font-weight: 600;
    color: var(--text);
  }}
  .zoom-btn {{
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 5px;
    color: var(--text-muted);
    font-size: .7em;
    padding: 4px 10px;
    cursor: pointer;
    font-family: inherit;
    transition: all .15s;
  }}
  .zoom-btn:hover {{ color: var(--accent); border-color: var(--accent); }}

  .diagram-wrap {{
    padding: 16px;
    background: var(--bg);
    overflow-x: auto;
  }}
  .diagram-wrap.fit .mermaid svg {{
    max-width: 100% !important;
    width: 100% !important;
    height: auto !important;
  }}
  .mermaid {{
    background: #fff;
    border-radius: 8px;
    padding: 20px;
    min-height: 80px;
    display: flex;
    justify-content: center;
  }}
  .mermaid svg {{
    max-height: 680px;
  }}

  /* ── SCROLLBAR ── */
  ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
  ::-webkit-scrollbar-track {{ background: var(--bg); }}
  ::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 3px; }}
  ::-webkit-scrollbar-thumb:hover {{ background: #3a3f5a; }}
</style>
</head>
<body>

<header>
  <div class="logo">B</div>
  <div class="header-title">
    <h1>BNBR Kenya &mdash; ApprovalMax Workflow Architecture</h1>
    <p>Document Ref: BNBR/FIN/AMWP/001/2026 &nbsp;|&nbsp; Effective: 1 April 2026 &nbsp;|&nbsp; Integrated with Xero</p>
  </div>
  <div class="header-meta">
    <div class="badge">Diagrams: <span>{len(diagrams)}</span></div>
    <div class="badge">Version <span>1.0</span></div>
  </div>
</header>

<div class="layout">
  <aside>
    <div class="sidebar-search">
      <input type="text" id="searchInput" placeholder="&#x1F50D; Search diagrams..." oninput="filterNav(this.value)">
    </div>
    <div class="sidebar-label">Workflow Diagrams</div>
    <nav>
      <ul id="navList">
        {nav_items}
      </ul>
    </nav>
    <div class="sidebar-counter">BNBR/FIN/AMWP/001/2026 &mdash; All data from source documents</div>
  </aside>

  <main id="mainContent">
    <div class="welcome">
      <div class="welcome-icon">&#x1F4CA;</div>
      <div class="welcome-text">
        <h2>BNBR ApprovalMax Workflow Architecture Package</h2>
        <p>All {len(diagrams)} workflow diagrams sourced exclusively from the BNBR Workflow Plan Extract (7 May 2026) and Staff List (22 May 2026). Use the sidebar to navigate. Click <strong>&#x26F6; Fit</strong> on any diagram to toggle between fit-to-screen and full-scroll view.</p>
      </div>
    </div>

    {cards}
  </main>
</div>

<script>
  mermaid.initialize({{
    startOnLoad: true,
    theme: 'default',
    flowchart: {{ useMaxWidth: true, htmlLabels: true, curve: 'stepBefore' }},
    fontSize: 13,
    fontFamily: 'Inter, sans-serif'
  }});

  // Active nav on scroll
  const sections = document.querySelectorAll('section.card');
  const navLinks = document.querySelectorAll('nav a');

  window.setActive = function(el) {{
    navLinks.forEach(a => a.classList.remove('active'));
    el.classList.add('active');
  }};

  const observer = new IntersectionObserver((entries) => {{
    entries.forEach(entry => {{
      if (entry.isIntersecting) {{
        const id = entry.target.id;
        navLinks.forEach(a => {{
          a.classList.toggle('active', a.getAttribute('href') === '#' + id);
        }});
      }}
    }});
  }}, {{ root: document.getElementById('mainContent'), rootMargin: '-20px 0px -60% 0px' }});

  sections.forEach(s => observer.observe(s));

  // Search filter
  window.filterNav = function(val) {{
    const q = val.toLowerCase();
    document.querySelectorAll('#navList li').forEach(li => {{
      li.style.display = li.textContent.toLowerCase().includes(q) ? '' : 'none';
    }});
  }};

  // Toggle fit
  window.toggleZoom = function(btn) {{
    const wrap = btn.closest('.card').querySelector('.diagram-wrap');
    wrap.classList.toggle('fit');
    btn.textContent = wrap.classList.contains('fit') ? '⛶ Scroll' : '⛶ Fit';
  }};

  // Apply fit by default after render
  mermaid.initialize({{ startOnLoad: false, flowchart: {{ curve: 'stepBefore' }} }});
  document.addEventListener('DOMContentLoaded', () => {{
    mermaid.run().then(() => {{
      document.querySelectorAll('.diagram-wrap').forEach(w => w.classList.add('fit'));
      document.querySelectorAll('.zoom-btn').forEach(b => b.textContent = '⛶ Scroll');
    }});
  }});
</script>
</body>
</html>'''

out = os.path.join(folder, 'BNBR_All_Diagrams.html')
with open(out, 'w', encoding='utf-8') as fh:
    fh.write(html)
print(f'Done: {out}')
print(f'Diagrams: {len(diagrams)}')
