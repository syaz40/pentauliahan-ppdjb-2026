import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r'03_Google_Apps_Script\Code.gs', 'r', encoding='utf-8') as f:
    code = f.read()

# Find getDashboardData function
idx = code.find('function getDashboardData')
if idx != -1:
    # Find end of function
    end = code.find('\nfunction ', idx+10)
    body = code[idx:end if end != -1 else idx+5000]
    print("=== getDashboardData() ===")
    print(body)
else:
    print("getDashboardData() NOT FOUND as standalone function")
    # Find where it's used
    for m in re.finditer(r'getDashboardData', code):
        print(f"Occurrence at {m.start()}: {code[m.start()-30:m.start()+200]}")
        print("---")
