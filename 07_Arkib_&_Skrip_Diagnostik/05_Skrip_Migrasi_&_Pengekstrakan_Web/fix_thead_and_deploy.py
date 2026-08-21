import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Ensuring <thead id='table-candidates-head'> and robust thead selection in JS...")

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the table thead markup
old_tbl_markup = """        <table class="styled-table" id="table-candidates">
          <thead>
            <tr>
              <th>No Badan</th>
              <th>Nama Calon</th>
              <th>Unit</th>
              <th>Sekolah</th>
              <th>Jumlah Markah</th>
              <th>Status Keputusan</th>
            </tr>
          </thead>"""

new_tbl_markup = """        <table class="styled-table" id="table-candidates">
          <thead id="table-candidates-head">
            <tr>
              <th style="text-align:center; width:140px;">No Badan</th>
              <th style="text-align:left;">Nama Calon</th>
              <th style="text-align:center; width:90px;">Unit</th>
              <th style="text-align:left;">Sekolah</th>
              <th style="text-align:center; width:140px;">Jumlah Markah</th>
              <th style="text-align:center; width:160px;">Status Keputusan</th>
            </tr>
          </thead>"""

html = html.replace(old_tbl_markup, new_tbl_markup)

# 2. Ensure renderCandidatesTable uses querySelector fallback
html = html.replace(
    "const thead = document.getElementById('table-candidates-head');",
    "const thead = document.getElementById('table-candidates-head') || document.querySelector('#table-candidates thead');"
)

# Save Netlify file
with open('04_Web_App_Netlify/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Saved 04_Web_App_Netlify/index.html ({len(html):,} bytes)")

# Prepare and save GAS Index.html
html_gas = html.replace(
    '<script id="server-data-payload" type="application/json">\n    null\n  </script>',
    '<script id="server-data-payload" type="application/json">\n    <?!= typeof initialData !== \'undefined\' && initialData ? JSON.stringify(initialData) : \'null\' ?>\n  </script>'
)

with open('03_Google_Apps_Script/Index.html', 'w', encoding='utf-8') as f:
    f.write(html_gas)
print(f"✓ Saved 03_Google_Apps_Script/Index.html ({len(html_gas):,} bytes)")
