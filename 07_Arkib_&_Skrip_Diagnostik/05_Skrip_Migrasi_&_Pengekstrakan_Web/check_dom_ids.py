import re

with open(r'03_Google_Apps_Script\Index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all element IDs in HTML
html_ids = set(re.findall(r'id=["\']([^"\']+)["\']', content))

# Find all document.getElementById in script
js_get_ids = re.findall(r'document\.getElementById\(["\']([^"\']+)["\']\)', content)

print(f"Total HTML IDs defined: {len(html_ids)}")
print(f"Total getElementById calls: {len(js_get_ids)}")

missing_ids = []
for gid in set(js_get_ids):
    if gid not in html_ids:
        missing_ids.append(gid)

print("\nMissing IDs called in getElementById:")
lines = content.split('\n')
for m in sorted(missing_ids):
    print(f"  - ID: '{m}'")
    for idx, line in enumerate(lines):
        if f"document.getElementById('{m}')" in line or f'document.getElementById("{m}")' in line:
            print(f"      Line {idx+1}: {line.strip()}")
