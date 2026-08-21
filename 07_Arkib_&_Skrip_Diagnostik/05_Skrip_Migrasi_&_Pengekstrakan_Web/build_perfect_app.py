import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Building Perfect Candidate Table (Public vs Admin) & Full Slip Modal...")

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# =========================================================================
# 1. ADD DIGITAL SLIP MODAL HTML (IF MISSING)
# =========================================================================
modal_slip_html = """
  <!-- MODAL SLIP KEPUTUSAN CALON RASMI (DIGITAL DOSSIER) -->
  <div id="modal-slip-backdrop" class="modal-backdrop" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(15,23,42,0.75); backdrop-filter:blur(4px); z-index:9999; justify-content:center; align-items:center; padding:16px;">
    <div class="modal-box-lg" style="background:#ffffff; border-radius:var(--radius-xl); border:1px solid #cbd5e1; max-width:680px; width:100%; max-height:90vh; overflow-y:auto; padding:32px; box-shadow:var(--shadow-modal); position:relative;">
      
      <!-- BUTANG TUTUP -->
      <button class="btn-close-modal" id="btn-close-slip-x" onclick="window.App.closeCandidateSlip()" style="position:absolute; top:20px; right:20px; background:transparent; border:none; font-size:22px; color:var(--slate-400); cursor:pointer;">
        <i class="fa-solid fa-xmark"></i>
      </button>

      <!-- PENGEPALA SLIP DENGAN LOGO -->
      <div style="text-align:center; padding-bottom:18px; margin-bottom:20px; border-bottom:2px solid var(--slate-200);">
        <div style="display:flex; justify-content:center; align-items:center; gap:16px; margin-bottom:10px;">
          <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKAAAABMCAYAAADqSbzUAAAsiElEQVR42u19d3xUVdr/95x7585kMuk9JBCS0IsgAiJoqCJgQTERy+qKigWwr4r6OsSKa1m7IqgLNgwoVqRJQKQjnVADBBLSe6bfe5/fH3lGZ3lRd/fd/amY8/nMZ+bee8pznvOc71POPWeAttSW2lJbakt9P6L/357g/z/E/8j9wSfeecW9c8tKhxuriYmRuIpC8oz3vQXvvRW47IxTkq4CEBTin9ktABcPCgUc+uWXrRpwrzUeaM6c0KCnX0w948QuGU9d9vcfVj08Mn/6/BPzbipdRrdv386P5vfgT5FFtbVU2qMrrm3bwaiQxwzNNj3NmH32M/vV1+Ewvyr4cloa2lqLgj2FqqioSB4HTtk4LuuM5w7Ln3z9p5tWjmqXOuOGU9Mu/Oij0NH8HyiE/0lqn0YA8uvNZDdvcZ47Mzn9pvPaphywPcqpi3Rut7lbm0bvd83fx2d3zaseMfPzBSUlJRKYKpYvB48qTBthtJN02KHuoaMOtyfmt7F5Obk21foACIIAYk2oaRQVhtDphyWyctCApAFlm/wlxcUQI0YU0+zZs7lDhw69L7hzwry3Fyw/9/va4L65AaTd0MftOrog+dgnSpuOOb8y7+VIpLY+oRi4VQPuZWW9cza0lM4TxzakHV23XPgrG4zpGtKc" alt="Logo PPD & KRS" style="height:54px; object-fit:contain;">
        </div>
        <h3 style="font-size:18px; font-weight:800; color:var(--slate-900); margin:4px 0;">SLIP KEPUTUSAN RASMI PENTAULIAHAN 2026</h3>
        <p style="font-size:13px; color:var(--slate-600); margin:0;">Pejabat Pendidikan Daerah Johor Bahru • 22 Ogos 2026</p>
      </div>

      <!-- BUTIRAN MAKLUMAT CALON -->
      <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:var(--radius-md); padding:16px; margin-bottom:20px;">
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; font-size:13.5px;">
          <div><strong style="color:var(--slate-500);">Nama Calon:</strong> <br><span id="slip-candidate-name" style="font-weight:800; color:var(--slate-900); font-size:14.5px;">-</span></div>
          <div><strong style="color:var(--slate-500);">No Badan:</strong> <br><span id="slip-candidate-nobadan" style="font-weight:800; color:var(--royal-blue); font-size:15px;">-</span></div>
          <div><strong style="color:var(--slate-500);">Unit & Pangkat:</strong> <br><span id="slip-candidate-unit" style="font-weight:700;">-</span></div>
          <div><strong style="color:var(--slate-500);">Sekolah:</strong> <br><span id="slip-candidate-sekolah" style="font-weight:700;">-</span></div>
        </div>
      </div>

      <!-- SKOR KESELURUHAN (PAPARAN AWAM & ADMIN) -->
      <div style="background:linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%); color:#ffffff; border-radius:var(--radius-lg); padding:20px; text-align:center; margin-bottom:20px;">
        <span style="font-size:12px; font-weight:700; color:#93c5fd; text-transform:uppercase; letter-spacing:0.5px;">MARKAH KESELURUHAN PENTAULIAHAN</span>
        <h2 id="slip-score-overall" style="font-size:38px; font-weight:800; color:#fde047; margin:6px 0;">0.0%</h2>
        <div id="slip-status-badge" style="margin-top:8px;">
          <span class="status-badge pass">Lulus (LLL)</span>
        </div>
      </div>

      <!-- PERINCIAN 3 MODUL (HANYA DITAMPILKAN KEPADA ADMIN) -->
      <div id="slip-admin-module-breakdown" style="display:none; margin-bottom:20px;">
        <h4 style="font-size:13px; font-weight:800; color:var(--slate-700); text-transform:uppercase; margin-bottom:10px;">
          <i class="fa-solid fa-lock" style="color:var(--royal-accent);"></i> Perincian Skor Modul (Akses Pentadbir):
        </h4>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; text-align:center;">
          <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:8px; padding:10px;">
            <span style="font-size:11px; font-weight:700; color:#1e40af; display:block;">Kawad (60%)</span>
            <strong id="slip-score-kawad" style="font-size:18px; color:#1e3a8a;">0%</strong>
          </div>
          <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:8px; padding:10px;">
            <span style="font-size:11px; font-weight:700; color:#1e40af; display:block;">B. Mula (20%)</span>
            <strong id="slip-score-bm" style="font-size:18px; color:#1e3a8a;">0%</strong>
          </div>
          <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:8px; padding:10px;">
            <span style="font-size:11px; font-weight:700; color:#1e40af; display:block;">Ikatan (20%)</span>
            <strong id="slip-score-ikatan" style="font-size:18px; color:#1e3a8a;">0%</strong>
          </div>
        </div>
      </div>

      <!-- TINDAKAN BUTANG CETAK & TUTUP -->
      <div style="display:flex; justify-content:flex-end; gap:12px; border-top:1px solid var(--slate-200); padding-top:18px;">
        <button id="btn-close-slip" onclick="window.App.closeCandidateSlip()" class="btn-action outline" style="width:auto; padding:8px 18px;">
          Tutup
        </button>
        <button id="btn-print-slip" onclick="window.print()" class="btn-action primary" style="width:auto; padding:8px 22px;">
          <i class="fa-solid fa-print"></i> Cetak Slip Rasmi
        </button>
      </div>

    </div>
  </div>
"""

