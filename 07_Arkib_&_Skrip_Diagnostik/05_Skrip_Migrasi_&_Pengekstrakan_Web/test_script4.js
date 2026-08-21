/**
 * =========================================================================
 * SISTEM PENGURUSAN PENTAULIAHAN KRS & TKRS DAERAH JOHOR BAHRU 2026
 * APLIKASI UTAMA (MAIN APP CONTROLLER & PROGRAMMATIC EVENT BINDINGS)
 * =========================================================================
 */

const App = {
  // State Utama
  state: {
    candidates: [],
    isAdminUnlocked: false,
    adminPIN: 'adminseketejb', // PIN Keselamatan Urus Setia
    activeTab: 'tab-overview',
    lastSyncTime: null,
    isSyncing: false,
    autoSyncInterval: null,
    sheetId: '1_YmAJ6XVfBREx4_NDTUWRMXAL1Jgi-1vSFS2528dtW0',
    currentThresholds: {
      kawad: 0.70,
      ikatan: 0.50, // Wajaran Bantu Mula + Ikatan
      overall: 0.70,
      wajaranKawad: 0.60,
      wajaranBantuMula: 0.20,
      wajaranIkatan: 0.20
    }
  },

  /**
   * Permulaan Aplikasi (Init)
   */
  init() {
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
  },

  /**
   * Penyegerakan Masa Nyata (Live Sync)
   */
  async syncLiveGoogleSheet() {
    if (this.state.isSyncing) return;
    this.state.isSyncing = true;
    this.updateSyncUI('syncing');

    // Jika dalam persekitaran Google Apps Script native
    if (typeof google !== 'undefined' && google.script && google.script.run) {
      google.script.run
        .withSuccessHandler(data => {
          if (data && data.candidates && data.candidates.length > 0) {
            if (data.thresholds) {
              this.state.currentThresholds = {
                kawad: data.thresholds.thresholdKawad,
                ikatan: data.thresholds.thresholdIkatan,
                overall: data.thresholds.thresholdOverall,
                wajaranKawad: data.thresholds.wajaranKawad,
                wajaranBantuMula: data.thresholds.wajaranBantuMula,
                wajaranIkatan: data.thresholds.wajaranIkatan
              };
            }
            this.state.candidates = AnalyticsEngine.processCandidates(data.candidates, this.state.currentThresholds);
            this.state.lastSyncTime = new Date();
            this.renderAll();
            this.updateSyncUI('success');
          }
          this.state.isSyncing = false;
        })
        .withFailureHandler(err => {
          console.warn('Google Script Run sync error, fallback to local/gviz:', err);
          this.fetchViaGViz();
        })
        .getDashboardData();
      return;
    }

    // Jika di luar Google Apps Script (Standard Browser)
    this.fetchViaGViz();
  },

  async fetchViaGViz() {
    try {
      const urlTKRS = `https://docs.google.com/spreadsheets/d/${this.state.sheetId}/gviz/tq?tqx=out:json&sheet=ANALISIS_TKRS`;
      const urlKRS = `https://docs.google.com/spreadsheets/d/${this.state.sheetId}/gviz/tq?tqx=out:json&sheet=ANALISIS_KRS`;

      const [resTKRS, resKRS] = await Promise.all([
        fetch(urlTKRS).then(r => r.text()),
        fetch(urlKRS).then(r => r.text())
      ]);

      const parseGViz = (txt, unit, pangkat) => {
        const jsonTxt = txt.substring(txt.indexOf('{'), txt.lastIndexOf('}') + 1);
        const data = JSON.parse(jsonTxt);
        const rows = data.table.rows;
        const result = [];

        for (let i = 1; i < rows.length; i++) {
          const c = rows[i].c;
          if (!c || !c[1] || !c[1].v) continue;

          const noGiliran = String(c[1].v).trim();
          const nama = c[2] ? String(c[2].v).trim() : '';
          const sekolah = c[3] ? String(c[3].v).trim() : '';
          const jantina = c[4] ? String(c[4].v).trim() : 'L';
          const agama = c[5] ? String(c[5].v).trim() : '';
          const rawKawad = c[6] && typeof c[6].v === 'number' ? c[6].v : 0;
          const rawBantuMula = c[7] && typeof c[7].v === 'number' ? c[7].v : 0;
          const rawIkatan = c[8] && typeof c[8].v === 'number' ? c[8].v : 0;
          const rawOverall = c[9] && typeof c[9].v === 'number' ? c[9].v : 0;
          const statusText = c[10] ? String(c[10].v).trim() : '';
          const catatan = c[11] ? String(c[11].v).trim() : '';

          result.push({
            noGiliran,
            nama,
            sekolah,
            jantina,
            agama,
            unit,
            pangkat,
            kawad: (rawKawad * 100).toFixed(1),
            bantuMula: (rawBantuMula * 100).toFixed(1),
            ikatan: (rawIkatan * 100).toFixed(1),
            overall: (rawOverall * 100).toFixed(1),
            rawKawad,
            rawBantuMula,
            rawIkatan,
            rawOverall,
            status: statusText,
            catatan
          });
        }
        return result;
      };

      const liveTKRS = parseGViz(resTKRS, 'TKRS', 'Koperal');
      const liveKRS = parseGViz(resKRS, 'KRS', 'Sarjan');

      if (liveTKRS.length > 0 || liveKRS.length > 0) {
        const combined = [...liveTKRS, ...liveKRS];
        this.state.candidates = AnalyticsEngine.processCandidates(combined, this.state.currentThresholds);
        this.state.lastSyncTime = new Date();
        this.renderAll();
        this.updateSyncUI('success');
      }
    } catch (e) {
      console.warn('Live Sheet API unreachable, using cached dataset:', e.message);
      this.updateSyncUI('cached');
    } finally {
      this.state.isSyncing = false;
    }
  },

  startAutoSync(intervalSeconds = 30) {
    if (this.state.autoSyncInterval) clearInterval(this.state.autoSyncInterval);
    this.state.autoSyncInterval = setInterval(() => {
      this.syncLiveGoogleSheet();
    }, intervalSeconds * 1000);
  },

  updateSyncUI(status) {
    const el = document.getElementById('live-sync-badge');
    if (!el) return;

    if (status === 'syncing') {
      el.innerHTML = '<span class="pulse-dot-syncing"></span> <span>Sedang synchronize...</span>';
    } else if (status === 'success') {
      const timeStr = this.state.lastSyncTime ? this.state.lastSyncTime.toLocaleTimeString('ms-MY') : '';
      el.innerHTML = `<span class="pulse-dot-live"></span> <span>Sync Masa Nyata (Live): ${timeStr}</span>`;
    } else {
      el.innerHTML = '<span class="pulse-dot-cached"></span> <span>Mod Tempatan (Offline Ready)</span>';
    }
  },

  /**
   * Render Semua Modul
   */
  renderAll() {
    this.renderKPIs();
    this.renderTokohChampions();
    this.renderStationLeaderboards();
    this.renderElementDeepAnalytics();
    this.renderSchoolLeague();
    this.renderGenderStats();
    this.renderCandidateDirectory();
    this.updateAdminVisibility();
  },

  renderKPIs() {
    if (typeof AnalyticsEngine === 'undefined') return;
    const kpis = AnalyticsEngine.getExecutiveKPIs(this.state.candidates);
    
    const elTotal = document.getElementById('kpi-total-candidates');
    const elTotalSub = document.getElementById('kpi-total-sub');
    const elPass = document.getElementById('kpi-pass-count');
    const elPassRate = document.getElementById('kpi-pass-rate');
    const elFail = document.getElementById('kpi-failed-count');
    const elPendingSub = document.getElementById('kpi-pending-sub');
    const elIssues = document.getElementById('kpi-issues-count');
    const elIssuesSub = document.getElementById('kpi-issues-sub');

    if (elTotal) elTotal.innerText = kpis.totalCandidates;
    if (elTotalSub) elTotalSub.innerText = `${kpis.totalTKRS} TKRS • ${kpis.totalKRS} KRS`;
    if (elPass) elPass.innerText = kpis.passCount;
    if (elPassRate) elPassRate.innerText = `${kpis.passRate}% Kadar Kelulusan`;
    if (elFail) elFail.innerText = kpis.failCount;
    if (elPendingSub) elPendingSub.innerText = `${kpis.evaluatedCount} Telah Dinilai • ${kpis.pendingCount} Belum`;
    if (elIssues) elIssues.innerText = kpis.absentCount + kpis.tarikDiriCount + kpis.tukarCount;
    if (elIssuesSub) elIssuesSub.innerText = `${kpis.absentCount} TH • ${kpis.tarikDiriCount} Tarik Diri • ${kpis.tukarCount} Gantian`;
  },

  renderTokohChampions() {
    if (typeof AnalyticsEngine === 'undefined') return;
    const champs = AnalyticsEngine.getOverallChampions(this.state.candidates);
    const container = document.getElementById('tokoh-champions-grid');
    if (!container) return;

    const createTokohCard = (title, category, cand, icon) => {
      if (!cand) {
        return `
          <div class="tokoh-card">
            <div class="tokoh-header">
              <div class="tokoh-icon">${icon}</div>
              <div>
                <div class="tokoh-category-badge">${category}</div>
                <div class="tokoh-title">${title}</div>
              </div>
            </div>
            <div style="color: var(--text-muted); font-size: 13px; text-align: center; padding: 20px 0;">
              Menunggu keputusan penilaian stesen...
            </div>
          </div>
        `;
      }

      return `
        <div class="tokoh-card">
          <div class="tokoh-header">
            <div class="tokoh-icon">${icon}</div>
            <div>
              <div class="tokoh-category-badge">${category}</div>
              <div class="tokoh-title">${title}</div>
            </div>
          </div>
          <div class="tokoh-name">${cand.nama}</div>
          <div class="tokoh-school">🏫 ${cand.sekolah} • <strong>${cand.noGiliran}</strong></div>
          <div class="tokoh-scores">
            <div class="tokoh-score-item">
              <div class="sc-lbl">Kawad</div>
              <div class="sc-val">${cand.displayKawad}</div>
            </div>
            <div class="tokoh-score-item">
              <div class="sc-lbl">Bantu Mula</div>
              <div class="sc-val">${cand.displayBantuMula}</div>
            </div>
            <div class="tokoh-score-item">
              <div class="sc-lbl">Ikatan</div>
              <div class="sc-val">${cand.displayIkatan}</div>
            </div>
            <div class="tokoh-score-item sc-total">
              <div class="sc-lbl">Jumlah</div>
              <div class="sc-val">${cand.displayOverall}</div>
            </div>
          </div>
        </div>
      `;
    };

    container.innerHTML = `
      ${createTokohCard('Tokoh Koperal TKRS (Lelaki)', 'TKRS', champs.tkrsLelaki, '👑')}
      ${createTokohCard('Tokoh Koperal TKRS (Perempuan)', 'TKRS', champs.tkrsPerempuan, '👑')}
      ${createTokohCard('Tokoh Sarjan KRS (Lelaki)', 'KRS', champs.krsLelaki, '🎖️')}
      ${createTokohCard('Tokoh Sarjan KRS (Perempuan)', 'KRS', champs.krsPerempuan, '🎖️')}
    `;
  },

  renderStationLeaderboards() {
    if (typeof AnalyticsEngine === 'undefined') return;
    const specialists = AnalyticsEngine.getStationSpecialists(this.state.candidates);
    
    const renderRankList = (containerId, list, scoreField) => {
      const container = document.getElementById(containerId);
      if (!container) return;

      if (!list || list.length === 0) {
        container.innerHTML = '<div style="color:var(--text-muted); font-size:12px; padding:10px;">Tiada rekod penilaian lagi.</div>';
        return;
      }

      let html = '<div class="rank-list">';
      list.forEach((c, idx) => {
        const rankClass = idx === 0 ? 'rank-1' : (idx === 1 ? 'rank-2' : (idx === 2 ? 'rank-3' : 'rank-other'));
        const scoreVal = (c[scoreField] * 100).toFixed(1) + '%';
        html += `
          <div class="rank-item">
            <div style="display:flex; align-items:center;">
              <div class="rank-badge ${rankClass}">${idx + 1}</div>
              <div>
                <div class="rank-cand-name">${c.nama}</div>
                <div class="rank-cand-school">${c.sekolah} • <strong>${c.noGiliran}</strong></div>
              </div>
            </div>
            <div class="rank-score">${scoreVal}</div>
          </div>
        `;
      });
      html += '</div>';
      container.innerHTML = html;
    };

    // Kawad Kaki
    renderRankList('lead-kawad-tkrs-l', specialists.kawad.tkrsLelaki, 'rawKawad');
    renderRankList('lead-kawad-tkrs-p', specialists.kawad.tkrsPerempuan, 'rawKawad');
    renderRankList('lead-kawad-krs-l', specialists.kawad.krsLelaki, 'rawKawad');
    renderRankList('lead-kawad-krs-p', specialists.kawad.krsPerempuan, 'rawKawad');

    // Bantu Mula
    renderRankList('lead-bm-tkrs-l', specialists.bantuMula.tkrsLelaki, 'rawBantuMula');
    renderRankList('lead-bm-tkrs-p', specialists.bantuMula.tkrsPerempuan, 'rawBantuMula');
    renderRankList('lead-bm-krs-l', specialists.bantuMula.krsLelaki, 'rawBantuMula');
    renderRankList('lead-bm-krs-p', specialists.bantuMula.krsPerempuan, 'rawBantuMula');

    // Tali Temali
    renderRankList('lead-ikatan-tkrs-l', specialists.ikatan.tkrsLelaki, 'rawIkatan');
    renderRankList('lead-ikatan-tkrs-p', specialists.ikatan.tkrsPerempuan, 'rawIkatan');
    renderRankList('lead-ikatan-krs-l', specialists.ikatan.krsLelaki, 'rawIkatan');
    renderRankList('lead-ikatan-krs-p', specialists.ikatan.krsPerempuan, 'rawIkatan');
  },

  renderElementDeepAnalytics() {
    if (typeof AnalyticsEngine === 'undefined' || typeof ChartsEngine === 'undefined') return;
    const elData = AnalyticsEngine.getElementAnalytics(this.state.candidates);
    ChartsEngine.renderElementBarChart('chart-krs-kawad-elements', elData.krs);
    ChartsEngine.renderElementBarChart('chart-tkrs-kawad-elements', elData.tkrs);
  },

  renderSchoolLeague() {
    if (typeof AnalyticsEngine === 'undefined') return;
    const schools = AnalyticsEngine.getSchoolRankings(this.state.candidates);
    const tbody = document.getElementById('school-table-body');
    if (!tbody) return;

    let html = '';
    schools.forEach((s, idx) => {
      const passRateBadge = s.passRate >= 100 ? 'badge-lulus' : (s.passRate >= 70 ? 'badge-lulus' : (s.passRate > 0 ? 'badge-th' : 'badge-pending'));
      html += `
        <tr>
          <td><strong>#${idx + 1}</strong></td>
          <td><strong>${s.sekolah}</strong></td>
          <td>${s.total} <span style="font-size:11px; color:var(--text-muted);">(${s.tkrsCount} TKRS, ${s.krsCount} KRS)</span></td>
          <td>${s.passed} / ${s.total}</td>
          <td><span class="badge-status ${passRateBadge}">${s.passRate}%</span></td>
          <td><strong>${s.avgOverall}%</strong></td>
          <td>${s.avgKawad}%</td>
          <td>
            <button class="btn-header btn-view-school" data-school="${escape(s.sekolah)}" style="padding:4px 10px; font-size:11px; color:var(--primary);">
              🔍 Lihat Calon
            </button>
          </td>
        </tr>
      `;
    });
    tbody.innerHTML = html;

    // Attach click events on school buttons
    tbody.querySelectorAll('.btn-view-school').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const sch = e.currentTarget.getAttribute('data-school');
        App.filterBySchool(sch);
      });
    });
  },

  filterSchoolTable() {
    const q = (document.getElementById('school-search-input')?.value || '').toLowerCase().trim();
    const rows = document.querySelectorAll('#school-table-body tr');
    rows.forEach(r => {
      const txt = r.innerText.toLowerCase();
      r.style.display = (!q || txt.includes(q)) ? '' : 'none';
    });
  },

  renderGenderStats() {
    if (typeof AnalyticsEngine === 'undefined' || typeof ChartsEngine === 'undefined') return;
    const genderStats = AnalyticsEngine.getGenderComparativeStats(this.state.candidates);
    ChartsEngine.renderGenderComparison('chart-gender-comparison', genderStats);

    const elBT = document.getElementById('gender-boys-total');
    const elBP = document.getElementById('gender-boys-pass');
    const elGT = document.getElementById('gender-girls-total');
    const elGP = document.getElementById('gender-girls-pass');

    if (elBT) elBT.innerText = `${genderStats.boys.total} Calon`;
    if (elBP) elBP.innerText = `${genderStats.boys.passCount} (${genderStats.boys.passRate}%)`;
    if (elGT) elGT.innerText = `${genderStats.girls.total} Calon`;
    if (elGP) elGP.innerText = `${genderStats.girls.passCount} (${genderStats.girls.passRate}%)`;
  },

  renderCandidateDirectory() {
    const tbody = document.getElementById('candidate-directory-body');
    if (!tbody) return;

    const q = (document.getElementById('dir-search-input')?.value || '').toLowerCase().trim();
    const unitFilter = document.getElementById('dir-unit-filter')?.value || 'ALL';
    const genderFilter = document.getElementById('dir-gender-filter')?.value || 'ALL';
    const statusFilter = document.getElementById('dir-status-filter')?.value || 'ALL';

    const list = this.state.candidates.filter(c => {
      const matchQ = !q || c.noGiliran.toLowerCase().includes(q) || c.nama.toLowerCase().includes(q) || c.sekolah.toLowerCase().includes(q);
      const matchUnit = unitFilter === 'ALL' || c.unit === unitFilter;
      const matchGender = genderFilter === 'ALL' || c.jantina === genderFilter;
      
      let matchStatus = true;
      if (statusFilter === 'PASS') matchStatus = c.isPass;
      else if (statusFilter === 'FAIL') matchStatus = (!c.isPass && c.isEvaluated);
      else if (statusFilter === 'ISSUES') matchStatus = (c.isAbsent || c.isTarikDiri || c.isTukar || !c.isEvaluated);

      return matchQ && matchUnit && matchGender && matchStatus;
    });

    if (list.length === 0) {
      tbody.innerHTML = '<tr><td colspan="10" style="text-align:center; padding:30px; color:var(--text-muted);">Tiada calon menepati kriteria carian.</td></tr>';
      return;
    }

    let html = '';
    list.forEach(c => {
      const badgeClass = c.isPass ? 'badge-lulus' : (c.isAbsent ? 'badge-gagal' : (c.isTarikDiri ? 'badge-gagal' : (c.isEvaluated ? 'badge-th' : 'badge-pending')));
      const statusText = c.isPass ? '🎖️ LULUS' : (c.isAbsent ? 'TH' : (c.isTarikDiri ? 'TARIK DIRI' : (c.isEvaluated ? 'BELUM CAPAI' : 'BELUM DINILAI')));

      html += `
        <tr>
          <td><strong>${c.noGiliran}</strong></td>
          <td>${c.nama}</td>
          <td><span class="badge-status" style="background:#f1f5f9; color:#334155;">${c.unit} (${c.jantina})</span></td>
          <td>${c.sekolah}</td>
          <td>${c.displayKawad}</td>
          <td>${c.displayBantuMula}</td>
          <td>${c.displayIkatan}</td>
          <td><strong>${c.displayOverall}</strong></td>
          <td><span class="badge-status ${badgeClass}">${statusText}</span></td>
          <td>
            <button class="btn-header btn-open-slip" data-id="${c.noGiliran}" style="padding:4px 10px; font-size:11px; color:var(--primary);">
              📄 Slip
            </button>
          </td>
        </tr>
      `;
    });
    tbody.innerHTML = html;

    // Attach click events on slip buttons
    tbody.querySelectorAll('.btn-open-slip').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.currentTarget.getAttribute('data-id');
        App.openCandidateSlip(id);
      });
    });
  },

  openCandidateSlip(noGiliran) {
    const cand = this.state.candidates.find(c => c.noGiliran === noGiliran);
    if (!cand) return;

    document.getElementById('slip-no-giliran').innerText = cand.noGiliran;
    document.getElementById('slip-nama').innerText = cand.nama;
    document.getElementById('slip-unit-pangkat').innerText = `${cand.unit} • Pangkat ${cand.pangkat}`;
    document.getElementById('slip-sekolah').innerText = cand.sekolah;
    
    document.getElementById('slip-score-kawad').innerText = cand.displayKawad;
    document.getElementById('slip-score-bm').innerText = cand.displayBantuMula;
    document.getElementById('slip-score-ikatan').innerText = cand.displayIkatan;
    document.getElementById('slip-score-overall').innerText = cand.displayOverall;

    const statusBadge = document.getElementById('slip-status-badge');
    if (cand.isPass) {
      statusBadge.className = 'badge-status badge-lulus';
      statusBadge.innerText = `🎖️ LAYAK DITAULIAHKAN PANGKAT ${cand.pangkat.toUpperCase()}`;
    } else {
      statusBadge.className = 'badge-status badge-gagal';
      statusBadge.innerText = `❌ BELUM MENCAPAI TAHAP KELAYAKAN PANGKAT`;
    }

    const modal = document.getElementById('modal-slip-backdrop');
    if (modal) modal.style.display = 'flex';
  },

  closeCandidateSlip() {
    const modal = document.getElementById('modal-slip-backdrop');
    if (modal) modal.style.display = 'none';
  },

  printSlip() {
    window.print();
  },

  /**
   * Kunci Keselamatan Urus Setia (PIN: adminseketejb)
   */
  openAdminPinModal() {
    if (this.state.isAdminUnlocked) {
      this.lockAdmin();
      return;
    }
    const modal = document.getElementById('modal-pin-backdrop');
    if (modal) modal.style.display = 'flex';
    const inp = document.getElementById('admin-pin-field');
    if (inp) {
      inp.value = '';
      inp.focus();
    }
  },

  closeAdminPinModal() {
    const modal = document.getElementById('modal-pin-backdrop');
    if (modal) modal.style.display = 'none';
    const inp = document.getElementById('admin-pin-field');
    if (inp) inp.value = '';
  },

  submitPin() {
    const entered = (document.getElementById('admin-pin-field')?.value || '').trim();

    if (entered === this.state.adminPIN) {
      this.state.isAdminUnlocked = true;
      this.closeAdminPinModal();
      this.updateAdminVisibility();
      this.switchTab('tab-admin');
      alert('🔓 Akses Urus Setia Berjaya Dibuka! Portal Pengurusan kini aktif.');
    } else {
      alert('❌ Kata Laluan / PIN Urus Setia Tidak Sah! Sila cuba lagi.');
      const inp = document.getElementById('admin-pin-field');
      if (inp) {
        inp.value = '';
        inp.focus();
      }
    }
  },

  lockAdmin() {
    this.state.isAdminUnlocked = false;
    this.updateAdminVisibility();
    alert('🔒 Mod Urus Setia Telah Dikunci.');
  },

  updateAdminVisibility() {
    const adminTabBtn = document.getElementById('tab-btn-admin');
    const adminGateBtn = document.getElementById('btn-admin-gate-text');
    
    if (this.state.isAdminUnlocked) {
      if (adminTabBtn) adminTabBtn.style.display = 'flex';
      if (adminGateBtn) adminGateBtn.innerText = '🔓 Urus Setia (Aktif - Klik Kunci)';
      this.syncAdminControls();
    } else {
      if (adminTabBtn) adminTabBtn.style.display = 'none';
      if (adminGateBtn) adminGateBtn.innerText = '🔒 Log Masuk Urus Setia';
      if (this.state.activeTab === 'tab-admin') {
        this.switchTab('tab-overview');
      }
    }
  },

  setSelectValueSafely(selectId, val, defaultVal) {
    const el = document.getElementById(selectId);
    if (!el) return;
    const num = typeof val === 'number' ? val : (parseFloat(val) || defaultVal);
    
    let matched = false;
    for (let i = 0; i < el.options.length; i++) {
      if (Math.abs(parseFloat(el.options[i].value) - num) < 0.001) {
        el.selectedIndex = i;
        matched = true;
        break;
      }
    }
    if (!matched) el.value = defaultVal.toFixed(2);
  },

  syncAdminControls() {
    const th = this.state.currentThresholds;
    this.setSelectValueSafely('admin-waj-kawad', th.wajaranKawad, 0.60);
    this.setSelectValueSafely('admin-waj-bm-ikatan', (th.wajaranBantuMula + th.wajaranIkatan), 0.40);
    this.setSelectValueSafely('sim-kawad', th.kawad, 0.70);
    this.setSelectValueSafely('sim-ikatan', th.ikatan, 0.50);
    this.setSelectValueSafely('sim-overall', th.overall, 0.70);
    this.runAdminSimulation();
  },

  runAdminSimulation() {
    const wK = parseFloat(document.getElementById('admin-waj-kawad')?.value) || 0.60;
    const wBM = parseFloat(document.getElementById('admin-waj-bm-ikatan')?.value) || 0.40;
    const tKawad = parseFloat(document.getElementById('sim-kawad')?.value) || 0.70;
    const tIkatan = parseFloat(document.getElementById('sim-ikatan')?.value) || 0.50;
    const tOverall = parseFloat(document.getElementById('sim-overall')?.value) || 0.70;

    const totalWeight = Math.round((wK + wBM) * 100);
    const weightBadge = document.getElementById('admin-weight-badge');
    if (weightBadge) {
      weightBadge.innerText = `Jumlah: ${totalWeight}%`;
      weightBadge.style.background = totalWeight === 100 ? '#dcfce7' : '#fee2e2';
      weightBadge.style.color = totalWeight === 100 ? '#166534' : '#991b1b';
    }

    const testThresholds = {
      kawad: tKawad,
      ikatan: tIkatan,
      overall: tOverall,
      wajaranKawad: wK,
      wajaranBantuMula: wBM / 2,
      wajaranIkatan: wBM / 2
    };

    const simulatedList = AnalyticsEngine.processCandidates(this.state.candidates, testThresholds);
    const simPassCount = simulatedList.filter(c => c.isPass).length;
    const simRate = simulatedList.length > 0 ? ((simPassCount / simulatedList.length) * 100).toFixed(1) : 0;
    const origPassCount = this.state.candidates.filter(c => c.isPass).length;
    const diff = simPassCount - origPassCount;
    const diffStr = diff >= 0 ? `(+${diff} calon)` : `(${diff} calon)`;

    const feedbackEl = document.getElementById('admin-sim-feedback');
    if (feedbackEl) {
      feedbackEl.innerHTML = `
        🔮 <strong>Hasil Simulasi Terkini:</strong><br>
        • Wajaran: Kawad <strong>${Math.round(wK*100)}%</strong> | Bantu Mula + Ikatan <strong>${Math.round(wBM*100)}%</strong><br>
        • Wajaran Lulus: Kawad ≥ <strong>${Math.round(tKawad*100)}%</strong> | Bantu Mula + Ikatan ≥ <strong>${Math.round(tIkatan*100)}%</strong> | Keseluruhan ≥ <strong>${Math.round(tOverall*100)}%</strong><br>
        👉 <strong>${simPassCount} / ${simulatedList.length} peserta</strong> (${simRate}%) dijangka <strong>LULUS PANGKAT</strong> ${diffStr}.
      `;
    }
  },

  applyAdminThresholds() {
    const wK = parseFloat(document.getElementById('admin-waj-kawad')?.value) || 0.60;
    const wBM = parseFloat(document.getElementById('admin-waj-bm-ikatan')?.value) || 0.40;
    const tKawad = parseFloat(document.getElementById('sim-kawad')?.value) || 0.70;
    const tIkatan = parseFloat(document.getElementById('sim-ikatan')?.value) || 0.50;
    const tOverall = parseFloat(document.getElementById('sim-overall')?.value) || 0.70;

    this.state.currentThresholds = {
      kawad: tKawad,
      ikatan: tIkatan,
      overall: tOverall,
      wajaranKawad: wK,
      wajaranBantuMula: wBM / 2,
      wajaranIkatan: wBM / 2
    };

    this.state.candidates = AnalyticsEngine.processCandidates(this.state.candidates, this.state.currentThresholds);
    this.renderAll();

    // Jika dalam persekitaran Google Apps Script, kemas kini juga script properties & spreadsheet formula
    if (typeof google !== 'undefined' && google.script && google.script.run) {
      google.script.run
        .withSuccessHandler(res => {
          alert('✅ ' + res);
        })
        .withFailureHandler(err => {
          alert('Ralat Google Sheet: ' + err.message);
        })
        .updatePassingThresholds({
          thresholdKawad: tKawad,
          thresholdIkatan: tIkatan,
          thresholdOverall: tOverall,
          wajaranKawad: wK,
          wajaranBantuMula: wBM / 2,
          wajaranIkatan: wBM / 2
        });
    } else {
      alert('✅ Wajaran baharu berjaya diguna pakai pada Analisis Sekarang!');
    }
  },

  applyAdminPreset(wK, wBM, tK, tBM, tO) {
    this.setSelectValueSafely('admin-waj-kawad', wK, 0.60);
    this.setSelectValueSafely('admin-waj-bm-ikatan', wBM, 0.40);
    this.setSelectValueSafely('sim-kawad', tK, 0.70);
    this.setSelectValueSafely('sim-ikatan', tBM, 0.50);
    this.setSelectValueSafely('sim-overall', tO, 0.70);
    this.runAdminSimulation();
  },

  switchTab(tabId) {
    this.state.activeTab = tabId;
    document.querySelectorAll('.tab-button').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-tab') === tabId);
    });
    document.querySelectorAll('.tab-pane').forEach(pane => {
      pane.classList.toggle('active', pane.id === tabId);
    });
  },

  filterBySchool(schoolName) {
    const unescaped = unescape(schoolName);
    this.switchTab('tab-directory');
    const searchInput = document.getElementById('dir-search-input');
    if (searchInput) {
      searchInput.value = unescaped;
      this.renderCandidateDirectory();
    }
  },

  toggleTheme() {
    document.body.classList.toggle('dark-theme');
    const btn = document.getElementById('btn-theme-toggle');
    if (btn) {
      btn.innerText = document.body.classList.contains('dark-theme') ? '☀️ Mod Terang' : '🌙 Mod Gelap';
    }
  },

  /**
   * Pemasangan Event Listeners Programatik
   */
  setupEventListeners() {
    // 1. Tab Buttons Navigation
    document.querySelectorAll('.tab-button').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const tabId = e.currentTarget.getAttribute('data-tab');
        if (tabId) this.switchTab(tabId);
      });
    });

    // 2. Header Action Buttons
    const btnSync = document.getElementById('btn-manual-sync');
    if (btnSync) btnSync.addEventListener('click', () => this.syncLiveGoogleSheet());

    const btnTheme = document.getElementById('btn-theme-toggle');
    if (btnTheme) btnTheme.addEventListener('click', () => this.toggleTheme());

    const btnPrint = document.getElementById('btn-print-report');
    if (btnPrint) btnPrint.addEventListener('click', () => window.print());

    const btnAdminGate = document.getElementById('btn-admin-gate');
    if (btnAdminGate) btnAdminGate.addEventListener('click', () => this.openAdminPinModal());

    const btnToAwards = document.getElementById('btn-to-awards');
    if (btnToAwards) btnToAwards.addEventListener('click', () => this.switchTab('tab-awards'));

    // 3. Search & Filters
    const schoolSearch = document.getElementById('school-search-input');
    if (schoolSearch) schoolSearch.addEventListener('keyup', () => this.filterSchoolTable());

    const dirSearch = document.getElementById('dir-search-input');
    if (dirSearch) dirSearch.addEventListener('keyup', () => this.renderCandidateDirectory());

    const dirUnit = document.getElementById('dir-unit-filter');
    if (dirUnit) dirUnit.addEventListener('change', () => this.renderCandidateDirectory());

    const dirGender = document.getElementById('dir-gender-filter');
    if (dirGender) dirGender.addEventListener('change', () => this.renderCandidateDirectory());

    const dirStatus = document.getElementById('dir-status-filter');
    if (dirStatus) dirStatus.addEventListener('change', () => this.renderCandidateDirectory());

    // 4. Modal PIN Listeners
    const btnSubmitPin = document.getElementById('btn-submit-pin');
    if (btnSubmitPin) btnSubmitPin.addEventListener('click', () => this.submitPin());

    const btnCancelPin = document.getElementById('btn-cancel-pin');
    if (btnCancelPin) btnCancelPin.addEventListener('click', () => this.closeAdminPinModal());

    const btnClosePinX = document.getElementById('btn-close-pin-modal');
    if (btnClosePinX) btnClosePinX.addEventListener('click', () => this.closeAdminPinModal());

    const pinField = document.getElementById('admin-pin-field');
    if (pinField) {
      pinField.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') this.submitPin();
      });
    }

    // 5. Modal Slip Listeners
    const btnPrintSlip = document.getElementById('btn-print-slip');
    if (btnPrintSlip) btnPrintSlip.addEventListener('click', () => this.printSlip());

    const btnCloseSlip = document.getElementById('btn-close-slip');
    if (btnCloseSlip) btnCloseSlip.addEventListener('click', () => this.closeCandidateSlip());

    const btnCloseSlipX = document.getElementById('btn-close-slip-modal');
    if (btnCloseSlipX) btnCloseSlipX.addEventListener('click', () => this.closeCandidateSlip());

    // 6. Admin Presets
    const presetStandard = document.getElementById('preset-standard');
    if (presetStandard) presetStandard.addEventListener('click', () => this.applyAdminPreset(0.60, 0.40, 0.70, 0.50, 0.70));

    const presetSederhana = document.getElementById('preset-sederhana');
    if (presetSederhana) presetSederhana.addEventListener('click', () => this.applyAdminPreset(0.60, 0.40, 0.65, 0.50, 0.65));

    const presetFleksibel = document.getElementById('preset-fleksibel');
    if (presetFleksibel) presetFleksibel.addEventListener('click', () => this.applyAdminPreset(0.50, 0.50, 0.60, 0.40, 0.60));

    const presetMinimum = document.getElementById('preset-minimum');
    if (presetMinimum) presetMinimum.addEventListener('click', () => this.applyAdminPreset(0.50, 0.50, 0.50, 0.30, 0.50));

    const selWajKawad = document.getElementById('admin-waj-kawad');
    if (selWajKawad) selWajKawad.addEventListener('change', () => this.runAdminSimulation());

    const selWajBMIkatan = document.getElementById('admin-waj-bm-ikatan');
    if (selWajBMIkatan) selWajBMIkatan.addEventListener('change', () => this.runAdminSimulation());

    const selSimKawad = document.getElementById('sim-kawad');
    if (selSimKawad) selSimKawad.addEventListener('change', () => this.runAdminSimulation());

    const selSimIkatan = document.getElementById('sim-ikatan');
    if (selSimIkatan) selSimIkatan.addEventListener('change', () => this.runAdminSimulation());

    const selSimOverall = document.getElementById('sim-overall');
    if (selSimOverall) selSimOverall.addEventListener('change', () => this.runAdminSimulation());

    const btnApplyAdmin = document.getElementById('btn-apply-admin-thresholds');
    if (btnApplyAdmin) btnApplyAdmin.addEventListener('click', () => this.applyAdminThresholds());
  }
};

// Pastikan App boleh diakses di window global
window.App = App;

// Bootstrap serta-merta tanpa bergantung semata-mata pada satu event
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => { App.init(); });
} else {
  App.init();
}

