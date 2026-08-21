import re

with open(r"i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\00_SEJARAH_PERBUALAN_LENGKAP_PROJECT.md", "r", encoding="utf-8") as f:
    text = f.read()

# Let's search for the modal HTML code blocks
modal_names = ['Dashboard.html', 'ModalAutomasi.html', 'ModalBaikiFormula.html', 'ModalKehadiran.html', 'ModalMengenai.html', 'ModalWajaran.html']

modals_content = []

for m in modal_names:
    pattern = rf'### (?:Fail: )?`?{m}`?.*?\n```html\n(.*?)```'
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        # try another pattern
        pattern = rf'`{m}`.*?\n```html\n(.*?)```'
        match = re.search(pattern, text, re.DOTALL)
    
    if match:
        content = match.group(1).strip()
        page_name = m.replace('.html', '')
        modals_content.append(f"<? if (page === '{page_name}') {{ ?>\n{content}\n<? }} ?>")
        print(f"Found {m}, length: {len(content)}")
    else:
        print(f"NOT found: {m}")

if len(modals_content) == 6:
    with open(r"i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\03_Google_Apps_Script\Modals.html", "w", encoding="utf-8") as f:
        f.write('\n\n'.join(modals_content))
    print("Created Modals.html successfully with all 6 modals!")
else:
    print(f"Only found {len(modals_content)} modals, let's refine search.")
