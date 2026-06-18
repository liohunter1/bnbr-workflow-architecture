import os
import subprocess
import time

FOLDER = r'C:\Users\le\OneDrive\Desktop\hanns docs\BNBR_Workflow_Architecture'
EDGE   = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
PDF_DIR = os.path.join(FOLDER, 'PDFs')
TMP_DIR = os.path.join(FOLDER, '_tmp_html')

os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(TMP_DIR, exist_ok=True)

# Only retry the failed ones
FAILED = [
    '01_Governance_Hierarchy'
]

import re

def md_to_html_content(md_path):
    with open(md_path, encoding='utf-8') as f:
        content = f.read()

    name = os.path.splitext(os.path.basename(md_path))[0]
    title = name.replace('_', ' ').strip()
    for line in content.split('\n'):
        if line.startswith('# '):
            title = line[2:].strip()
            break

    parts = re.split(r'```mermaid(.*?)```', content, flags=re.DOTALL)
    out_parts = []
    for i, part in enumerate(parts):
        if i % 2 == 0:
            p = part
            p = re.sub(r'^### (.+)$', r'<h3>\1</h3>', p, flags=re.MULTILINE)
            p = re.sub(r'^## (.+)$',  r'<h2>\1</h2>', p, flags=re.MULTILINE)
            p = re.sub(r'^# (.+)$',   r'<h1>\1</h1>', p, flags=re.MULTILINE)
            p = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', p)
            def table_replace(m):
                lines = [l.strip() for l in m.group(0).strip().split('\n')
                         if l.strip() and not re.match(r'^\|[-| :]+\|$', l.strip())]
                rows = []
                for idx, line in enumerate(lines):
                    cells = [c.strip() for c in line.strip('|').split('|')]
                    tag = 'th' if idx == 0 else 'td'
                    rows.append('<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>')
                return '<table>' + ''.join(rows) + '</table>'
            p = re.sub(r'(\|.+\|\n)+', table_replace, p)
            p = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', p, flags=re.MULTILINE)
            p = re.sub(r'^---+$', r'<hr>', p, flags=re.MULTILINE)
            p = re.sub(r'^[\*\-] (.+)$', r'<li>\1</li>', p, flags=re.MULTILINE)
            p = re.sub(r'^\d+\. (.+)$', r'<li>\1</li>', p, flags=re.MULTILINE)
            p = re.sub(r'(<li>.*?</li>\n?)+', lambda m: '<ul>' + m.group(0) + '</ul>', p, flags=re.DOTALL)
            lines2 = p.split('\n')
            new_lines = []
            for ln in lines2:
                s = ln.strip()
                if s and not s.startswith('<'):
                    new_lines.append(f'<p>{s}</p>')
                else:
                    new_lines.append(ln)
            p = '\n'.join(new_lines)
            out_parts.append(p)
        else:
            diagram_code = part.strip()
            out_parts.append(f'<div class="mermaid-wrap"><div class="mermaid">{diagram_code}</div></div>')

    body_html = ''.join(out_parts)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title} - BNBR ApprovalMax</title>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Inter', Arial, sans-serif; font-size: 11pt; color: #1a1a2e; background: #fff; }}
  .page-header {{ background: #1a1a2e; color: #fff; padding: 18px 28px 14px; border-bottom: 4px solid #f0c040; page-break-after: avoid; }}
  .page-header .doc-ref {{ font-size: 8pt; color: #9ca3c9; margin-bottom: 4px; }}
  .page-header h1 {{ font-size: 16pt; font-weight: 700; color: #fff; line-height: 1.25; }}
  .page-header .subtitle {{ font-size: 8.5pt; color: #c0c8e8; margin-top: 5px; }}
  .content {{ padding: 20px 28px 28px; }}
  h1 {{ font-size: 14pt; color: #1a1a2e; margin: 18px 0 8px; border-bottom: 2px solid #f0c040; padding-bottom: 4px; page-break-after: avoid; }}
  h2 {{ font-size: 12pt; color: #0f3460; margin: 16px 0 6px; page-break-after: avoid; }}
  h3 {{ font-size: 10.5pt; color: #533483; margin: 12px 0 5px; page-break-after: avoid; }}
  p  {{ margin: 5px 0 8px; line-height: 1.55; font-size: 10pt; }}
  ul {{ margin: 6px 0 8px 18px; }}
  li {{ margin: 3px 0; font-size: 10pt; line-height: 1.5; }}
  table {{ width: 100%; border-collapse: collapse; margin: 12px 0 16px; font-size: 9pt; page-break-inside: avoid; }}
  th {{ background: #1a1a2e; color: #fff; padding: 7px 10px; text-align: left; font-weight: 600; }}
  td {{ padding: 6px 10px; border: 1px solid #d0d4e8; vertical-align: top; line-height: 1.45; }}
  tr:nth-child(even) td {{ background: #f4f5fb; }}
  blockquote {{ border-left: 4px solid #f0c040; background: #fffbf0; padding: 8px 14px; margin: 10px 0; font-size: 9.5pt; color: #444; page-break-inside: avoid; }}
  hr {{ border: none; border-top: 1px solid #ddd; margin: 16px 0; }}
  strong {{ color: #0f3460; }}
  .mermaid-wrap {{ margin: 14px 0 18px; padding: 14px; background: #f8f9ff; border: 1px solid #d0d4e8; border-radius: 6px; text-align: center; page-break-inside: avoid; }}
  .mermaid {{ display: inline-block; max-width: 100%; }}
  .mermaid svg {{ max-width: 100%; height: auto; }}
  @page {{ size: A4 landscape; margin: 10mm 12mm 14mm 12mm; }}
</style>
</head>
<body>
<div class="page-header">
  <div class="doc-ref">BNBR/FIN/AMWP/001/2026 | Effective: 1 April 2026 | ApprovalMax integrated with Xero | CONFIDENTIAL</div>
  <h1>{title}</h1>
  <div class="subtitle">Basic Needs Basic Rights Kenya - ApprovalMax Workflow Architecture Package</div>
</div>
<div class="content">{body_html}</div>
<script>
  mermaid.initialize({{startOnLoad:true, theme:'default', flowchart:{{useMaxWidth:true, htmlLabels:true, curve:'stepBefore'}}, fontSize:11}});
</script>
</body></html>'''
    return html


success = []
errors = []

for base in FAILED:
    md_path = os.path.join(FOLDER, base + '.md')
    if not os.path.exists(md_path):
        print(f'SKIP {base} - md file not found')
        continue

    tmp_html = os.path.join(TMP_DIR, base + '.html')
    out_pdf  = os.path.join(PDF_DIR, base + '.pdf')

    html_content = md_to_html_content(md_path)
    with open(tmp_html, 'w', encoding='utf-8') as f:
        f.write(html_content)

    file_url = 'file:///' + tmp_html.replace('\\', '/').replace(' ', '%20')

    cmd = [
        EDGE,
        '--headless=new',
        '--disable-gpu',
        '--no-sandbox',
        '--disable-software-rasterizer',
        '--run-all-compositor-stages-before-draw',
        '--virtual-time-budget=15000',   # 15 sec render budget
        f'--print-to-pdf={out_pdf}',
        '--print-to-pdf-no-header',
        '--no-pdf-header-footer',
        file_url
    ]
    print(f'Rendering {base} ...')
    try:
        result = subprocess.run(cmd, timeout=90, capture_output=True)  # 90s timeout
        if os.path.exists(out_pdf) and os.path.getsize(out_pdf) > 1000:
            size_kb = os.path.getsize(out_pdf) // 1024
            success.append(base)
            print(f'  OK  {base}.pdf  ({size_kb} KB)')
        else:
            errors.append(base)
            print(f'  ERR {base}.pdf - empty or missing')
    except subprocess.TimeoutExpired:
        errors.append(base)
        print(f'  ERR {base}.pdf - timed out at 90s')
    except Exception as e:
        errors.append(base)
        print(f'  ERR {base}.pdf - {e}')

    time.sleep(2)

# Cleanup
import shutil
shutil.rmtree(TMP_DIR, ignore_errors=True)

print(f'\nRetry complete: {len(success)} succeeded, {len(errors)} failed.')
if errors:
    for e in errors:
        print(f'  STILL FAILED: {e}')
print(f'PDFs in: {PDF_DIR}')
