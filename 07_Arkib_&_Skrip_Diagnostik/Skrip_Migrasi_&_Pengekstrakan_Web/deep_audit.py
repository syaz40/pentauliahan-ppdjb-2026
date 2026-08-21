import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== CHECKING DOM IDS AND JS LOGIC IN INDEX.HTML ===")

for path in ['03_Google_Apps_Script/Index.html', '04_Web_App_Netlify/index.html']:
    print(f"\n--- Analyzing {path} ---")
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    dom_ids_in_html = set(re.findall(r'id=["\']([a-zA-Z0-9_-]+)["\']', html))
    queried_ids = set(re.findall(r'document\.getElementById\(["\']([a-zA-Z0-9_-]+)["\']\)', html))

    missing_ids = queried_ids - dom_ids_in_html
    print(f"Total HTML IDs found: {len(dom_ids_in_html)}")
    print(f"Total queried JS IDs: {len(queried_ids)}")
    if missing_ids:
        print(f"WARNING: Queried IDs not in HTML: {missing_ids}")
    else:
        print("[OK] All queried DOM element IDs exist in HTML!")

    # Check chart destruction before render
    chart_matches = re.findall(r'new Chart\(document\.getElementById\(["\']([a-zA-Z0-9_-]+)["\']\)', html)
    print(f"Charts initialized: {chart_matches}")
    
    # Check tabs
    tab_buttons = set(re.findall(r'data-tab=["\']([a-zA-Z0-9_-]+)["\']', html))
    tab_contents = set(re.findall(r'class=["\'][^"\']*tab-pane[^"\']*["\'] id=["\']([a-zA-Z0-9_-]+)["\']', html))
    tab_contents_alt = set(re.findall(r'id=["\']([a-zA-Z0-9_-]+)["\'] class=["\'][^"\']*tab-pane[^"\']*["\']', html))
    all_tab_panes = tab_contents | tab_contents_alt
    print(f"Tabs registered in navigation: {tab_buttons}")
    print(f"Tab panes in DOM: {all_tab_panes}")
    diff_tabs = tab_buttons - all_tab_panes
    if diff_tabs:
        print(f"WARNING: Missing tab panes for buttons: {diff_tabs}")
    else:
        print("[OK] All navigation tabs have matching tab panes!")

    # Check modal IDs
    modal_ids = set(re.findall(r'class=["\'][^"\']*modal-backdrop[^"\']*["\'] id=["\']([a-zA-Z0-9_-]+)["\']', html))
    modal_ids_alt = set(re.findall(r'id=["\']([a-zA-Z0-9_-]+)["\'] class=["\'][^"\']*modal-backdrop[^"\']*["\']', html))
    all_modals = modal_ids | modal_ids_alt
    print(f"Modals in DOM: {all_modals}")

print("\n=== DOM & JS AUDIT COMPLETED ===")
