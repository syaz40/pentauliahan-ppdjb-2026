import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Applying 3 major user enhancements: Top 20 Tab, Admin Score Columns Fix, and Google Sheet Attendance Tab...")

# =========================================================================
# 1. UPDATE GOOGLE APPS SCRIPT (Code.gs)
# =========================================================================
with open('03_Google_Apps_Script/Code.gs', 'r', encoding='utf-8') as f:
    codegs = f.read()

old_update_fn = """function updateCandidateStatusRecord(payload, pin) {
  if (pin) {
    var auth = verifyAdminPIN(pin);
    if (!auth.success) throw new Error("PIN Admin tidak sah.");
  }
  
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  if (!ss) {
    try { ss = SpreadsheetApp.openById(SPREADSHEET_ID); } catch(e) {}
  }
  
  var noGiliran = String(payload.noGiliran || '').trim();
  var newStatus = String(payload.newStatus || '').trim();
  var newName = String(payload.newName || '').trim();
  var catatan = String(payload.catatan || '').trim();
  
  if (!noGiliran) throw new Error("No Giliran peserta diperlukan.");
  
  var isTKRS = noGiliran.toUpperCase().indexOf('TKRS') !== -1;
  var sheetName = isTKRS ? 'ANALISIS_TKRS' : 'ANALISIS_KRS';
  var listSheetName = isTKRS ? 'SENARAI_TKRS_KOPERAL' : 'SENARAI_KRS_SARJAN';
  
  var sheet = ss ? ss.getSheetByName(sheetName) : null;
  var listSheet = ss ? ss.getSheetByName(listSheetName) : null;
  var updated = false;
  
  if (sheet) {
    var data = sheet.getDataRange().getValues();
    for (var i = 2; i < data.length; i++) {
      if (String(data[i][1]).trim() === noGiliran) {
        var rowNum = i + 1;
        var finalCatatan = newStatus;
        if (catatan) finalCatatan += " - " + catatan;
        if (newName && newStatus === 'TUKAR PESERTA') {
          finalCatatan += " [GANTIAN: " + newName + "]";
          sheet.getRange(rowNum, 3).setValue(newName);
        }
        sheet.getRange(rowNum, 12).setValue(finalCatatan);
        updated = true;
        break;
      }
    }
  }
  
  if (listSheet && newName && newStatus === 'TUKAR PESERTA') {
    var listData = listSheet.getDataRange().getValues();
    for (var k = 1; k < listData.length; k++) {
      if (String(listData[k][1]).trim() === noGiliran) {
        listSheet.getRange(k + 1, 3).setValue(newName);
        break;
      }
    }
  }
  
  if (!updated && sheet) throw new Error("Peserta dengan No Giliran " + noGiliran + " tidak dijumpai.");
  return "Status peserta " + noGiliran + " berjaya dikemas kini kepada [" + newStatus + "]!";
}"""

