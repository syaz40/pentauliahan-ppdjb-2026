import os
import re
import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

print("Applying user customizations from implementation plan comments...")

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# =========================================================================
# 1. HEADER & BADGES
# =========================================================================
# Make header badges slightly larger and prominent
html = html.replace(
    '.header-badge {\n      display: inline-flex;\n      align-items: center;\n      gap: 7px;\n      padding: 7px 15px;\n      border-radius: 8px;\n      font-size: 12.5px;\n      font-weight: 700;',
    '.header-badge {\n      display: inline-flex;\n      align-items: center;\n      gap: 8px;\n      padding: 9px 18px;\n      border-radius: 10px;\n      font-size: 14px;\n      font-weight: 800;'
)

# Update admin auth pill text
html = html.replace(
    'PEGAWAI DATA SEKRETARIAT JB',
    'PEGAWAI DATA TKRS JB | KAPTEN MOHD SYAZWAN BIN SULAIMAN'
)
html = html.replace(
    'PENTADBIR SISTEM (ADMIN)',
    'PEGAWAI DATA TKRS JB | KAPTEN MOHD SYAZWAN BIN SULAIMAN'
)

# =========================================================================
# 2. TAB 1: MAKLUMAT PROGRAM & MODUL & TENTATIF
# =========================================================================
# Change 'Calon Layak Diuji' -> 'Calon Pengujian'
html = html.replace('<p>Calon Layak Diuji</p>', '<p>Calon Pengujian</p>')
html = html.replace('<p>Selesai Dinilai</p>', '<p>Selesai Pengujian</p>')

# Kawad pergerakan: Statik, Kawad Dinamik, Hormat
html = html.replace(
    '<li><strong>TKRS:</strong> 15 Pergerakan asas (Kawad Statik, Dinamik, Hormat). Markah Penuh: 95.</li>',
    '<li><strong>TKRS:</strong> 15 Pergerakan asas (Kawad Statik, Kawad Dinamik, Hormat). Markah Penuh: 95.</li>'
)
html = html.replace(
    '<li><strong>KRS:</strong> 22 Pergerakan (Statik, Dinamik, Hormat, Perlahan Jalan). Markah Penuh: 137.</li>',
    '<li><strong>KRS:</strong> 22 Pergerakan (Kawad Statik, Kawad Dinamik, Hormat, Perlahan Jalan). Markah Penuh: 137.</li>'
)

# Bantu Mula: Add detailed breakdown for TKRS and KRS
old_bm_desc = """            <ul class="module-list">
              <li>Rawatan patah bahagian keting menggunakan pembebat & anduh segi tiga.</li>
              <li>Kekemasan ikatan anduh & keselesaan mangsa.</li>
              <li>Penerangan lisan prosedur keselamatan (Markah Penuh: 20).</li>
            </ul>"""

new_bm_desc = """            <ul class="module-list">
              <li><strong>TKRS:</strong> Rawatan luka pada tapak tangan menggunakan pembebat & kain anduh segi tiga (Markah Penuh: 20).</li>
              <li><strong>KRS:</strong> Rawatan patah bahagian keting/tibia menggunakan kayu tuap, pembebat & kain anduh segi tiga, serta penerangan lisan prosedur keselamatan (Markah Penuh: 20).</li>
            </ul>"""

html = html.replace(old_bm_desc, new_bm_desc)

# Tentatif Program (Schedule timeline update)
old_schedule_pattern = r'<div class="schedule-grid">[\s\S]*?</div>\s*</div>\s*</div>'
new_schedule = """<div class="schedule-grid">
          <div class="schedule-item">
            <span class="schedule-time">07:30 AM</span>
            <span class="schedule-desc">Pendaftaran</span>
          </div>
          <div class="schedule-item">
            <span class="schedule-time">08:00 AM</span>
            <span class="schedule-desc">Taklimat</span>
          </div>
          <div class="schedule-item">
            <span class="schedule-time">08:30 AM</span>
            <span class="schedule-desc">Ujian Kawad Kaki</span>
          </div>
          <div class="schedule-item">
            <span class="schedule-time">10:30 AM</span>
            <span class="schedule-desc">Rehat</span>
          </div>
          <div class="schedule-item">
            <span class="schedule-time">11:00 AM</span>
            <span class="schedule-desc">Ujian Tali Temali</span>
          </div>
          <div class="schedule-item">
            <span class="schedule-time">01:00 PM</span>
            <span class="schedule-desc">Rehat / Solat</span>
          </div>
          <div class="schedule-item">
            <span class="schedule-time">02:00 PM</span>
            <span class="schedule-desc">Ujian Bantu Mula</span>
          </div>
          <div class="schedule-item">
            <span class="schedule-time">03:30 PM</span>
            <span class="schedule-desc">Persiapan Majlis Penutup</span>
          </div>
          <div class="schedule-item">
            <span class="schedule-time">04:00 PM</span>
            <span class="schedule-desc">Majlis Penutup</span>
          </div>
          <div class="schedule-item">
            <span class="schedule-time">05:30 PM</span>
            <span class="schedule-desc">Bersurai</span>
          </div>
        </div>
      </div>
    </div>"""

