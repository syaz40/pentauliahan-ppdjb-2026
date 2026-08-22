import sys, io, re, subprocess, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# =========================================================
# 1. SYNTAX CHECK: Code.gs
# =========================================================
print("=" * 60)
print("1. SEMAKAN SINTAKS: Code.gs")
print("=" * 60)

with open(r'03_Google_Apps_Script\Code.gs', 'r', encoding='utf-8') as f:
    code_gs = f.read()

with open('_tmp_code.js', 'w', encoding='utf-8') as f:
    f.write(code_gs)

res = subprocess.run(['node', '-c', '_tmp_code.js'], capture_output=True, text=True)
if res.returncode == 0:
    print("Code.gs: LULUS (0 Ralat Sintaks)")
else:
    print("Code.gs: RALAT!\n", res.stderr)

os.remove('_tmp_code.js')

# =========================================================
# 2. SYNTAX CHECK: Index.html scripts
# =========================================================
print("\n" + "=" * 60)
print("2. SEMAKAN SINTAKS: Index.html (semua blok <script>)")
print("=" * 60)

with open(r'03_Google_Apps_Script\Index.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
print(f"Jumlah blok <script>: {len(scripts)}")

script_errors = []
for i, s in enumerate(scripts):
    if not s.strip(): continue
    with open(f'_tmp_{i}.js', 'w', encoding='utf-8') as f:
        f.write(s)
    res = subprocess.run(['node', '-c', f'_tmp_{i}.js'], capture_output=True, text=True)
    if res.returncode != 0:
        if '<' in s or '?!=' in s:
            print(f"Script {i}: Template GAS (DIJANGKA - OK)")
        else:
            print(f"Script {i}: RALAT SINTAKS!\n  {res.stderr[:200]}")
            script_errors.append(i)
    else:
        print(f"Script {i}: LULUS")
    os.remove(f'_tmp_{i}.js')

if not script_errors:
    print("\nSemua skrip JS: LULUS (0 Ralat)")

# =========================================================
# 3. EMBEDDED DATA: Count candidates
# =========================================================
print("\n" + "=" * 60)
print("3. ANALISIS DATA CALON TERTANAM (EMBEDDED)")
print("=" * 60)

matches = re.findall(r'EMBEDDED_CANDIDATES\s*=\s*(\[.*?\]);', html, re.DOTALL)
if matches:
    import json
    try:
        cands = json.loads(matches[0])
        print(f"Jumlah calon tertanam: {len(cands)}")
        
        krs = [c for c in cands if c.get('unit') == 'KRS']
        tkrs = [c for c in cands if c.get('unit') == 'TKRS']
        krs_l = [c for c in krs if c.get('jantina') == 'L']
        krs_p = [c for c in krs if c.get('jantina') == 'P']
        tkrs_l = [c for c in tkrs if c.get('jantina') == 'L']
        tkrs_p = [c for c in tkrs if c.get('jantina') == 'P']
        
        print(f"\nPecahan Unit:")
        print(f"  KRS  : {len(krs)} calon  (L:{len(krs_l)}, P:{len(krs_p)})")
        print(f"  TKRS : {len(tkrs)} calon  (L:{len(tkrs_l)}, P:{len(tkrs_p)})")
        
        # Breakdown by kumpulan
        kumpulans = sorted(set(c.get('kumpulan','') for c in cands))
        print(f"\nPecahan Kumpulan: {kumpulans}")
        for k in kumpulans:
            k_cands = [c for c in cands if c.get('kumpulan') == k]
            print(f"  Kumpulan {k}: {len(k_cands)}")
        
        # Schools
        schools = set(c.get('sekolah','') for c in cands)
        print(f"\nJumlah sekolah unik: {len(schools)}")
        
        # Catatan / status
        has_catatan = [c for c in cands if c.get('catatan','').strip()]
        has_absent = [c for c in cands if c.get('isAbsent')]
        has_td = [c for c in cands if c.get('isTarikDiri')]
        print(f"\nCalon dengan catatan: {len(has_catatan)}")
        print(f"Calon tandakan Absent: {len(has_absent)}")
        print(f"Calon tandakan Tarik Diri: {len(has_td)}")
        
    except json.JSONDecodeError as e:
        print(f"GAGAL parse JSON: {e}")
else:
    print("EMBEDDED_CANDIDATES tidak dijumpai!")

# =========================================================
# 4. CHARTS ANALYSIS 
# =========================================================
print("\n" + "=" * 60)
print("4. ANALISIS DEFINISI GRAF (initCharts)")
print("=" * 60)

charts_start = html.find('initCharts()')
if charts_start != -1:
    charts_block = html[charts_start:charts_start + 8000]
    chart_types = re.findall(r"type:\s*['\"]([^'\"]+)['\"]", charts_block)
    chart_ids = re.findall(r"getElementById\(['\"]([^'\"]+)['\"]\)", charts_block)
    print(f"Jenis Graf Dijumpai: {chart_types}")
    print(f"Canvas IDs: {chart_ids[:15]}")
else:
    print("initCharts tidak dijumpai!")