new_update_fn = """function updateCandidateStatusRecord(payload, pin) {
  if (pin) {
    var auth = verifyAdminPIN(pin);
    if (!auth.success) throw new Error("PIN Admin tidak sah.");
  }
  
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  if (!ss) {
    try { ss = SpreadsheetApp.openById(SPREADSHEET_ID); } catch(e) {}
  }
  
  var noBadan = String(payload.noBadan || payload.noGiliran || '').trim();
  var newStatus = String(payload.newStatus || '').trim().toUpperCase();
  var newName = String(payload.newName || '').trim().toUpperCase();
  var catatan = String(payload.catatan || '').trim();
  
  if (!noBadan) throw new Error("No Badan peserta diperlukan.");
  
  var isTKRS = noBadan.toUpperCase().indexOf('TKRS') !== -1;
  var sheetName = isTKRS ? 'ANALISIS_TKRS' : 'ANALISIS_KRS';
  var listSheetName = isTKRS ? 'SENARAI_TKRS_KOPERAL' : 'SENARAI_KRS_SARJAN';
  
  var sheet = ss ? ss.getSheetByName(sheetName) : null;
  var listSheet = ss ? ss.getSheetByName(listSheetName) : null;
  var originalName = '';
  var originalSchool = '';
  var updated = false;
  
  if (sheet) {
    var data = sheet.getDataRange().getValues();
    for (var i = 2; i < data.length; i++) {
      if (String(data[i][1]).trim().toUpperCase() === noBadan.toUpperCase()) {
        var rowNum = i + 1;
        originalName = String(data[i][2]);
        originalSchool = String(data[i][5]);
        var finalCatatan = newStatus;
        if (catatan && catatan !== newStatus) finalCatatan += " - " + catatan;
        if (newName && newStatus.indexOf('TUKAR') !== -1) {
          finalCatatan += " [GANTIAN: " + newName + "]";
          sheet.getRange(rowNum, 3).setValue(newName);
        }
        sheet.getRange(rowNum, 12).setValue(finalCatatan);
        updated = true;
        break;
      }
    }
  }
  
  if (listSheet && newName && newStatus.indexOf('TUKAR') !== -1) {
    var listData = listSheet.getDataRange().getValues();
    for (var k = 1; k < listData.length; k++) {
      if (String(listData[k][1]).trim().toUpperCase() === noBadan.toUpperCase()) {
        listSheet.getRange(k + 1, 3).setValue(newName);
        break;
      }
    }
  }

  // CIPTA & REKOD KE DALAM TAB BARU KHAS: LOG_KEHADIRAN_CALON
  if (ss) {
    try {
      var logSheetName = 'LOG_KEHADIRAN_CALON';
      var logSheet = ss.getSheetByName(logSheetName);
      if (!logSheet) {
        logSheet = ss.insertSheet(logSheetName);
        var headers = [
          'TARIKH & MASA',
          'NO BADAN',
          'UNIT',
          'NAMA ASAL CALON',
          'SEKOLAH',
          'STATUS TINDAKAN / KEHADIRAN',
          'NAMA CALON BAHARU (JIKA GANTIAN)',
          'CATATAN TAMBAHAN',
          'DIKEMAS KINI OLEH'
        ];
        logSheet.appendRow(headers);
        var hRange = logSheet.getRange(1, 1, 1, headers.length);
        hRange.setBackground('#0f172a')
              .setFontColor('#ffffff')
              .setFontWeight('bold')
              .setHorizontalAlignment('center');
        logSheet.setFrozenRows(1);
      }
      
      var nowStr = Utilities.formatDate(new Date(), Session.getScriptTimeZone() || 'Asia/Kuala_Lumpur', 'yyyy-MM-dd HH:mm:ss');
      logSheet.appendRow([
        nowStr,
        noBadan,
        isTKRS ? 'TKRS' : 'KRS',
        originalName || '-',
        originalSchool || '-',
        newStatus,
        (newName && newStatus.indexOf('TUKAR') !== -1) ? newName : '-',
        catatan || '-',
        'PEGAWAI DATA TKRS JB | KAPTEN MOHD SYAZWAN BIN SULAIMAN'
      ]);
    } catch(logErr) {
      Logger.log("Ralat mencatat ke tab log kehadiran: " + logErr);
    }
  }
  
  return "Status calon " + noBadan + " berjaya dikemas kini kepada [" + newStatus + "] dan dicatat ke tab LOG_KEHADIRAN_CALON!";
}"""

codegs = codegs.replace(old_update_fn, new_update_fn)

with open('03_Google_Apps_Script/Code.gs', 'w', encoding='utf-8') as f:
    f.write(codegs)
print("✓ Updated 03_Google_Apps_Script/Code.gs with automated LOG_KEHADIRAN_CALON tab creation")

