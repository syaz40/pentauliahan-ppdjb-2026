import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r'03_Google_Apps_Script\Index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find tab-analytics
target = 'id="tab-analytics"'
idx = html.find(target)
if idx == -1:
    target = "id='tab-analytics'"
    idx = html.find(target)

print(f"Found {target!r} at {idx}")

if idx != -1:
    section = html[idx:idx+60000]
    with open('_analisis_section.html', 'w', encoding='utf-8') as f:
        f.write(section)
    print("Written to _analisis_section.html")
    print("PREVIEW (first 3000 chars):")
    print(section[:3000])
