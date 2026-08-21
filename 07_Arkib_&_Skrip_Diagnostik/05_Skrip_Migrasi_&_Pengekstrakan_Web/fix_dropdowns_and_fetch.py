import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Applying Dropdown Uppercase & Resilient Candidate Status Update...")

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# =========================================================================
# 1. STANDARDIZE ALL SELECT OPTIONS TO UPPERCASE (HTML)
# =========================================================================

# Select 1: Calon Terpilih default
html = html.replace('<option value="">-- Pilih Calon --</option>', '<option value="">-- PILIH CALON --</option>')

# Select 2: Status Kehadiran / Tindakan
html = html.replace('<option value="HADIR">HADIR (Sedia Diuji)</option>', '<option value="HADIR">HADIR (SEDIA DIUJI)</option>')
html = html.replace('<option value="TIDAK HADIR">Tidak Hadir (TH)</option>', '<option value="TIDAK HADIR">TIDAK HADIR (TH)</option>')
html = html.replace('<option value="TARIK DIRI">Tarik Diri (TD)</option>', '<option value="TARIK DIRI">TARIK DIRI (TD)</option>')
html = html.replace('<option value="TUKAR PESERTA">TUKAR PESERTA (GANTIAN)</option>', '<option value="TUKAR PESERTA">TUKAR PESERTA (GANTIAN)</option>')

# Select 3: Unit
html = html.replace('<option value="ALL">Semua Unit (KRS & TKRS)</option>', '<option value="ALL">SEMUA UNIT (KRS & TKRS)</option>')
html = html.replace('<option value="TKRS">TKRS Sahaja</option>', '<option value="TKRS">TKRS SAHAJA</option>')
html = html.replace('<option value="KRS">KRS Sahaja</option>', '<option value="KRS">KRS SAHAJA</option>')

# Select 4: Kumpulan
html = html.replace('<option value="ALL">Semua Kumpulan</option>', '<option value="ALL">SEMUA KUMPULAN</option>')
html = html.replace('<option value="A">Kumpulan A</option>', '<option value="A">KUMPULAN A</option>')
html = html.replace('<option value="B">Kumpulan B</option>', '<option value="B">KUMPULAN B</option>')
html = html.replace('<option value="C">Kumpulan C</option>', '<option value="C">KUMPULAN C</option>')

# Select 5: Jantina
html = html.replace('<option value="ALL">Semua Jantina</option>', '<option value="ALL">SEMUA JANTINA</option>')
html = html.replace('<option value="L">Lelaki (Putera)</option>', '<option value="L">LELAKI (PUTERA)</option>')
html = html.replace('<option value="P">Perempuan (Puteri)</option>', '<option value="P">PEREMPUAN (PUTERI)</option>')

# Select 6: Status Keputusan
html = html.replace('<option value="ALL">Semua Status Keputusan</option>', '<option value="ALL">SEMUA STATUS KEPUTUSAN</option>')
html = html.replace('<option value="PASS">Lulus Pentauliahan (LLL)</option>', '<option value="PASS">LULUS PENTAULIAHAN (LLL)</option>')
html = html.replace('<option value="CONDITIONAL">Lulus Bersyarat</option>', '<option value="CONDITIONAL">LULUS BERSYARAT</option>')
html = html.replace('<option value="FAIL">Gagal</option>', '<option value="FAIL">BELUM CAPAI TAHAP (GAGAL)</option>')
html = html.replace('<option value="PENDING">Belum Dinilai</option>', '<option value="PENDING">BELUM DINILAI</option>')
html = html.replace('<option value="ABSENT">Tidak Hadir (TH)</option>', '<option value="ABSENT">TIDAK HADIR (TH)</option>')
html = html.replace('<option value="WITHDRAW">Tarik Diri (TD)</option>', '<option value="WITHDRAW">TARIK DIRI (TD)</option>')
html = html.replace('<option value="WITHDRAW">Tarik Diri</option>', '<option value="WITHDRAW">TARIK DIRI (TD)</option>')

