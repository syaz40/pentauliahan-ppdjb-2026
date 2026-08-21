import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('03_Google_Apps_Script/Index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("--- SECTIONS & IDS IN HTML BODY ---")
sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\'][^>]*>', html)
print("Sections with IDs:", sections)

div_tabs = re.findall(r'<div[^>]*id=["\'](tab-[^"\']+)["\'][^>]*>', html)
print("Divs starting with tab-:", div_tabs)

nav_tabs = re.findall(r'data-tab=["\']([^"\']+)["\']', html)
print("Data-tab navigation buttons:", nav_tabs)

js_tab_handling = re.findall(r'tab[a-zA-Z0-9_]*\.addEventListener|switchTab|showTab|tab-pane|tab-content', html)
print("JS tab handling keywords:", set(js_tab_handling))