html = re.sub(old_schedule_pattern, new_schedule, html)

# =========================================================================
# 3. TAB 2: CARTA WARNA KONTRA TINGGI
# =========================================================================
# High contrast colors for 4 categories in Chart.js
html = html.replace(
    "backgroundColor: ['#3b82f6', '#ec4899', '#1e3a8a', '#be185d']",
    "backgroundColor: ['#059669', '#d97706', '#1e40af', '#db2777']"
)
html = html.replace(
    "backgroundColor: ['#2563eb', '#db2777', '#1e3a8a', '#9d174d']",
    "backgroundColor: ['#059669', '#d97706', '#1e40af', '#db2777']"
)

# =========================================================================
# 4. TAB 3: SENARAI CALON, PRIVASI SKOR, NO BADAN, STATUS TD/TH & CETAKAN
# =========================================================================
# Terminology 'No Giliran' -> 'No Badan'
html = html.replace('No Giliran', 'No Badan')
html = html.replace('noGiliran', 'noBadan')
html = html.replace('No. Giliran', 'No. Badan')

# Status 'TARIK DIRI' -> 'Tarik Diri (TD)', 'TIDAK HADIR' -> 'Tidak Hadir (TH)'
html = html.replace('<option value="TIDAK HADIR">TIDAK HADIR (TH)</option>', '<option value="TIDAK HADIR">Tidak Hadir (TH)</option>')
html = html.replace('<option value="TARIK DIRI">TARIK DIRI</option>', '<option value="TARIK DIRI">Tarik Diri (TD)</option>')
html = html.replace('<option value="ABSENT">Tidak Hadir Sahaja</option>', '<option value="ABSENT">Tidak Hadir (TH)</option>')
html = html.replace('<option value="WITHDRAW">Tarik Diri Sahaja</option>', '<option value="WITHDRAW">Tarik Diri (TD)</option>')

# Add CSS for Admin-Only Score Columns and Print Styling
custom_css = """
    /* SKOR KOMPONEN HANYA MUNCUL APABILA ADMIN LOG MASUK */
    .admin-score-col {
      display: none !important;
    }
    body.is-admin .admin-score-col {
      display: table-cell !important;
    }

    .admin-only-slip-scores {
      display: none !important;
    }
    body.is-admin .admin-only-slip-scores {
      display: grid !important;
    }

    /* FORMAT CETAKAN SLIP RASMI BERKUALITI TINGGI (A4 PAGE / PDF) */
    @media print {
      body * {
        visibility: hidden !important;
      }
      #modal-slip-backdrop, #modal-slip-backdrop * {
        visibility: visible !important;
      }
      #modal-slip-backdrop {
        position: fixed !important;
        left: 0 !important;
        top: 0 !important;
        width: 100% !important;
        height: 100% !important;
        background: #ffffff !important;
        padding: 0 !important;
        margin: 0 !important;
        display: flex !important;
        align-items: flex-start !important;
        justify-content: center !important;
      }
      .modal-box-lg {
        box-shadow: none !important;
        border: 2px solid #0f172a !important;
        width: 100% !important;
        max-width: 750px !important;
        margin: 20px auto !important;
        padding: 36px !important;
        border-radius: 8px !important;
        background: #ffffff !important;
        color: #000000 !important;
      }
      .btn-close-modal, #btn-print-slip, #btn-close-slip {
        display: none !important;
      }
      .status-badge {
        border: 1.5px solid #0f172a !important;
        color: #000000 !important;
        font-weight: 800 !important;
      }
    }
"""

html = html.replace('</style>', custom_css + '\n  </style>')

