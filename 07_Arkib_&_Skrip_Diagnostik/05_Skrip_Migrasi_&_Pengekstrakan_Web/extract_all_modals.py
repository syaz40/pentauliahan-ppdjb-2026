import json, os

transcript_path = r"C:\Users\SKSRITEBRAUGURU1\.gemini\antigravity-ide\brain\03aac6d1-d22e-4888-92f8-729db7079142\.system_generated\logs\transcript_full.jsonl"

modals = {}
files_to_find = ['Dashboard.html', 'ModalAutomasi.html', 'ModalBaikiFormula.html', 'ModalKehadiran.html', 'ModalMengenai.html', 'ModalWajaran.html', 'ModalAmbang.html']

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        for target in files_to_find:
            if target not in modals and target in line and 'write_to_file' in line:
                try:
                    obj = json.loads(line)
                    tool_calls = obj.get('tool_calls', [])
                    for tc in tool_calls:
                        if tc.get('name') == 'write_to_file':
                            args = tc.get('args', {})
                            if target in args.get('TargetFile', ''):
                                modals[target] = args.get('CodeContent', '')
                                print(f"Found {target}! Length: {len(modals[target])}")
                except Exception as e:
                    pass

if 'ModalWajaran.html' not in modals and 'ModalAmbang.html' in modals:
    content = modals['ModalAmbang.html']
    # replace Ambang with Wajaran
    content = content.replace('Ambang', 'Wajaran').replace('ambang', 'wajaran')
    modals['ModalWajaran.html'] = content
    print("Adapted ModalAmbang to ModalWajaran!")

order = ['Dashboard.html', 'ModalAutomasi.html', 'ModalBaikiFormula.html', 'ModalKehadiran.html', 'ModalMengenai.html', 'ModalWajaran.html']
merged = []
for target in order:
    if target in modals:
        page_name = target.replace('.html', '')
        merged.append(f"<? if (page === '{page_name}') {{ ?>\n{modals[target]}\n<? }} ?>")

with open(r"i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\03_Google_Apps_Script\Modals.html", "w", encoding="utf-8") as f:
    f.write('\n\n'.join(merged))

print("Created Modals.html successfully! Total modals included:", len(merged))
