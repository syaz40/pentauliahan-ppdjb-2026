import re

# 1. Update Code.gs
code_path = r"i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\03_Google_Apps_Script\Code.gs"
with open(code_path, "r", encoding="utf-8") as f:
    code = f.read()

new_doget = """function doGet(e) {
  if (e && e.parameter && e.parameter.format === 'json') {
    var data = getDashboardData();
    return ContentService.createTextOutput(JSON.stringify(data))
      .setMimeType(ContentService.MimeType.JSON);
  }
  
  var template = HtmlService.createTemplateFromFile('Index');
  try {
    template.initialData = getDashboardData();
  } catch (err) {
    template.initialData = null;
  }
  return template.evaluate()
    .setTitle('Dashboard Pentauliahan Pangkat & Analisis Keputusan — PPD Johor Bahru 2026')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}"""

code = re.sub(r'function doGet\(e\)\s*\{.*?return\s+(?:template\.evaluate\(\)|HtmlService\.createHtmlOutputFromFile\(\'Index\'\)).*?\}', new_doget, code, flags=re.DOTALL)

with open(code_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated Code.gs with initialData injection!")

# 2. Update Index.html
index_path = r"i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\03_Google_Apps_Script\Index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Prepend SERVER_DATA injection right after <script>
server_injection = """<script>
  // =========================================================================
  // SUNTIKAN DATA MASA NYATA DARI GOOGLE SHEET (SERVER-SIDE HYDRATION)
  // =========================================================================
  const SERVER_DATA = <?!= typeof initialData !== 'undefined' && initialData ? JSON.stringify(initialData) : 'null' ?>;
  if (SERVER_DATA && SERVER_DATA.candidates && SERVER_DATA.candidates.length > 0) {
    window.RAW_CANDIDATES_DATA = SERVER_DATA.candidates;
    console.log('✅ Berjaya menyuntik ' + SERVER_DATA.candidates.length + ' data calon terus dari Google Sheet!');
  }
"""

html = html.replace("<script>\n", server_injection, 1)

# Now update App.init in Index.html to utilize SERVER_DATA
old_init_regex = r'init\(\)\s*\{.*?console\.log\(\'🏛️ Web App Pentauliahan KRS/TKRS JB 2026 sedia sepenuhnya!\'\);.*?\}'

new_init_code = """init() {
    try {
      console.log('🚀 Memulakan inisialisasi Web App Pentauliahan...');
      
      // 1. PASANG SEMUA EVENT LISTENER TERLEBIH DAHULU
      this.setupEventListeners();

      // 2. Ambil data calon daripada Server Data (Live Google Sheet) atau Local Fallback
      let rawList = [];
      if (typeof SERVER_DATA !== 'undefined' && SERVER_DATA && SERVER_DATA.candidates && SERVER_DATA.candidates.length > 0) {
        rawList = SERVER_DATA.candidates;
        if (SERVER_DATA.thresholds) {
          this.state.currentThresholds = {
            kawad: SERVER_DATA.thresholds.thresholdKawad,
            ikatan: SERVER_DATA.thresholds.thresholdIkatan,
            overall: SERVER_DATA.thresholds.thresholdOverall,
            wajaranKawad: SERVER_DATA.thresholds.wajaranKawad,
            wajaranBantuMula: SERVER_DATA.thresholds.wajaranBantuMula,
            wajaranIkatan: SERVER_DATA.thresholds.wajaranIkatan
          };
        }
        console.log('📊 Memproses ' + rawList.length + ' calon dari Google Sheet...');
      } else if (typeof RAW_CANDIDATES_DATA !== 'undefined' && RAW_CANDIDATES_DATA.length > 0) {
        rawList = RAW_CANDIDATES_DATA;
      }

      if (rawList.length > 0 && typeof AnalyticsEngine !== 'undefined') {
        this.state.candidates = AnalyticsEngine.processCandidates(rawList, this.state.currentThresholds);
      }
      this.state.lastSyncTime = new Date();
      
      // 3. Render keseluruhan UI & KPI Cards (305 Calon, Sekolah, dll)
      this.renderAll();
      
      // 4. Mulakan auto-sync berskala berkala
      this.startAutoSync(30);

      console.log('🏛️ Web App Pentauliahan KRS/TKRS JB 2026 sedia sepenuhnya dengan ' + this.state.candidates.length + ' calon!');
    } catch (err) {
      console.error('Ralat semasa inisialisasi App:', err);
    }
  },"""

html = re.sub(old_init_regex, new_init_code, html, flags=re.DOTALL)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated Index.html with live server hydration!")
