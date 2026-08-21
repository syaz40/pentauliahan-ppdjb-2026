import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Clean replacement of parseCsvLines block using raw string
new_block = r'''parseCsvLines = (csvText) => {
              const cleanText = csvText.split(/\r?\n/).filter(function(l) { return l.trim().length > 0; });
              if (cleanText.length <= 1) return [];
              return cleanText.slice(1).map(function(line) {
                const cols = line.split(/,(?=(?:(?:[^\"]*\"){2})*[^\"]*$)/).map(function(c) { return c.replace(/^\"|\"$/g, '').trim(); });
                return cols;
              });
            };'''

pattern = r'parseCsvLines\s*=\s*\(csvText\)\s*=>\s*\{[\s\S]*?return cols;\s*\}\);\s*\};'
html = re.sub(pattern, new_block, html)

with open('04_Web_App_Netlify/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

html_gas = html.replace(
    '<script id="server-data-payload" type="application/json">\n    null\n  </script>',
    '<script id="server-data-payload" type="application/json">\n    <?!= typeof initialData !== \'undefined\' && initialData ? JSON.stringify(initialData) : \'null\' ?>\n  </script>'
)

with open('03_Google_Apps_Script/Index.html', 'w', encoding='utf-8') as f:
    f.write(html_gas)

print("Saved clean index files.")
