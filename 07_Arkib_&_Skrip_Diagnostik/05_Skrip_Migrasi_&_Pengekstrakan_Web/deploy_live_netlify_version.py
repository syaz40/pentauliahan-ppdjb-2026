import os
import re
import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

print("Reading downloaded live Netlify HTML...")
with open('07_Arkib_&_Skrip_Diagnostik/05_Skrip_Migrasi_&_Pengekstrakan_Web/live_netlify_download.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix exportToCSV raw newlines
bad_csv_header = "let csv = 'No Giliran,Nama Calon,Unit,Jantina,Kumpulan,Sekolah,Jumlah Markah,Status Keputusan\n\n';"
good_csv_header = "let csv = 'No Giliran,Nama Calon,Unit,Jantina,Kumpulan,Sekolah,Jumlah Markah,Status Keputusan\\n';"

bad_csv_row = 'csv += `"${c.noGiliran}","${c.nama}","${c.unit}","${c.jantina}","${c.kumpulan}","${c.sekolah}","${c.overall}","${c.statusText}"\n\n`;'
good_csv_row = 'csv += `"${c.noGiliran}","${c.nama}","${c.unit}","${c.jantina}","${c.kumpulan}","${c.sekolah}","${c.overall}","${c.statusText}"\\n`;'

html = html.replace(bad_csv_header, good_csv_header)
html = html.replace(bad_csv_row, good_csv_row)

# 2. Fix scriptlet injection for GAS and Netlify
scriptlet_pattern = r'const SERVER_DATA = <\?!=.*?\?>;'

gas_hydration = """<!-- SERVER DATA PAYLOAD FOR GOOGLE APPS SCRIPT -->
  <script id="server-data-payload" type="application/json">
    <?!= typeof initialData !== 'undefined' && initialData ? JSON.stringify(initialData) : 'null' ?>
  </script>"""

netlify_hydration = """<!-- SERVER DATA PAYLOAD FOR NETLIFY -->
  <script id="server-data-payload" type="application/json">
    null
  </script>"""

reader_logic = """let SERVER_DATA = null;
      try {
        const payloadEl = document.getElementById('server-data-payload');
        const payloadText = payloadEl ? payloadEl.textContent.trim() : '';
        if (payloadText && payloadText !== 'null') {
          SERVER_DATA = JSON.parse(payloadText);
        }
      } catch (e) {
        SERVER_DATA = null;
      }"""

# Insert hydration payload before <script> in both files
html_gas = html.replace('<script>', gas_hydration + '\n  <script>', 1)
html_gas = re.sub(scriptlet_pattern, reader_logic, html_gas)

html_netlify = html.replace('<script>', netlify_hydration + '\n  <script>', 1)
html_netlify = re.sub(scriptlet_pattern, reader_logic, html_netlify)

# Save GAS Index.html
with open('03_Google_Apps_Script/Index.html', 'w', encoding='utf-8') as f:
    f.write(html_gas)
print(f"✓ Saved 03_Google_Apps_Script/Index.html ({len(html_gas):,} bytes)")

# Save Netlify index.html
with open('04_Web_App_Netlify/index.html', 'w', encoding='utf-8') as f:
    f.write(html_netlify)
print(f"✓ Saved 04_Web_App_Netlify/index.html ({len(html_netlify):,} bytes)")

# Verify syntax on both files
print("\n--- SYNTAX VERIFICATION ---")
for fname in ['03_Google_Apps_Script/Index.html', '04_Web_App_Netlify/index.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        fc = f.read()
    scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', fc, re.DOTALL)
    for i, sc in enumerate(scripts):
        clean_sc = re.sub(r'<\?!=.*?\?>', 'null', sc)
        if len(clean_sc.strip()) == 0 or clean_sc.strip() == 'null':
            continue
        with open('temp_check.js', 'w', encoding='utf-8') as tf:
            tf.write(clean_sc)
        res = subprocess.run(['node', '--check', 'temp_check.js'], capture_output=True, text=True)
        print(f"{fname} script #{i+1}:", "VALID (0 SYNTAX ERRORS!)" if res.returncode == 0 else f"ERROR: {res.stderr.strip()}")
        if os.path.exists('temp_check.js'):
            os.remove('temp_check.js')