# Insert modal before closing </body> tag
if 'id="modal-slip-backdrop"' not in html:
    html = html.replace('</body>', modal_slip_html + '\n</body>')

# =========================================================================
# 2. UPDATE TABLE STRUCTURE & DYNAMIC RENDER FOR PUBLIC VS ADMIN
# =========================================================================
# Replace table header in tab-candidates to have id="table-candidates-head"
old_tbl_markup = """      <!-- JADUAL 6 LAJUR -->
      <div class="table-container">
        <table class="styled-table" id="table-candidates">
          <thead>
            <tr>
              <th>No Badan</th>
              <th>Nama Calon</th>
              <th>Unit</th>
              <th>Sekolah</th>
              <th>Jumlah Markah</th>
              <th>Status Keputusan</th>
            </tr>
          </thead>
          <tbody id="table-candidates-body">
          </tbody>
        </table>
      </div>"""

new_tbl_markup = """      <!-- JADUAL CALON DINAMIK (AWAM / ADMIN) -->
      <div class="table-container">
        <table class="styled-table" id="table-candidates">
          <thead id="table-candidates-head">
            <!-- Dijana Dinamik Mengikut Status Log Masuk Admin -->
          </thead>
          <tbody id="table-candidates-body">
          </tbody>
        </table>
      </div>"""

html = html.replace(old_tbl_markup, new_tbl_markup)

