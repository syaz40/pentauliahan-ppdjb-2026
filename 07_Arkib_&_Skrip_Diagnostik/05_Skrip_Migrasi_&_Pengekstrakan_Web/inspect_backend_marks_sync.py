import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('03_Google_Apps_Script/Code.gs', 'r', encoding='utf-8') as f:
    code = f.read()

idx = code.find('getDashboardData()')
print("=== getDashboardData in Code.gs ===")
print(code[idx:idx+2500])

idx_sync = code.find('syncAndValidateAnalysis')
print("\n=== syncAndValidateAnalysis in Code.gs ===")
print(code[idx_sync:idx_sync+2500])
