import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Building Clean Corporate UI (Centered Data, No Urus/Slip buttons, Instant Admin View)...")

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# =========================================================================
# 1. TAB 4: KEPUTUSAN CALON TERBAIK (REMOVED SLIP COLUMN & ENHANCED UI)
# =========================================================================
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
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(520px, 1fr)); gap:24px;">
        
        <!-- 1. TKRS LELAKI -->
        <div class="top-category-card">
          <div class="top-category-header">
            <div class="top-category-title" style="color:#059669;">
              <i class="fa-solid fa-medal" style="color:#eab308; font-size:20px;"></i>
              <span>5 TERBAIK TKRS — LELAKI</span>
            </div>
            <span class="unit-badge tkrs">SEKOLAH RENDAH</span>
          </div>
          <div class="table-container" style="box-shadow:none; border:1px solid var(--slate-200);">
            <table class="data-table">
              <thead>
                <tr>
                  <th style="width:70px; text-align:center;">Ked.</th>
                  <th style="width:130px; text-align:center;">No Badan</th>
                  <th style="text-align:left;">Nama Calon</th>
                  <th style="text-align:left;">Sekolah</th>
                  <th style="width:130px; text-align:center;">Markah (%)</th>
                  <th style="width:140px; text-align:center;">Status</th>
                </tr>
              </thead>
              <tbody id="top-tbody-tkrs-l">
                <!-- Dijana Dinamik -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- 2. TKRS PEREMPUAN -->
        <div class="top-category-card">
          <div class="top-category-header">
            <div class="top-category-title" style="color:#d97706;">
              <i class="fa-solid fa-medal" style="color:#eab308; font-size:20px;"></i>
              <span>5 TERBAIK TKRS — PEREMPUAN</span>
            </div>
            <span class="unit-badge tkrs">SEKOLAH RENDAH</span>
          </div>
          <div class="table-container" style="box-shadow:none; border:1px solid var(--slate-200);">
            <table class="data-table">
              <thead>
                <tr>
                  <th style="width:70px; text-align:center;">Ked.</th>
                  <th style="width:130px; text-align:center;">No Badan</th>
                  <th style="text-align:left;">Nama Calon</th>
                  <th style="text-align:left;">Sekolah</th>
                  <th style="width:130px; text-align:center;">Markah (%)</th>
                  <th style="width:140px; text-align:center;">Status</th>
                </tr>
              </thead>
              <tbody id="top-tbody-tkrs-p">
                <!-- Dijana Dinamik -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- 3. KRS LELAKI -->
        <div class="top-category-card">
          <div class="top-category-header">
            <div class="top-category-title" style="color:#1e40af;">
              <i class="fa-solid fa-medal" style="color:#eab308; font-size:20px;"></i>
              <span>5 TERBAIK KRS — LELAKI</span>
            </div>
            <span class="unit-badge krs">SEKOLAH MENENGAH</span>
          </div>
          <div class="table-container" style="box-shadow:none; border:1px solid var(--slate-200);">
            <table class="data-table">
              <thead>
                <tr>
                  <th style="width:70px; text-align:center;">Ked.</th>
                  <th style="width:130px; text-align:center;">No Badan</th>
                  <th style="text-align:left;">Nama Calon</th>
                  <th style="text-align:left;">Sekolah</th>
                  <th style="width:130px; text-align:center;">Markah (%)</th>
                  <th style="width:140px; text-align:center;">Status</th>
                </tr>
              </thead>
              <tbody id="top-tbody-krs-l">
                <!-- Dijana Dinamik -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- 4. KRS PEREMPUAN -->
        <div class="top-category-card">
          <div class="top-category-header">
            <div class="top-category-title" style="color:#db2777;">
              <i class="fa-solid fa-medal" style="color:#eab308; font-size:20px;"></i>
              <span>5 TERBAIK KRS — PEREMPUAN</span>
            </div>
            <span class="unit-badge krs">SEKOLAH MENENGAH</span>
          </div>
          <div class="table-container" style="box-shadow:none; border:1px solid var(--slate-200);">
            <table class="data-table">
              <thead>
                <tr>
                  <th style="width:70px; text-align:center;">Ked.</th>
                  <th style="width:130px; text-align:center;">No Badan</th>
                  <th style="text-align:left;">Nama Calon</th>
                  <th style="text-align:left;">Sekolah</th>
                  <th style="width:130px; text-align:center;">Markah (%)</th>
                  <th style="width:140px; text-align:center;">Status</th>
                </tr>
              </thead>
              <tbody id="top-tbody-krs-p">
                <!-- Dijana Dinamik -->
              </tbody>
            </table>
          </div>
        </div>

      </div>
    </section>"""

# Replace tab-top-results in HTML
sec_pattern = r'<section class=[\x22\x27]tab-content[\x22\x27] id=[\x22\x27]tab-top-results[\x22\x27]>[\s\S]*?</section>'
html = re.sub(sec_pattern, tab_top_results_html.strip(), html)

# =========================================================================
# 2. JAVASCRIPT: RENDER TOP RESULTS (NO SLIP BUTTONS, CENTERED RANKS/SCORES)
# =========================================================================
js_top_results = """
      renderTopResults() {
        const renderGroup = (elementId, candidatesList) => {
          const tbody = document.getElementById(elementId);
          if (!tbody) return;
          if (!candidatesList || candidatesList.length === 0) {
            tbody.innerHTML = '<tr><td colspan="6" style="text-align:center; padding:24px; color:#94a3b8; font-weight:600;">Tiada rekod calon berdaftar.</td></tr>';
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
            
            let statusBadge = '<span class="status-badge pending">Belum Dinilai</span>';
            if (c.statusText === 'LLL') {
              statusBadge = '<span class="status-badge pass"><i class="fa-solid fa-circle-check"></i> Lulus (LLL)</span>';
            } else if (c.rawOverall >= 0.50) {
              statusBadge = `<span class="status-badge conditional">Bersyarat (${c.statusText || 'LLG'})</span>`;
            } else if (c.rawOverall > 0) {
              statusBadge = `<span class="status-badge fail">Gagal (${c.statusText || 'GGG'})</span>`;
            }

            return `
              <tr>
                <td style="text-align:center; vertical-align:middle;">${badge}</td>
                <td style="text-align:center; font-weight:800; color:var(--royal-blue); vertical-align:middle;">${c.noBadan || c.noGiliran}</td>
                <td style="text-align:left; font-weight:800; color:var(--slate-900); vertical-align:middle;">${(c.nama || '').toUpperCase()}</td>
                <td style="text-align:left; font-size:13px; color:var(--slate-700); font-weight:600; vertical-align:middle;">${(c.sekolah || '').toUpperCase()}</td>
                <td style="text-align:center; font-weight:800; color:#1e3a8a; font-size:16px; vertical-align:middle;">${c.overall}%</td>
                <td style="text-align:center; vertical-align:middle;">${statusBadge}</td>
              </tr>
            `;
          }).join('');
        };

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