# =========================================================================
# 2. UPDATE FRONTEND (04_Web_App_Netlify/index.html & 03_Google_Apps_Script/Index.html)
# =========================================================================
with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 2.1 Update Nav Bar to 5 tabs: Maklumat Program, Analisis & Statistik, Senarai Calon, Keputusan Calon Terbaik, Tetapan Admin
old_nav = """      <nav class="tab-nav-group">
        <button class="tab-btn active" data-tab="tab-program">
          <i class="fa-solid fa-circle-info"></i> Maklumat Program
        </button>
        <button class="tab-btn" data-tab="tab-analytics">
          <i class="fa-solid fa-chart-pie"></i> Analisis & Statistik
        </button>
        <button class="tab-btn" data-tab="tab-candidates">
          <i class="fa-solid fa-users"></i> Senarai Calon & Keputusan
        </button>
        <button class="tab-btn" data-tab="tab-admin">
          <i class="fa-solid fa-sliders"></i> Tetapan Admin
        </button>
      </nav>"""

new_nav = """      <nav class="tab-nav-group">
        <button class="tab-btn active" data-tab="tab-program">
          <i class="fa-solid fa-circle-info"></i> Maklumat Program
        </button>
        <button class="tab-btn" data-tab="tab-analytics">
          <i class="fa-solid fa-chart-pie"></i> Analisis & Statistik
        </button>
        <button class="tab-btn" data-tab="tab-candidates">
          <i class="fa-solid fa-address-book"></i> Senarai Calon
        </button>
        <button class="tab-btn" data-tab="tab-top-results">
          <i class="fa-solid fa-trophy"></i> Keputusan Calon Terbaik
        </button>
        <button class="tab-btn" data-tab="tab-admin">
          <i class="fa-solid fa-sliders"></i> Tetapan Admin
        </button>
      </nav>"""

html = html.replace(old_nav, new_nav)

# 2.2 Fix Admin vs Public Score Columns styling
old_score_css = """    /* SKOR KOMPONEN HANYA MUNCUL APABILA ADMIN LOG MASUK */
    .admin-score-col {
      display: none !important;
    }
    body.is-admin .admin-score-col {
      display: table-cell !important;
    }"""

new_score_css = """    /* KAWALAN PAPARAN KOLUM MARKAH: TERSEMBUNYI UNTUK AWAM, MUNCUL KETIKA ADMIN */
    th.admin-score-col, td.admin-score-col {
      display: none;
    }
    body.is-admin th.admin-score-col {
      display: table-cell !important;
      background: #1e3a8a !important;
      color: #ffffff !important;
    }
    body.is-admin td.admin-score-col {
      display: table-cell !important;
      background: #f8fafc !important;
      font-weight: 700;
    }

    .admin-mode-indicator {
      display: none;
      background: #ecfdf5;
      border: 1px solid #6ee7b7;
      color: #065f46;
      padding: 10px 16px;
      border-radius: var(--radius-md);
      font-size: 13.5px;
      font-weight: 800;
      margin-bottom: 14px;
    }
    body.is-admin .admin-mode-indicator {
      display: flex !important;
      align-items: center;
      gap: 10px;
    }

    /* KAD PODIUM CALON TERBAIK */
    .top-category-card {
      background: #ffffff;
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-lg);
      padding: 22px;
      box-shadow: var(--shadow-sm);
      margin-bottom: 24px;
    }
    .top-category-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 2px solid var(--slate-100);
    }
    .top-category-title {
      font-size: 17px;
      font-weight: 800;
      color: var(--slate-900);
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .rank-badge {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      font-weight: 800;
      font-size: 13px;
    }
    .rank-1 { background: #fef08a; color: #854d0e; border: 1.5px solid #eab308; }
    .rank-2 { background: #e2e8f0; color: #334155; border: 1.5px solid #94a3b8; }
    .rank-3 { background: #fed7aa; color: #9a3412; border: 1.5px solid #f97316; }
    .rank-4, .rank-5 { background: #f1f5f9; color: #475569; border: 1px solid #cbd5e1; }"""

html = html.replace(old_score_css, new_score_css)