# Update table headers with .admin-score-col class
html = html.replace('<th>Kawad (60%)</th>', '<th class="admin-score-col">Kawad (60%)</th>')
html = html.replace('<th>B. Mula (20%)</th>', '<th class="admin-score-col">B. Mula (20%)</th>')
html = html.replace('<th>Ikatan (20%)</th>', '<th class="admin-score-col">Ikatan (20%)</th>')

# =========================================================================
# 5. TAB 4: TETAPAN ADMIN, PIN SEKETEJB26 & BUANG PRESET & UNJURAN DETAIL
# =========================================================================
# Update Admin PIN to seketejb26
html = html.replace("'adminseketejb'", "'seketejb26'")
html = html.replace('"adminseketejb"', '"seketejb26"')

# Remove quick preset buttons block
html = re.sub(r'<!-- 1-CLICK PRESETS -->[\s\S]*?<!-- PELARAS WAJARAN -->', '<!-- PELARAS WAJARAN -->', html)
html = re.sub(r'<div class="sym-grid-4" style="margin-bottom:20px;">\s*<button class="btn-action outline" id="btn-preset-standard"[\s\S]*?</div>\s*</div>\s*</div>\s*<!-- PELARAS WAJARAN -->', '<!-- PELARAS WAJARAN -->', html)

# Simulator Detailed Breakdown Card
old_sim_card = """      <!-- UNJURAN KEPUTUSAN HASIL PELARASAN -->
      <div class="sim-deck">
        <div class="card-head">
          <div class="card-heading"><i class="fa-solid fa-calculator"></i> Unjuran Keputusan Mengikut Syarat Kelulusan Semasa</div>
        </div>
        
        <div class="sym-grid-4">
          <div class="metric-tile green">
            <div class="metric-icon"><i class="fa-solid fa-percent"></i></div>
            <div class="metric-data">
              <h3 id="sim-pass-rate">0.0%</h3>
              <p>Unjuran Kadar Kelulusan</p>
            </div>
          </div>
          <div class="metric-tile">
            <div class="metric-icon"><i class="fa-solid fa-user-check"></i></div>
            <div class="metric-data">
              <h3 id="sim-pass-count">0 / 305</h3>
              <p>Calon Lulus Penuh</p>
            </div>
          </div>
          <div class="metric-tile gold">
            <div class="metric-icon"><i class="fa-solid fa-user-clock"></i></div>
            <div class="metric-data">
              <h3 id="sim-conditional-count">0</h3>
              <p>Calon Lulus Bersyarat</p>
            </div>
          </div>
          <div class="metric-tile red">
            <div class="metric-icon"><i class="fa-solid fa-user-xmark"></i></div>
            <div class="metric-data">
              <h3 id="sim-fail-count">0</h3>
              <p>Calon Gagal</p>
            </div>
          </div>
        </div>
      </div>"""

new_sim_card = """      <!-- UNJURAN KEPUTUSAN HASIL PELARASAN (STATUS CODE BREAKDOWN) -->
      <div class="sim-deck">
        <div class="card-head">
          <div class="card-heading"><i class="fa-solid fa-calculator"></i> Unjuran Keputusan Mengikut Syarat Kelulusan Semasa</div>
        </div>
        
        <div class="sym-grid-4" style="margin-bottom:18px;">
          <div class="metric-tile green">
            <div class="metric-icon"><i class="fa-solid fa-percent"></i></div>
            <div class="metric-data">
              <h3 id="sim-pass-rate">0.0%</h3>
              <p>Unjuran Kadar Kelulusan</p>
            </div>
          </div>
          <div class="metric-tile">
            <div class="metric-icon"><i class="fa-solid fa-user-check"></i></div>
            <div class="metric-data">
              <h3 id="sim-pass-count">0 / 305</h3>
              <p>Lulus Penuh (LLL)</p>
            </div>
          </div>
          <div class="metric-tile gold">
            <div class="metric-icon"><i class="fa-solid fa-user-clock"></i></div>
            <div class="metric-data">
              <h3 id="sim-conditional-count">0</h3>
              <p>Lulus Bersyarat (LLG/LGL/GLL)</p>
            </div>
          </div>
          <div class="metric-tile red">
            <div class="metric-icon"><i class="fa-solid fa-user-xmark"></i></div>
            <div class="metric-data">
              <h3 id="sim-fail-count">0</h3>
              <p>Belum Capai Tahap (LGG/GLG/GGL/GGG)</p>
            </div>
          </div>
        </div>

        <!-- PERINCIAN KOD STATUS PENGUJIAN -->
        <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:var(--radius-md); padding:16px;">
          <h4 style="font-size:14px; font-weight:800; color:var(--slate-800); margin-bottom:10px;">
            <i class="fa-solid fa-list-check" style="color:var(--royal-accent);"></i> Perincian Pecahan Kod Status Pengujian:
          </h4>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; font-size:13px; font-weight:700;">
            <div style="background:#dcfce7; color:#166534; padding:10px 14px; border-radius:8px; border:1px solid #86efac;">
              🟢 <strong>LLL (Lulus Penuh):</strong> <span id="sim-code-lll">0</span> Calon
            </div>
            <div style="background:#fef3c7; color:#92400e; padding:10px 14px; border-radius:8px; border:1px solid #fcd34d;">
              🟡 <strong>LLG / LGL / GLL:</strong> <span id="sim-code-cond">0</span> Calon
            </div>
            <div style="background:#fee2e2; color:#991b1b; padding:10px 14px; border-radius:8px; border:1px solid #fca5a5;">
              🔴 <strong>LGG / GLG / GGL / GGG:</strong> <span id="sim-code-fail">0</span> Calon
            </div>
            <div style="background:#f1f5f9; color:#475569; padding:10px 14px; border-radius:8px; border:1px solid #cbd5e1;">
              ⚪ <strong>TH / TD:</strong> <span id="sim-code-issues">0</span> Calon
            </div>
          </div>
        </div>
      </div>"""

