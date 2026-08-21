import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Applying Final Cleanups: Removing Status column from Top 5 Tables...")

with open('04_Web_App_Netlify/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the table headers in #tab-top-results
# Replace all occurrences of the 6-col header with 5-col header (without Status)
old_top_thead = """                <tr>
                  <th style="width:70px; text-align:center;">Ked.</th>
                  <th style="width:130px; text-align:center;">No Badan</th>
                  <th style="text-align:left;">Nama Calon</th>
                  <th style="text-align:left;">Sekolah</th>
                  <th style="width:130px; text-align:center;">Markah (%)</th>
                  <th style="width:140px; text-align:center;">Status</th>
                </tr>"""

new_top_thead = """                <tr>
                  <th style="width:70px; text-align:center;">Ked.</th>
                  <th style="width:130px; text-align:center;">No Badan</th>
                  <th style="text-align:left;">Nama Calon</th>
                  <th style="text-align:left;">Sekolah</th>
                  <th style="width:140px; text-align:center;">Markah Keseluruhan (%)</th>
                </tr>"""

html = html.replace(old_top_thead, new_top_thead)

# 2. Update renderTopResults in JavaScript to render 5 columns (without Status)
old_render_group_pattern = r'renderTopResults\(\)\s*\{[\s\S]*?renderCandidatesTable\(\)\s*\{'

new_render_top_js = """renderTopResults() {
        const renderGroup = (elementId, candidatesList) => {
          const tbody = document.getElementById(elementId);
          if (!tbody) return;
          if (!candidatesList || candidatesList.length === 0) {
            tbody.innerHTML = '<tr><td colspan="5" style="text-align:center; padding:24px; color:#94a3b8; font-weight:600;">Tiada rekod calon berdaftar.</td></tr>';
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
                <td style="text-align:center; vertical-align:middle;">${badge}</td>
                <td style="text-align:center; font-weight:800; color:var(--royal-blue); vertical-align:middle;">${c.noBadan || c.noGiliran}</td>
                <td style="text-align:left; font-weight:800; color:var(--slate-900); vertical-align:middle;">${(c.nama || '').toUpperCase()}</td>
                <td style="text-align:left; font-size:13px; color:var(--slate-700); font-weight:600; vertical-align:middle;">${(c.sekolah || '').toUpperCase()}</td>
                <td style="text-align:center; font-weight:800; color:#1e3a8a; font-size:16px; vertical-align:middle;">${c.overall}%</td>
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

      renderCandidatesTable() {"""

html = re.sub(old_render_group_pattern, new_render_top_js, html)

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