# Replace renderTopResults in JS
top_fn_pattern = r'renderTopResults\(\)\s*\{[\s\S]*?renderCandidatesTable\(\)\s*\{'
html = re.sub(top_fn_pattern, js_top_results.strip() + '\n\n      renderCandidatesTable() {', html)

# =========================================================================
# 3. JAVASCRIPT: RENDER CANDIDATES TABLE (NO URUS BUTTON, CENTERED, 9 COLS IN ADMIN)
# =========================================================================
js_candidates_table = """
      renderCandidatesTable() {
        const thead = document.getElementById('table-candidates-head');
        const tbody = document.getElementById('table-candidates-body');
        if (!tbody) return;

        const isAdmin = this.state.isAdminLoggedIn;

        // 1. RENDER THEAD MENGIKUT STATUS ADMIN
        if (thead) {
          if (isAdmin) {
            thead.innerHTML = `
              <tr>
                <th style="text-align:center; width:130px;">No Badan</th>
                <th style="text-align:left;">Nama Calon</th>
                <th style="text-align:center; width:80px;">Unit</th>
                <th style="text-align:left;">Sekolah</th>
                <th style="text-align:center; background:#1e3a8a; color:#ffffff; width:110px;">Kawad (60%)</th>
                <th style="text-align:center; background:#1e3a8a; color:#ffffff; width:110px;">B. Mula (20%)</th>
                <th style="text-align:center; background:#1e3a8a; color:#ffffff; width:110px;">Ikatan (20%)</th>
                <th style="text-align:center; width:120px;">Jumlah Markah</th>
                <th style="text-align:center; width:150px;">Status Keputusan</th>
              </tr>
            `;
          } else {
            thead.innerHTML = `
              <tr>
                <th style="text-align:center; width:140px;">No Badan</th>
                <th style="text-align:left;">Nama Calon</th>
                <th style="text-align:center; width:90px;">Unit</th>
                <th style="text-align:left;">Sekolah</th>
                <th style="text-align:center; width:140px;">Jumlah Markah</th>
                <th style="text-align:center; width:160px;">Status Keputusan</th>
              </tr>
            `;
          }
        }

        // 2. PENAPISAN DATA CALON
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
        const colspanCount = isAdmin ? 9 : 6;
        if (filtered.length === 0) {
          tbody.innerHTML = `<tr><td colspan="${colspanCount}" style="text-align:center; padding:32px; color:var(--slate-500); font-weight:600;">Tiada rekod calon yang sepadan dengan carian atau penapis anda.</td></tr>`;
          return;
        }

        // 3. RENDER BARIS JADUAL
        tbody.innerHTML = filtered.map(c => {
          let badgeHtml = '<span class="status-badge pending">Belum Dinilai</span>';
          if (c.isTarikDiri || c.statusText === 'TARIK DIRI' || (c.catatan && c.catatan.includes('TARIK DIRI'))) {
            badgeHtml = '<span class="status-badge withdraw"><i class="fa-solid fa-person-walking-arrow-right"></i> Tarik Diri (TD)</span>';
          } else if (c.statusText === 'TH' || c.isAbsent || (c.catatan && c.catatan.includes('TIDAK HADIR'))) {
            badgeHtml = '<span class="status-badge absent"><i class="fa-solid fa-user-slash"></i> Tidak Hadir (TH)</span>';
          } else if (c.statusText === 'LLL') {
            badgeHtml = '<span class="status-badge pass"><i class="fa-solid fa-circle-check"></i> Lulus (LLL)</span>';
          } else if (c.rawOverall >= 0.50) {
            badgeHtml = `<span class="status-badge conditional"><i class="fa-solid fa-triangle-exclamation"></i> Bersyarat (${c.statusText || 'LLG'})</span>`;
          } else if (c.rawOverall > 0) {
            badgeHtml = `<span class="status-badge fail"><i class="fa-solid fa-circle-xmark"></i> Gagal (${c.statusText || 'GGG'})</span>`;
          }

          if (isAdmin) {
            return `
              <tr>
                <td style="text-align:center; font-weight:800; color:var(--royal-blue); vertical-align:middle;">${c.noBadan || c.noGiliran}</td>
                <td style="text-align:left; font-weight:700; color:var(--slate-900); vertical-align:middle;">${(c.nama || '').toUpperCase()}</td>
                <td style="text-align:center; vertical-align:middle;"><span class="unit-badge ${c.unit.toLowerCase()}">${c.unit}</span></td>
                <td style="text-align:left; color:var(--slate-700); font-weight:600; vertical-align:middle;">${(c.sekolah || '').toUpperCase()}</td>
                <td style="text-align:center; font-weight:800; color:#1e40af; background:#f8fafc; vertical-align:middle;">${c.kawad}%</td>
                <td style="text-align:center; font-weight:800; color:#1e40af; background:#f8fafc; vertical-align:middle;">${c.bantuMula}%</td>
                <td style="text-align:center; font-weight:800; color:#1e40af; background:#f8fafc; vertical-align:middle;">${c.ikatan}%</td>
                <td style="text-align:center; font-weight:800; font-size:15px; color:var(--slate-900); vertical-align:middle;">${c.overall}%</td>
                <td style="text-align:center; vertical-align:middle;">${badgeHtml}</td>
              </tr>
            `;
          } else {
            return `
              <tr>
                <td style="text-align:center; font-weight:800; color:var(--royal-blue); vertical-align:middle;">${c.noBadan || c.noGiliran}</td>
                <td style="text-align:left; font-weight:700; color:var(--slate-900); vertical-align:middle;">${(c.nama || '').toUpperCase()}</td>
                <td style="text-align:center; vertical-align:middle;"><span class="unit-badge ${c.unit.toLowerCase()}">${c.unit}</span></td>
                <td style="text-align:left; color:var(--slate-700); font-weight:600; vertical-align:middle;">${(c.sekolah || '').toUpperCase()}</td>
                <td style="text-align:center; font-weight:800; font-size:15px; color:var(--slate-900); vertical-align:middle;">${c.overall}%</td>
                <td style="text-align:center; vertical-align:middle;">${badgeHtml}</td>
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

# Replace renderCandidatesTable in JS
cand_fn_pattern = r'renderCandidatesTable\(\)\s*\{[\s\S]*?populateCandidateDropdown\(\)\s*\{'
html = re.sub(cand_fn_pattern, js_candidates_table.strip() + '\n\n      populateCandidateDropdown() {', html)

# =========================================================================
# 4. UPDATE AUTH VISUALS & STATE INITIALIZATION
# =========================================================================
# Check if pentauliahan_admin_auth is stored in sessionStorage on init
init_auth_code = """
        const savedAuth = sessionStorage.getItem('pentauliahan_admin_auth');
        if (savedAuth === 'true') {
          this.state.isAdminLoggedIn = true;
        }
        this.updateAuthVisuals();
"""

html = html.replace('this.updateAuthVisuals();', init_auth_code.strip())

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