# 2.3 Add Admin Indicator bar before Candidate Table
old_candidate_table_start = """      <!-- SENARAI CALON & KEPUTUSAN TABLE -->
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>No Badan</th>
              <th>Nama Calon</th>
              <th>Jantina</th>
              <th>Unit</th>
              <th>Pangkat</th>
              <th>Sekolah</th>
              <th class="admin-score-col">Kawad (60%)</th>
              <th class="admin-score-col">B. Mula (20%)</th>
              <th class="admin-score-col">Ikatan (20%)</th>
              <th>Jumlah (%)</th>
              <th>Keputusan</th>
              <th>Tindakan</th>
            </tr>
          </thead>"""

new_candidate_table_start = """      <!-- INDIKATOR STATUS ADMIN CALON -->
      <div class="admin-mode-indicator">
        <i class="fa-solid fa-lock-open" style="font-size:16px;"></i>
        <span><strong>MOD PENTADBIR AKTIF:</strong> Semua Kolum Markah Pengujian Penuh (Kawad Kaki, Bantu Mula & Ikatan) Dipaparkan Secara Terperinci.</span>
      </div>

      <!-- SENARAI CALON TABLE -->
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>No Badan</th>
              <th>Nama Calon</th>
              <th>Jantina</th>
              <th>Unit</th>
              <th>Pangkat</th>
              <th>Sekolah</th>
              <th class="admin-score-col">Kawad (60%)</th>
              <th class="admin-score-col">B. Mula (20%)</th>
              <th class="admin-score-col">Ikatan (20%)</th>
              <th>Jumlah (%)</th>
              <th>Status Keputusan</th>
              <th>Slip</th>
            </tr>
          </thead>"""

html = html.replace(old_candidate_table_start, new_candidate_table_start)