# =========================================================================
# 3. REWRITE renderCandidatesTable & openCandidateSlip IN JS
# =========================================================================
new_render_and_slip_js = """
      openCandidateSlip(noBadan) {
        const c = this.state.candidates.find(x => (x.noBadan === noBadan || x.noGiliran === noBadan));
        if (!c) {
          alert('Maklumat calon tidak dijumpai.');
          return;
        }

        const modal = document.getElementById('modal-slip-backdrop');
        if (!modal) return;

        document.getElementById('slip-candidate-name').innerText = (c.nama || '').toUpperCase();
        document.getElementById('slip-candidate-nobadan').innerText = c.noBadan || c.noGiliran || '-';
        document.getElementById('slip-candidate-unit').innerText = `${c.unit} • ${c.pangkat || (c.unit === 'TKRS' ? 'KOPERAL TKRS' : 'SARJAN KRS')}`;
        document.getElementById('slip-candidate-sekolah').innerText = (c.sekolah || '').toUpperCase();
        document.getElementById('slip-score-overall').innerText = `${c.overall}%`;

        // Breakdown scores for Admin
        document.getElementById('slip-score-kawad').innerText = `${c.kawad}%`;
        document.getElementById('slip-score-bm').innerText = `${c.bantuMula}%`;
        document.getElementById('slip-score-ikatan').innerText = `${c.ikatan}%`;

        const adminBreakdown = document.getElementById('slip-admin-module-breakdown');
        if (adminBreakdown) {
          adminBreakdown.style.display = this.state.isAdminLoggedIn ? 'block' : 'none';
        }

        // Status badge
        let badgeHtml = '<span class="status-badge pending">Belum Dinilai</span>';
        if (c.isTarikDiri || c.statusText === 'TARIK DIRI' || (c.catatan && c.catatan.includes('TARIK DIRI'))) {
          badgeHtml = '<span class="status-badge withdraw"><i class="fa-solid fa-person-walking-arrow-right"></i> Tarik Diri (TD)</span>';
        } else if (c.statusText === 'TH' || c.isAbsent || (c.catatan && c.catatan.includes('TIDAK HADIR'))) {
          badgeHtml = '<span class="status-badge absent"><i class="fa-solid fa-user-slash"></i> Tidak Hadir (TH)</span>';
        } else if (c.statusText === 'LLL') {
          badgeHtml = '<span class="status-badge pass"><i class="fa-solid fa-circle-check"></i> Lulus Pentauliahan (LLL)</span>';
        } else if (c.rawOverall >= 0.50) {
          badgeHtml = `<span class="status-badge conditional"><i class="fa-solid fa-triangle-exclamation"></i> Lulus Bersyarat (${c.statusText || 'LLG'})</span>`;
        } else if (c.rawOverall > 0) {
          badgeHtml = `<span class="status-badge fail"><i class="fa-solid fa-circle-xmark"></i> Belum Capai Tahap (${c.statusText || 'GGG'})</span>`;
        }
        document.getElementById('slip-status-badge').innerHTML = badgeHtml;

        modal.style.display = 'flex';
      },

      closeCandidateSlip() {
        const modal = document.getElementById('modal-slip-backdrop');
        if (modal) modal.style.display = 'none';
      },

      renderCandidatesTable() {
        const thead = document.getElementById('table-candidates-head');
        const tbody = document.getElementById('table-candidates-body');
        if (!tbody) return;

        const isAdmin = this.state.isAdminLoggedIn;

        // 1. RENDER HEADER MENGIKUT MOD (AWAM VS ADMIN)
        if (thead) {
          if (isAdmin) {
            thead.innerHTML = `
              <tr>
                <th>No Badan</th>
                <th>Nama Calon</th>
                <th>Unit</th>
                <th>Sekolah</th>
                <th style="background:#1e3a8a; color:#ffffff; text-align:center;">Kawad (60%)</th>
                <th style="background:#1e3a8a; color:#ffffff; text-align:center;">B. Mula (20%)</th>
                <th style="background:#1e3a8a; color:#ffffff; text-align:center;">Ikatan (20%)</th>
                <th style="text-align:center;">Jumlah Markah</th>
                <th style="text-align:center;">Status Keputusan</th>
                <th style="text-align:center;">Slip</th>
              </tr>
            `;
          } else {
            thead.innerHTML = `
              <tr>
                <th>No Badan</th>
                <th>Nama Calon</th>
                <th>Unit</th>
                <th>Sekolah</th>
                <th style="text-align:center;">Jumlah Markah</th>
                <th style="text-align:center;">Status Keputusan</th>
              </tr>
            `;
          }
        }

        // 2. FILTER DATA
        const searchQuery = (document.getElementById('input-candidate-search')?.value || '').toLowerCase();
        const filterUnit = document.getElementById('select-unit')?.value || 'ALL';
        const filterKumpulan = document.getElementById('select-kumpulan')?.value || 'ALL';
        const filterJantina = document.getElementById('select-jantina')?.value || 'ALL';
        const filterStatus = document.getElementById('select-status')?.value || 'ALL';

        const filtered = this.state.candidates.filter(c => {
          const matchSearch = (c.nama || '').toLowerCase().includes(searchQuery) ||
                              (c.noBadan || '').toLowerCase().includes(searchQuery) ||
                              (c.sekolah || '').toLowerCase().includes(searchQuery);
          
          const matchUnit = filterUnit === 'ALL' || c.unit === filterUnit;
          const matchKumpulan = filterKumpulan === 'ALL' || c.kumpulan === filterKumpulan;
          const matchJantina = filterJantina === 'ALL' || c.jantina === filterJantina;

          let matchStatus = true;
          if (filterStatus === 'PASS') {
            matchStatus = c.statusText === 'LLL';
          } else if (filterStatus === 'CONDITIONAL') {
            matchStatus = c.statusText !== 'LLL' && !c.isAbsent && !c.isTarikDiri && (c.rawOverall >= 0.5);
          } else if (filterStatus === 'FAIL') {
            matchStatus = c.statusText !== 'LLL' && !c.isAbsent && !c.isTarikDiri && c.rawOverall < 0.5 && (c.rawOverall > 0);
          } else if (filterStatus === 'PENDING') {
            matchStatus = (!c.rawOverall || c.rawOverall === 0) && !c.isAbsent && !c.isTarikDiri;
          } else if (filterStatus === 'ABSENT') {
            matchStatus = c.isAbsent || c.statusText === 'TH' || (c.catatan && c.catatan.includes('TIDAK HADIR'));
          } else if (filterStatus === 'WITHDRAW') {
            matchStatus = c.isTarikDiri || c.statusText === 'TARIK DIRI' || (c.catatan && c.catatan.includes('TARIK DIRI'));
          }

          return matchSearch && matchUnit && matchKumpulan && matchJantina && matchStatus;
        });

        tbody.innerHTML = '';
        const colspanCount = isAdmin ? 10 : 6;
        if (filtered.length === 0) {
          tbody.innerHTML = `<tr><td colspan="${colspanCount}" style="text-align:center; padding:32px; color:var(--slate-500); font-weight:600;">Tiada rekod calon yang sepadan dengan carian atau penapis anda.</td></tr>`;
          return;
        }

        // 3. RENDER ROWS (AWAM VS ADMIN)
        tbody.innerHTML = filtered.map(c => {
          let badgeHtml = '<span class="status-badge pending">Belum Dinilai</span>';
          if (c.isTarikDiri || c.statusText === 'TARIK DIRI' || (c.catatan && c.catatan.includes('TARIK DIRI'))) {
            badgeHtml = '<span class="status-badge withdraw"><i class="fa-solid fa-person-walking-arrow-right"></i> Tarik Diri (TD)</span>';
          } else if (c.statusText === 'TH' || c.isAbsent || (c.catatan && c.catatan.includes('TIDAK HADIR'))) {
            badgeHtml = '<span class="status-badge absent"><i class="fa-solid fa-user-slash"></i> Tidak Hadir (TH)</span>';
          } else if (c.statusText === 'LLL') {
            badgeHtml = '<span class="status-badge pass"><i class="fa-solid fa-circle-check"></i> Lulus (LLL)</span>';
          } else if (c.rawOverall >= 0.50) {
            badgeHtml = `<span class="status-badge conditional"><i class="fa-solid fa-triangle-exclamation"></i> Lulus Bersyarat (${c.statusText || 'LLG'})</span>`;
          } else if (c.rawOverall > 0) {
            badgeHtml = `<span class="status-badge fail"><i class="fa-solid fa-circle-xmark"></i> Belum Capai Tahap (${c.statusText || 'GGG'})</span>`;
          }

          if (isAdmin) {
            return `
              <tr>
                <td style="font-weight:800; color:var(--royal-blue);">${c.noBadan || c.noGiliran}</td>
                <td style="font-weight:700;">${c.nama}</td>
                <td><span class="unit-badge ${c.unit.toLowerCase()}">${c.unit}</span></td>
                <td>${c.sekolah}</td>
                <td style="text-align:center; font-weight:700; background:#f8fafc; color:#1e40af;">${c.kawad}%</td>
                <td style="text-align:center; font-weight:700; background:#f8fafc; color:#1e40af;">${c.bantuMula}%</td>
                <td style="text-align:center; font-weight:700; background:#f8fafc; color:#1e40af;">${c.ikatan}%</td>
                <td style="text-align:center; font-weight:800; font-size:15px; color:var(--slate-900);">${c.overall}%</td>
                <td style="text-align:center;">${badgeHtml}</td>
                <td style="text-align:center;">
                  <button class="btn-table-slip" onclick="window.App.openCandidateSlip('${c.noBadan || c.noGiliran}')" style="padding:6px 12px; background:#eff6ff; border:1px solid #bfdbfe; border-radius:6px; color:var(--royal-accent); font-size:12.5px; font-weight:700; cursor:pointer;">
                    <i class="fa-solid fa-file-lines"></i> Slip
                  </button>
                </td>
              </tr>
            `;
          } else {
            return `
              <tr>
                <td style="font-weight:800; color:var(--royal-blue);">${c.noBadan || c.noGiliran}</td>
                <td style="font-weight:700;">${c.nama}</td>
                <td><span class="unit-badge ${c.unit.toLowerCase()}">${c.unit}</span></td>
                <td>${c.sekolah}</td>
                <td style="text-align:center; font-weight:800; font-size:15px; color:var(--slate-900);">${c.overall}%</td>
                <td style="text-align:center;">${badgeHtml}</td>
              </tr>
            `;
          }
        }).join('');

        const countEl = document.getElementById('label-table-count');
        if (countEl) {
          countEl.innerText = `Memaparkan ${filtered.length} daripada ${this.state.candidates.length} calon`;
        }
      },
"""

