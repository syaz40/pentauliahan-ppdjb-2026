import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r'03_Google_Apps_Script\Index.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
main_script = scripts[-1] if scripts else ''

# Find the full recalculateAllStats function - get the key isPass logic
print('=== isPass LOGIC in recalculateAllStats ===')
idx = main_script.find('recalculateAllStats() {')
if idx == -1:
    idx = main_script.find('recalculateAllStats()')
if idx != -1:
    # Get 3000 chars
    body = main_script[idx:idx+4000]
    print(body)

print()
print('=== SLIDER onChange HANDLER ===')
idx2 = main_script.find('range-wajaran-min-kawad')
if idx2 != -1:
    # Find the addEventListener around it
    start = max(0, idx2-500)
    print(main_script[start:idx2+500])

print()
print('=== getActiveWajaranConfig in Code.gs ===')
with open(r'03_Google_Apps_Script\Code.gs', 'r', encoding='utf-8') as f:
    code = f.read()
idx3 = code.find('function getActiveWajaranConfig')
if idx3 != -1:
    end = code.find('\nfunction ', idx3+10)
    print(code[idx3:end if end != -1 else idx3+1000])
