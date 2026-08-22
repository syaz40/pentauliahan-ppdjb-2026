import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r'03_Google_Apps_Script\Index.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
main_script = scripts[-1] if scripts else ""

# Write the main script to a file for inspection
with open('_main_script_extracted.js', 'w', encoding='utf-8') as f:
    f.write(main_script)

print(f"Script length: {len(main_script)}")

# Find all chart-related function bodies by line range
lines = main_script.split('\n')
init_chart_start = None
update_chart_start = None

for i, line in enumerate(lines):
    if 'initCharts()' in line and 'initCharts():' not in line:
        init_chart_start = i
        print(f"initCharts starts at script line {i}")
    if 'updateCharts()' in line and 'updateCharts():' not in line and init_chart_start is not None and i > init_chart_start:
        update_chart_start = i
        print(f"updateCharts starts at script line {i}")

# Show the full initCharts and full updateCharts
if init_chart_start and update_chart_start:
    init_lines = lines[init_chart_start:update_chart_start]
    print("\n=== initCharts() FULL BODY ===")
    print('\n'.join(init_lines))
    
    # updateCharts -- find its end (next method)
    next_method = None
    for i, line in enumerate(lines[update_chart_start+1:], start=update_chart_start+1):
        if re.match(r'\s{6}[a-zA-Z]+\s*\(', line) and i > update_chart_start + 10:
            next_method = i
            break
    
    update_lines = lines[update_chart_start:next_method if next_method else update_chart_start+200]
    print("\n=== updateCharts() FULL BODY ===")
    print('\n'.join(update_lines))
