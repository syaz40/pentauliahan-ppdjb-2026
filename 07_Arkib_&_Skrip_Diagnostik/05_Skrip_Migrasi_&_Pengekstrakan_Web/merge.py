import os
import re

dir_path = r'i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\03_Google_Apps_Script'
html_files = ['Dashboard.html', 'ModalAutomasi.html', 'ModalBaikiFormula.html', 'ModalKehadiran.html', 'ModalMengenai.html', 'ModalWajaran.html', 'WebDashboard.html']

merged_html = []
for file in html_files:
    file_path = os.path.join(dir_path, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    page_name = file.replace('.html', '')
    merged_html.append(f'<? if (page === \'{page_name}\') {{ ?>\n{content}\n<? }} ?>')

with open(os.path.join(dir_path, 'Index.html'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(merged_html))
    
with open(os.path.join(dir_path, 'Code.js'), 'r', encoding='utf-8') as f:
    code = f.read()

# Replace HtmlService.createHtmlOutputFromFile('X')
# with:
# var template = HtmlService.createTemplateFromFile('Index'); template.page = 'X'; var html = template.evaluate()
code = re.sub(r"var html = HtmlService\.createHtmlOutputFromFile\('([^']+)'\)", 
              r"var template = HtmlService.createTemplateFromFile('Index');\n  template.page = '\g<1>';\n  var html = template.evaluate()", 
              code)

# Replace HtmlService.createTemplateFromFile('WebDashboard')
# with:
# var template = HtmlService.createTemplateFromFile('Index'); template.page = 'WebDashboard'; return template.evaluate()
code = re.sub(r"return HtmlService\.createTemplateFromFile\('WebDashboard'\)\n\s*\.evaluate\(\)",
              r"var template = HtmlService.createTemplateFromFile('Index');\n  template.page = 'WebDashboard';\n  return template.evaluate()",
              code)

with open(os.path.join(dir_path, 'Code.gs'), 'w', encoding='utf-8') as f:
    f.write(code)

# Remove the old html files and Code.js
for file in html_files:
    os.remove(os.path.join(dir_path, file))
os.remove(os.path.join(dir_path, 'Code.js'))

print('Merged files successfully!')