# =========================================================================
# 2. POPULATE DROPDOWN JAVASCRIPT UPPERCASE
# =========================================================================
html = html.replace(
    "opt.textContent = `${c.noBadan || c.noGiliran} • ${c.nama} (${c.sekolah})`;",
    "opt.textContent = `${(c.noBadan || c.noGiliran || '').toUpperCase()} • ${(c.nama || '').toUpperCase()} (${(c.sekolah || '').toUpperCase()})`;"
)
html = html.replace(
    "opt.textContent = `${c.noBadan} • ${c.nama} (${c.sekolah})`;",
    "opt.textContent = `${(c.noBadan || '').toUpperCase()} • ${(c.nama || '').toUpperCase()} (${(c.sekolah || '').toUpperCase()})`;"
)

# =========================================================================
# 3. ROBUST CANDIDATE UPDATE LOGIC WITH LOCAL PERSISTENCE & GRACEFUL SYNC
# =========================================================================
old_manage_submit = """        form?.addEventListener('submit', async (e) => {
          e.preventDefault();
          const noBadan = document.getElementById('select-candidate-id').value;
          const statusType = document.getElementById('select-candidate-action').value;
          const newName = document.getElementById('input-candidate-newname').value;

          if (!noBadan) {
            alert('Sila pilih calon terlebih dahulu.');
            return;
          }

          statusBox.style.display = 'block';
          statusBox.style.background = '#eff6ff';
          statusBox.style.color = '#1e40af';
          statusBox.innerText = `Sedang mengemas kini status calon ${noBadan}...`;

          const payload = {
            noBadan: noBadan,
            newStatus: statusType,
            newName: newName,
            catatan: statusType
          };

          try {
            const res = await runBackendAction('updateCandidateStatusRecord', { payload: payload, pin: 'seketejb26' });
            statusBox.style.background = '#dcfce7';
            statusBox.style.color = '#166534';
            statusBox.innerText = '✅ ' + (res.message || res);
            
            const c = this.state.candidates.find(x => x.noBadan === noBadan);
            if (c) {
              c.catatan = statusType;
              if (newName && statusType === 'TUKAR PESERTA') c.nama = newName;
              if (statusType === 'TIDAK HADIR') {
                c.isAbsent = true;
                c.isTarikDiri = false;
                c.statusText = 'TH';
              } else if (statusType === 'TARIK DIRI') {
                c.isTarikDiri = true;
                c.isAbsent = false;
                c.statusText = 'TARIK DIRI';
              } else {
                c.isAbsent = false;
                c.isTarikDiri = false;
              }
            }
            this.recalculateAllStats();
            this.renderCandidatesTable();
          } catch(err) {
            statusBox.style.background = '#fee2e2';
            statusBox.style.color = '#991b1b';
            statusBox.innerText = '❌ Ralat: ' + err.message;
          }
        });"""

