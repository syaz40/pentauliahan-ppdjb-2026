import os

base_dir = r"i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\05_Web_Application_Dashboard"

with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

with open(os.path.join(base_dir, "css", "style.css"), "r", encoding="utf-8") as f:
    css = f.read()

with open(os.path.join(base_dir, "js", "data.js"), "r", encoding="utf-8") as f:
    js_data = f.read()

with open(os.path.join(base_dir, "js", "analytics.js"), "r", encoding="utf-8") as f:
    js_analytics = f.read()

with open(os.path.join(base_dir, "js", "charts.js"), "r", encoding="utf-8") as f:
    js_charts = f.read()

with open(os.path.join(base_dir, "js", "app.js"), "r", encoding="utf-8") as f:
    js_app = f.read()

# Replace <link rel="stylesheet" href="css/style.css"> with inline <style>
style_tag = f"<style>\n{css}\n</style>"
html = html.replace('<link rel="stylesheet" href="css/style.css">', style_tag)

# Replace script tags at the bottom with one single consolidated script block
script_references = """  <script src="js/data.js"></script>
  <script src="js/analytics.js"></script>
  <script src="js/charts.js"></script>
  <script src="js/app.js"></script>"""

# Add explicit window attachments for sandboxed environment
globals_safety = """
// Jaminan Global Object dalam persekitaran Google Apps Script Sandbox
window.RAW_CANDIDATES_DATA = typeof RAW_CANDIDATES_DATA !== 'undefined' ? RAW_CANDIDATES_DATA : [];
window.RUBRICS_CONFIG = typeof RUBRICS_CONFIG !== 'undefined' ? RUBRICS_CONFIG : {};
"""

combined_js = f"""<script>
{js_data}

{globals_safety}

{js_analytics}

{js_charts}

{js_app}
</script>"""

if script_references in html:
    html = html.replace(script_references, combined_js)
else:
    print("Script references not found exactly, doing regex replace")
    import re
    html = re.sub(r'<script src="js/data\.js"></script>.*?<script src="js/app\.js"></script>', combined_js, html, flags=re.DOTALL)

out_path = r"i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\03_Google_Apps_Script\Index.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Generated 100% PURE Web App Index.html successfully!")
print("File size:", len(html))
