import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('extracted_styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's print the entire CSS in sections or examine specific parts
lines = css.split('\n')
print(f"Total CSS lines: {len(lines)}")

# Let's look for @media rules
import re
print("\n--- Existing @media rules ---")
for m in re.finditer(r'@media[^{]+{(.*?)\n    }', css, re.DOTALL):
    print(m.group(0))
