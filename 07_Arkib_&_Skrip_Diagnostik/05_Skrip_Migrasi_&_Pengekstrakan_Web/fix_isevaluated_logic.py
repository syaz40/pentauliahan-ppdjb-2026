import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# =====================================================================
# BETULKAN LOGIK isEvaluated: || (OR) → && (AND)
# Murid dikira "Selesai Pengujian" HANYA bila SEMUA 3 modul ada markah
# =====================================================================

# ── 1. Code.gs ──────────────────────────────────────────────────────
with open(r'03_Google_Apps_Script\Code.gs', 'r', encoding='utf-8') as f:
    code = f.read()

old_eval_gs = 'var isEvaluated = (kawad > 0 || bantuMula > 0 || ikatan > 0);'
new_eval_gs = 'var isEvaluated = (kawad > 0 && bantuMula > 0 && ikatan > 0); // Selesai = SEMUA 3 modul ada markah'

count_gs = code.count(old_eval_gs)
if count_gs > 0:
    code = code.replace(old_eval_gs, new_eval_gs)
    with open(r'03_Google_Apps_Script\Code.gs', 'w', encoding='utf-8') as f:
        f.write(code)
    print(f'Code.gs: SELESAI - {count_gs} tempat diubah (|| -> &&)')
else:
    print('Code.gs: Tidak dijumpai pattern lama')

# ── 2. Index.html ────────────────────────────────────────────────────
with open(r'03_Google_Apps_Script\Index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern 1: dalam updateStats / recalculate (rawKawad, rawBantuMula, rawIkatan)
old_eval_html_1 = 'c.isEvaluated = (s.rawKawad > 0 || s.rawBantuMula > 0 || s.rawIkatan > 0);'
new_eval_html_1 = 'c.isEvaluated = (s.rawKawad > 0 && s.rawBantuMula > 0 && s.rawIkatan > 0); // Selesai = SEMUA 3 modul'
count1 = html.count(old_eval_html_1)
if count1 > 0:
    html = html.replace(old_eval_html_1, new_eval_html_1)
    print(f'Index.html pattern 1: {count1} tempat diubah')

# Pattern 2: dalam updateCharts (rawK, rawBM, rawIK)
old_eval_html_2 = 'if (rawK > 0 || rawBM > 0 || rawIK > 0) {'
new_eval_html_2 = 'if (rawK > 0 && rawBM > 0 && rawIK > 0) { // Selesai = SEMUA 3 modul ada markah'
count2 = html.count(old_eval_html_2)
if count2 > 0:
    html = html.replace(old_eval_html_2, new_eval_html_2)
    print(f'Index.html pattern 2 (updateCharts): {count2} tempat diubah')

# Pattern 3: dalam recalculateAllStats / stat update blocks
old_eval_html_3 = 'if (rawK > 0 || rawBM > 0 || rawIK > 0)'
new_eval_html_3 = 'if (rawK > 0 && rawBM > 0 && rawIK > 0) // Selesai = SEMUA 3 modul'
count3 = html.count(old_eval_html_3)
if count3 > 0:
    html = html.replace(old_eval_html_3, new_eval_html_3)
    print(f'Index.html pattern 3: {count3} tempat diubah')

with open(r'03_Google_Apps_Script\Index.html', 'w', encoding='utf-8') as f:
    f.write(html)

total_html = count1 + count2 + count3
print(f'Index.html: SELESAI - {total_html} tempat diubah')

# ── 3. Verify ────────────────────────────────────────────────────────
print()
print('=== PENGESAHAN ===')
# Re-read and verify no old patterns remain
with open(r'03_Google_Apps_Script\Code.gs', 'r', encoding='utf-8') as f:
    code_check = f.read()
with open(r'03_Google_Apps_Script\Index.html', 'r', encoding='utf-8') as f:
    html_check = f.read()

# Check for remaining old OR patterns
remaining_gs = code_check.count('kawad > 0 || bantuMula > 0 || ikatan > 0')
remaining_html = html_check.count('rawK > 0 || rawBM > 0 || rawIK > 0')

print(f'Baki OR (||) dalam Code.gs  : {remaining_gs}')
print(f'Baki OR (||) dalam Index.html: {remaining_html}')

# Count AND patterns
and_gs = code_check.count('kawad > 0 && bantuMula > 0 && ikatan > 0')
and_html = html_check.count('rawK > 0 && rawBM > 0 && rawIK > 0')
print(f'Pattern AND (&&) dalam Code.gs  : {and_gs}')
print(f'Pattern AND (&&) dalam Index.html: {and_html}')

if remaining_gs == 0 and remaining_html == 0:
    print()
    print('SEMUA isEvaluated logik berjaya ditukar: || -> &&')
    print('Murid kini dikira SELESAI PENGUJIAN hanya bila SEMUA 3 modul ada markah')
else:
    print()
    print('AMARAN: Masih ada pattern lama yang belum ditukar!')
