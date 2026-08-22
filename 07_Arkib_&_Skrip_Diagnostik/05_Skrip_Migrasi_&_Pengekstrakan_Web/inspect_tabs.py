import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r'03_Google_Apps_Script\Index.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
main_script = scripts[-1] if scripts else ''

# 1. Find renderTopResults function
print('=== renderTopResults() FUNCTION ===')
idx = main_script.find('renderTopResults()')
if idx != -1:
    print(main_script[idx:idx+4000])

print()
print('=== TAB-TOP-RESULTS - ALL TABLE HEADERS ===')
idx2 = html.find('id="tab-top-results"')
if idx2 != -1:
    section = html[idx2:idx2+20000]
    # Find all <th> tags with context
    for m in re.finditer(r'<th[^>]*>(.*?)</th>', section, re.DOTALL):
        print(f'TH: {m.group(1).strip()!r}')

print()
print('=== ALL COLUMN HEADERS IN CANDIDATES TABLE ===')
idx3 = html.find('id="tab-candidates"')
if idx3 != -1:
    section3 = html[idx3:idx3+10000]
    for m in re.finditer(r'<th[^>]*>(.*?)</th>', section3, re.DOTALL):
        print(f'TH: {m.group(1).strip()!r}')