html = html.replace(old_sim_card, new_sim_card)

# =========================================================================
# 6. FOOTER
# =========================================================================
html = html.replace(
    'Sistem Pengurusan & Analisis Pentauliahan Pangkat KRS & TKRS Peringkat Daerah Johor Bahru.',
    'DISEDIAKAN OLEH PEGAWAI DATA TKRS JOHOR BAHRU | KAPTEN MOHD SYAZWAN BIN SULAIMAN'
)

# =========================================================================
# 7. JAVASCRIPT UPDATES (Admin Toggle, Simulator Breakdown, Score Privacy)
# =========================================================================
# Update JS to toggle body.is-admin on login
old_auth_fn = """      updateAuthVisuals() {
        const badge = document.getElementById('badge-admin-auth');
        const manageCard = document.getElementById('admin-candidate-manage-card');
        const screenLogin = document.getElementById('screen-admin-login');
        const screenControl = document.getElementById('screen-admin-control');

        if (this.state.adminLoggedIn) {
          if (badge) {
            badge.style.display = 'inline-flex';
            badge.classList.add('logged-in');
            badge.innerHTML = '<i class="fa-solid fa-shield-halved"></i> PEGAWAI DATA SEKRETARIAT JB';
          }
          if (manageCard) manageCard.style.display = 'block';
          if (screenLogin) screenLogin.style.display = 'none';
          if (screenControl) screenControl.style.display = 'block';
        } else {
          if (badge) badge.style.display = 'none';
          if (manageCard) manageCard.style.display = 'none';
          if (screenLogin) screenLogin.style.display = 'block';
          if (screenControl) screenControl.style.display = 'none';
        }
      },"""

new_auth_fn = """      updateAuthVisuals() {
        const badge = document.getElementById('badge-admin-auth');
        const manageCard = document.getElementById('admin-candidate-manage-card');
        const screenLogin = document.getElementById('screen-admin-login');
        const screenControl = document.getElementById('screen-admin-control');

        if (this.state.adminLoggedIn) {
          document.body.classList.add('is-admin');
          if (badge) {
            badge.style.display = 'inline-flex';
            badge.classList.add('logged-in');
            badge.innerHTML = '<i class="fa-solid fa-shield-halved"></i> PEGAWAI DATA TKRS JB | KAPTEN MOHD SYAZWAN BIN SULAIMAN';
          }
          if (manageCard) manageCard.style.display = 'block';
          if (screenLogin) screenLogin.style.display = 'none';
          if (screenControl) screenControl.style.display = 'block';
        } else {
          document.body.classList.remove('is-admin');
          if (badge) badge.style.display = 'none';
          if (manageCard) manageCard.style.display = 'none';
          if (screenLogin) screenLogin.style.display = 'block';
          if (screenControl) screenControl.style.display = 'none';
        }
        this.renderCandidatesTable();
      },"""

html = html.replace(old_auth_fn, new_auth_fn)

