import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('03_Google_Apps_Script/Index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("--- MODALS IN INDEX.HTML ---")
modals = re.findall(r'<div[^>]*class=["\'][^"\']*modal[^"\']*["\'][^>]*id=["\']([^"\']+)["\']', html)
modals_alt = re.findall(r'<div[^>]*id=["\']([^"\']+)["\'][^>]*class=["\'][^"\']*modal[^"\']*["\']', html)
all_modals = set(modals + modals_alt)
print(f"Modals found ({len(all_modals)}):", all_modals)

# Check modal openers in JS
openers = re.findall(r'document\.getElementById\(["\'](modal-[a-zA-Z0-9_-]+|admin-[a-zA-Z0-9_-]+|slip-[a-zA-Z0-9_-]+)["\']\)', html)
print(f"Modal related JS queries ({len(openers)}):", set(openers))