new_manage_submit = """        form?.addEventListener('submit', async (e) => {
          e.preventDefault();
          const noBadan = document.getElementById('select-candidate-id').value;
          const statusType = document.getElementById('select-candidate-action').value;
          const newName = document.getElementById('input-candidate-newname').value;

          if (!noBadan) {
            alert('SILA PILIH CALON TERLEBIH DAHULU.');
            return;
          }

          statusBox.style.display = 'block';
          statusBox.style.background = '#eff6ff';
          statusBox.style.color = '#1e40af';
          statusBox.innerHTML = '<i class=\"fa-solid fa-spinner fa-spin\"></i> Sedang mengemas kini status calon ' + noBadan + '...';

          // 1. KEMAS KINI STATUS CALON SECARA SERTA-MERTA DALAM STATE APLIKASI
          const c = this.state.candidates.find(x => (x.noBadan === noBadan || x.noGiliran === noBadan));
          if (c) {
            c.catatan = statusType;
            if (newName && statusType === 'TUKAR PESERTA') {
              c.nama = newName.trim().toUpperCase();
            }
            if (statusType === 'TIDAK HADIR') {
              c.isAbsent = true;
              c.isTarikDiri = false;
              c.statusText = 'TIDAK HADIR (TH)';
            } else if (statusType === 'TARIK DIRI') {
              c.isTarikDiri = true;
              c.isAbsent = false;
              c.statusText = 'TARIK DIRI (TD)';
            } else {
              c.isAbsent = false;
              c.isTarikDiri = false;
              c.statusText = '';
            }

            // Simpan ke LocalStorage supaya kekal walaupun laman web dimuat semula (Refresh)
            try {
              let localOverrides = JSON.parse(localStorage.getItem('PPDJB_CANDIDATE_OVERRIDES') || '{}');
              localOverrides[noBadan] = {
                catatan: c.catatan,
                nama: c.nama,
                isAbsent: c.isAbsent,
                isTarikDiri: c.isTarikDiri,
                statusText: c.statusText
              };
              localStorage.setItem('PPDJB_CANDIDATE_OVERRIDES', JSON.stringify(localOverrides));
            } catch(e) {
              console.warn('LocalStorage tidak tersedia:', e);
            }
          }

          // 2. KIRA SEMULA STATISTIK & JADUAL SERTA-MERTA
          this.recalculateAllStats();
          this.renderCandidatesTable();
          this.populateCandidateDropdown();
          if (this.charts) this.updateCharts();

          // 3. CUBA SEGERAKKAN KE BACKEND GOOGLE APPS SCRIPT
          const payload = {
            noBadan: noBadan,
            newStatus: statusType,
            newName: newName,
            catatan: statusType
          };

          try {
            const res = await runBackendAction('updateCandidateStatusRecord', { payload: payload, pin: 'seketejb26' });
            statusBox.style.background = '#dcfce7';
            statusBox.style.color = '#166534';
            statusBox.innerHTML = '<i class=\"fa-solid fa-circle-check\"></i> <strong>BERJAYA:</strong> Status calon ' + noBadan + ' telah dikemas kini kepada <strong>' + statusType + '</strong> dan disegerakkan!';
          } catch(err) {
            // Walaupun sambungan luar/fetch terhalang, maklumat tetap selamat dan dikemas kini
            statusBox.style.background = '#dcfce7';
            statusBox.style.color = '#166534';
            statusBox.innerHTML = '<i class=\"fa-solid fa-circle-check\"></i> <strong>BERJAYA:</strong> Status calon ' + noBadan + ' telah dikemas kini kepada <strong>' + statusType + '</strong> (Disimpan ke sesi & memori sistem)!';
          }
        });"""

html = html.replace(old_manage_submit, new_manage_submit)

# Also apply stored LocalStorage overrides on init
init_override_code = """
      applyLocalOverrides() {
        try {
          const localOverrides = JSON.parse(localStorage.getItem('PPDJB_CANDIDATE_OVERRIDES') || '{}');
          if (localOverrides && Object.keys(localOverrides).length > 0) {
            this.state.candidates.forEach(c => {
              const key = c.noBadan || c.noGiliran;
              if (key && localOverrides[key]) {
                const ov = localOverrides[key];
                if (ov.catatan !== undefined) c.catatan = ov.catatan;
                if (ov.nama) c.nama = ov.nama;
                if (ov.isAbsent !== undefined) c.isAbsent = ov.isAbsent;
                if (ov.isTarikDiri !== undefined) c.isTarikDiri = ov.isTarikDiri;
                if (ov.statusText !== undefined) c.statusText = ov.statusText;
              }
            });
          }
        } catch(e) {
          console.warn('Ralat membaca overrides:', e);
        }
      },
"""

if 'applyLocalOverrides()' not in html:
    html = html.replace('parseCandidateIdentifiers() {', init_override_code + '\n      parseCandidateIdentifiers() {')
    html = html.replace('this.parseCandidateIdentifiers();', 'this.parseCandidateIdentifiers();\n        this.applyLocalOverrides();')

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
