import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Refining Chart Performance Calculations & Live Sheet Sync...")

# =========================================================================
# 1. UPDATE updateCharts() IN index.html
# =========================================================================
with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_update_charts_js = """      updateCharts() {
        if (!this.state.charts || !this.state.charts.categoryGender) return;

        let tkrsL = 0, tkrsP = 0, krsL = 0, krsP = 0;
        let sumK_TKRS = 0, countK_TKRS = 0;
        let sumBM_TKRS = 0, countBM_TKRS = 0;
        let sumIK_TKRS = 0, countIK_TKRS = 0;
        let sumTot_TKRS = 0, countTot_TKRS = 0;

        let sumK_KRS = 0, countK_KRS = 0;
        let sumBM_KRS = 0, countBM_KRS = 0;
        let sumIK_KRS = 0, countIK_KRS = 0;
        let sumTot_KRS = 0, countTot_KRS = 0;

        let passLLL = 0, passCond = 0, failCount = 0, pendingCount = 0, absentOrWithdraw = 0;
        const schoolMap = {};

        this.state.candidates.forEach(c => {
          const isTKRS = c.unit === 'TKRS';
          const isL = c.jantina === 'L';

          if (isTKRS) {
            if (isL) tkrsL++; else tkrsP++;
          } else {
            if (isL) krsL++; else krsP++;
          }

          if (c.sekolah) {
            schoolMap[c.sekolah] = (schoolMap[c.sekolah] || 0) + 1;
          }

          if (c.isAbsent || c.isTarikDiri || c.statusText === 'TH' || c.statusText === 'TARIK DIRI') {
            absentOrWithdraw++;
            return;
          }

          const rawK = parseFloat(c.rawKawad) || 0;
          const rawBM = parseFloat(c.rawBantuMula) || 0;
          const rawIK = parseFloat(c.rawIkatan) || 0;
          const rawTot = parseFloat(c.rawOverall) || 0;

          if (isTKRS) {
            if (rawK > 0) { sumK_TKRS += rawK; countK_TKRS++; }
            if (rawBM > 0) { sumBM_TKRS += rawBM; countBM_TKRS++; }
            if (rawIK > 0) { sumIK_TKRS += rawIK; countIK_TKRS++; }
            if (rawTot > 0) { sumTot_TKRS += rawTot; countTot_TKRS++; }
          } else {
            if (rawK > 0) { sumK_KRS += rawK; countK_KRS++; }
            if (rawBM > 0) { sumBM_KRS += rawBM; countBM_KRS++; }
            if (rawIK > 0) { sumIK_KRS += rawIK; countIK_KRS++; }
            if (rawTot > 0) { sumTot_KRS += rawTot; countTot_KRS++; }
          }

          if (c.statusText === 'LLL') {
            passLLL++;
          } else if (rawTot >= 0.50) {
            passCond++;
          } else if (rawTot > 0) {
            failCount++;
          } else {
            pendingCount++;
          }
        });

        // 1. Chart Demografi Kategori & Jantina
        if (this.state.charts.categoryGender) {
          this.state.charts.categoryGender.data.datasets[0].data = [tkrsL, tkrsP, krsL, krsP];
          this.state.charts.categoryGender.update();
        }

        // 2. Chart Purata Skor Pencapaian Modul (Dikira mengikut calon yang telah diuji bagi setiap modul)
        if (this.state.charts.modulePerf) {
          const avgTKRS = [
            countK_TKRS > 0 ? ((sumK_TKRS / countK_TKRS) * 100).toFixed(1) : 0,
            countBM_TKRS > 0 ? ((sumBM_TKRS / countBM_TKRS) * 100).toFixed(1) : 0,
            countIK_TKRS > 0 ? ((sumIK_TKRS / countIK_TKRS) * 100).toFixed(1) : 0,
            countTot_TKRS > 0 ? ((sumTot_TKRS / countTot_TKRS) * 100).toFixed(1) : 0
          ];
          const avgKRS = [
            countK_KRS > 0 ? ((sumK_KRS / countK_KRS) * 100).toFixed(1) : 0,
            countBM_KRS > 0 ? ((sumBM_KRS / countBM_KRS) * 100).toFixed(1) : 0,
            countIK_KRS > 0 ? ((sumIK_KRS / countIK_KRS) * 100).toFixed(1) : 0,
            countTot_KRS > 0 ? ((sumTot_KRS / countTot_KRS) * 100).toFixed(1) : 0
          ];

          this.state.charts.modulePerf.data.datasets[0].data = avgTKRS;
          this.state.charts.modulePerf.data.datasets[1].data = avgKRS;
          this.state.charts.modulePerf.update();
        }

        // 3. Chart 10 Sekolah Penyertaan Tertinggi
        if (this.state.charts.topSchools) {
          const sortedSchools = Object.keys(schoolMap)
            .map(k => ({ name: k, count: schoolMap[k] }))
            .sort((a, b) => b.count - a.count)
            .slice(0, 10);

          this.state.charts.topSchools.data.labels = sortedSchools.map(s => s.name);
          this.state.charts.topSchools.data.datasets[0].data = sortedSchools.map(s => s.count);
          this.state.charts.topSchools.update();
        }

        // 4. Chart Unjuran Status Kelayakan
        if (this.state.charts.passStatus) {
          this.state.charts.passStatus.data.datasets[0].data = [
            passLLL,
            passCond,
            failCount,
            pendingCount,
            absentOrWithdraw
          ];
          this.state.charts.passStatus.update();
        }
      },"""

# Replace updateCharts in html
pattern = r'updateCharts\(\)\s*\{[\s\S]*?renderTopResults\(\)\s*\{'
html = re.sub(pattern, new_update_charts_js.strip() + '\n\n      renderTopResults() {', html)

# Save Netlify file
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
