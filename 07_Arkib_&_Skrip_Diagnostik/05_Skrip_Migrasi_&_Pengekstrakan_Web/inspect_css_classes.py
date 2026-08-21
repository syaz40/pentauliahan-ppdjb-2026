import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import re

with open(r'03_Google_Apps_Script\Index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the entire structure of the CSS to see classes
style_match = re.search(r'<style[^>]*>(.*?)</style>', text, re.DOTALL | re.IGNORECASE)
css = style_match.group(1) if style_match else ""

# Search for all classes defined
classes = set(re.findall(r'\.([a-zA-Z0-9_\-]+)\s*\{', css))
print(f"Total CSS classes: {len(classes)}")
print("Sample classes:", sorted(list(classes))[:40])
