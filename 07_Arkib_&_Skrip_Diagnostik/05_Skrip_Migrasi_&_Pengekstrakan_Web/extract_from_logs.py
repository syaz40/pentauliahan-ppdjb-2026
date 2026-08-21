import json, os

transcript_path = r"C:\Users\SKSRITEBRAUGURU1\.gemini\antigravity-ide\brain\03aac6d1-d22e-4888-92f8-729db7079142\.system_generated\logs\transcript_full.jsonl"
if not os.path.exists(transcript_path):
    transcript_path = r"C:\Users\SKSRITEBRAUGURU1\.gemini\antigravity-ide\brain\03aac6d1-d22e-4888-92f8-729db7079142\.system_generated\logs\transcript.jsonl"

print("Reading transcript from:", transcript_path)

modals = {}
files_to_find = ['Dashboard.html', 'ModalAutomasi.html', 'ModalBaikiFormula.html', 'ModalKehadiran.html', 'ModalMengenai.html', 'ModalWajaran.html']

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        for target in files_to_find:
            if target not in modals and target in line and 'write_to_file' in line:
                try:
                    obj = json.loads(line)
                    # Check tool calls
                    tool_calls = obj.get('tool_calls', [])
                    for tc in tool_calls:
                        if tc.get('name') == 'write_to_file':
                            args = tc.get('args', {})
                            if target in args.get('TargetFile', ''):
                                modals[target] = args.get('CodeContent', '')
                                print(f"Found {target}! Length: {len(modals[target])}")
                except Exception as e:
                    pass

print("Total modals extracted:", len(modals))

if len(modals) == 6:
    merged = []
    for target in files_to_find:
        page_name = target.replace('.html', '')
        merged.append(f"<? if (page === '{page_name}') {{ ?>\n{modals[target]}\n<? }} ?>")
    
    with open(r"i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\03_Google_Apps_Script\Modals.html", "w", encoding="utf-8") as f:
        f.write('\n\n'.join(merged))
    print("Successfully wrote Modals.html!")
