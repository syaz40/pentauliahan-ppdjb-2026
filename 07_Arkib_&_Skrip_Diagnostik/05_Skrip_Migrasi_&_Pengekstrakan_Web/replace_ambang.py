import os

files = ['WebDashboard.html', 'ModalMengenai.html', 'Code.js', 'ModalAmbang.html']
for f in files:
    if os.path.exists(f):
        with open(f, encoding='utf-8') as file:
            content = file.read()
        
        content = content.replace('Ambang', 'Wajaran')
        content = content.replace('ambang', 'wajaran')
        content = content.replace('AMBANG', 'WAJARAN')
        
        # Clean up duplicates
        content = content.replace('Wajaran Wajaran', 'Wajaran')
        content = content.replace('wajaran wajaran', 'wajaran')
        content = content.replace('Wajaran & Wajaran', 'Wajaran')
        content = content.replace('Wajaran dan wajaran', 'wajaran')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
