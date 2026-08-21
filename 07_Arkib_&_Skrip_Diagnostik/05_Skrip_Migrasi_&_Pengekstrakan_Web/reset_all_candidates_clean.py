import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Resetting all 305 candidates to clean 0.0% initial state (No mock/test data)...")

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Parse EMBEDDED_CANDIDATES
idx = html.find('const EMBEDDED_CANDIDATES = ')
idx_end = html.find(';\n', idx)
data_str = html[idx + len('const EMBEDDED_CANDIDATES = '):idx_end].strip()
candidates = json.loads(data_str)

# Clean every candidate
for c in candidates:
    c['rawKawad'] = 0.0
    c['rawBantuMula'] = 0.0
    c['rawIkatan'] = 0.0
    c['rawOverall'] = 0.0
    c['kawad'] = "0.0"
    c['bantuMula'] = "0.0"
    c['ikatan'] = "0.0"
    c['overall'] = "0.0%"
    c['statusText'] = "GGG"
    c['isPass'] = False
    c['isEvaluated'] = False
    c['catatan'] = ""
    c['isAbsent'] = False
    c['isTarikDiri'] = False
    c['isTukar'] = False

cleaned_json_str = json.dumps(candidates, ensure_ascii=False)

# Replace in html
html = html[:idx + len('const EMBEDDED_CANDIDATES = ')] + cleaned_json_str + html[idx_end:]

# 2. Direct Google Sheet Live Sync Engine in fetchLiveServerData()
# When on Netlify, fetch ANALISIS_TKRS and ANALISIS_KRS directly via GViz CSV
live_sync_js = """      async fetchLiveServerData() {
        const syncBadge = document.getElementById('sync-badge');
        if (syncBadge) syncBadge.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Menyegerak...';

        const SPREADSHEET_ID = '1_YmAJ6XVfBREx4_NDTUWRMXAL1Jgi-1vSFS2528dtW0';
        
        // Helper untuk memuat turun CSV Google Sheet
        const fetchSheetCsv = async (sheetName) => {
          try {
            const url = `https://docs.google.com/spreadsheets/d/${SPREADSHEET_ID}/gviz/tq?tqx=out:csv&sheet=${encodeURIComponent(sheetName)}`;
            const resp = await fetch(url);
            if (!resp.ok) return null;
            const text = await resp.text();
            return text;
          } catch(e) {
            return null;
          }
        };

        try {
          // 1. Cuba segerak daripada CSV Google Sheet secara langsung
          const [csvTKRS, csvKRS] = await Promise.all([
            fetchSheetCsv('ANALISIS_TKRS'),
            fetchSheetCsv('ANALISIS_KRS')
          ]);

          if (csvTKRS && csvKRS) {
            const parseCsvLines = (csvText) => {
              const lines = csvText.split('\\n').filter(l => l.trim().length > 0);
              if (lines.length <= 1) return [];
              return lines.slice(1).map(line => {
                // Parse CSV columns
                const cols = line.split(/,(?=(?:(?:[^\"]*\"){2})*[^\"]*$)/).map(c => c.replace(/^\"|\"$/g, '').trim());
                return cols;
              });
            };

            const rowsTKRS = parseCsvLines(csvTKRS);
            const rowsKRS = parseCsvLines(csvKRS);
            const allRows = [...rowsTKRS, ...rowsKRS];

            if (allRows.length > 0) {
              const scoreMap = {};
              allRows.forEach(r => {
                // Col 1: ID_PESERTA, Col 6: Kawad, Col 7: Bantu Mula, Col 8: Ikatan, Col 9: Overall, Col 10: Status, Col 11: Catatan
                const id = r[1];
                if (id) {
                  const parsePct = (val) => {
                    if (!val) return 0;
                    const clean = val.replace('%', '').trim();
                    const num = parseFloat(clean);
                    return isNaN(num) ? 0 : (num > 1 ? num / 100 : num);
                  };

                  scoreMap[id] = {
                    rawKawad: parsePct(r[6]),
                    rawBantuMula: parsePct(r[7]),
                    rawIkatan: parsePct(r[8]),
                    rawOverall: parsePct(r[9]),
                    statusText: r[10] || 'GGG',
                    catatan: r[11] || ''
                  };
                }
              });

              // Kemas kini calon dalam state
              this.state.candidates.forEach(c => {
                const id = c.noBadan || c.noGiliran;
                if (scoreMap[id]) {
                  const s = scoreMap[id];
                  c.rawKawad = s.rawKawad;
                  c.rawBantuMula = s.rawBantuMula;
                  c.rawIkatan = s.rawIkatan;
                  c.rawOverall = s.rawOverall;
                  c.kawad = (s.rawKawad * 100).toFixed(1);
                  c.bantuMula = (s.rawBantuMula * 100).toFixed(1);
                  c.ikatan = (s.rawIkatan * 100).toFixed(1);
                  c.overall = (s.rawOverall * 100).toFixed(1) + '%';
                  c.statusText = s.statusText || 'GGG';
                  c.catatan = s.catatan || '';
                  c.isEvaluated = (s.rawKawad > 0 || s.rawBantuMula > 0 || s.rawIkatan > 0);
                  if (c.catatan.includes('TIDAK HADIR')) {
                    c.isAbsent = true;
                    c.statusText = 'TH';
                  } else if (c.catatan.includes('TARIK DIRI')) {
                    c.isTarikDiri = true;
                    c.statusText = 'TARIK DIRI';
                  }
                }
              });
            }
          }

          this.parseCandidateIdentifiers();
          this.applyLocalOverrides();
          this.recalculateAllStats();
          this.renderCandidatesTable();
          this.renderTopResults();
          this.populateCandidateDropdown();
          this.updateCharts();

          if (syncBadge) {
            syncBadge.className = 'header-badge green';
            syncBadge.innerHTML = '<i class="fa-solid fa-circle-check"></i> Data Disegerak (Live)';
          }
        } catch(err) {
          console.warn('Ralat segerak langsung:', err);
          if (syncBadge) {
            syncBadge.className = 'header-badge';
            syncBadge.innerHTML = '<i class="fa-solid fa-circle-check"></i> Mod Sedia';
          }
        }
      },"""

# Replace fetchLiveServerData in html
fetch_fn_pattern = r'async fetchLiveServerData\(\)\s*\{[\s\S]*?recalculateAllStats\(\)\s*\{'
html = re.sub(fetch_fn_pattern, live_sync_js.strip() + '\n\n      recalculateAllStats() {', html)

# Save Netlify file
with open('04_Web_App_Netlify/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Saved clean 04_Web_App_Netlify/index.html ({len(html):,} bytes)")

# Prepare and save GAS Index.html
html_gas = html.replace(
    '<script id="server-data-payload" type="application/json">\n    null\n  </script>',
    '<script id="server-data-payload" type="application/json">\n    <?!= typeof initialData !== \'undefined\' && initialData ? JSON.stringify(initialData) : \'null\' ?>\n  </script>'
)

with open('03_Google_Apps_Script/Index.html', 'w', encoding='utf-8') as f:
    f.write(html_gas)
print(f"✓ Saved clean 03_Google_Apps_Script/Index.html ({len(html_gas):,} bytes)")
