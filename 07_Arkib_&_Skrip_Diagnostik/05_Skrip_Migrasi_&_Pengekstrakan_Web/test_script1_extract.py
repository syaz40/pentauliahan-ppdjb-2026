with open('Index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

script1 = ''.join(lines[3088:8977])
with open('test_script1.js', 'w', encoding='utf-8') as f:
    f.write(script1)

print("Wrote test_script1.js, length:", len(script1))
