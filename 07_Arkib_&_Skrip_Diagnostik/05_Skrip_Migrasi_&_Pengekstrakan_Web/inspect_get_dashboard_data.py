import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('03_Google_Apps_Script/Code.gs', 'r', encoding='utf-8') as f:
    code = f.read()

idx = code.find('function getDashboardData()')
print("=== function getDashboardData() ===")
print(code[idx:idx+3500])
