import re

with open('Index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract WebDashboard
start_tag = "<? if (page === 'WebDashboard') { ?>"
start = content.find(start_tag)
if start == -1:
    print("Start tag not found!")
    exit(1)

end_tag = "<? } ?>"
end = content.find(end_tag, start)
web_content = content[start:end]

# Extract all <script>...</script>
scripts = re.findall(r'<script>(.*?)</script>', web_content, re.DOTALL)
print(f'Total script tags found: {len(scripts)}')

full_js = '\n'.join(scripts)
with open('test_web_script.js', 'w', encoding='utf-8') as f:
    f.write(full_js)

print('Wrote test_web_script.js successfully, size:', len(full_js))
