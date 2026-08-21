import subprocess
import os
import re

for fp in ['03_Google_Apps_Script/Index.html', '04_Web_App_Netlify/index.html']:
    if not os.path.exists(fp):
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', content, re.DOTALL)
    for i, s in enumerate(scripts):
        if not s.strip():
            continue
        s_clean = re.sub(r'<\?!=.*?\?>', 'null', s)
        with open('temp_test.js', 'w', encoding='utf-8') as tf:
            tf.write(s_clean)
        r = subprocess.run(['node', '--check', 'temp_test.js'], capture_output=True, text=True)
        if r.returncode == 0:
            print(f'{fp} [Script {i+1}]: VALID')
        else:
            print(f'{fp} [Script {i+1}]: SYNTAX ERROR ->\n{r.stderr}')

if os.path.exists('temp_test.js'):
    os.remove('temp_test.js')
