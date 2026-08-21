import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('initCharts() {')
idx_end = html.find('bindNavEvents() {', idx)
print("=== initCharts implementation ===")
print(html[idx:idx_end])