# Update renderCandidatesTable to add .admin-score-col to td
old_row_render = """            <tr>
              <td style="font-weight:800; color:var(--royal-blue);">${c.noGiliran}</td>
              <td style="font-weight:700;">${c.nama}</td>
              <td style="font-weight:800;">${c.jantina}</td>
              <td><span class="unit-badge ${c.unit.toLowerCase()}">${c.unit}</span></td>
              <td style="font-weight:600;">${c.pangkat}</td>
              <td>${c.sekolah}</td>
              <td style="font-weight:700;">${c.kawad}%</td>
              <td style="font-weight:700;">${c.bantuMula}%</td>
              <td style="font-weight:700;">${c.ikatan}%</td>
              <td style="font-weight:800; color:var(--slate-900); font-size:15px;">${c.overall}%</td>
              <td>${statusBadge}</td>
              <td>
                <button class="btn-table-slip" onclick="window.App.openCandidateSlip('${c.noGiliran}')" style="padding:6px 12px; background:#eff6ff; border:1px solid #bfdbfe; border-radius:6px; color:var(--royal-accent); font-size:12.5px; font-weight:700; cursor:pointer;">
                  <i class="fa-solid fa-file-lines"></i> Slip
                </button>
              </td>
            </tr>"""

new_row_render = """            <tr>
              <td style="font-weight:800; color:var(--royal-blue);">${c.noBadan || c.noGiliran}</td>
              <td style="font-weight:700;">${c.nama}</td>
              <td style="font-weight:800;">${c.jantina}</td>
              <td><span class="unit-badge ${c.unit.toLowerCase()}">${c.unit}</span></td>
              <td style="font-weight:600;">${c.pangkat}</td>
              <td>${c.sekolah}</td>
              <td class="admin-score-col" style="font-weight:700;">${c.kawad}%</td>
              <td class="admin-score-col" style="font-weight:700;">${c.bantuMula}%</td>
              <td class="admin-score-col" style="font-weight:700;">${c.ikatan}%</td>
              <td style="font-weight:800; color:var(--slate-900); font-size:15px;">${c.overall}%</td>
              <td>${statusBadge}</td>
              <td>
                <button class="btn-table-slip" onclick="window.App.openCandidateSlip('${c.noBadan || c.noGiliran}')" style="padding:6px 12px; background:#eff6ff; border:1px solid #bfdbfe; border-radius:6px; color:var(--royal-accent); font-size:12.5px; font-weight:700; cursor:pointer;">
                  <i class="fa-solid fa-file-lines"></i> Slip
                </button>
              </td>
            </tr>"""

html = html.replace(old_row_render, new_row_render)

# Update Simulator calculation in recalculateAllStats to update LLL, cond, fail, issues count
old_sim_update = """        // Kemas kini Simulator Urus Setia
        const elSimPassRate = document.getElementById('sim-pass-rate');
        const elSimPassCount = document.getElementById('sim-pass-count');
        const elSimCondCount = document.getElementById('sim-conditional-count');
        const elSimFailCount = document.getElementById('sim-fail-count');

        if (elSimPassRate) elSimPassRate.innerText = passRate.toFixed(1) + '%';
        if (elSimPassCount) elSimPassCount.innerText = `${passCount} / ${total}`;
        if (elSimCondCount) elSimCondCount.innerText = condCount;
        if (elSimFailCount) elSimFailCount.innerText = failCount;"""

new_sim_update = """        // Kemas kini Simulator Urus Setia & Pecahan Kod Status
        const elSimPassRate = document.getElementById('sim-pass-rate');
        const elSimPassCount = document.getElementById('sim-pass-count');
        const elSimCondCount = document.getElementById('sim-conditional-count');
        const elSimFailCount = document.getElementById('sim-fail-count');

        if (elSimPassRate) elSimPassRate.innerText = passRate.toFixed(1) + '%';
        if (elSimPassCount) elSimPassCount.innerText = `${passCount} / ${total}`;
        if (elSimCondCount) elSimCondCount.innerText = condCount;
        if (elSimFailCount) elSimFailCount.innerText = failCount;

        const elCodeLLL = document.getElementById('sim-code-lll');
        const elCodeCond = document.getElementById('sim-code-cond');
        const elCodeFail = document.getElementById('sim-code-fail');
        const elCodeIssues = document.getElementById('sim-code-issues');

        if (elCodeLLL) elCodeLLL.innerText = passCount;
        if (elCodeCond) elCodeCond.innerText = condCount;
        if (elCodeFail) elCodeFail.innerText = failCount;
        if (elCodeIssues) elCodeIssues.innerText = issuesCount;"""

