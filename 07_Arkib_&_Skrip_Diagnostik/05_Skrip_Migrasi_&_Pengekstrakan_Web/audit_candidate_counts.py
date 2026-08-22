import sys, io, re, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r'03_Google_Apps_Script\Index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Get EMBEDDED_CANDIDATES
pattern = r'const EMBEDDED_CANDIDATES\s*=\s*(\[.*?\]);'
m = re.search(pattern, html, re.DOTALL)
if not m:
    print("NOT FOUND - trying simpler pattern")
    idx = html.find('EMBEDDED_CANDIDATES')
    if idx != -1:
        print(html[idx:idx+200])
    sys.exit()

candidates = json.loads(m.group(1))
print(f"Total calon tertanam (HTML): {len(candidates)}")

# Count by unit and jantina
krs_l = [c for c in candidates if c['unit']=='KRS' and c['jantina']=='L']
krs_p = [c for c in candidates if c['unit']=='KRS' and c['jantina']=='P']
tkrs_l = [c for c in candidates if c['unit']=='TKRS' and c['jantina']=='L']
tkrs_p = [c for c in candidates if c['unit']=='TKRS' and c['jantina']=='P']

print(f"\n--- Pecahan Unit & Jantina ---")
print(f"KRS Putera (L)  : {len(krs_l)}")
print(f"KRS Puteri (P)  : {len(krs_p)}")
print(f"TKRS Putera (L) : {len(tkrs_l)}")
print(f"TKRS Puteri (P) : {len(tkrs_p)}")
print(f"JUMLAH KRS      : {len(krs_l) + len(krs_p)}")
print(f"JUMLAH TKRS     : {len(tkrs_l) + len(tkrs_p)}")
print(f"GRAND TOTAL     : {len(candidates)}")

print(f"\n--- Pecahan Kumpulan ---")
for k in ['A', 'B', 'C']:
    k_krs = [c for c in candidates if c.get('kumpulan')==k and c['unit']=='KRS']
    k_tkrs = [c for c in candidates if c.get('kumpulan')==k and c['unit']=='TKRS']
    print(f"Kumpulan {k}: KRS={len(k_krs)}, TKRS={len(k_tkrs)}, Jumlah={len(k_krs)+len(k_tkrs)}")

# Check for duplicate noBadan
no_badan_list = [c.get('noBadan','') for c in candidates]
duplicates = [x for x in no_badan_list if no_badan_list.count(x) > 1]
dupes_unique = list(set(duplicates))
print(f"\n--- Semakan Duplikat No Badan ---")
print(f"Duplikat ditemui: {len(dupes_unique)}")
if dupes_unique:
    for d in dupes_unique:
        print(f"  DUPLIKAT: {d}")

# Check no urutan gaps
all_no_badan = sorted(no_badan_list)
print(f"\nSample 10 pertama noBadan: {all_no_badan[:10]}")

# Check how charts use the data  
print(f"\n--- Nilai Digunakan Dalam Graf Carta Anugerah ---")
print(f"chartCategoryGender: TKRS Putera={len(tkrs_l)}, TKRS Puteri={len(tkrs_p)}, KRS Putera={len(krs_l)}, KRS Puteri={len(krs_p)}")
print(f"  Ini adalah data hardcoded di initCharts: [98, 63, 82, 62]")
print(f"  Nilai sebenar dari data: TKRS L={len(tkrs_l)}, TKRS P={len(tkrs_p)}, KRS L={len(krs_l)}, KRS P={len(krs_p)}")

hardcoded = [98, 63, 82, 62]
actual = [len(tkrs_l), len(tkrs_p), len(krs_l), len(krs_p)]
if hardcoded != actual:
    print(f"\n  *** AMARAN: Nilai hardcoded TIDAK SEPADAN dengan data sebenar! ***")
    print(f"  Hardcoded: {hardcoded}")
    print(f"  Sebenar  : {actual}")
