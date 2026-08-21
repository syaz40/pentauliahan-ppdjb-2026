import re

with open(r'03_Google_Apps_Script\Index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Has nav-scroll-container:", 'nav-scroll-container' in html)
print("Has table-responsive:", 'table-responsive' in html or 'table-container' in html)

# Check candidates table wrapper
idx_cands = html.find('id="table-candidates"')
if idx_cands != -1:
    print("\nCandidates table surrounding markup:")
    print(html[idx_cands-150:idx_cands+250])

# Check nav wrapper
idx_nav = html.find('class="tab-nav-group"')
if idx_nav != -1:
    print("\nNav surrounding markup:")
    print(html[idx_nav-150:idx_nav+250])
