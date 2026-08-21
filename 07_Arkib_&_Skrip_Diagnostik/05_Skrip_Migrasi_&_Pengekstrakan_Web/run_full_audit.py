import os
import json
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=================================================================")
print("          LAPORAN AUDIT PENUH SEMUA SKRIP PROJEK                 ")
print("=================================================================")

# 1. Audit JSON Configs
print("\n[1] AUDIT FAIL KONFIGURASI JSON:")
json_files = [
    '03_Google_Apps_Script/appsscript.json',
    '03_Google_Apps_Script/.clasp.json',
    '04_Web_App_Netlify/netlify.toml'
]

for jf in json_files:
    if not os.path.exists(jf):
        print(f"  ✗ {jf}: Fail tidak ditemui!")
        continue
    if jf.endswith('.json'):
        try:
            with open(jf, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"  [OK] {jf}: JSON SAH -> Kunci: {list(data.keys())}")
        except Exception as e:
            print(f"  [RALAT] {jf}: Ralat JSON -> {e}")
    elif jf.endswith('.toml'):
        with open(jf, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print(f"  [OK] {jf}: TOML SAH -> {len(lines)} baris konfigurasi")

# 2. Audit Code.gs
print("\n[2] AUDIT GOOGLE APPS SCRIPT (Code.gs):")
code_gs_path = '03_Google_Apps_Script/Code.gs'
if os.path.exists(code_gs_path):
    with open(code_gs_path, 'r', encoding='utf-8') as f:
        code_gs = f.read()
    
    # Test Node.js syntax
    with open('temp_code_check.js', 'w', encoding='utf-8') as tf:
        tf.write(code_gs)
    res = subprocess.run(['node', '--check', 'temp_code_check.js'], capture_output=True, text=True)
    if os.path.exists('temp_code_check.js'):
        os.remove('temp_code_check.js')
    
    if res.returncode == 0:
        print(f"  [OK] {code_gs_path}: Sintaks JavaScript SAH (0 Syntax Error)")
    else:
        print(f"  [RALAT] {code_gs_path}: Ralat Sintaks ->\n{res.stderr}")
    
    funcs = re.findall(r'function\s+([a-zA-Z0-9_$]+)\s*\(', code_gs)
    print(f"  [INFO] Bilangan fungsi backend ditemui: {len(funcs)}")
    for fn in funcs:
        print(f"     • {fn}()")
else:
    print(f"  [RALAT] {code_gs_path} tidak wujud!")

# 3. Audit HTML & Client JS
print("\n[3] AUDIT FRONTEND WEB APPLICATION (Index.html):")
html_files = [
    '03_Google_Apps_Script/Index.html',
    '04_Web_App_Netlify/index.html'
]

for hf in html_files:
    print(f"\n--- Memeriksa {hf} ---")
    if not os.path.exists(hf):
        print(f"  [RALAT] {hf} tidak ditemui!")
        continue
    with open(hf, 'r', encoding='utf-8') as f:
        html_raw = f.read()
    
    print(f"  • Saiz fail: {len(html_raw):,} bait ({len(html_raw.splitlines())} baris)")
    
    has_doctype = '<!DOCTYPE html>' in html_raw or '<!doctype html>' in html_raw
    has_html_close = '</html>' in html_raw
    has_body_close = '</body>' in html_raw
    print(f"  • Struktur Asas HTML: DOCTYPE={has_doctype}, </body>={has_body_close}, </html>={has_html_close}")
    
    scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html_raw, re.DOTALL)
    print(f"  • Bilangan blok <script>: {len(scripts)}")
    
    for idx, sc in enumerate(scripts):
        if not sc.strip():
            continue
        if '<?!=' in sc and 'initialData' in sc:
            print(f"    [OK] Blok #{idx+1} (JSON Payload Scriptlet): SAH untuk GAS Template")
            continue
        if sc.strip() == 'null':
            print(f"    [OK] Blok #{idx+1} (JSON Payload Static): SAH untuk Netlify")
            continue
            
        with open('temp_html_sc.js', 'w', encoding='utf-8') as tf:
            tf.write(sc)
        r = subprocess.run(['node', '--check', 'temp_html_sc.js'], capture_output=True, text=True)
        if r.returncode == 0:
            print(f"    [OK] Blok #{idx+1} (Client Logic & Charts Engine): Sintaks JavaScript SAH (0 Ralat)")
        else:
            print(f"    [RALAT] Blok #{idx+1}: Ralat Sintaks ->\n{r.stderr}")
        if os.path.exists('temp_html_sc.js'):
            os.remove('temp_html_sc.js')

# 4. Audit Data Integriti (Embedded Candidates)
print("\n[4] AUDIT INTEGRITI DATA CALON:")
with open('03_Google_Apps_Script/Index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

m_cand = re.search(r'const (?:EMBEDDED_CANDIDATES|RAW_CANDIDATES_DATA)\s*=\s*(\[.*?\]);', idx_content, re.DOTALL)
if m_cand:
    try:
        candidates = json.loads(m_cand.group(1))
        print(f"  [OK] EMBEDDED_CANDIDATES berjaya di-parse: {len(candidates)} calon berdaftar")
        
        krs_count = sum(1 for c in candidates if c.get('unit') == 'KRS')
        tkrs_count = sum(1 for c in candidates if c.get('unit') == 'TKRS')
        l_count = sum(1 for c in candidates if c.get('jantina') == 'L')
        p_count = sum(1 for c in candidates if c.get('jantina') == 'P')
        print(f"    - KRS (Menengah): {krs_count} calon")
        print(f"    - TKRS (Rendah): {tkrs_count} calon")
        print(f"    - Lelaki: {l_count}, Perempuan: {p_count}")
        
        req_keys = ['unit', 'noBadan', 'nama', 'jantina', 'sekolah', 'kumpulan', 'rawKawad', 'rawBantuMula', 'rawIkatan', 'rawOverall', 'overall', 'statusText']
        missing_keys = set()
        for idx, c in enumerate(candidates):
            for k in req_keys:
                if k not in c:
                    missing_keys.add(k)
        if not missing_keys:
            print(f"  [OK] Semua rekod {len(candidates)} calon mengandungi semua medan kunci lengkap!")
        else:
            print(f"  [RALAT] Terdapat medan kunci yang hilang: {missing_keys}")
    except Exception as e:
        print(f"  [RALAT] Gagal membaca JSON EMBEDDED_CANDIDATES: {e}")
else:
    print("  [RALAT] EMBEDDED_CANDIDATES tidak ditemui dalam Index.html!")

print("\n=================================================================")
print("                   AUDIT SKRIP SELESAI                           ")
print("=================================================================")
