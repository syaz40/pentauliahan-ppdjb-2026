import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace parseCsvLines with standard String char code logic
new_block = """parseCsvLines = function(csvText) {
              if (!csvText) return [];
              var rawLines = csvText.split(String.fromCharCode(10));
              var lines = [];
              for (var i = 0; i < rawLines.length; i++) {
                var cleaned = rawLines[i].replace(String.fromCharCode(13), '').trim();
                if (cleaned.length > 0) lines.push(cleaned);
              }
              if (lines.length <= 1) return [];
              var result = [];
              for (var j = 1; j < lines.length; j++) {
                var line = lines[j];
                var cols = line.split(/,(?=(?:(?:[^\"]*\"){2})*[^\"]*$)/);
                var cleanedCols = [];
                for (var k = 0; k < cols.length; k++) {
                  cleanedCols.push(cols[k].replace(/^\"|\"$/g, '').trim());
                }
                result.push(cleanedCols);
              }
              return result;
            };"""

pattern = r'parseCsvLines\s*=\s*(?:function\([^)]*\)|\([^)]*\)\s*=>)\s*\{[\s\S]*?return (?:cols|result);\s*(?:\}\);|\})\s*\};'
html = re.sub(pattern, new_block, html)

with open('04_Web_App_Netlify/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

html_gas = html.replace(
    '<script id="server-data-payload" type="application/json">\n    null\n  </script>',
    '<script id="server-data-payload" type="application/json">\n    <?!= typeof initialData !== \'undefined\' && initialData ? JSON.stringify(initialData) : \'null\' ?>\n  </script>'
)

with open('03_Google_Apps_Script/Index.html', 'w', encoding='utf-8') as f:
    f.write(html_gas)

print("Saved clean index files with String.fromCharCode.")
