import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Check tab-candidates section
idx = html.find('id="tab-candidates"')
idx_end = html.find('</section>', idx)
print("=== TAB CANDIDATES SECTION ===")
print(html[idx:idx_end])

# 2. Check openCandidateSlip function and modal-slip-backdrop
print("\n=== SLIP MODAL BACKDROP IN HTML ===")
if 'id="modal-slip-backdrop"' in html:
    idx_m = html.find('id="modal-slip-backdrop"')
    print(html[idx_m-50:idx_m+1500])
else:
    print("WARNING: modal-slip-backdrop NOT FOUND in HTML!")

# 3. Check openCandidateSlip function in JS
print("\n=== openCandidateSlip in JS ===")
idx_fn = html.find('openCandidateSlip')
print(html[idx_fn-50:idx_fn+2000])
