import re

with open(r'03_Google_Apps_Script\Index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check .nav-wrapper and .nav-inner in CSS
for cls in ['.nav-wrapper', '.nav-inner', '.tab-nav-group']:
    match = re.search(r'(' + re.escape(cls) + r'\s*\{[^}]+\})', html)
    if match:
        print(match.group(1))
