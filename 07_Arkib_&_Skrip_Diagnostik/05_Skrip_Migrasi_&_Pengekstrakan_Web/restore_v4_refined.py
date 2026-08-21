import os
import re
import sys
import subprocess
import json

sys.stdout.reconfigure(encoding='utf-8')

print("Refining Version 4 from backup...")

with open('07_Arkib_&_Skrip_Diagnostik/01_Backup_GAS_Terdahulu/Index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix duplicated catch block
html = html.replace('  }, catch (err) {\n      console.error(\'Ralat semasa inisialisasi App:\', err);\n    }\n  },', '  },')
html = html.replace('}, catch (err) {\n      console.error(\'Ralat semasa inisialisasi App:\', err);\n    }\n  },', '  },')

# 2. Replace all occurrences of "ambang"
replacements = [
    ('buat pelarasan wajaran (10% - 100%) dan ambang lulus bagi Kawad', 'buat pelarasan wajaran (10% - 100%) dan syarat kelulusan minimum bagi Kawad'),
    ('<!-- 2. AMBANG LULUS (10% - 100%) -->', '<!-- 2. SYARAT KELULUSAN MINIMUM (10% - 100%) -->'),
    ('2️⃣ Pelaras Ambang Kelulusan Pangkat (%)', '2️⃣ Pelaras Syarat Kelulusan Minimum Pangkat (%)'),
    ('Ambang Kawad Kaki:', 'Syarat Minimum Kawad Kaki:'),
    ('Ambang Bantu Mula + Ikatan:', 'Syarat Minimum Bantu Mula + Ikatan:'),
    ('Ambang Keseluruhan:', 'Syarat Minimum Keseluruhan:'),
    ('Tukar wajaran dan ambang di atas untuk melihat simulasi', 'Tukar wajaran dan syarat kelulusan di atas untuk melihat simulasi'),
    ('// Tetapan Ambang Lulus Lalai (Standard Rasmi PPDJB 2026)', '// Tetapan Syarat Kelulusan Minimum Lalai (Standard Rasmi PPDJB 2026)'),
    ('ikatan: 0.50, // Ambang Bantu Mula + Ikatan', 'ikatan: 0.50, // Syarat Bantu Mula + Ikatan'),
    ('• Ambang Lulus: Kawad ≥', '• Syarat Kelulusan: Kawad ≥')
]

for old, new in replacements:
    html = html.replace(old, new)

# 3. Fix scriptlet hydration block
old_script_start = """  <!-- Scripts -->
<script>
  // =========================================================================
  // SUNTIKAN DATA MASA NYATA DARI GOOGLE SHEET (SERVER-SIDE HYDRATION)
  // =========================================================================
  const SERVER_DATA = <?!= typeof initialData !== 'undefined' && initialData ? JSON.stringify(initialData) : 'null' ?>;"""

new_script_start_gas = """  <!-- Scripts -->
  <script id="server-data-payload" type="application/json">
    <?!= typeof initialData !== 'undefined' && initialData ? JSON.stringify(initialData) : 'null' ?>
  </script>

  <script>
  let SERVER_DATA = null;
  try {
    const payloadEl = document.getElementById('server-data-payload');
    const payloadText = payloadEl ? payloadEl.textContent.trim() : '';
    if (payloadText && payloadText !== 'null') {
      SERVER_DATA = JSON.parse(payloadText);
    }
  } catch (e) {
    SERVER_DATA = null;
  }"""

new_script_start_netlify = """  <!-- Scripts -->
  <script id="server-data-payload" type="application/json">
    null
  </script>

  <script>
  let SERVER_DATA = null;
  try {
    const payloadEl = document.getElementById('server-data-payload');
    const payloadText = payloadEl ? payloadEl.textContent.trim() : '';
    if (payloadText && payloadText !== 'null') {
      SERVER_DATA = JSON.parse(payloadText);
    }
  } catch (e) {
    SERVER_DATA = null;
  }"""

if old_script_start in html:
    html_gas = html.replace(old_script_start, new_script_start_gas)
    html_netlify = html.replace(old_script_start, new_script_start_netlify)
else:
    pattern = r'<!-- Scripts -->\s*<script>\s*// =========================================================================\s*// SUNTIKAN DATA MASA NYATA DARI GOOGLE SHEET \(SERVER-SIDE HYDRATION\)\s*// =========================================================================\s*const SERVER_DATA = <\?!=.*?\?>;'
    html_gas = re.sub(pattern, new_script_start_gas, html)
    html_netlify = re.sub(pattern, new_script_start_netlify, html)

# 4. Enhance CSS with corporate polish
enhanced_css = """
/* ENHANCED CORPORATE POLISH & SHARP ELEVATION */
:root {
  --primary: #1e3a8a;
  --primary-dark: #070b14;
  --primary-light: #2563eb;
  --primary-glow: rgba(37, 99, 235, 0.25);
  --accent-gold: #f59e0b;
  --accent-gold-dark: #b45309;
  --success: #10b981;
  --danger: #f43f5e;
  --bg-main: #f1f5f9;
  --card-bg: #ffffff;
  --card-border: #cbd5e1;
  --text-main: #0f172a;
  --text-muted: #64748b;
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
  --shadow-md: 0 4px 16px -2px rgba(15, 23, 42, 0.08), 0 0 0 1px rgba(203, 213, 225, 0.7);
  --shadow-lg: 0 12px 28px -4px rgba(15, 23, 42, 0.12), 0 0 0 1px rgba(203, 213, 225, 0.8);
}

body {
  background-color: var(--bg-main);
  color: var(--text-main);
}

.kpi-card, .leaderboard-card, .table-container, .tokoh-card {
  box-shadow: var(--shadow-md) !important;
  border: 1px solid var(--card-border) !important;
}

.kpi-card:hover, .leaderboard-card:hover, .tokoh-card:hover {
  box-shadow: var(--shadow-lg) !important;
}

.tab-button {
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.tab-button.active {
  box-shadow: 0 4px 14px rgba(30, 58, 138, 0.35) !important;
}

.data-table th {
  background: #f8fafc !important;
  font-weight: 800 !important;
  color: #334155 !important;
  border-bottom: 2px solid #cbd5e1 !important;
}

.data-table tr:hover {
  background-color: #eff6ff !important;
}
"""

html_gas = html_gas.replace('</style>', enhanced_css + '\n</style>')
html_netlify = html_netlify.replace('</style>', enhanced_css + '\n</style>')

# Save GAS Index.html
with open('03_Google_Apps_Script/Index.html', 'w', encoding='utf-8') as f:
    f.write(html_gas)
print(f"✓ Saved 03_Google_Apps_Script/Index.html ({len(html_gas):,} bytes)")

# Save Netlify index.html
with open('04_Web_App_Netlify/index.html', 'w', encoding='utf-8') as f:
    f.write(html_netlify)
print(f"✓ Saved 04_Web_App_Netlify/index.html ({len(html_netlify):,} bytes)")
