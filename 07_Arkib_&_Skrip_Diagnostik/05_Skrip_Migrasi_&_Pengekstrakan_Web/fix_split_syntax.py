import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Fixing split('\\n') escape in live sync logic...")

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix literal newline inside split
html = html.replace("const lines = csvText.split('\n');", "const lines = csvText.split(/\\r?\\n/);")
html = html.replace("const lines = csvText.split('\r\n');", "const lines = csvText.split(/\\r?\\n/);")

# If still broken, let's regex replace the parseCsvLines function
parse_fn_old = r'const parseCsvLines = \(csvText\) => \{[\s\S]*?return lines\.slice\(1\)'
parse_fn_new = """const parseCsvLines = (csvText) => {
              const lines = csvText.split(/\\r?\\n/).filter(l => l.trim().length > 0);
              if (lines.length <= 1) return [];
              return lines.slice(1)"""

html = re.sub(parse_fn_old, parse_fn_new, html)

# Save Netlify file
with open('04_Web_App_Netlify/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Saved clean 04_Web_App_Netlify/index.html ({len(html):,} bytes)")

# Prepare and save GAS Index.html
html_gas = html.replace(
    '<script id="server-data-payload" type="application/json">\n    null\n  </script>',
    '<script id="server-data-payload" type="application/json">\n    <?!= typeof initialData !== \'undefined\' && initialData ? JSON.stringify(initialData) : \'null\' ?>\n  </script>'
)

with open('03_Google_Apps_Script/Index.html', 'w', encoding='utf-8') as f:
    f.write(html_gas)
print(f"✓ Saved clean 03_Google_Apps_Script/Index.html ({len(html_gas):,} bytes)")
