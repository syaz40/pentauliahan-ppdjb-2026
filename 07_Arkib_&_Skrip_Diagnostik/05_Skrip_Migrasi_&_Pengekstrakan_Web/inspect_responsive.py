import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import re

with open(r'03_Google_Apps_Script\Index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract tab-analytics section
start = text.find('id="tab-analytics"')
end = text.find('id="tab-candidates"', start)
print("=== TAB ANALYTICS FULL HTML ===")
print(text[start:end])

# Also check header and nav
header_match = re.search(r'<header.*?</header>', text, re.DOTALL)
if header_match:
    print("\n=== HEADER HTML ===")
    print(header_match.group(0))

nav_match = re.search(r'<nav.*?</nav>', text, re.DOTALL)
if nav_match:
    print("\n=== NAV HTML ===")
    print(nav_match.group(0))
