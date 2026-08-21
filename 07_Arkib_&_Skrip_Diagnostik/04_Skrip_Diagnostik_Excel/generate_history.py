import json
import os

log_path = r'C:\Users\SKSRITEBRAUGURU1\.gemini\antigravity-ide\brain\03aac6d1-d22e-4888-92f8-729db7079142\.system_generated\logs\transcript_full.jsonl'
output_path = r'i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\00_SEJARAH_PERBUALAN_LENGKAP_PROJECT.md'

entries = []

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
            step_type = obj.get('type')
            source = obj.get('source')
            content = obj.get('content', '')
            
            if step_type == 'USER_INPUT' and source in ['USER_EXPLICIT', 'USER']:
                user_text = content
                if '<USER_REQUEST>' in content:
                    start = content.find('<USER_REQUEST>') + len('<USER_REQUEST>')
                    end = content.find('</USER_REQUEST>')
                    user_text = content[start:end].strip()
                elif '{{ CHECKPOINT' in content:
                    # Parse user requests from checkpoint summary if present
                    user_text = content.strip()
                else:
                    user_text = content.strip()
                
                entries.append({'role': 'USER', 'text': user_text})
                
            elif step_type == 'PLANNER_RESPONSE' and source == 'MODEL':
                if content and content.strip():
                    entries.append({'role': 'ASSISTANT', 'text': content.strip()})
        except Exception as e:
            pass

with open(output_path, 'w', encoding='utf-8') as out:
    out.write('# 📜 REKOD SEJARAH PERBUALAN & LOG KESELURUHAN PROJEK PENTAULIAHAN 2026\n\n')
    out.write('> **Nota Rasmi:** Fail ini merekodkan keseluruhan rentetan arahan, perbincangan konsep, analisis AppSheet/Google Sheets, pengaturcaraan kod Apps Script & Web App, serta penyelesaian masalah dari awal hingga akhir.\n\n---\n\n')
    
    turn = 1
    for item in entries:
        if item['role'] == 'USER':
            out.write(f'## 👤 SESI PERBUALAN #{turn}: ARAHAN PENGGUNA (USER)\n\n')
            out.write('```text\n')
            out.write(item['text'])
            out.write('\n```\n\n')
        else:
            out.write('### 🤖 MAKLUM BALAS & TINDAKAN SISTEM (AI ASSISTANT)\n\n')
            out.write(item['text'])
            out.write('\n\n---\n\n')
            turn += 1

print(f'Done! Generated full conversation log to {output_path}')
