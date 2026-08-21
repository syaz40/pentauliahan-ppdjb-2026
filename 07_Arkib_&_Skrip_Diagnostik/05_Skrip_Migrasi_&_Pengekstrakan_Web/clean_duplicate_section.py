import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Cleaning duplicate section...")

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

delimiter = '<section class="tab-content" id="tab-top-results">'
parts = html.split(delimiter)
print(f"Found {len(parts)-1} instances of tab-top-results section")

if len(parts) > 2:
    # First section content
    first_sec = parts[1].split('</section>')[0] + '</section>'
    # Rest of HTML after all duplicate sections
    rest = parts[-1].split('</section>', 1)[1]
    html = parts[0] + delimiter + first_sec + rest
    print("✓ Merged to single tab-top-results section")

with open('04_Web_App_Netlify/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

html_gas = html.replace(
    '<script id="server-data-payload" type="application/json">\n    null\n  </script>',
    '<script id="server-data-payload" type="application/json">\n    <?!= typeof initialData !== \'undefined\' && initialData ? JSON.stringify(initialData) : \'null\' ?>\n  </script>'
)

with open('03_Google_Apps_Script/Index.html', 'w', encoding='utf-8') as f:
    f.write(html_gas)

print(f"✓ Saved Netlify ({len(html):,} bytes) and GAS ({len(html_gas):,} bytes)")
