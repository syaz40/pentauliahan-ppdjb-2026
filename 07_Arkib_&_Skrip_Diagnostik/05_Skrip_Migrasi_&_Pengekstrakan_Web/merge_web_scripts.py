import re

with open('Index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate WebDashboard section
web_start_tag = "<? if (page === 'WebDashboard') { ?>"
web_start = content.find(web_start_tag)
web_end_tag = "<? } ?>"
web_end = content.find(web_end_tag, web_start)

web_part = content[web_start:web_end]

# Extract the HTML before the first <script> in WebDashboard
first_script_idx = web_part.find('<script>')
html_before_scripts = web_part[:first_script_idx]

# Combine the 4 script contents
with open('test_script1.js', 'r', encoding='utf-8') as f:
    s1 = f.read()
with open('test_script2.js', 'r', encoding='utf-8') as f:
    s2 = f.read()
with open('test_script3.js', 'r', encoding='utf-8') as f:
    s3 = f.read()
with open('test_script4.js', 'r', encoding='utf-8') as f:
    s4 = f.read()

# Fix init in s4 to ensure setupEventListeners runs FIRST and safely
# Let's inspect init() in s4
old_init = """  init() {
    try {
      console.log('🚀 Memulakan inisialisasi Web App Pentauliahan...');
      
      // 1. Muatkan data tempatan
      if (typeof RAW_CANDIDATES_DATA !== 'undefined' && typeof AnalyticsEngine !== 'undefined') {
        this.state.candidates = AnalyticsEngine.processCandidates(RAW_CANDIDATES_DATA, this.state.currentThresholds);
      }
      this.state.lastSyncTime = new Date();
      
      // 2. Render UI
      this.renderAll();
      
      // 3. Pasang semua Event Listener secara programatik (Kalis sekatan CSP Google Workspace MOE)
      this.setupEventListeners();
      
      // 4. Mulakan penyegerakan masa nyata
      this.syncLiveGoogleSheet();
      this.startAutoSync(30);

      console.log('🏛️ Web App Pentauliahan KRS/TKRS JB 2026 sedia sepenuhnya!');
    } catch (err) {
      console.error('Ralat semasa inisialisasi App:', err);
    }
  },"""

new_init = """  init() {
    try {
      console.log('🚀 Memulakan inisialisasi Web App Pentauliahan...');
      
      // 1. PASANG SEMUA EVENT LISTENER TERLEBIH DAHULU (Supaya semua butang sedia ditekan serta-merta)
      this.setupEventListeners();
      
      // 2. Muatkan data calon
      const rawData = (typeof RAW_CANDIDATES_DATA !== 'undefined') ? RAW_CANDIDATES_DATA : (window.RAW_CANDIDATES_DATA || []);
      if (rawData.length > 0 && typeof AnalyticsEngine !== 'undefined') {
        this.state.candidates = AnalyticsEngine.processCandidates(rawData, this.state.currentThresholds);
      }
      this.state.lastSyncTime = new Date();
      
      // 3. Render keseluruhan UI
      this.renderAll();
      
      // 4. Mulakan penyegerakan masa nyata secara langsung dari Google Sheet
      this.syncLiveGoogleSheet();
      this.startAutoSync(30);

      console.log('🏛️ Web App Pentauliahan KRS/TKRS JB 2026 sedia sepenuhnya!');
    } catch (err) {
      console.error('Ralat semasa inisialisasi App:', err);
    }
  },"""

if old_init in s4:
    s4 = s4.replace(old_init, new_init)
    print("Successfully replaced init() in s4!")
else:
    print("WARNING: old_init pattern not matched exactly in s4, doing regex replace!")
    s4 = re.sub(r'init\(\)\s*\{.*?console\.log\(\'🏛️ Web App Pentauliahan KRS/TKRS JB 2026 sedia sepenuhnya!\'\);.*?\}', new_init, s4, flags=re.DOTALL)

# Ensure explicit global attachment
globals_header = """
// Jaminan pembolehubah global boleh diakses dalam semua skop sandboxed
window.RAW_CANDIDATES_DATA = typeof RAW_CANDIDATES_DATA !== 'undefined' ? RAW_CANDIDATES_DATA : [];
window.RUBRICS_CONFIG = typeof RUBRICS_CONFIG !== 'undefined' ? RUBRICS_CONFIG : {};
"""

combined_js = s1 + "\n\n" + globals_header + "\n\n" + s2 + "\n\n" + s3 + "\n\n" + s4

new_web_part = html_before_scripts + "  <script>\n" + combined_js + "\n  </script>\n</body>\n</html>\n\n"

new_full_content = content[:web_start] + new_web_part + content[web_end:]

with open('Index.html', 'w', encoding='utf-8') as f:
    f.write(new_full_content)

print("Updated Index.html with unified, rock-solid script architecture!")