# 2.4 Add Section for Tab 4: Keputusan Calon Terbaik (Top 20)
tab_top_results_html = """    <!-- ===================================================================
         TAB 4: KEPUTUSAN CALON TERBAIK (TOP 5 SETIAP KATEGORI / TOP 20 DAERAH)
         =================================================================== -->
    <section class="tab-content" id="tab-top-results">
      <!-- HERO BANNER KEPUTUSAN TERBAIK -->
      <div class="app-card" style="margin-bottom:24px; background:linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%); color:#ffffff; border:none;">
        <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:16px;">
          <div>
            <span class="header-badge gold" style="margin-bottom:10px; display:inline-flex;">
              <i class="fa-solid fa-award"></i> ANUGERAH KECEMERLANGAN PENTAULIAHAN 2026
            </span>
            <h2 style="font-size:22px; font-weight:800; color:#ffffff; margin:6px 0;">
              🏆 KEPUTUSAN 5 CALON TERBAIK SETIAP KATEGORI (TOP 20 DAERAH)
            </h2>
            <p style="font-size:14px; color:#cbd5e1; margin:0;">
              Pengiktirafan rasmi bagi calon-calon berprestasi tertinggi daerah mengikut Kategori TKRS & KRS (Lelaki & Perempuan).
            </p>
          </div>
          <div style="background:rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.2); border-radius:12px; padding:12px 20px; text-align:center;">
            <span style="font-size:12px; font-weight:700; color:#fde047; text-transform:uppercase;">Jumlah Calon Terbaik</span>
            <h3 style="font-size:28px; font-weight:800; color:#ffffff; margin:2px 0;">20 Calon</h3>
          </div>
        </div>
      </div>

      <!-- GRID 4 KATEGORI (2x2) -->
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(500px, 1fr)); gap:24px;">
        
        <!-- 1. TKRS LELAKI (PUTERA) -->
        <div class="top-category-card">
          <div class="top-category-header">
            <div class="top-category-title" style="color:#059669;">
              <i class="fa-solid fa-medal" style="color:#eab308; font-size:20px;"></i>
              <span>5 TERBAIK TKRS — LELAKI (PUTERA)</span>
            </div>
            <span class="unit-badge tkrs">SEKOLAH RENDAH</span>
          </div>
          <div class="table-container" style="box-shadow:none; border:1px solid var(--slate-200);">
            <table class="data-table">
              <thead>
                <tr>
                  <th style="width:60px; text-align:center;">Ked.</th>
                  <th>No Badan</th>
                  <th>Nama Calon</th>
                  <th>Sekolah</th>
                  <th style="text-align:center;">Markah (%)</th>
                  <th style="text-align:center;">Slip</th>
                </tr>
              </thead>
              <tbody id="top-tbody-tkrs-l">
                <!-- Dijana Dinamik -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- 2. TKRS PEREMPUAN (PUTERI) -->
        <div class="top-category-card">
          <div class="top-category-header">
            <div class="top-category-title" style="color:#d97706;">
              <i class="fa-solid fa-medal" style="color:#eab308; font-size:20px;"></i>
              <span>5 TERBAIK TKRS — PEREMPUAN (PUTERI)</span>
            </div>
            <span class="unit-badge tkrs">SEKOLAH RENDAH</span>
          </div>
          <div class="table-container" style="box-shadow:none; border:1px solid var(--slate-200);">
            <table class="data-table">
              <thead>
                <tr>
                  <th style="width:60px; text-align:center;">Ked.</th>
                  <th>No Badan</th>
                  <th>Nama Calon</th>
                  <th>Sekolah</th>
                  <th style="text-align:center;">Markah (%)</th>
                  <th style="text-align:center;">Slip</th>
                </tr>
              </thead>
              <tbody id="top-tbody-tkrs-p">
                <!-- Dijana Dinamik -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- 3. KRS LELAKI (PUTERA) -->
        <div class="top-category-card">
          <div class="top-category-header">
            <div class="top-category-title" style="color:#1e40af;">
              <i class="fa-solid fa-medal" style="color:#eab308; font-size:20px;"></i>
              <span>5 TERBAIK KRS — LELAKI (PUTERA)</span>
            </div>
            <span class="unit-badge krs">SEKOLAH MENENGAH</span>
          </div>
          <div class="table-container" style="box-shadow:none; border:1px solid var(--slate-200);">
            <table class="data-table">
              <thead>
                <tr>
                  <th style="width:60px; text-align:center;">Ked.</th>
                  <th>No Badan</th>
                  <th>Nama Calon</th>
                  <th>Sekolah</th>
                  <th style="text-align:center;">Markah (%)</th>
                  <th style="text-align:center;">Slip</th>
                </tr>
              </thead>
              <tbody id="top-tbody-krs-l">
                <!-- Dijana Dinamik -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- 4. KRS PEREMPUAN (PUTERI) -->
        <div class="top-category-card">
          <div class="top-category-header">
            <div class="top-category-title" style="color:#db2777;">
              <i class="fa-solid fa-medal" style="color:#eab308; font-size:20px;"></i>
              <span>5 TERBAIK KRS — PEREMPUAN (PUTERI)</span>
            </div>
            <span class="unit-badge krs">SEKOLAH MENENGAH</span>
          </div>
          <div class="table-container" style="box-shadow:none; border:1px solid var(--slate-200);">
            <table class="data-table">
              <thead>
                <tr>
                  <th style="width:60px; text-align:center;">Ked.</th>
                  <th>No Badan</th>
                  <th>Nama Calon</th>
                  <th>Sekolah</th>
                  <th style="text-align:center;">Markah (%)</th>
                  <th style="text-align:center;">Slip</th>
                </tr>
              </thead>
              <tbody id="top-tbody-krs-p">
                <!-- Dijana Dinamik -->
              </tbody>
            </table>
          </div>
        </div>

      </div>
    </section>
"""

# Insert Tab 4 before Tab Admin
html = html.replace('<!-- TAB 4: TETAPAN ADMIN -->', tab_top_results_html + '\n    <!-- TAB 5: TETAPAN ADMIN -->')
html = html.replace('<section class="tab-content" id="tab-admin">', tab_top_results_html + '\n    <section class="tab-content" id="tab-admin">')

