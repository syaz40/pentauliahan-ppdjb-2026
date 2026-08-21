/**
 * =========================================================================
 * ENJIN VISUALISASI CARTA & GRAF MIKRO (CHARTS & VISUALIZATION ENGINE)
 * Dibina berasaskan SVG & CSS Responsive Canvas (100% Offline Compatible)
 * =========================================================================
 */

const ChartsEngine = {
  /**
   * Menjana Bar Graf Mendatar untuk Ketepatan Elemen Kawad Kaki
   */
  renderElementBarChart(containerId, elementsList) {
    const container = document.getElementById(containerId);
    if (!container || !elementsList) return;

    let html = '<div class="chart-bars-list">';
    elementsList.forEach((item, idx) => {
      const pct = item.accuracy;
      let colorClass = 'bar-pass';
      if (pct >= 80) colorClass = 'bar-excellent';
      else if (pct >= 70) colorClass = 'bar-good';
      else if (pct >= 60) colorClass = 'bar-warn';
      else colorClass = 'bar-danger';

      html += `
        <div class="bar-row">
          <div class="bar-header">
            <span class="bar-title"><strong>${idx + 1}.</strong> ${item.name}</span>
            <span class="bar-value ${colorClass}-text">${pct}%</span>
          </div>
          <div class="bar-track">
            <div class="bar-fill ${colorClass}" style="width: ${pct}%;"></div>
          </div>
        </div>
      `;
    });
    html += '</div>';
    container.innerHTML = html;
  },

  /**
   * Menjana Carta Radial / Donut Gauge untuk Kadar Kelulusan
   */
  renderRadialGauge(containerId, percentage, label = 'KADAR KELULUSAN') {
    const container = document.getElementById(containerId);
    if (!container) return;

    const strokeDash = (percentage / 100) * 283;
    const color = percentage >= 70 ? '#10b981' : (percentage >= 50 ? '#f59e0b' : '#ef4444');

    container.innerHTML = `
      <div class="radial-gauge-wrap">
        <svg viewBox="0 0 100 100" class="radial-svg">
          <circle cx="50" cy="50" r="45" class="radial-bg-circle" />
          <circle cx="50" cy="50" r="45" class="radial-fill-circle"
            style="stroke-dasharray: ${strokeDash} 283; stroke: ${color};" />
        </svg>
        <div class="radial-text-wrap">
          <div class="radial-pct" style="color: ${color};">${percentage}%</div>
          <div class="radial-lbl">${label}</div>
        </div>
      </div>
    `;
  },

  /**
   * Menjana Perbandingan Bar Graf Berkembar (Lelaki vs Perempuan)
   */
  renderGenderComparison(containerId, stats) {
    const container = document.getElementById(containerId);
    if (!container || !stats || !stats.boys || !stats.girls) return;

    const metrics = [
      { label: 'Kawad Kaki (60%)', boy: stats.boys.avgKawad, girl: stats.girls.avgKawad },
      { label: 'Bantu Mula (20%)', boy: stats.boys.avgBantuMula, girl: stats.girls.avgBantuMula },
      { label: 'Tali Temali (20%)', boy: stats.boys.avgIkatan, girl: stats.girls.avgIkatan },
      { label: 'Keseluruhan (%)', boy: stats.boys.avgOverall, girl: stats.girls.avgOverall }
    ];

    let html = '<div class="comparison-bars-wrap">';
    metrics.forEach(m => {
      html += `
        <div class="comp-metric-row">
          <div class="comp-label">${m.label}</div>
          <div class="comp-dual-bars">
            <div class="comp-single-bar">
              <span class="comp-gender-tag boy-tag">👦 L: ${m.boy}%</span>
              <div class="comp-track"><div class="comp-fill boy-fill" style="width: ${m.boy}%;"></div></div>
            </div>
            <div class="comp-single-bar">
              <span class="comp-gender-tag girl-tag">👧 P: ${m.girl}%</span>
              <div class="comp-track"><div class="comp-fill girl-fill" style="width: ${m.girl}%;"></div></div>
            </div>
          </div>
        </div>
      `;
    });
    html += '</div>';
    container.innerHTML = html;
  }
};

window.ChartsEngine = ChartsEngine;

