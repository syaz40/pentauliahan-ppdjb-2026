import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Removing (PUTERA) and (PUTERI) labels from Top 20 Tab...")

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace titles
html = html.replace('5 TERBAIK TKRS — LELAKI (PUTERA)', '5 TERBAIK TKRS — LELAKI')
html = html.replace('5 TERBAIK TKRS — PEREMPUAN (PUTERI)', '5 TERBAIK TKRS — PEREMPUAN')
html = html.replace('5 TERBAIK KRS — LELAKI (PUTERA)', '5 TERBAIK KRS — LELAKI')
html = html.replace('5 TERBAIK KRS — PEREMPUAN (PUTERI)', '5 TERBAIK KRS — PEREMPUAN')

html = html.replace('TKRS — LELAKI (PUTERA)', 'TKRS — LELAKI')
html = html.replace('TKRS — PEREMPUAN (PUTERI)', 'TKRS — PEREMPUAN')
html = html.replace('KRS — LELAKI (PUTERA)', 'KRS — LELAKI')
html = html.replace('KRS — PEREMPUAN (PUTERI)', 'KRS — PEREMPUAN')

# Save Netlify index.html
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
