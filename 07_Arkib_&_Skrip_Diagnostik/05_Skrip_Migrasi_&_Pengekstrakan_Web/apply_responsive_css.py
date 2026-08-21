import re

# Comprehensive Mobile-Responsive CSS additions
RESPONSIVE_CSS = """
    /* ==========================================================================
       RESPONSIVE & ANTI-OVERFLOW STYLES (IPHONE / ANDROID PORTRAIT & LANDSCAPE)
       ========================================================================== */
    
    *, *::before, *::after {
      box-sizing: border-box;
    }

    html, body {
      width: 100%;
      max-width: 100vw;
      overflow-x: hidden;
      -webkit-overflow-scrolling: touch;
      margin: 0;
      padding: 0;
    }

    .app-container, .main-content, .top-header, .header-inner, .tab-section, .app-card, .table-container, .table-responsive {
      width: 100%;
      max-width: 100%;
      box-sizing: border-box;
      min-width: 0;
    }

    /* Horizontal scroll container for Navigation Bar */
    .nav-wrapper {
      width: 100%;
      max-width: 100%;
      box-sizing: border-box;
      overflow: hidden;
    }

    .nav-inner {
      width: 100%;
      max-width: 1400px;
      margin: 0 auto;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
      -ms-overflow-style: none;
      padding: 4px 10px;
      box-sizing: border-box;
    }
    .nav-inner::-webkit-scrollbar {
      display: none;
    }

    .tab-nav-group {
      display: flex;
      flex-direction: row;
      align-items: center;
      gap: 6px;
      width: max-content;
      min-width: 100%;
      box-sizing: border-box;
    }

    .tab-btn {
      white-space: nowrap;
      flex-shrink: 0;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      touch-action: manipulation;
    }

    /* Anti-overflow for CSS Grids */
    .sym-grid-4, .sym-grid-3, .sym-grid-2, .admin-btn-grid, .kpi-quick-bar, .objective-grid, .matlamat-pillars, .schedule-grid {
      display: grid;
      width: 100%;
      max-width: 100%;
      box-sizing: border-box;
    }

    .sym-grid-4 > *, .sym-grid-3 > *, .sym-grid-2 > *, .admin-btn-grid > *, .kpi-quick-bar > *, .objective-grid > *, .matlamat-pillars > *, .schedule-grid > * {
      min-width: 0;
      max-width: 100%;
      box-sizing: border-box;
    }

    /* Table Scroll Wrapping */
    .table-container, .table-responsive {
      width: 100%;
      max-width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      display: block;
      border-radius: 8px;
    }

    .table-container table, .table-responsive table {
      width: 100%;
      border-collapse: collapse;
    }

    /* Modals Anti-Blowout */
    .modal-backdrop, #modal-slip-backdrop, #modal-admin-backdrop, #modal-candidate-manage {
      box-sizing: border-box;
      padding: 10px;
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
    }

    .modal-box, .modal-box-lg {
      max-width: 100% !important;
      box-sizing: border-box !important;
      overflow-x: hidden !important;
    }

    /* --------------------------------------------------------------------------
       MEDIA QUERIES: TABLET & MOBILE LANDSCAPE (max-width: 992px)
       -------------------------------------------------------------------------- */
    @media (max-width: 992px) {
      .sym-grid-4 {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 12px;
      }
      .sym-grid-2 {
        grid-template-columns: 1fr !important;
        gap: 14px;
      }
      .chart-box {
        height: 280px;
        position: relative;
        width: 100%;
        max-width: 100%;
        min-width: 0;
      }
    }

    /* --------------------------------------------------------------------------
       MEDIA QUERIES: MOBILE PORTRAIT & LANDSCAPE (max-width: 768px)
       -------------------------------------------------------------------------- */
    @media (max-width: 768px) {
      .top-header {
        padding: 10px 12px !important;
      }
      .header-inner {
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
      }
      .header-brand {
        width: 100%;
        gap: 8px;
      }
      .header-logo-img {
        height: 40px !important;
        width: auto !important;
      }
      .logo-divider {
        height: 32px !important;
      }
      .header-text h1 {
        font-size: 15px !important;
        line-height: 1.25 !important;
      }
      .header-text p {
        font-size: 11px !important;
      }
      .header-pills {
        width: 100%;
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
      }
      .header-badge {
        font-size: 11px !important;
        padding: 4px 8px !important;
      }

      .main-content {
        padding: 12px 10px !important;
      }
      .tab-section {
        gap: 14px !important;
      }

      .app-card {
        padding: 14px 12px !important;
        border-radius: 10px !important;
      }
      .card-head {
        flex-direction: column;
        align-items: flex-start;
        gap: 8px;
      }
      .card-heading h2 {
        font-size: 15px !important;
      }

      /* Tab Analisis: KPI Tiles */
      .sym-grid-4 {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 8px !important;
      }
      .metric-tile {
        padding: 10px 8px !important;
        gap: 8px !important;
        border-radius: 8px !important;
      }
      .metric-icon {
        width: 36px !important;
        height: 36px !important;
        font-size: 16px !important;
        border-radius: 8px !important;
      }
      .metric-data h3 {
        font-size: 17px !important;
        line-height: 1.15 !important;
      }
      .metric-data p {
        font-size: 10.5px !important;
      }

      /* Tab Analisis: Chart Boxes */
      .sym-grid-2 {
        grid-template-columns: 1fr !important;
        gap: 12px !important;
      }
      .chart-box {
        height: 240px !important;
        position: relative !important;
        width: 100% !important;
        max-width: 100% !important;
        min-width: 0 !important;
        overflow: hidden !important;
      }
      .chart-box canvas {
        width: 100% !important;
        max-width: 100% !important;
        height: 100% !important;
      }

      /* Tab Senarai Calon: Filter Toolbar */
      .filter-toolbar {
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 8px !important;
        width: 100% !important;
      }
      .search-box, .select-box, #input-candidate-search, #select-unit, #select-kumpulan, #select-jantina, #select-status {
        width: 100% !important;
        max-width: 100% !important;
      }

      /* Tab Senarai Calon: KPI Quick Bar */
      .kpi-quick-bar {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 6px !important;
      }
      .kpi-quick-card {
        padding: 8px 10px !important;
      }
      .kpi-quick-card .count {
        font-size: 16px !important;
      }
      .kpi-quick-card .label {
        font-size: 10px !important;
      }

      /* Tab 5 Terbaik */
      .top-cards-grid {
        grid-template-columns: 1fr !important;
        gap: 14px !important;
      }
      .top-filter-btn {
        padding: 6px 10px !important;
        font-size: 11.5px !important;
      }

      /* Program Tab */
      .matlamat-pillars, .objective-grid, .schedule-grid {
        grid-template-columns: 1fr !important;
        gap: 10px !important;
      }

      /* Admin Tab */
      .admin-login-card {
        width: 100% !important;
        max-width: 100% !important;
        padding: 16px 12px !important;
      }
      .admin-btn-grid {
        grid-template-columns: 1fr !important;
        gap: 10px !important;
      }

      /* Slip Modal Mobile */
      .modal-box-lg {
        padding: 14px 10px !important;
        max-height: 94vh !important;
      }
      .slip-official-header {
        flex-direction: column !important;
        text-align: center !important;
        gap: 8px !important;
      }
      .slip-logos-crest {
        justify-content: center !important;
      }
      .slip-meta-grid {
        grid-template-columns: 1fr !important;
        gap: 6px !important;
      }
    }

    /* --------------------------------------------------------------------------
       EXTRA COMPACT MOBILE (max-width: 420px - iPhone SE / Standard Android)
       -------------------------------------------------------------------------- */
    @media (max-width: 420px) {
      .header-text h1 {
        font-size: 13.5px !important;
      }
      .header-badge {
        font-size: 10px !important;
        padding: 3px 6px !important;
      }
      .tab-btn {
        padding: 6px 10px !important;
        font-size: 11.5px !important;
      }
      .metric-data h3 {
        font-size: 15px !important;
      }
      .metric-data p {
        font-size: 9.5px !important;
      }
      .chart-box {
        height: 220px !important;
      }
    }
"""

def update_html_with_responsive_css(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    style_end = content.find('</style>')
    if style_end == -1:
        print(f"No </style> found in {file_path}")
        return False

    if 'RESPONSIVE & ANTI-OVERFLOW STYLES' in content:
        pattern = r'/\* ==========================================================================\s*RESPONSIVE & ANTI-OVERFLOW STYLES.*?</style>'
        new_content = re.sub(pattern, RESPONSIVE_CSS.strip() + '\n\n  </style>', content, flags=re.DOTALL)
    else:
        new_content = content[:style_end] + '\n' + RESPONSIVE_CSS + '\n  ' + content[style_end:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully updated responsive CSS in {file_path}")
    return True

update_html_with_responsive_css(r'03_Google_Apps_Script\Index.html')
update_html_with_responsive_css(r'index.html')
update_html_with_responsive_css(r'04_Web_App_Netlify\index.html')
