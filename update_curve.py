import os

FOLDER = r'C:\Users\le\OneDrive\Desktop\hanns docs\BNBR_Workflow_Architecture'
scripts = [
    'build_viewer.py',
    'print_pdfs.py',
    'retry_failed_pdfs.py',
    'retry_staff_exit.py'
]

for script in scripts:
    path = os.path.join(FOLDER, script)
    if not os.path.exists(path): continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace("curve: 'basis'", "curve: 'stepBefore'")
    content = content.replace("curve:'basis'", "curve:'stepBefore'")
    content = content.replace("flowchart: { useMaxWidth: true, htmlLabels: true }", "flowchart: { useMaxWidth: true, htmlLabels: true, curve: 'stepBefore' }")
    content = content.replace("flowchart:{useMaxWidth:true, htmlLabels:true}", "flowchart:{useMaxWidth:true, htmlLabels:true, curve:'stepBefore'}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Scripts updated.')