# Replace old renderCandidatesTable in html with new_render_and_slip_js
pattern = r'renderCandidatesTable\(\)\s*\{[\s\S]*?populateCandidateDropdown\(\)\s*\{'
html = re.sub(pattern, new_render_and_slip_js.strip() + '\n\n      populateCandidateDropdown() {', html)

# Ensure window.App = App is executed
if 'window.App = App;' not in html:
    html = html.replace('if (document.readyState === \'loading\') {', 'window.App = App;\n    if (document.readyState === \'loading\') {')

# Also update updateAuthVisuals to re-render candidate table immediately upon login/logout
old_update_auth = """        if (this.state.isAdminLoggedIn) {
          if (badge) {
            badge.style.display = 'inline-flex';
            badge.classList.add('logged-in');
            badge.innerHTML = '<i class="fa-solid fa-shield-halved"></i> PEGAWAI DATA TKRS JB | KAPTEN MOHD SYAZWAN BIN SULAIMAN';
          }
          if (manageCard) manageCard.style.display = 'block';
          if (screenLogin) screenLogin.style.display = 'none';
          if (screenControl) screenControl.style.display = 'block';
        } else {
          if (badge) badge.style.display = 'none';
          if (manageCard) manageCard.style.display = 'none';
          if (screenLogin) screenLogin.style.display = 'block';
          if (screenControl) screenControl.style.display = 'none';
        }"""

new_update_auth = """        if (this.state.isAdminLoggedIn) {
          document.body.classList.add('is-admin');
          if (badge) {
            badge.style.display = 'inline-flex';
            badge.classList.add('logged-in');
            badge.innerHTML = '<i class="fa-solid fa-shield-halved"></i> PEGAWAI DATA TKRS JB | KAPTEN MOHD SYAZWAN BIN SULAIMAN';
          }
          if (manageCard) manageCard.style.display = 'block';
          if (screenLogin) screenLogin.style.display = 'none';
          if (screenControl) screenControl.style.display = 'block';
          const btnCsv = document.getElementById('btn-csv-export');
          if (btnCsv) btnCsv.style.display = 'inline-flex';
        } else {
          document.body.classList.remove('is-admin');
          if (badge) badge.style.display = 'none';
          if (manageCard) manageCard.style.display = 'none';
          if (screenLogin) screenLogin.style.display = 'block';
          if (screenControl) screenControl.style.display = 'none';
          const btnCsv = document.getElementById('btn-csv-export');
          if (btnCsv) btnCsv.style.display = 'none';
        }
        this.renderCandidatesTable();"""

html = html.replace(old_update_auth, new_update_auth)

# Save Netlify index.html
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