# 2.5 Add JavaScript Logic for Top 20 Candidates rendering
js_render_top_fn = """
      renderTopResults() {
        const renderGroup = (elementId, candidatesList) => {
          const tbody = document.getElementById(elementId);
          if (!tbody) return;
          if (!candidatesList || candidatesList.length === 0) {
            tbody.innerHTML = '<tr><td colspan="6" style="text-align:center; padding:20px; color:#94a3b8;">Tiada rekod calon.</td></tr>';
            return;
          }

          const rankBadges = [
            '<span class="rank-badge rank-1">🥇 1</span>',
            '<span class="rank-badge rank-2">🥈 2</span>',
            '<span class="rank-badge rank-3">🥉 3</span>',
            '<span class="rank-badge rank-4">4</span>',
            '<span class="rank-badge rank-5">5</span>'
          ];

          tbody.innerHTML = candidatesList.map((c, idx) => {
            const badge = rankBadges[idx] || `<span class="rank-badge">${idx + 1}</span>`;
            return `
              <tr>
                <td style="text-align:center;">${badge}</td>
                <td style="font-weight:800; color:var(--royal-blue);">${c.noBadan || c.noGiliran}</td>
                <td style="font-weight:800;">${(c.nama || '').toUpperCase()}</td>
                <td style="font-size:13px; color:var(--slate-700);">${(c.sekolah || '').toUpperCase()}</td>
                <td style="text-align:center; font-weight:800; color:var(--slate-900); font-size:15px;">${c.overall}%</td>
                <td style="text-align:center;">
                  <button class="btn-table-slip" onclick="window.App.openCandidateSlip('${c.noBadan || c.noGiliran}')" style="padding:5px 10px; background:#eff6ff; border:1px solid #bfdbfe; border-radius:6px; color:var(--royal-accent); font-size:12px; font-weight:700; cursor:pointer;">
                    <i class="fa-solid fa-file-lines"></i> Slip
                  </button>
                </td>
              </tr>
            `;
          }).join('');
        };

        // Filter & Sort Top 5 for each category
        const activeCandidates = this.state.candidates.filter(c => !c.isAbsent && !c.isTarikDiri);
        
        const tkrsL = activeCandidates.filter(c => c.unit === 'TKRS' && c.jantina === 'L').sort((a,b) => b.overall - a.overall).slice(0, 5);
        const tkrsP = activeCandidates.filter(c => c.unit === 'TKRS' && c.jantina === 'P').sort((a,b) => b.overall - a.overall).slice(0, 5);
        const krsL = activeCandidates.filter(c => c.unit === 'KRS' && c.jantina === 'L').sort((a,b) => b.overall - a.overall).slice(0, 5);
        const krsP = activeCandidates.filter(c => c.unit === 'KRS' && c.jantina === 'P').sort((a,b) => b.overall - a.overall).slice(0, 5);

        renderGroup('top-tbody-tkrs-l', tkrsL);
        renderGroup('top-tbody-tkrs-p', tkrsP);
        renderGroup('top-tbody-krs-l', krsL);
        renderGroup('top-tbody-krs-p', krsP);
      },
"""

html = html.replace('renderCandidatesTable() {', js_render_top_fn + '\n      renderCandidatesTable() {')

# Hook renderTopResults to recalculateAllStats and tab navigation
html = html.replace('this.renderCandidatesTable();', 'this.renderCandidatesTable();\n        this.renderTopResults();')

# Save updated Netlify index.html
with open('04_Web_App_Netlify/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Saved 04_Web_App_Netlify/index.html ({len(html):,} bytes)")

# Prepare and save GAS Index.html
html_gas = html.replace(
    '<script id="server-data-payload" type="application/json">\n    null\n  </script>',
    '<script id="server-data-payload" type="application/json">\n    <?!= typeof initialData !== \'undefined\' && initialData ? JSON.stringify(initialData) : \'null\' ?>\n  </script>'
)

with open('03_Google_Apps_Script/Index.html', 'w', encoding='utf-8') as f:
    f.write(html_gas)
print(f"✓ Saved 03_Google_Apps_Script/Index.html ({len(html_gas):,} bytes)")
