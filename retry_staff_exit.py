import os
import subprocess
import re
import shutil

FOLDER  = r'C:\Users\le\OneDrive\Desktop\hanns docs\BNBR_Workflow_Architecture'
EDGE    = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
PDF_DIR = os.path.join(FOLDER, 'PDFs')
TMP_DIR = os.path.join(FOLDER, '_tmp_html')
os.makedirs(TMP_DIR, exist_ok=True)

md_path  = os.path.join(FOLDER, '16_WF13_Staff_Exit.md')
tmp_html = os.path.join(TMP_DIR, '16_WF13_Staff_Exit.html')
out_pdf  = os.path.join(PDF_DIR, '16_WF13_Staff_Exit.pdf')

with open(md_path, encoding='utf-8') as f:
    content = f.read()

# Extract mermaid diagram
m = re.search(r'```mermaid(.*?)```', content, re.DOTALL)
diagram = m.group(1).strip() if m else ''

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: Arial, sans-serif; font-size: 10pt; color: #1a1a2e; background: #fff; }
.hdr { background: #1a1a2e; color: #fff; padding: 16px 24px; border-bottom: 4px solid #f0c040; }
.hdr .ref { font-size: 7.5pt; color: #9ca3c9; margin-bottom: 3px; }
.hdr h1 { font-size: 15pt; font-weight: 700; }
.hdr .sub { font-size: 8pt; color: #c0c8e8; margin-top: 4px; }
.body { padding: 18px 24px; }
.mermaid-wrap { margin: 12px 0; padding: 12px; background: #f8f9ff; border: 1px solid #d0d4e8; border-radius: 6px; text-align: center; }
.mermaid svg { max-width: 100%; height: auto; }
table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 8.5pt; }
th { background: #1a1a2e; color: #fff; padding: 6px 9px; text-align: left; }
td { padding: 5px 9px; border: 1px solid #d0d4e8; vertical-align: top; }
tr:nth-child(even) td { background: #f4f5fb; }
blockquote { border-left: 4px solid #f0c040; background: #fffbf0; padding: 7px 12px; margin: 8px 0; font-size: 9pt; }
h2 { font-size: 11pt; color: #0f3460; margin: 14px 0 5px; }
@page { size: A4 landscape; margin: 10mm 12mm 12mm 12mm; }
"""

JS = """
mermaid.initialize({
  startOnLoad: true,
  theme: 'default',
  flowchart: { useMaxWidth: true, htmlLabels: true, curve: 'stepBefore' },
  fontSize: 10
});
"""

html_parts = [
    '<!DOCTYPE html><html lang="en"><head>',
    '<meta charset="UTF-8">',
    '<title>WF13 Staff Exit - BNBR ApprovalMax</title>',
    '<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>',
    '<style>' + CSS + '</style>',
    '</head><body>',
    '<div class="hdr">',
    '  <div class="ref">BNBR/FIN/AMWP/001/2026 | Effective: 1 April 2026 | CONFIDENTIAL</div>',
    '  <h1>WORKFLOW 13 &mdash; STAFF EXIT</h1>',
    '  <div class="sub">Basic Needs Basic Rights Kenya &mdash; ApprovalMax Workflow Architecture Package</div>',
    '</div>',
    '<div class="body">',
    '  <div class="mermaid-wrap">',
    '    <div class="mermaid">',
    diagram,
    '    </div>',
    '  </div>',
    '</div>',
    '<script>' + JS + '</script>',
    '</body></html>',
]

with open(tmp_html, 'w', encoding='utf-8') as f:
    f.write('\n'.join(html_parts))

print(f'HTML written: {tmp_html}')

file_url = 'file:///' + tmp_html.replace('\\', '/').replace(' ', '%20')

cmd = [
    EDGE,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--run-all-compositor-stages-before-draw',
    '--virtual-time-budget=25000',
    f'--print-to-pdf={out_pdf}',
    '--print-to-pdf-no-header',
    '--no-pdf-header-footer',
    file_url
]

print('Rendering 16_WF13_Staff_Exit.pdf ...')
try:
    result = subprocess.run(cmd, timeout=150, capture_output=True)
    if os.path.exists(out_pdf) and os.path.getsize(out_pdf) > 1000:
        print(f'OK  16_WF13_Staff_Exit.pdf  ({os.path.getsize(out_pdf) // 1024} KB)')
    else:
        print('ERR - PDF empty or missing')
        print(result.stderr.decode('utf-8', 'ignore')[:400])
except subprocess.TimeoutExpired:
    print('ERR - timed out at 150s')
except Exception as e:
    print(f'ERR - {e}')

shutil.rmtree(TMP_DIR, ignore_errors=True)
print('Done.')
