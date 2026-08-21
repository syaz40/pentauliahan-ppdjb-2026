with open('Index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[3080:8980], start=3081):
    if '<' in line or '>' in line or '<?' in line or '?>' in line:
        print(f"Line {i}: {line.strip()}")
