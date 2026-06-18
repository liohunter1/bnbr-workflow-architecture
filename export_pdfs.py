"""
export_pdfs.py
──────────────
Renders every *.md file in the BNBR_Workflow_Architecture folder
as a styled HTML page (Mermaid diagrams included) and exports each
one to a PDF using Playwright's headless Chromium.

Requirements (run once):
    pip install playwright
    playwright install chromium
"""

import asyncio, os, glob, re, pathlib, sys
# Force UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
from playwright.async_api import async_playwright

# ── CONFIG ────────────────────────────────────────────────────────────────────
FOLDER = r'C:\Users\le\OneDrive\Desktop\hanns docs\BNBR_Workflow_Architecture'
OUT_DIR = os.path.join(FOLDER, 'PDF_Exports')
os.makedirs(OUT_DIR, exist_ok=True)

# ── CSS (same dark→white palette from the viewer, but print-friendly) ─────────
PAGE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
  --accent: #2563eb;
  --accent2: #d97706;
  --bg: #ffffff;
  --surface: #f8fafc;
  --surface2: #f1f5f9;
  --border: #e2e8f0;
  --text: #1e293b;
  --text-muted: #64748b;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Inter', -apple-system, sans-serif;
  background: var(--bg);
  color: var(--text);
  padding: 32px 40px;
  font-size: 13px;
  line-height: 1.6;
}

