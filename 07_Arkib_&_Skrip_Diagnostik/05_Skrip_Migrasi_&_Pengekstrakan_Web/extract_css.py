import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import re

with open(r'03_Google_Apps_Script\Index.html', 'r', encoding='utf-8') as f:
    text = f.read()

style_match = re.search(r'<style[^>]*>(.*?)</style>', text, re.DOTALL | re.IGNORECASE)
if style_match:
    css = style_match.group(1)
    with open('extracted_styles.css', 'w', encoding='utf-8') as sf:
        sf.write(css)
    print("Saved extracted_styles.css, length:", len(css))
