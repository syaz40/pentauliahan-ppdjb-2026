import sys
import json
sys.stdout.reconfigure(encoding='utf-8')

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('const EMBEDDED_CANDIDATES =')
idx_end = html.find('];', idx)
print("=== EMBEDDED_CANDIDATES first 1000 chars ===")
print(html[idx:idx+1500])