html = html.replace(old_sim_update, new_sim_update)

# Update Digital Slip Modal: Component scores only shown for admin
old_slip_scores_html = """      <div class="tokoh-scores" style="margin-bottom: 20px;">
        <div class="tokoh-score-item">
          <div class="sc-lbl">Kawad Kaki (60%)</div>
          <div class="sc-val" id="slip-score-kawad">0%</div>
        </div>
        <div class="tokoh-score-item">
          <div class="sc-lbl">Bantu Mula (20%)</div>
          <div class="sc-val" id="slip-score-bm">0%</div>
        </div>
        <div class="tokoh-score-item">
          <div class="sc-lbl">Ikatan (20%)</div>
          <div class="sc-val" id="slip-score-ikatan">0%</div>
        </div>
        <div class="tokoh-score-item sc-total">
          <div class="sc-lbl">Jumlah (%)</div>
          <div class="sc-val" id="slip-score-overall">0%</div>
        </div>
      </div>"""

new_slip_scores_html = """      <!-- SKOR KOMPONEN: HANYA MUNCUL UNTUK ADMIN -->
      <div class="tokoh-scores admin-only-slip-scores" style="margin-bottom: 20px;">
        <div class="tokoh-score-item">
          <div class="sc-lbl">Kawad Kaki (60%)</div>
          <div class="sc-val" id="slip-score-kawad">0%</div>
        </div>
        <div class="tokoh-score-item">
          <div class="sc-lbl">Bantu Mula (20%)</div>
          <div class="sc-val" id="slip-score-bm">0%</div>
        </div>
        <div class="tokoh-score-item">
          <div class="sc-lbl">Ikatan (20%)</div>
          <div class="sc-val" id="slip-score-ikatan">0%</div>
        </div>
        <div class="tokoh-score-item sc-total">
          <div class="sc-lbl">Jumlah (%)</div>
          <div class="sc-val" id="slip-score-overall">0%</div>
        </div>
      </div>

      <!-- PAPARAN SKOR KESELURUHAN UNTUK UMUM -->
      <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:var(--radius-md); padding:16px; text-align:center; margin-bottom:20px;">
        <span style="font-size:12px; font-weight:800; color:#1e40af; text-transform:uppercase;">Markah Keseluruhan Pentauliahan</span>
        <h2 style="font-size:32px; font-weight:800; color:var(--royal-blue); margin:4px 0;" id="slip-score-public-overall">0.0%</h2>
      </div>"""

html = html.replace(old_slip_scores_html, new_slip_scores_html)

# Update openCandidateSlip JS to populate slip-score-public-overall
html = html.replace(
    "document.getElementById('slip-score-overall').innerText = candidate.overall + '%';",
    "document.getElementById('slip-score-overall').innerText = candidate.overall + '%';\n        const elPubOv = document.getElementById('slip-score-public-overall'); if (elPubOv) elPubOv.innerText = candidate.overall + '%';"
)

# Also update Code.gs default PIN to seketejb26
with open('03_Google_Apps_Script/Code.gs', 'r', encoding='utf-8') as f:
    codegs = f.read()

codegs = codegs.replace("'adminseketejb'", "'seketejb26'")
codegs = codegs.replace('"adminseketejb"', '"seketejb26"')

with open('03_Google_Apps_Script/Code.gs', 'w', encoding='utf-8') as f:
    f.write(codegs)
print("✓ Updated 03_Google_Apps_Script/Code.gs with default PIN 'seketejb26'")

# Prepare GAS Index.html
html_gas = html.replace(
    '<script id="server-data-payload" type="application/json">\n    null\n  </script>',
    '<script id="server-data-payload" type="application/json">\n    <?!= typeof initialData !== \'undefined\' && initialData ? JSON.stringify(initialData) : \'null\' ?>\n  </script>'
)

# Save GAS Index.html
with open('03_Google_Apps_Script/Index.html', 'w', encoding='utf-8') as f:
    f.write(html_gas)
print(f"✓ Saved 03_Google_Apps_Script/Index.html ({len(html_gas):,} bytes)")

# Save Netlify index.html
with open('04_Web_App_Netlify/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Saved 04_Web_App_Netlify/index.html ({len(html):,} bytes)")