/* ── HEADER BANNER ── */
.doc-header {
  background: linear-gradient(135deg, #1e40af, #7c3aed);
  color: #fff;
  border-radius: 10px;
  padding: 18px 24px;
  margin-bottom: 28px;
  display: flex;
  align-items: center;
  gap: 14px;
}
.doc-header .logo {
  width: 36px; height: 36px;
  background: rgba(255,255,255,0.2);
  border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  font-size: 18px; font-weight: 700;
  flex-shrink: 0;
}
.doc-header .title-block h1 { font-size: 1em; font-weight: 700; }
.doc-header .title-block p  { font-size: 0.72em; opacity: 0.8; margin-top: 2px; }

/* ── MARKDOWN PROSE ── */
h1, h2, h3, h4 { color: var(--text); margin: 22px 0 8px; }
h1 { font-size: 1.35em; border-bottom: 2px solid var(--accent); padding-bottom: 6px; }
h2 { font-size: 1.1em; border-bottom: 1px solid var(--border); padding-bottom: 4px; }
h3 { font-size: 0.95em; }
p  { margin: 8px 0; }
ul, ol { margin: 8px 0 8px 20px; }
li { margin-bottom: 3px; }
code {
  background: var(--surface2);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 1px 5px;
  font-size: 0.88em;
  font-family: 'Courier New', monospace;
}
pre code { display: block; padding: 10px; overflow-x: auto; }
blockquote {
  border-left: 4px solid var(--accent);
  background: var(--surface);
  padding: 10px 16px;
  margin: 12px 0;
  border-radius: 0 6px 6px 0;
  color: var(--text-muted);
}

/* ── TABLES ── */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 16px 0;
  font-size: 0.82em;
}
th {
  background: var(--accent);
  color: #fff;
  padding: 8px 10px;
  text-align: left;
  font-weight: 600;
}
td {
  padding: 7px 10px;
  border-bottom: 1px solid var(--border);
}
tr:nth-child(even) td { background: var(--surface); }
tr:hover td { background: #eff6ff; }

/* ── DIAGRAM CARDS ── */
.diag-card {
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
  margin: 20px 0;
  page-break-inside: avoid;
}
.diag-card-header {
  background: var(--surface2);
  border-bottom: 1px solid var(--border);
  padding: 10px 16px;
  font-size: 0.8em;
  font-weight: 600;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 8px;
}
.diag-card-header .dot {
  width: 8px; height: 8px;
  background: var(--accent);
  border-radius: 50%;
  flex-shrink: 0;
}
.diag-body {
  padding: 16px;
  background: #fff;
  display: flex;
  justify-content: center;
  min-height: 60px;
}
.mermaid { width: 100%; }
.mermaid svg { max-width: 100% !important; height: auto !important; }

/* ── FOOTER ── */
.doc-footer {
  margin-top: 32px;
  border-top: 1px solid var(--border);
  padding-top: 12px;
  font-size: 0.68em;
  color: var(--text-muted);
  display: flex;
  justify-content: space-between;
}

/* ── PRINT ── */
@media print {
  body { padding: 20px 28px; }
  .diag-card { page-break-inside: avoid; }
}
"""


def md_to_html_body(content: str) -> tuple[str, list[str]]:
    """
    Very lightweight Markdown → HTML converter.
    Also extracts mermaid blocks and replaces them with diagram card placeholders.
    Returns (html_body_string, [mermaid_code, ...])
    """
    mermaid_blocks: list[str] = []

    # 1. Extract mermaid fenced blocks → placeholders
    def replace_mermaid(m):
        idx = len(mermaid_blocks)
        mermaid_blocks.append(m.group(1).strip())
        return f'__MERMAID_{idx}__'

    content = re.sub(r'```mermaid\n(.*?)```', replace_mermaid, content, flags=re.DOTALL)

    # 2. Remove remaining fenced code blocks (non-mermaid) but keep content
    content = re.sub(r'```(?:\w+)?\n(.*?)```', lambda m: f'<pre><code>{m.group(1)}</code></pre>', content, flags=re.DOTALL)

    lines = content.split('\n')
    html_parts: list[str] = []
    in_table = False
    table_rows: list[str] = []

    def flush_table():
        nonlocal in_table, table_rows
        if not table_rows:
            return
        html_parts.append('<table>')
        for ri, row in enumerate(table_rows):
            cells = [c.strip() for c in row.strip('|').split('|')]
            if ri == 0:
                html_parts.append('<thead><tr>' + ''.join(f'<th>{c}</th>' for c in cells) + '</tr></thead><tbody>')
            elif ri == 1 and all(re.match(r'^[-: ]+$', c) for c in cells):
                pass  # separator row
            else:
                html_parts.append('<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>')
        html_parts.append('</tbody></table>')
        table_rows = []
        in_table = False

    for line in lines:
        # Mermaid placeholder
        m = re.match(r'__MERMAID_(\d+)__', line.strip())
        if m:
            flush_table()
            idx = int(m.group(1))
            code = mermaid_blocks[idx]
            card = (
                f'<div class="diag-card">'
                f'<div class="diag-card-header"><span class="dot"></span>Workflow Diagram</div>'
                f'<div class="diag-body"><div class="mermaid">{code}</div></div>'
                f'</div>'
            )
            html_parts.append(card)
            continue

        # Pre-rendered code blocks
        if '<pre><code>' in line:
            flush_table()
            html_parts.append(line)
            continue

        # Table rows
        if line.startswith('|'):
            if not in_table:
                in_table = True
            table_rows.append(line)
            continue
        else:
            flush_table()

        # Headings
        if line.startswith('#### '):
            html_parts.append(f'<h4>{escape_inline(line[5:])}</h4>')
        elif line.startswith('### '):
            html_parts.append(f'<h3>{escape_inline(line[4:])}</h3>')
        elif line.startswith('## '):
            html_parts.append(f'<h2>{escape_inline(line[3:])}</h2>')
        elif line.startswith('# '):
            html_parts.append(f'<h1>{escape_inline(line[2:])}</h1>')
        # Horizontal rule
        elif re.match(r'^[-*_]{3,}$', line.strip()):
            html_parts.append('<hr>')
        # Unordered list
        elif re.match(r'^\s*[-*+] ', line):
            text = re.sub(r'^\s*[-*+] ', '', line)
            html_parts.append(f'<li>{escape_inline(text)}</li>')
        # Ordered list
        elif re.match(r'^\s*\d+\. ', line):
            text = re.sub(r'^\s*\d+\. ', '', line)
            html_parts.append(f'<li>{escape_inline(text)}</li>')
        # Blockquote
        elif line.startswith('> '):
            html_parts.append(f'<blockquote>{escape_inline(line[2:])}</blockquote>')
        # Empty line
        elif line.strip() == '':
            html_parts.append('')
        # Paragraph
        else:
            html_parts.append(f'<p>{escape_inline(line)}</p>')

    flush_table()

    # Wrap consecutive <li> into <ul>
    body = '\n'.join(html_parts)
    body = re.sub(r'(<li>.*?</li>\n?)+', lambda m: '<ul>' + m.group(0) + '</ul>', body, flags=re.DOTALL)

    return body, mermaid_blocks


def escape_inline(text: str) -> str:
    """Convert inline markdown (bold, italic, code, links) to HTML."""
    # Bold + italic
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Links [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text


def build_html_page(md_path: str) -> str:
    """Return a complete HTML document for a single markdown file."""
    with open(md_path, encoding='utf-8') as fh:
        content = fh.read()

    body_html, _ = md_to_html_body(content)

    # Friendly doc title from filename
    basename = os.path.basename(md_path).replace('.md', '').replace('_', ' ')

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BNBR – {basename}</title>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<style>{PAGE_CSS}</style>
</head>
<body>

<div class="doc-header">
  <div class="logo">B</div>
  <div class="title-block">
    <h1>BNBR Kenya &mdash; ApprovalMax Workflow Architecture</h1>
    <p>Document Ref: BNBR/FIN/AMWP/001/2026 &nbsp;|&nbsp; Effective: 1 April 2026 &nbsp;|&nbsp; {basename}</p>
  </div>
</div>

{body_html}

<div class="doc-footer">
  <span>BNBR/FIN/AMWP/001/2026 &mdash; Confidential</span>
  <span>Generated {__import__('datetime').date.today().isoformat()}</span>
</div>

<script>
  mermaid.initialize({{
    startOnLoad: false,
    theme: 'default',
    flowchart: {{ useMaxWidth: true, htmlLabels: true, curve: 'basis' }},
    fontSize: 13,
    fontFamily: 'Inter, sans-serif'
  }});
  document.addEventListener('DOMContentLoaded', () => mermaid.run());
</script>
</body>
</html>"""


async def export_pdf(page, html_content: str, pdf_path: str, label: str):
    # Write a temp HTML file so local resources resolve
    tmp_html = pdf_path.replace('.pdf', '_tmp.html')
    with open(tmp_html, 'w', encoding='utf-8') as fh:
        fh.write(html_content)

    await page.goto(f'file:///{tmp_html.replace(chr(92), "/")}', wait_until='networkidle')

    # Wait for Mermaid diagrams to render (up to 15 s)
    try:
        await page.wait_for_function(
            """() => {
                const divs = document.querySelectorAll('.mermaid');
                if (divs.length === 0) return true;
                return [...divs].every(d => d.querySelector('svg') !== null);
            }""",
            timeout=15000
        )
    except Exception:
        print(f'  WARN  Mermaid timeout for {label} - printing anyway')

    await page.pdf(
        path=pdf_path,
        format='A3',
        print_background=True,
        margin={'top': '15mm', 'bottom': '15mm', 'left': '12mm', 'right': '12mm'}
    )

    # Clean up temp file
    try:
        os.remove(tmp_html)
    except Exception:
        pass

    print(f'  OK  {label}  ->  {os.path.basename(pdf_path)}')


async def main():
    md_files = sorted(glob.glob(os.path.join(FOLDER, '*.md')))
    print(f'Found {len(md_files)} markdown files\nOutput -> {OUT_DIR}\n')

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        # Allow local file access
        page.set_default_timeout(30000)

        for md_path in md_files:
            label = os.path.basename(md_path).replace('.md', '')
            html_content = build_html_page(md_path)
            pdf_filename = label + '.pdf'
            pdf_path = os.path.join(OUT_DIR, pdf_filename)
            await export_pdf(page, html_content, pdf_path, label)

        await browser.close()

    print(f'\nAll done! {len(md_files)} PDFs saved to:\n  {OUT_DIR}')


if __name__ == '__main__':
    asyncio.run(main())
