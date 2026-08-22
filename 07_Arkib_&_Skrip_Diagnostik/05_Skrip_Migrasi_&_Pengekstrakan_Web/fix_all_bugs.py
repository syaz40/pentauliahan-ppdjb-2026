import re, sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# =====================================================================
# SKRIP PEMBETULAN BUG + EKSPORT SEMULA DATA
# Membetulkan 3 bug yang dijumpai dalam sistem
# =====================================================================

with open(r'03_Google_Apps_Script\Index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("=" * 60)
print("BUG #3 FIX: Betulkan logik Lulus Bersyarat dalam updateCharts")
print("=" * 60)

# Fix Bug #3: Lulus Bersyarat logic in updateCharts
# Current (wrong): else if (rawTot >= 0.50) passCond++;
# Fixed (correct): use proper thresholds - kawad >= 0.70, avg(bm,ikatan) >= 0.50, overall >= 0.70

old_chart_logic = """          if (c.statusText === 'LLL') passLLL++;

            else if (rawTot >= 0.50) passCond++;

            else failCount++;"""

new_chart_logic = """          if (c.statusText === 'LLL') passLLL++;

            else if (rawK >= 0.70 && rawBM >= 0.50 && rawIK >= 0.50 && rawTot >= 0.70) passCond++;

            else failCount++;"""

if old_chart_logic in html:
    html = html.replace(old_chart_logic, new_chart_logic)
    print("✅ Bug #3 SELESAI: Logik Lulus Bersyarat diperbetulkan")
    print("   Sebelum: else if (rawTot >= 0.50) passCond++")
    print("   Selepas: semak semua threshold (kawad ≥ 70%, BM ≥ 50%, Ikatan ≥ 50%, Overall ≥ 70%)")
else:
    print("⚠️  Logik lama tidak dijumpai - mungkin sudah dibetulkan atau format berbeza")
    # Try alternate format
    idx = html.find('else if (rawTot >= 0.50) passCond++')
    if idx != -1:
        print(f"  Dijumpai format alternatif di {idx}")
        html = html.replace(
            'else if (rawTot >= 0.50) passCond++',
            'else if (rawK >= 0.70 && rawBM >= 0.50 && rawIK >= 0.50 && rawTot >= 0.70) passCond++'
        )
        print("  ✅ Diperbetulkan")

print()
print("=" * 60)
print("BUG #1 FIX: Tambah nota dalam Code.gs (filter baris kosong)")
print("=" * 60)

# For Code.gs - add filter for empty rows
with open(r'03_Google_Apps_Script\Code.gs', 'r', encoding='utf-8') as f:
    code_gs = f.read()

old_dataTKRS = """  var dataTKRS = sheetTKRS && sheetTKRS.getLastRow() >= 3 ? sheetTKRS.getRange(3, 1, sheetTKRS.getLastRow() - 2, 12).getValues() : [];
  var dataKRS = sheetKRS && sheetKRS.getLastRow() >= 3 ? sheetKRS.getRange(3, 1, sheetKRS.getLastRow() - 2, 12).getValues() : [];"""

new_dataTKRS = """  // Ambil data dan tapis baris kosong (kolum Sekolah mestilah ada nilai)
  var rawDataTKRS = sheetTKRS && sheetTKRS.getLastRow() >= 3 ? sheetTKRS.getRange(3, 1, sheetTKRS.getLastRow() - 2, 12).getValues() : [];
  var rawDataKRS = sheetKRS && sheetKRS.getLastRow() >= 3 ? sheetKRS.getRange(3, 1, sheetKRS.getLastRow() - 2, 12).getValues() : [];
  // PEMBETULAN: Tapis baris kosong supaya getLastRow() tidak mengira baris kosong sebagai calon
  var dataTKRS = rawDataTKRS.filter(function(row) { return row[3] && String(row[3]).trim() !== ''; });
  var dataKRS = rawDataKRS.filter(function(row) { return row[3] && String(row[3]).trim() !== ''; });"""

if old_dataTKRS in code_gs:
    code_gs = code_gs.replace(old_dataTKRS, new_dataTKRS)
    print("✅ Bug #1 SELESAI: Filter baris kosong ditambah dalam Code.gs")
    print("   getLastRow() kini tidak akan kira baris kosong sebagai calon")
else:
    print("⚠️  Kod lama tidak dijumpai persis - semak manual")
    print("   Cari: dataTKRS = sheetTKRS && sheetTKRS.getLastRow()")

# Save Code.gs
with open(r'03_Google_Apps_Script\Code.gs', 'w', encoding='utf-8') as f:
    f.write(code_gs)
print("   Code.gs disimpan")

print()
print("=" * 60)
print("BUG #2 INFO: GitHub Pages tidak auto-sync")
print("=" * 60)
print("ℹ️  Bug ini TIDAK boleh dibaiki automatik - ia sifat bina")
print("   Penyelesaian: Jalankan skrip eksport dan push setiap kali data berubah")
print("   Atau: GitHub Actions untuk auto-sync (projek masa depan)")

# Save the fixed HTML
with open(r'03_Google_Apps_Script\Index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print()
print("=" * 60)
print("SELESAI: Semua pembetulan disimpan ke Index.html dan Code.gs")
print("=" * 60)
