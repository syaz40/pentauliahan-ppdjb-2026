import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('03_Google_Apps_Script/Index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find any overlays / modals / dialogs
overlays = re.findall(r'<div[^>]*class=["\'][^"\']*(?:overlay|dialog|backdrop|popup|drawer)[^"\']*["\'][^>]*>', html)
print("Overlay tags in HTML:", overlays)

# Find CSS classes defined for dialogs/modals
classes = re.findall(r'\.([a-zA-Z0-9_-]*(?:modal|dialog|overlay|popup|toast)[a-zA-Z0-9_-]*)\s*\{', html)
print("CSS Classes related to modal/toast:", set(classes))
