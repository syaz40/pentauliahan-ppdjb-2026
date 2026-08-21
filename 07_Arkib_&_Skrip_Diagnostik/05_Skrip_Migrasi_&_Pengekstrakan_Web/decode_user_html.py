import json, re

with open(r'C:\Users\SKSRITEBRAUGURU1\.gemini\antigravity-ide\brain\03aac6d1-d22e-4888-92f8-729db7079142\.system_generated\steps\1212\content.md', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'goog\.script\.init\("((?:[^"\\]|\\.)*)"\)', content)
if m:
    raw_str = m.group(1)
    # decode hex escapes like \x7b -> {
    decoded = raw_str.encode('utf-8').decode('unicode_escape')
    data = json.loads(decoded)
    userHtml = data.get('userHtml', '')
    print(f"Decoded userHtml length: {len(userHtml)}")
    print(f"userHtml end snippet:\n{userHtml[-500:]}")
    # Search for script tags in userHtml
    scripts_in_user_html = re.findall(r'<script>(.*?)</script>', userHtml, re.DOTALL)
    print(f"Number of <script> in userHtml: {len(scripts_in_user_html)}")
    for i, s in enumerate(scripts_in_user_html):
        print(f"Script {i} length: {len(s)}")
else:
    print("Pattern not matched!")
