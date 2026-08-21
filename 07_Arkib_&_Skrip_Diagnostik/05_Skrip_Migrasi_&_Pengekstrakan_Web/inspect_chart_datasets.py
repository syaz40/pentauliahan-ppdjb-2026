import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('this.state.charts.modulePerf.data.datasets[0].data =')
print("=== chart module dataset assignment ===")
print(html[idx-100:idx+800])
