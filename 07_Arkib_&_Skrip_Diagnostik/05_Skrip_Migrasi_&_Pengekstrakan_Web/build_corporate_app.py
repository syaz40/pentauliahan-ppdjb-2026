import os
import re
import json
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Generating corporate-grade Web App for Google Apps Script & Netlify...")

with open('03_Google_Apps_Script/Index.html', 'r', encoding='utf-8') as f:
    orig_html = f.read()

m_cand = re.search(r'const EMBEDDED_CANDIDATES\s*=\s*(\[.*?\]);', orig_html, re.DOTALL)
if not m_cand:
    raise ValueError("EMBEDDED_CANDIDATES not found!")
embedded_candidates_json = m_cand.group(1)

logos = re.findall(r'src=[\x22\x27](data:image/png;base64,[^\x22\x27]+)[\x22\x27]', orig_html)
logo_ppd = logos[0] if len(logos) > 0 else ''
logo_krs = logos[1] if len(logos) > 1 else ''

def build_html(is_gas=True):
    payload_scriptlet = '<?!= typeof initialData !== \'undefined\' && initialData ? JSON.stringify(initialData) : \'null\' ?>' if is_gas else 'null'

    html = f"""<!DOCTYPE html>
<html lang="ms">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Lembaga Pentauliahan KRS & TKRS PPD Johor Bahru 2026 — Sistem Pengurusan & Analisis Prestasi</title>
  
  <!-- Modern Typography & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <!-- Chart.js CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>

  <style>
    /* ==========================================================================
       CORPORATE DESIGN SYSTEM & CSS TOKENS
       ========================================================================== */
    :root {{
      --navy-950: #070b14;
      --navy-900: #0b132b;
      --navy-850: #101c3d;
      --navy-800: #1c2541;
      --navy-700: #23315a;
      --blue-600: #2563eb;
      --blue-500: #3b82f6;
      --blue-400: #60a5fa;
      --blue-100: #dbeafe;
      --blue-50: #eff6ff;
      --gold-600: #b45309;
      --gold-500: #d97706;
      --gold-400: #f59e0b;
      --gold-100: #fef3c7;
      --gold-50: #fffbeb;
      --emerald-700: #047857;
      --emerald-600: #059669;
      --emerald-500: #10b981;
      --emerald-100: #d1fae5;
      --emerald-50: #ecfdf5;
      --rose-600: #e11d48;
      --rose-500: #f43f5e;
      --rose-100: #ffe4e6;
      --amber-600: #d97706;
      --amber-100: #fef3c7;
      --slate-900: #0f172a;
      --slate-800: #1e293b;
      --slate-700: #334155;
      --slate-600: #475569;
      --slate-500: #64748b;
      --slate-400: #94a3b8;
      --slate-300: #cbd5e1;
      --slate-200: #e2e8f0;
      --slate-100: #f1f5f9;
      --slate-50: #f8fafc;
      --white: #ffffff;

      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 18px;
      --radius-xl: 24px;
      --radius-full: 9999px;

      --shadow-sm: 0 1px 2px 0 rgba(15, 23, 42, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(15, 23, 42, 0.07), 0 2px 4px -2px rgba(15, 23, 42, 0.05);
      --shadow-lg: 0 10px 15px -3px rgba(15, 23, 42, 0.08), 0 4px 6px -4px rgba(15, 23, 42, 0.04);
      --shadow-xl: 0 20px 25px -5px rgba(15, 23, 42, 0.10), 0 8px 10px -6px rgba(15, 23, 42, 0.05);
      --shadow-card: 0 4px 20px -2px rgba(15, 23, 42, 0.06), 0 0 0 1px rgba(226, 232, 240, 0.8);
      --shadow-card-hover: 0 12px 30px -4px rgba(15, 23, 42, 0.12), 0 0 0 1px rgba(191, 219, 254, 0.8);

      --font-heading: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: var(--font-body);
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      background: #f1f5f9;
      background-image: 
        radial-gradient(at 0% 0%, rgba(37, 99, 235, 0.03) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(217, 119, 6, 0.03) 0px, transparent 50%);
      color: var(--slate-900);
      font-size: 14px;
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    h1, h2, h3, h4, h5, h6 {{
      font-family: var(--font-heading);
      color: var(--slate-900);
      font-weight: 700;
      letter-spacing: -0.02em;
    }}

    /* ==========================================================================
       TOP CORPORATE HEADER & OFFICIAL CREST
       ========================================================================== */
    .top-header {{
      background: linear-gradient(135deg, #070b14 0%, #0b132b 45%, #1c2541 100%);
      color: var(--white);
      padding: 20px 24px;
      border-bottom: 3px solid var(--gold-500);
      box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.4);
      position: relative;
      z-index: 100;
    }}

    .top-header::after {{
      content: "";
      position: absolute;
      bottom: -3px;
      left: 0;
      right: 0;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(251, 191, 36, 0.8), transparent);
    }}

    .header-inner {{
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 18px;
    }}

    .header-brand {{
      display: flex;
      align-items: center;
      gap: 18px;
    }}

    .logo-container {{
      display: flex;
      align-items: center;
      gap: 14px;
      background: rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(12px);
      padding: 8px 16px;
      border-radius: var(--radius-md);
      border: 1px solid rgba(255, 255, 255, 0.15);
      box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.1);
    }}

    .header-logo-img {{
      height: 48px;
      width: auto;
      max-width: 60px;
      object-fit: contain;
      filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
    }}

    .logo-divider {{
      width: 1px;
      height: 36px;
      background: rgba(255, 255, 255, 0.2);
    }}

    .header-text {{
      display: flex;
      flex-direction: column;
    }}

    .gov-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--gold-400);
      margin-bottom: 3px;
    }}

    .header-text h1 {{
      font-size: 20px;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.2;
      letter-spacing: -0.03em;
    }}

    .header-text p {{
      font-size: 13px;
      color: #93c5fd;
      font-weight: 500;
      margin-top: 4px;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .header-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      border-radius: var(--radius-md);
      font-size: 12.5px;
      font-weight: 700;
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #ffffff;
      backdrop-filter: blur(8px);
    }}

    .header-badge.green {{
      background: rgba(5, 150, 105, 0.2);
      border-color: rgba(16, 185, 129, 0.5);
      color: #a7f3d0;
    }}

    .pulse-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
      animation: pulseGreen 2s infinite;
    }}

    @keyframes pulseGreen {{
      0% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }}
      70% {{ transform: scale(1); box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }}
      100% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }}
    }}

    .btn-header-action {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      border-radius: var(--radius-md);
      font-size: 12.5px;
      font-weight: 700;
      background: var(--blue-600);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.2);
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
      text-decoration: none;
    }}

    .btn-header-action:hover {{
      background: #1d4ed8;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
    }}

    .btn-header-action.gold {{
      background: linear-gradient(135deg, var(--gold-500) 0%, var(--gold-600) 100%);
      border-color: rgba(254, 243, 199, 0.3);
    }}

    .btn-header-action.gold:hover {{
      background: linear-gradient(135deg, var(--gold-600) 0%, #92400e 100%);
      box-shadow: 0 4px 12px rgba(217, 119, 6, 0.4);
    }}

    /* ==========================================================================
       STICKY NAVIGATION BAR
       ========================================================================== */
    .nav-wrapper {{
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--slate-200);
      position: sticky;
      top: 0;
      z-index: 90;
      box-shadow: 0 4px 12px -2px rgba(15, 23, 42, 0.05);
    }}

    .nav-inner {{
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
      overflow-x: auto;
      scrollbar-width: none;
    }}

    .nav-inner::-webkit-scrollbar {{
      display: none;
    }}

    .tab-nav-group {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .tab-btn {{
      padding: 16px 20px;
      background: transparent;
      border: none;
      border-bottom: 3px solid transparent;
      font-size: 14px;
      font-weight: 700;
      color: var(--slate-600);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 9px;
      transition: all 0.2s ease;
      white-space: nowrap;
    }}

    .tab-btn:hover {{
      color: var(--blue-600);
      background-color: var(--slate-50);
    }}

    .tab-btn.active {{
      color: var(--blue-600);
      border-bottom-color: var(--blue-600);
      background-color: var(--blue-50);
    }}

    .tab-btn i {{
      font-size: 16px;
    }}

    .auth-pill {{
      display: none;
      align-items: center;
      gap: 8px;
      font-size: 12.5px;
      font-weight: 700;
      padding: 7px 16px;
      border-radius: var(--radius-full);
      white-space: nowrap;
    }}

    .auth-pill.logged-in {{
      display: inline-flex;
      background: var(--emerald-50);
      color: var(--emerald-700);
      border: 1px solid var(--emerald-500);
    }}

    /* ==========================================================================
       MAIN APP CONTAINER & LAYOUT
       ========================================================================== */
    .app-container {{
      max-width: 1440px;
      width: 100%;
      margin: 24px auto;
      padding: 0 20px 48px 20px;
      flex: 1;
    }}

    .tab-content {{
      display: none;
      animation: tabFadeIn 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .tab-content.active {{
      display: block;
    }}

    @keyframes tabFadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* ==========================================================================
       CARDS & CONTAINERS
       ========================================================================== */
    .app-card {{
      background: var(--white);
      border-radius: var(--radius-lg);
      border: 1px solid var(--slate-200);
      box-shadow: var(--shadow-card);
      padding: 24px 28px;
      margin-bottom: 24px;
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
    }}

    .app-card:hover {{
      box-shadow: var(--shadow-card-hover);
    }}

    .card-head {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 16px;
      margin-bottom: 20px;
      border-bottom: 1px solid var(--slate-100);
      flex-wrap: wrap;
      gap: 12px;
    }}

    .card-heading {{
      font-size: 17px;
      font-weight: 800;
      color: var(--slate-900);
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .card-heading i {{
      color: var(--blue-600);
      font-size: 18px;
    }}

    /* ==========================================================================
       EXECUTIVE HERO METRICS
       ========================================================================== */
    .sym-grid-4 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 18px;
      margin-bottom: 24px;
    }}

    .sym-grid-3 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin-bottom: 24px;
    }}

    .sym-grid-2 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
      gap: 24px;
      margin-bottom: 24px;
    }}

    .metric-tile {{
      background: var(--white);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-md);
      padding: 20px 22px;
      display: flex;
      align-items: center;
      gap: 18px;
      box-shadow: var(--shadow-card);
      position: relative;
      overflow: hidden;
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .metric-tile:hover {{
      transform: translateY(-3px);
      box-shadow: var(--shadow-card-hover);
    }}

    .metric-tile::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 5px;
      height: 100%;
      background: var(--blue-600);
    }}

    .metric-tile.gold::before {{ background: var(--gold-500); }}
    .metric-tile.green::before {{ background: var(--emerald-600); }}
    .metric-tile.purple::before {{ background: #8b5cf6; }}
    .metric-tile.rose::before {{ background: var(--rose-600); }}

    .metric-icon {{
      width: 52px;
      height: 52px;
      border-radius: var(--radius-md);
      background: var(--blue-50);
      color: var(--blue-600);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      flex-shrink: 0;
    }}

    .metric-tile.gold .metric-icon {{ background: var(--gold-50); color: var(--gold-500); }}
    .metric-tile.green .metric-icon {{ background: var(--emerald-50); color: var(--emerald-600); }}
    .metric-tile.purple .metric-icon {{ background: #f5f3ff; color: #8b5cf6; }}
    .metric-tile.rose .metric-icon {{ background: var(--rose-100); color: var(--rose-600); }}

    .metric-data {{
      flex: 1;
    }}

    .metric-data h3 {{
      font-size: 28px;
      font-weight: 800;
      color: var(--slate-900);
      line-height: 1.1;
      letter-spacing: -0.03em;
    }}

    .metric-data p {{
      font-size: 12px;
      color: var(--slate-500);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-top: 4px;
    }}

    .metric-sub-pills {{
      display: flex;
      gap: 6px;
      margin-top: 8px;
      flex-wrap: wrap;
    }}

    .sub-pill {{
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: var(--radius-full);
      background: var(--slate-100);
      color: var(--slate-700);
    }}

    /* ==========================================================================
       HALL OF FAME (ANUGERAH 5 CALON TERBAIK)
       ========================================================================== */
    .top5-section {{
      margin-bottom: 28px;
    }}

    .top5-nav-pills {{
      display: flex;
      gap: 8px;
      margin-bottom: 16px;
    }}

    .top5-tab-btn {{
      padding: 8px 18px;
      border-radius: var(--radius-full);
      font-size: 13px;
      font-weight: 700;
      border: 1px solid var(--slate-200);
      background: var(--white);
      color: var(--slate-700);
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .top5-tab-btn.active {{
      background: var(--slate-900);
      color: var(--white);
      border-color: var(--slate-900);
      box-shadow: var(--shadow-sm);
    }}

    .top5-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 16px;
    }}

    .top5-card {{
      background: var(--white);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-md);
      padding: 18px;
      box-shadow: var(--shadow-card);
      position: relative;
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .top5-card:hover {{
      transform: translateY(-4px);
      box-shadow: var(--shadow-card-hover);
    }}

    .top5-card.rank-1 {{
      border: 2px solid var(--gold-400);
      background: linear-gradient(180deg, #fffbeb 0%, #ffffff 100%);
    }}

    .top5-card.rank-2 {{
      border: 2px solid #94a3b8;
      background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
    }}

    .top5-card.rank-3 {{
      border: 2px solid #d97706;
      background: linear-gradient(180deg, #fff7ed 0%, #ffffff 100%);
    }}

    .top5-badge {{
      position: absolute;
      top: -12px;
      right: 14px;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      font-weight: 800;
      box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }}

    .rank-1 .top5-badge {{ background: var(--gold-400); color: #78350f; }}
    .rank-2 .top5-badge {{ background: #cbd5e1; color: #334155; }}
    .rank-3 .top5-badge {{ background: #fed7aa; color: #9a3412; }}
    .rank-4 .top5-badge, .rank-5 .top5-badge {{ background: var(--slate-100); color: var(--slate-600); width:28px; height:28px; font-size:12px; }}

    .top5-name {{
      font-size: 13.5px;
      font-weight: 800;
      color: var(--slate-900);
      line-height: 1.3;
      margin-top: 6px;
      margin-bottom: 4px;
    }}

    .top5-school {{
      font-size: 12px;
      color: var(--slate-500);
      margin-bottom: 12px;
      font-weight: 500;
    }}

    .top5-score-box {{
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      padding-top: 10px;
      border-top: 1px solid var(--slate-100);
    }}

    .top5-score {{
      font-size: 20px;
      font-weight: 800;
      font-family: var(--font-mono);
      color: var(--blue-600);
    }}

    /* ==========================================================================
       PROGRAM INFO & MODULE TIMELINE CARDS
       ========================================================================== */
    .matlamat-box {{
      background: var(--slate-50);
      border: 1px solid var(--slate-200);
      border-left: 5px solid var(--blue-600);
      border-radius: var(--radius-md);
      padding: 22px 24px;
      box-shadow: var(--shadow-sm);
    }}

    .matlamat-box p {{
      font-size: 14.5px;
      line-height: 1.7;
      color: var(--slate-700);
      margin-bottom: 18px;
    }}

    .matlamat-pillars {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 14px;
    }}

    .pillar-item {{
      background: var(--white);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-sm);
      padding: 14px 16px;
      box-shadow: var(--shadow-sm);
    }}

    .pillar-item h5 {{
      font-size: 13.5px;
      font-weight: 700;
      color: var(--blue-600);
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 5px;
    }}

    .pillar-item p {{
      font-size: 12px;
      color: var(--slate-600);
      line-height: 1.5;
      margin-bottom: 0;
    }}

    .objective-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 14px;
    }}

    .objective-card {{
      background: var(--slate-50);
      border: 1px solid var(--slate-200);
      border-left: 4px solid var(--blue-600);
      border-radius: var(--radius-sm);
      padding: 16px;
      display: flex;
      align-items: flex-start;
      gap: 14px;
      transition: all 0.2s ease;
    }}

    .objective-card:hover {{
      background: var(--white);
      border-left-color: var(--gold-500);
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }}

    .objective-num {{
      width: 32px;
      height: 32px;
      border-radius: var(--radius-sm);
      background: var(--blue-50);
      color: var(--blue-600);
      font-weight: 800;
      font-size: 13px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      border: 1px solid var(--blue-100);
    }}

    .objective-text {{
      font-size: 13.5px;
      color: var(--slate-700);
      font-weight: 600;
      line-height: 1.5;
    }}

    .module-card {{
      background: var(--white);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-md);
      padding: 22px;
      box-shadow: var(--shadow-card);
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
      overflow: hidden;
    }}

    .module-card:hover {{
      transform: translateY(-3px);
      box-shadow: var(--shadow-card-hover);
    }}

    .module-card.kwd {{ border-top: 4px solid var(--blue-600); }}
    .module-card.bm {{ border-top: 4px solid var(--gold-500); }}
    .module-card.ikt {{ border-top: 4px solid var(--emerald-600); }}

    .module-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}

    .module-title {{
      font-size: 16px;
      font-weight: 800;
      color: var(--slate-900);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .module-desc {{
      font-size: 13px;
      color: var(--slate-600);
      margin-bottom: 14px;
      line-height: 1.5;
    }}

    .module-list {{
      font-size: 13px;
      color: var(--slate-700);
      line-height: 1.7;
      padding-left: 18px;
    }}

    .schedule-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 14px;
    }}

    .schedule-item {{
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 14px 18px;
      background: var(--slate-50);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-sm);
      transition: all 0.15s ease;
    }}

    .schedule-item:hover {{
      background: var(--blue-50);
      border-color: var(--blue-200);
    }}

    .schedule-time {{
      font-weight: 800;
      font-size: 13px;
      font-family: var(--font-mono);
      color: var(--blue-600);
      min-width: 80px;
      background: var(--white);
      padding: 5px 8px;
      border-radius: 6px;
      text-align: center;
      border: 1px solid var(--slate-300);
    }}

    .schedule-desc {{
      font-size: 13.5px;
      font-weight: 600;
      color: var(--slate-800);
    }}

    /* ==========================================================================
       ANALYTICS & CHARTS
       ========================================================================== */
    .chart-box {{
      position: relative;
      height: 300px;
      width: 100%;
    }}

    .simulator-box {{
      background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-md);
      padding: 22px;
    }}

    .sim-slider-group {{
      margin-bottom: 18px;
    }}

    .sim-slider-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }}

    .sim-slider-label {{
      font-size: 13px;
      font-weight: 700;
      color: var(--slate-700);
    }}

    .sim-slider-val {{
      font-size: 14px;
      font-weight: 800;
      font-family: var(--font-mono);
      color: var(--blue-600);
    }}

    .sim-range-input {{
      width: 100%;
      height: 6px;
      border-radius: var(--radius-full);
      background: var(--slate-200);
      outline: none;
      -webkit-appearance: none;
    }}

    .sim-range-input::-webkit-slider-thumb {{
      -webkit-appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: var(--blue-600);
      cursor: pointer;
      box-shadow: 0 2px 5px rgba(37, 99, 235, 0.4);
      border: 2px solid #ffffff;
      transition: transform 0.1s ease;
    }}

    .sim-range-input::-webkit-slider-thumb:hover {{
      transform: scale(1.15);
    }}

    .sim-results-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
      gap: 12px;
      margin-top: 18px;
      padding-top: 18px;
      border-top: 1px solid var(--slate-200);
    }}

    .sim-res-card {{
      background: var(--white);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-sm);
      padding: 12px;
      text-align: center;
    }}

    .sim-res-card.pass {{ border-top: 3px solid var(--emerald-600); }}
    .sim-res-card.cond {{ border-top: 3px solid var(--amber-600); }}
    .sim-res-card.fail {{ border-top: 3px solid var(--rose-600); }}

    .sim-res-card h4 {{
      font-size: 20px;
      font-weight: 800;
      font-family: var(--font-mono);
      margin-bottom: 2px;
    }}

    .sim-res-card p {{
      font-size: 11px;
      font-weight: 700;
      color: var(--slate-500);
      text-transform: uppercase;
    }}

    /* ==========================================================================
       CANDIDATES DIRECTORY & TABLE
       ========================================================================== */
    .action-toolbar {{
      background: var(--white);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-md);
      padding: 18px 22px;
      margin-bottom: 20px;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      align-items: center;
      justify-content: space-between;
    }}

    .search-input-group {{
      position: relative;
      flex: 1;
      min-width: 260px;
    }}

    .search-input-group i {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--slate-400);
      font-size: 14px;
    }}

    .form-control-input {{
      width: 100%;
      padding: 10px 14px 10px 38px;
      border-radius: var(--radius-md);
      border: 1px solid var(--slate-300);
      font-size: 13.5px;
      outline: none;
      transition: all 0.2s ease;
      background: var(--slate-50);
    }}

    .form-control-input:focus {{
      border-color: var(--blue-600);
      background: var(--white);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
    }}

    .filter-select-group {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .form-select-input {{
      padding: 10px 14px;
      border-radius: var(--radius-md);
      border: 1px solid var(--slate-300);
      font-size: 13px;
      font-weight: 600;
      color: var(--slate-700);
      background: var(--slate-50);
      outline: none;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .form-select-input:focus {{
      border-color: var(--blue-600);
      background: var(--white);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
    }}

    .table-container {{
      overflow-x: auto;
      border-radius: var(--radius-md);
      border: 1px solid var(--slate-200);
      box-shadow: var(--shadow-sm);
      background: var(--white);
    }}

    .app-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13.5px;
    }}

    .app-table thead th {{
      background: var(--slate-100);
      color: var(--slate-700);
      font-weight: 800;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 14px 18px;
      border-bottom: 2px solid var(--slate-200);
      white-space: nowrap;
    }}

    .app-table tbody tr {{
      border-bottom: 1px solid var(--slate-100);
      transition: background 0.15s ease;
    }}

    .app-table tbody tr:hover {{
      background: var(--blue-50);
    }}

    .app-table tbody td {{
      padding: 14px 18px;
      vertical-align: middle;
      color: var(--slate-800);
    }}

    .candidate-id-badge {{
      font-family: var(--font-mono);
      font-weight: 700;
      font-size: 12.5px;
      padding: 4px 8px;
      border-radius: 6px;
      background: var(--slate-100);
      color: var(--slate-700);
      border: 1px solid var(--slate-200);
      display: inline-block;
    }}

    .unit-badge {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 4px 10px;
      border-radius: var(--radius-full);
      font-size: 11.5px;
      font-weight: 800;
      text-transform: uppercase;
    }}

    .unit-badge.krs {{
      background: #eff6ff;
      color: #1e40af;
      border: 1px solid #bfdbfe;
    }}

    .unit-badge.tkrs {{
      background: #fefce8;
      color: #854d0e;
      border: 1px solid #fef08a;
    }}

    .status-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      border-radius: var(--radius-full);
      font-size: 12px;
      font-weight: 700;
      white-space: nowrap;
    }}

    .status-badge.pass {{
      background: var(--emerald-50);
      color: var(--emerald-700);
      border: 1px solid var(--emerald-500);
    }}

    .status-badge.conditional {{
      background: var(--amber-100);
      color: #92400e;
      border: 1px solid #f59e0b;
    }}

    .status-badge.fail {{
      background: var(--rose-100);
      color: #9f1239;
      border: 1px solid var(--rose-500);
    }}

    .status-badge.pending {{
      background: var(--slate-100);
      color: var(--slate-600);
      border: 1px solid var(--slate-300);
    }}

    .status-badge.absent {{
      background: #fee2e2;
      color: #991b1b;
      border: 1px solid #f87171;
    }}

    .status-badge.withdraw {{
      background: #f1f5f9;
      color: #475569;
      border: 1px solid #94a3b8;
    }}

    .btn-table-action {{
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      font-size: 12px;
      font-weight: 700;
      border: 1px solid var(--slate-200);
      background: var(--white);
      color: var(--slate-700);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s ease;
    }}

    .btn-table-action:hover {{
      background: var(--blue-50);
      color: var(--blue-600);
      border-color: var(--blue-300);
    }}

    .btn-table-action.btn-slip {{
      background: #f8fafc;
      color: #1e3a8a;
      border-color: #cbd5e1;
    }}

    .btn-table-action.btn-slip:hover {{
      background: #eff6ff;
      border-color: #93c5fd;
    }}

    /* ==========================================================================
       PRINTABLE OFFICIAL SLIP & CERTIFICATE MODAL
       ========================================================================== */
    .modal-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.65);
      backdrop-filter: blur(8px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 16px;
      animation: modalFade 0.2s ease;
    }}

    .modal-overlay.active {{
      display: flex;
    }}

    @keyframes modalFade {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}

    .modal-card {{
      background: var(--white);
      border-radius: var(--radius-lg);
      width: 100%;
      max-width: 760px;
      max-height: 92vh;
      overflow-y: auto;
      box-shadow: var(--shadow-xl);
      border: 1px solid var(--slate-200);
      position: relative;
    }}

    .modal-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 18px 24px;
      border-bottom: 1px solid var(--slate-200);
      background: var(--slate-50);
      border-top-left-radius: var(--radius-lg);
      border-top-right-radius: var(--radius-lg);
    }}

    .modal-title {{
      font-size: 16px;
      font-weight: 800;
      color: var(--slate-900);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .btn-modal-close {{
      background: transparent;
      border: none;
      font-size: 18px;
      color: var(--slate-400);
      cursor: pointer;
      padding: 4px;
      border-radius: 6px;
      transition: all 0.15s ease;
    }}

    .btn-modal-close:hover {{
      color: var(--slate-700);
      background: var(--slate-200);
    }}

    .modal-body {{
      padding: 24px;
    }}

    /* SLIP RASMI DOCUMENT STYLING */
    .official-slip-doc {{
      background: var(--white);
      border: 2px solid var(--slate-300);
      border-radius: var(--radius-sm);
      padding: 32px 28px;
      position: relative;
      box-shadow: inset 0 0 0 1px rgba(0, 0, 0, 0.05);
    }}

    .slip-doc-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 16px;
      margin-bottom: 20px;
      border-bottom: 2px solid var(--slate-800);
      gap: 16px;
    }}

    .slip-header-text {{
      text-align: center;
      flex: 1;
    }}

    .slip-header-text h3 {{
      font-size: 15px;
      font-weight: 800;
      color: var(--slate-900);
      line-height: 1.25;
      text-transform: uppercase;
    }}

    .slip-header-text h4 {{
      font-size: 13px;
      font-weight: 700;
      color: var(--blue-600);
      margin-top: 3px;
    }}

    .slip-header-text p {{
      font-size: 11px;
      color: var(--slate-500);
      font-weight: 600;
      margin-top: 2px;
    }}

    .slip-meta-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px 20px;
      background: var(--slate-50);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-sm);
      padding: 14px 18px;
      margin-bottom: 20px;
      font-size: 13px;
    }}

    .slip-meta-row {{
      display: flex;
    }}

    .slip-meta-label {{
      width: 110px;
      font-weight: 700;
      color: var(--slate-500);
    }}

    .slip-meta-val {{
      font-weight: 800;
      color: var(--slate-900);
      flex: 1;
    }}

    .slip-score-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 24px;
      font-size: 13px;
    }}

    .slip-score-table th, .slip-score-table td {{
      padding: 10px 14px;
      border: 1px solid var(--slate-300);
      text-align: left;
    }}

    .slip-score-table th {{
      background: var(--slate-100);
      font-weight: 800;
      color: var(--slate-800);
      text-transform: uppercase;
      font-size: 11.5px;
    }}

    .slip-score-table td.text-center, .slip-score-table th.text-center {{
      text-align: center;
    }}

    .slip-score-table tr.total-row {{
      background: var(--blue-50);
      font-weight: 800;
    }}

    .slip-sign-section {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
      margin-top: 36px;
      padding-top: 16px;
      border-top: 1px dashed var(--slate-300);
    }}

    .slip-sign-box {{
      text-align: center;
    }}

    .slip-sign-line {{
      height: 48px;
      border-bottom: 1px solid var(--slate-400);
      margin-bottom: 8px;
    }}

    .slip-sign-title {{
      font-size: 11.5px;
      font-weight: 700;
      color: var(--slate-700);
    }}

    .modal-footer {{
      display: flex;
      align-items: center;
      justify-content: flex-end;
      gap: 12px;
      padding: 16px 24px;
      background: var(--slate-50);
      border-top: 1px solid var(--slate-200);
      border-bottom-left-radius: var(--radius-lg);
      border-bottom-right-radius: var(--radius-lg);
    }}

    /* ==========================================================================
       ADMIN PORTAL
       ========================================================================== */
    .admin-auth-card {{
      max-width: 440px;
      margin: 40px auto;
      text-align: center;
      padding: 36px 30px;
    }}

    .admin-auth-icon {{
      width: 68px;
      height: 68px;
      border-radius: 50%;
      background: var(--blue-50);
      color: var(--blue-600);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 28px;
      margin: 0 auto 18px auto;
      border: 1px solid var(--blue-100);
    }}

    .btn-submit-action {{
      padding: 11px 24px;
      background: var(--blue-600);
      color: #ffffff;
      border: none;
      border-radius: var(--radius-md);
      font-size: 13.5px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}

    .btn-submit-action:hover {{
      background: #1d4ed8;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }}

    .btn-secondary-action {{
      padding: 11px 20px;
      background: var(--white);
      color: var(--slate-700);
      border: 1px solid var(--slate-300);
      border-radius: var(--radius-md);
      font-size: 13.5px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}

    .btn-secondary-action:hover {{
      background: var(--slate-100);
    }}

    /* ==========================================================================
       FOOTER
       ========================================================================== */
    .app-footer {{
      background: var(--slate-900);
      color: var(--slate-400);
      padding: 32px 24px;
      margin-top: auto;
      border-top: 1px solid var(--slate-800);
      text-align: center;
    }}

    .footer-logos {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 18px;
      margin-bottom: 16px;
    }}

    .footer-logo-img {{
      height: 38px;
      width: auto;
      opacity: 0.8;
      filter: grayscale(20%);
    }}

    .footer-text {{
      font-size: 12.5px;
      line-height: 1.6;
    }}

    /* ==========================================================================
       PRINT MEDIA QUERY (OPTIMIZED OFFICIAL SLIP PRINTING)
       ========================================================================== */
    @media print {{
      body * {{
        visibility: hidden;
      }}
      #modal-slip, #modal-slip * {{
        visibility: visible;
      }}
      #modal-slip {{
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        margin: 0;
        padding: 0;
        background: transparent;
        display: block !important;
      }}
      .modal-card {{
        border: none;
        box-shadow: none;
        max-width: 100%;
        max-height: 100%;
      }}
      .modal-header, .modal-footer, .top-header, .nav-wrapper, .app-footer {{
        display: none !important;
      }}
      .modal-body {{
        padding: 0;
      }}
      .official-slip-doc {{
        border: 2px solid #000000;
        box-shadow: none;
        padding: 20px;
      }}
    }}

    @media (max-width: 768px) {{
      .top-header {{ padding: 16px; }}
      .header-text h1 {{ font-size: 17px; }}
      .header-brand {{ flex-direction: column; align-items: flex-start; gap: 10px; }}
      .sym-grid-4, .sym-grid-3, .sym-grid-2 {{ grid-template-columns: 1fr; }}
      .slip-meta-grid {{ grid-template-columns: 1fr; }}
      .slip-sign-section {{ grid-template-columns: 1fr; gap: 18px; }}
    }}
  </style>
</head>
<body>

  <!-- TOP EXECUTIVE HEADER -->
  <header class="top-header">
    <div class="header-inner">
      <div class="header-brand">
        <div class="logo-container">
          <img src="{logo_ppd}" alt="Logo PPD Johor Bahru" class="header-logo-img">
          <div class="logo-divider"></div>
          <img src="{logo_krs}" alt="Logo Kadet Remaja Sekolah" class="header-logo-img">
        </div>
        <div class="header-text">
          <span class="gov-badge"><i class="fa-solid fa-award"></i> LEMBAGA PENTAULIAHAN KADET REMAJA SEKOLAH NEGERI JOHOR</span>
          <h1>DAERAH JOHOR BAHRU 2026</h1>
          <p>Sistem Pengurusan & Analisis Prestasi Kenaikan Pangkat Sarjan KRS & Koperal TKRS</p>
        </div>
      </div>
      <div class="header-actions">
        <div class="header-badge green" id="sync-badge">
          <div class="pulse-dot"></div>
          <span>Sistem Aktif • Segerak Google Sheets</span>
        </div>
        <button class="btn-header-action" id="btn-quick-sync" title="Segerak data terkini daripada Google Sheet">
          <i class="fa-solid fa-arrows-rotate"></i> Segerak
        </button>
        <button class="btn-header-action gold" id="btn-quick-top5" title="Lihat Senarai Calon Terbaik">
          <i class="fa-solid fa-trophy"></i> 5 Terbaik
        </button>
      </div>
    </div>
  </header>

  <!-- STICKY NAVIGATION BAR -->
  <nav class="nav-wrapper">
    <div class="nav-inner">
      <div class="tab-nav-group">
        <button class="tab-btn active" data-tab="tab-program">
          <i class="fa-solid fa-compass"></i> Maklumat & Jadual
        </button>
        <button class="tab-btn" data-tab="tab-analytics">
          <i class="fa-solid fa-chart-pie"></i> Dashboard Eksekutif
        </button>
        <button class="tab-btn" data-tab="tab-candidates">
          <i class="fa-solid fa-users-viewfinder"></i> Direktori Calon
        </button>
        <button class="tab-btn" data-tab="tab-admin">
          <i class="fa-solid fa-shield-halved"></i> Pusat Kawalan Urus Setia
        </button>
      </div>
      <div class="auth-pill" id="nav-auth-pill">
        <i class="fa-solid fa-user-shield"></i> URUS SETIA AKTIF
      </div>
    </div>
  </nav>

  <!-- MAIN APP CONTENT -->
  <main class="app-container">

    <!-- ====================================================================
         TAB 1: MAKLUMAT PROGRAM & JADUAL PENGUJIAN
         ==================================================================== -->
    <section id="tab-program" class="tab-content active">

      <!-- Executive Overview Card -->
      <div class="app-card">
        <div class="card-head">
          <div class="card-heading">
            <i class="fa-solid fa-landmark"></i> Matlamat & Falsafah Program Pentauliahan
          </div>
          <span class="unit-badge krs"><i class="fa-solid fa-calendar-day"></i> 22 Ogos 2026</span>
        </div>
        <div class="matlamat-box">
          <p>
            Ujian Kenaikan Pangkat Sarjan KRS (Sekolah Menengah) dan Koperal TKRS (Sekolah Rendah) Daerah Johor Bahru Tahun 2026 merupakan penanda aras kecemerlangan sahsiah, ketrampilan berpasukan, ketahanan mental, serta pematuhan standard disiplin tertinggi bagi melahirkan barisan kadet berwibawa berteraskan moto <strong>"ILMU, IMAN, AMAL"</strong>.
          </p>
          <div class="matlamat-pillars">
            <div class="pillar-item">
              <h5><i class="fa-solid fa-shield-heart"></i> Ketrampilan Disiplin</h5>
              <p>Penguasaan tatatertib pakaian seragam dan kemantapan gerak kawad kaki.</p>
            </div>
            <div class="pillar-item">
              <h5><i class="fa-solid fa-user-tie"></i> Kepimpinan Kadet</h5>
              <p>Membina keyakinan diri dan daya kepimpinan instruktur di peringkat sekolah.</p>
            </div>
            <div class="pillar-item">
              <h5><i class="fa-solid fa-kit-medical"></i> Kemahiran Hidup</h5>
              <p>Kecekapan praktikal aplikasi Bantu Mula dan seni Ikatan & Tali Temali.</p>
            </div>
            <div class="pillar-item">
              <h5><i class="fa-solid fa-flag"></i> Kenegaraan & Sahsiah</h5>
              <p>Pemupukan nilai patriotisme, akhlak terpuji dan perpaduan rentas kaum.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- 3 Module Overview Cards -->
      <div class="sym-grid-3">
        <div class="module-card kwd">
          <div class="module-head">
            <div class="module-title"><i class="fa-solid fa-person-walking"></i> Modul 1: Kawad Kaki</div>
            <span class="unit-badge krs">60% Wajaran</span>
          </div>
          <div class="module-desc">Penilaian kemahiran kawad statik, dinamik, hormat dan kawad formasi tanpa senjata.</div>
          <ul class="module-list">
            <li>Pemeriksaan Kekemasan Pakaian Seragam No. 3 / No. 4</li>
            <li>Kawad Statik: Buka/Tutup Barisan, Ke Kanan Lurus</li>
            <li>Kawad Dinamik: Cepat Jalan, Perlahan Jalan & Belok</li>
            <li>Memberi Perintah Kawad (*Khusus untuk Sarjan KRS*)</li>
          </ul>
        </div>

        <div class="module-card bm">
          <div class="module-head">
            <div class="module-title"><i class="fa-solid fa-truck-medical"></i> Modul 2: Bantu Mula</div>
            <span class="unit-badge tkrs">20% Wajaran</span>
          </div>
          <div class="module-desc">Aplikasi pertolongan cemas, pembebat, anduh dan pengurusan mangsa kecemasan.</div>
          <ul class="module-list">
            <li>Anduh Besar & Anduh Kecil (Kain Segi Tiga)</li>
            <li>Balutan Luka Kepala, Tangan & Lutut</li>
            <li>Prinsip Asas D.R.A.B.C & Rawatan Renjatan</li>
            <li>Teknik Usungan & Memindahkan Mangsa Cedera</li>
          </ul>
        </div>

        <div class="module-card ikt">
          <div class="module-head">
            <div class="module-title"><i class="fa-solid fa-ring"></i> Modul 3: Ikatan & Simpulan</div>
            <span class="unit-badge tkrs">20% Wajaran</span>
          </div>
          <div class="module-desc">Kecekapan ikatan tali temali perintis dan keselamatan gajet perkhemahan.</div>
          <ul class="module-list">
            <li>Simpulan Asas: Buku Sila, Bunga Geti & Tindih Kasih</li>
            <li>Simpul Manuk & Ikatan Balak</li>
            <li>Ikatan Seraya, Silang Gunting & Lilit Kacang</li>
            <li>Ujian Kelajuan & Keteguhan Struktur Ikatan</li>
          </ul>
        </div>
      </div>

      <!-- Schedule Timeline -->
      <div class="app-card">
        <div class="card-head">
          <div class="card-heading">
            <i class="fa-solid fa-timeline"></i> Tentatif & Jadual Pengujian Hari Pentauliahan
          </div>
          <span class="sub-pill">SMK Dato' Jaafar & SMK Mohd Khalid</span>
        </div>
        <div class="schedule-grid">
          <div class="schedule-item">
            <div class="schedule-time">07:00 AM</div>
            <div class="schedule-desc">Pendaftaran Calon, Pembahagian Nombor Giliran & Taklimat Urus Setia</div>
          </div>
          <div class="schedule-item">
            <div class="schedule-time">08:00 AM</div>
            <div class="schedule-desc">Pemeriksaan Pakaian Seragam & Ujian Modul 1: Kawad Kaki</div>
          </div>
          <div class="schedule-item">
            <div class="schedule-time">10:30 AM</div>
            <div class="schedule-desc">Ujian Modul 2 (Bantu Mula) & Modul 3 (Ikatan & Simpulan)</div>
          </div>
          <div class="schedule-item">
            <div class="schedule-time">01:00 PM</div>
            <div class="schedule-desc">Rehat, Makan Tengah Hari & Pengurusan Solat Zohor</div>
          </div>
          <div class="schedule-item">
            <div class="schedule-time">02:30 PM</div>
            <div class="schedule-desc">Semakan Markah Terakhir & Mesyuarat Lembaga Pengesahan Pentauliahan</div>
          </div>
          <div class="schedule-item">
            <div class="schedule-time">03:30 PM</div>
            <div class="schedule-desc">Majlis Penutup, Penyampaian Sijil & Pengumuman Calon Terbaik</div>
          </div>
        </div>
      </div>

    </section>

    <!-- ====================================================================
         TAB 2: DASHBOARD EKSEKUTIF & ANALISIS STATISTIK
         ==================================================================== -->
    <section id="tab-analytics" class="tab-content">

      <!-- Macro Metrics Grid -->
      <div class="sym-grid-4">
        <div class="metric-tile">
          <div class="metric-icon"><i class="fa-solid fa-users"></i></div>
          <div class="metric-data">
            <h3 id="stat-macro-total">305</h3>
            <p>Jumlah Calon Berdaftar</p>
            <div class="metric-sub-pills">
              <span class="sub-pill">144 KRS</span>
              <span class="sub-pill">161 TKRS</span>
            </div>
          </div>
        </div>

        <div class="metric-tile green">
          <div class="metric-icon"><i class="fa-solid fa-clipboard-check"></i></div>
          <div class="metric-data">
            <h3 id="stat-macro-eval">0</h3>
            <p>Calon Selesai Dinilai</p>
            <div class="metric-sub-pills">
              <span class="sub-pill" id="stat-macro-pending-pill">305 Belum Dinilai</span>
            </div>
          </div>
        </div>

        <div class="metric-tile gold">
          <div class="metric-icon"><i class="fa-solid fa-medal"></i></div>
          <div class="metric-data">
            <h3 id="stat-macro-passrate">0.0%</h3>
            <p>Kadar Kelulusan Penuh (LLL)</p>
            <div class="metric-sub-pills">
              <span class="sub-pill">Ambang: 70% | 50% | 70%</span>
            </div>
          </div>
        </div>

        <div class="metric-tile purple">
          <div class="metric-icon"><i class="fa-solid fa-chart-line"></i></div>
          <div class="metric-data">
            <h3 id="avg-score-overall">0.0%</h3>
            <p>Purata Skor Keseluruhan</p>
            <div class="metric-sub-pills">
              <span class="sub-pill">Pemberat 60:20:20</span>
            </div>
          </div>
        </div>
      </div>

      <!-- HALL OF FAME: TOP 5 PERFORMERS -->
      <div class="app-card top5-section">
        <div class="card-head">
          <div class="card-heading">
            <i class="fa-solid fa-crown" style="color:var(--gold-500);"></i> Anugerah Prestasi Cemerlang (5 Calon Terbaik)
          </div>
          <div class="top5-nav-pills">
            <button class="top5-tab-btn active" id="btn-top5-tkrs"><i class="fa-solid fa-graduation-cap"></i> TKRS (Koperal)</button>
            <button class="top5-tab-btn" id="btn-top5-krs"><i class="fa-solid fa-award"></i> KRS (Sarjan)</button>
          </div>
        </div>

        <!-- Top 5 TKRS Grid -->
        <div id="top5-tkrs-container" class="top5-grid">
          <!-- Dynamically populated by JavaScript -->
        </div>

        <!-- Top 5 KRS Grid -->
        <div id="top5-krs-container" class="top5-grid" style="display:none;">
          <!-- Dynamically populated by JavaScript -->
        </div>
      </div>

      <!-- Module Score Performance Averages -->
      <div class="sym-grid-3">
        <div class="metric-tile">
          <div class="metric-icon"><i class="fa-solid fa-person-walking"></i></div>
          <div class="metric-data">
            <h3 id="avg-score-kawad">0.0%</h3>
            <p>Purata Kawad Kaki (60%)</p>
          </div>
        </div>
        <div class="metric-tile gold">
          <div class="metric-icon"><i class="fa-solid fa-kit-medical"></i></div>
          <div class="metric-data">
            <h3 id="avg-score-bm">0.0%</h3>
            <p>Purata Bantu Mula (20%)</p>
          </div>
        </div>
        <div class="metric-tile green">
          <div class="metric-icon"><i class="fa-solid fa-ring"></i></div>
          <div class="metric-data">
            <h3 id="avg-score-ikatan">0.0%</h3>
            <p>Purata Ikatan (20%)</p>
          </div>
        </div>
      </div>

      <!-- Charts Section -->
      <div class="sym-grid-2">
        <div class="app-card">
          <div class="card-head">
            <div class="card-heading"><i class="fa-solid fa-chart-column"></i> Prestasi Purata Komponen Ujian</div>
          </div>
          <div class="chart-box">
            <canvas id="chartModulePerformance"></canvas>
          </div>
        </div>

        <div class="app-card">
          <div class="card-head">
            <div class="card-heading"><i class="fa-solid fa-chart-pie"></i> Taburan Status Keputusan Keseluruhan</div>
          </div>
          <div class="chart-box">
            <canvas id="chartPassStatus"></canvas>
          </div>
        </div>
      </div>

      <div class="sym-grid-2">
        <div class="app-card">
          <div class="card-head">
            <div class="card-heading"><i class="fa-solid fa-chart-pie"></i> Komposisi Calon Mengikut Unit & Jantina</div>
          </div>
          <div class="chart-box">
            <canvas id="chartCategoryGender"></canvas>
          </div>
        </div>

        <div class="app-card">
          <div class="card-head">
            <div class="card-heading"><i class="fa-solid fa-school"></i> 10 Sekolah Penyertaan Tertinggi</div>
          </div>
          <div class="chart-box">
            <canvas id="chartTopSchools"></canvas>
          </div>
        </div>
      </div>

      <!-- Passing Threshold Simulator -->
      <div class="app-card">
        <div class="card-head">
          <div class="card-heading">
            <i class="fa-solid fa-sliders"></i> Simulator Ambang Kelulusan & Analisis Sensitiviti
          </div>
          <span class="sub-pill">Kiraan Interaktif Masa Nyata</span>
        </div>
        <div class="simulator-box">
          <div class="sym-grid-3">
            <div class="sim-slider-group">
              <div class="sim-slider-header">
                <span class="sim-slider-label">Ambang Minima Kawad Kaki</span>
                <span class="sim-slider-val" id="text-wajaran-min-kawad">70%</span>
              </div>
              <input type="range" min="0" max="100" value="70" class="sim-range-input" id="range-wajaran-min-kawad">
            </div>

            <div class="sim-slider-group">
              <div class="sim-slider-header">
                <span class="sim-slider-label">Ambang Minima Kemahiran (Ikatan/BM)</span>
                <span class="sim-slider-val" id="text-wajaran-min-ikatan">50%</span>
              </div>
              <input type="range" min="0" max="100" value="50" class="sim-range-input" id="range-wajaran-min-ikatan">
            </div>

            <div class="sim-slider-group">
              <div class="sim-slider-header">
                <span class="sim-slider-label">Ambang Minima Keseluruhan</span>
                <span class="sim-slider-val" id="text-wajaran-min-overall">70%</span>
              </div>
              <input type="range" min="0" max="100" value="70" class="sim-range-input" id="range-wajaran-min-overall">
            </div>
          </div>

          <div class="sim-results-grid">
            <div class="sim-res-card">
              <h4 id="sim-rate-val">0.0%</h4>
              <p>Kadar Lulus</p>
            </div>
            <div class="sim-res-card pass">
              <h4 id="sim-pass-val" style="color:var(--emerald-600);">0 / 305</h4>
              <p>Lulus Penuh (LLL)</p>
            </div>
            <div class="sim-res-card cond">
              <h4 id="sim-cond-val" style="color:var(--amber-600);">0</h4>
              <p>Lulus Bersyarat</p>
            </div>
            <div class="sim-res-card fail">
              <h4 id="sim-fail-val" style="color:var(--rose-600);">0</h4>
              <p>Gagal</p>
            </div>
          </div>
        </div>
      </div>

    </section>

    <!-- ====================================================================
         TAB 3: DIREKTORI & SEMAKAN CALON
         ==================================================================== -->
    <section id="tab-candidates" class="tab-content">

      <!-- Action & Filter Toolbar -->
      <div class="action-toolbar">
        <div class="search-input-group">
          <i class="fa-solid fa-magnifying-glass"></i>
          <input type="text" id="input-candidate-search" class="form-control-input" placeholder="Cari Nama Calon, No Giliran atau Nama Sekolah...">
        </div>

        <div class="filter-select-group">
          <select id="select-unit" class="form-select-input">
            <option value="ALL">Semua Unit (KRS & TKRS)</option>
            <option value="TKRS">TKRS (Sekolah Rendah)</option>
            <option value="KRS">KRS (Sekolah Menengah)</option>
          </select>

          <select id="select-kumpulan" class="form-select-input">
            <option value="ALL">Semua Kumpulan</option>
            <option value="A">Kumpulan A</option>
            <option value="B">Kumpulan B</option>
            <option value="C">Kumpulan C</option>
          </select>

          <select id="select-jantina" class="form-select-input">
            <option value="ALL">Semua Jantina</option>
            <option value="L">Lelaki</option>
            <option value="P">Perempuan</option>
          </select>

          <select id="select-status" class="form-select-input">
            <option value="ALL">Semua Status Keputusan</option>
            <option value="PASS">Lulus (LLL)</option>
            <option value="CONDITIONAL">Lulus Bersyarat</option>
            <option value="FAIL">Gagal</option>
            <option value="PENDING">Belum Dinilai</option>
            <option value="ABSENT">Tidak Hadir (TH)</option>
            <option value="WITHDRAW">Tarik Diri</option>
          </select>

          <button class="btn-secondary-action" id="btn-csv-export" style="display:none;" title="Eksport senarai ke CSV">
            <i class="fa-solid fa-file-csv"></i> Muat Turun CSV
          </button>
        </div>
      </div>

      <!-- Candidate Data Table -->
      <div class="app-card" style="padding:0; overflow:hidden;">
        <div class="table-container">
          <table class="app-table">
            <thead>
              <tr>
                <th style="width:120px;">No Giliran</th>
                <th>Nama Calon & Sekolah</th>
                <th style="width:100px;">Unit</th>
                <th style="width:80px;">Kump</th>
                <th style="width:90px;">Markah</th>
                <th style="width:170px;">Status Keputusan</th>
                <th style="width:130px; text-align:center;">Tindakan</th>
              </tr>
            </thead>
            <tbody id="table-candidates-body">
              <!-- Dynamically populated by JavaScript -->
            </tbody>
          </table>
        </div>
      </div>

    </section>

    <!-- ====================================================================
         TAB 4: PUSAT KAWALAN URUS SETIA (ADMIN PANEL)
         ==================================================================== -->
    <section id="tab-admin" class="tab-content">

      <!-- SCREEN A: ADMIN PIN LOGIN -->
      <div id="screen-admin-login" class="app-card admin-auth-card">
        <div class="admin-auth-icon">
          <i class="fa-solid fa-lock"></i>
        </div>
        <h3>Pengesahan Pegawai Urus Setia</h3>
        <p style="color:var(--slate-500); font-size:13px; margin:8px 0 24px 0;">
          Sila masukkan PIN Keselamatan Urus Setia untuk membuka fungsi pengurusan status calon, pelarasan wajaran dan penyelenggaraan data.
        </p>

        <form id="form-admin-auth">
          <div style="margin-bottom:18px;">
            <input type="password" id="input-admin-pin" class="form-control-input" placeholder="Masukkan PIN Urus Setia..." style="text-align:center; font-size:16px; letter-spacing:3px; padding:12px;" required>
          </div>
          <div id="auth-error-alert" style="display:none; color:var(--rose-600); background:var(--rose-100); padding:10px; border-radius:var(--radius-sm); font-size:12.5px; margin-bottom:16px; font-weight:700;">
            PIN tidak sah. Sila cuba lagi.
          </div>
          <button type="submit" class="btn-submit-action" style="width:100%; justify-content:center;">
            <i class="fa-solid fa-key"></i> Log Masuk Urus Setia
          </button>
        </form>
      </div>

      <!-- SCREEN B: LOGGED-IN ADMIN COMMAND CENTER -->
      <div id="screen-admin-panel" style="display:none;">

        <!-- Top Status Alert -->
        <div class="app-card" style="background:var(--slate-900); color:var(--white); border-color:var(--slate-800);">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:14px;">
            <div>
              <div style="display:flex; align-items:center; gap:8px; color:var(--gold-400); font-weight:800; font-size:13px; text-transform:uppercase;">
                <i class="fa-solid fa-shield-check"></i> Sesi Urus Setia Aktif
              </div>
              <h3 style="color:#ffffff; margin-top:4px;">Pusat Kawalan & Penyelenggaraan Sistem</h3>
            </div>
            <button class="btn-secondary-action" id="btn-logout" style="background:rgba(255,255,255,0.1); color:#ffffff; border-color:rgba(255,255,255,0.2);">
              <i class="fa-solid fa-right-from-bracket"></i> Log Keluar
            </button>
          </div>
        </div>

        <!-- Candidate Status & Attendance Manager -->
        <div class="app-card" id="admin-candidate-manage-card">
          <div class="card-head">
            <div class="card-heading">
              <i class="fa-solid fa-user-pen"></i> Pengurusan Kehadiran & Penukaran Calon
            </div>
            <span class="sub-pill" id="manage-filter-count">305 Calon Sedia Ada</span>
          </div>

          <form id="form-manage-candidate">
            <div class="sym-grid-2" style="margin-bottom:16px;">
              <div>
                <label style="display:block; font-size:12.5px; font-weight:700; color:var(--slate-700); margin-bottom:6px;">Cari & Pilih Calon</label>
                <input type="text" id="input-manage-search" class="form-control-input" placeholder="Tapis calon mengikut nama/no giliran..." style="margin-bottom:8px;">
                <select id="select-candidate-id" class="form-select-input" style="width:100%;" required>
                  <option value="">-- Pilih Calon --</option>
                </select>
              </div>

              <div>
                <label style="display:block; font-size:12.5px; font-weight:700; color:var(--slate-700); margin-bottom:6px;">Tindakan Status</label>
                <select id="select-candidate-action" class="form-select-input" style="width:100%;" required>
                  <option value="HADIR">Calon Hadir (Normal)</option>
                  <option value="TIDAK HADIR">Tidak Hadir (TH)</option>
                  <option value="TARIK DIRI">Tarik Diri</option>
                  <option value="TUKAR PESERTA">Tukar Nama Calon Pengganti</option>
                </select>
                <div id="wrapper-newname" style="margin-top:8px;">
                  <input type="text" id="input-candidate-newname" class="form-control-input" placeholder="Nama penuh calon pengganti (jika tukar)...">
                </div>
              </div>
            </div>

            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
              <div id="candidate-action-status" style="display:none; font-weight:700; font-size:13px; padding:8px 14px; border-radius:6px;"></div>
              <button type="submit" class="btn-submit-action">
                <i class="fa-solid fa-floppy-disk"></i> Simpan Kemas Kini Calon
              </button>
            </div>
          </form>
        </div>

        <!-- Weightage Configuration & Google Sheets Maintenance -->
        <div class="sym-grid-2">
          <div class="app-card">
            <div class="card-head">
              <div class="card-heading"><i class="fa-solid fa-sliders"></i> Tetapan Wajaran Markah Rasmi</div>
              <span id="badge-wajaran-total" class="status-badge pass">Jumlah Wajaran: 100%</span>
            </div>

            <div class="sim-slider-group">
              <div class="sim-slider-header">
                <span class="sim-slider-label">Wajaran Kawad Kaki</span>
                <span class="sim-slider-val" id="text-wajaran-kawad">60%</span>
              </div>
              <input type="range" min="0" max="100" value="60" class="sim-range-input" id="range-wajaran-kawad">
            </div>

            <div class="sim-slider-group">
              <div class="sim-slider-header">
                <span class="sim-slider-label">Wajaran Bantu Mula</span>
                <span class="sim-slider-val" id="text-wajaran-bm">20%</span>
              </div>
              <input type="range" min="0" max="100" value="20" class="sim-range-input" id="range-wajaran-bm">
            </div>

            <div class="sim-slider-group">
              <div class="sim-slider-header">
                <span class="sim-slider-label">Wajaran Ikatan & Simpulan</span>
                <span class="sim-slider-val" id="text-wajaran-ikatan">20%</span>
              </div>
              <input type="range" min="0" max="100" value="20" class="sim-range-input" id="range-wajaran-ikatan">
            </div>

            <div style="margin-top:20px;">
              <button class="btn-submit-action" id="btn-save-wajaran" style="width:100%; justify-content:center;">
                <i class="fa-solid fa-cloud-arrow-up"></i> Simpan Tetapan ke Google Sheet
              </button>
            </div>
          </div>

          <div class="app-card">
            <div class="card-head">
              <div class="card-heading"><i class="fa-solid fa-screwdriver-wrench"></i> Penyelenggaraan Google Sheet</div>
            </div>
            <p style="font-size:13px; color:var(--slate-600); margin-bottom:18px;">
              Gunakan fungsi ini untuk menyelaraskan formula VLOOKUP, membaiki format nombor atau memasang trigger automasi pada helaian Google Sheet live.
            </p>

            <div style="display:flex; flex-direction:column; gap:12px;">
              <button class="btn-secondary-action" id="btn-repair-formulas" style="justify-content:flex-start;">
                <i class="fa-solid fa-wand-magic-sparkles" style="color:var(--blue-600);"></i> Baiki Semua Formula VLOOKUP & Format Sheet
              </button>
              <button class="btn-secondary-action" id="btn-install-triggers" style="justify-content:flex-start;">
                <i class="fa-solid fa-bolt" style="color:var(--gold-500);"></i> Pasang Trigger Automasi Segerak (onChange)
              </button>
            </div>

            <div id="wajaran-action-status" style="display:none; font-weight:700; font-size:13px; padding:10px 14px; border-radius:6px; margin-top:16px;"></div>
          </div>
        </div>

      </div>

    </section>

  </main>

  <!-- ====================================================================
       OFFICIAL PRINTABLE SLIP MODAL (SLIP KEPUTUSAN RASMI)
       ==================================================================== -->
  <div id="modal-slip" class="modal-overlay">
    <div class="modal-card">
      <div class="modal-header">
        <div class="modal-title">
          <i class="fa-solid fa-file-certificate" style="color:var(--gold-500);"></i> Slip Keputusan Rasmi Pentauliahan
        </div>
        <button class="btn-modal-close" id="btn-close-slip"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <div class="official-slip-doc" id="printable-slip-area">
          <div class="slip-doc-header">
            <img src="{logo_ppd}" alt="Logo PPD JB" style="height:55px; width:auto;">
            <div class="slip-header-text">
              <h3>JABATAN PENDIDIKAN NEGERI JOHOR</h3>
              <h4>PEJABAT PENDIDIKAN DAERAH JOHOR BAHRU</h4>
              <p>UJIAN KENAIKAN PANGKAT SARJAN KRS & KOPERAL TKRS 2026</p>
            </div>
            <img src="{logo_krs}" alt="Logo KRS" style="height:55px; width:auto;">
          </div>

          <div class="slip-meta-grid">
            <div class="slip-meta-row">
              <span class="slip-meta-label">No Giliran:</span>
              <span class="slip-meta-val" id="slip-val-nogiliran">-</span>
            </div>
            <div class="slip-meta-row">
              <span class="slip-meta-label">Unit/Pangkat:</span>
              <span class="slip-meta-val" id="slip-val-unit">-</span>
            </div>
            <div class="slip-meta-row" style="grid-column: span 2;">
              <span class="slip-meta-label">Nama Calon:</span>
              <span class="slip-meta-val" id="slip-val-nama">-</span>
            </div>
            <div class="slip-meta-row" style="grid-column: span 2;">
              <span class="slip-meta-label">Sekolah:</span>
              <span class="slip-meta-val" id="slip-val-sekolah">-</span>
            </div>
            <div class="slip-meta-row">
              <span class="slip-meta-label">Kumpulan:</span>
              <span class="slip-meta-val" id="slip-val-kumpulan">-</span>
            </div>
            <div class="slip-meta-row">
              <span class="slip-meta-label">Jantina:</span>
              <span class="slip-meta-val" id="slip-val-jantina">-</span>
            </div>
          </div>

          <table class="slip-score-table">
            <thead>
              <tr>
                <th style="width:40px;" class="text-center">Bil</th>
                <th>Komponen Penilaian</th>
                <th style="width:100px;" class="text-center">Wajaran</th>
                <th style="width:110px;" class="text-center">Skor Mentah</th>
                <th style="width:120px;" class="text-center">Markah Diperoleh</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="text-center">1</td>
                <td><strong>Kawad Kaki</strong> (Statik, Dinamik & Perintah)</td>
                <td class="text-center">60%</td>
                <td class="text-center" id="slip-score-raw-kawad">-</td>
                <td class="text-center" id="slip-score-weight-kawad" style="font-weight:700;">-</td>
              </tr>
              <tr>
                <td class="text-center">2</td>
                <td><strong>Bantu Mula</strong> (Pertolongan Cemas & Anduh)</td>
                <td class="text-center">20%</td>
                <td class="text-center" id="slip-score-raw-bm">-</td>
                <td class="text-center" id="slip-score-weight-bm" style="font-weight:700;">-</td>
              </tr>
              <tr>
                <td class="text-center">3</td>
                <td><strong>Ikatan & Simpulan</strong> (Tali Temali & Gajet)</td>
                <td class="text-center">20%</td>
                <td class="text-center" id="slip-score-raw-ikatan">-</td>
                <td class="text-center" id="slip-score-weight-ikatan" style="font-weight:700;">-</td>
              </tr>
              <tr class="total-row">
                <td colspan="3" style="text-align:right;"><strong>JUMLAH KESELURUHAN & KEPUTUSAN</strong></td>
                <td class="text-center" id="slip-score-total" style="font-size:15px; font-family:var(--font-mono); color:var(--blue-600);">-</td>
                <td class="text-center" id="slip-score-status">-</td>
              </tr>
            </tbody>
          </table>

          <div class="slip-sign-section">
            <div class="slip-sign-box">
              <div class="slip-sign-line"></div>
              <div class="slip-sign-title">Pengerusi Jawatankuasa Teknikal<br>Pentauliahan KRS/TKRS PPD Johor Bahru</div>
            </div>
            <div class="slip-sign-box">
              <div class="slip-sign-line"></div>
              <div class="slip-sign-title">Pegawai Meja Kadet Remaja Sekolah<br>Pejabat Pendidikan Daerah Johor Bahru</div>
            </div>
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn-secondary-action" id="btn-cancel-slip">Tutup</button>
        <button class="btn-submit-action" id="btn-print-slip"><i class="fa-solid fa-print"></i> Cetak Slip (PDF / Pencetak)</button>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <footer class="app-footer">
    <div class="footer-logos">
      <img src="{logo_ppd}" alt="Logo PPD JB" class="footer-logo-img">
      <img src="{logo_krs}" alt="Logo KRS" class="footer-logo-img">
    </div>
    <div class="footer-text">
      <strong>Hak Cipta Terpelihara © 2026 Lembaga Pentauliahan Kadet Remaja Sekolah Daerah Johor Bahru</strong><br>
      Sistem Pengurusan Data & Web App disediakan khas untuk Ujian Kenaikan Pangkat Sarjan KRS & Koperal TKRS Daerah Johor Bahru.
    </div>
  </footer>

  <!-- SERVER DATA PAYLOAD & LOGIC ENGINE -->
  <script id="server-data-payload" type="application/json">
    {payload_scriptlet}
  </script>

  <script>
    let SERVER_DATA = null;
    try {{
      const payloadEl = document.getElementById('server-data-payload');
      const payloadText = payloadEl ? payloadEl.textContent.trim() : '';
      if (payloadText && payloadText !== 'null') {{
        SERVER_DATA = JSON.parse(payloadText);
      }}
    }} catch (e) {{
      console.warn("Server hydration payload parse warning:", e);
      SERVER_DATA = null;
    }}

    const EMBEDDED_CANDIDATES = {embedded_candidates_json};

    const GAS_EXEC_URL = "https://script.google.com/macros/s/AKfycbw7QzD_8naN4kFR_1BRk6UO3EjclkmESDP8lW55t7Gvbf-ldcwE-LGbSLF76h6jW3s7/exec";

    async function runBackendAction(actionName, params = {{}}) {{
      if (typeof google !== 'undefined' && google.script && google.script.run) {{
        return new Promise((resolve, reject) => {{
          const runner = google.script.run
            .withSuccessHandler(res => resolve(res))
            .withFailureHandler(err => reject(err));
          
          if (actionName === 'getDashboardData') runner.getDashboardData();
          else if (actionName === 'verifyAdminPIN') runner.verifyAdminPIN(params.pin);
          else if (actionName === 'updatePassingWajaran') runner.updatePassingWajaran(params.config, params.pin);
          else if (actionName === 'updateCandidateStatusRecord') runner.updateCandidateStatusRecord(params.payload, params.pin);
          else if (actionName === 'repairAllFormulasAndFormat') runner.repairAllFormulasAndFormat();
          else if (actionName === 'setupAutoSyncTriggers') runner.setupAutoSyncTriggers();
          else reject(new Error("Aksi tidak sah: " + actionName));
        }});
      }}

      try {{
        const response = await fetch(GAS_EXEC_URL, {{
          method: 'POST',
          headers: {{ 'Content-Type': 'text/plain;charset=utf-8' }},
          body: JSON.stringify({{ action: actionName, params: params }})
        }});
        const data = await response.json();
        if (data.success === false || data.error) {{
          throw new Error(data.error || "Ralat pelayan backend.");
        }}
        return data.result;
      }} catch (postErr) {{
        try {{
          const url = new URL(GAS_EXEC_URL);
          url.searchParams.set('action', actionName);
          url.searchParams.set('payload', JSON.stringify(params));
          const getRes = await fetch(url.toString());
          const getData = await getRes.json();
          if (getData.success === false || getData.error) {{
            throw new Error(getData.error || postErr.message);
          }}
          return getData.result;
        }} catch (getErr) {{
          throw postErr;
        }}
      }}
    }}

    const App = {{
      state: {{
        candidates: (SERVER_DATA && SERVER_DATA.candidates) ? SERVER_DATA.candidates : EMBEDDED_CANDIDATES,
        currentWajaran: {{
          kawad: 0.70,
          ikatan: 0.50,
          overall: 0.70,
          wajaranKawad: 0.60,
          wajaranBM: 0.20,
          wajaranIkatan: 0.20
        }},
        isAdminLoggedIn: false,
        activeTab: 'tab-program',
        top5Unit: 'TKRS',
        charts: {{}}
      }},

      init() {{
        this.parseCandidateIdentifiers();

        if (sessionStorage.getItem('pentauliahan_admin_auth') === 'true') {{
          this.state.isAdminLoggedIn = true;
        }}

        if (SERVER_DATA && SERVER_DATA.wajaran) {{
          this.state.currentWajaran = {{
            kawad: SERVER_DATA.wajaran.wajaranMinKawad || 0.70,
            ikatan: SERVER_DATA.wajaran.wajaranMinIkatan || 0.50,
            overall: SERVER_DATA.wajaran.wajaranMinOverall || 0.70,
            wajaranKawad: SERVER_DATA.wajaran.wajaranKawad || 0.60,
            wajaranBM: SERVER_DATA.wajaran.wajaranBantuMula || 0.20,
            wajaranIkatan: SERVER_DATA.wajaran.wajaranIkatan || 0.20
          }};
        }}

        this.bindNavEvents();
        this.bindFilterEvents();
        this.bindAdminEvents();
        this.bindCandidateManageEvents();
        this.bindSlipModalEvents();
        this.bindTop5Events();

        this.recalculateAllStats();
        this.renderCandidatesTable();
        this.populateCandidateDropdown();
        this.syncSliderInputs();
        this.updateAuthVisuals();
        this.renderTop5Podium();
        this.initCharts();

        if (!SERVER_DATA) {{
          this.refreshLiveData(true);
        }}
      }},

      parseCandidateIdentifiers() {{
        this.state.candidates.forEach(c => {{
          if (c.noGiliran) {{
            const parts = c.noGiliran.split('-');
            if (parts.length >= 2) {{
              c.unit = parts[0];
              const code = parts[1];
              c.jantina = code.charAt(0);
              c.kumpulan = code.charAt(1);
            }}
          }}
        }});
      }},

      async refreshLiveData(silent = false) {{
        const syncBadge = document.getElementById('sync-badge');
        if (syncBadge && !silent) {{
          syncBadge.className = 'header-badge';
          syncBadge.innerHTML = '<i class="fa-solid fa-arrows-rotate fa-spin"></i> Menyegerak Data...';
        }}

        try {{
          const data = await runBackendAction('getDashboardData');
          if (data && data.candidates && data.candidates.length > 0) {{
            this.state.candidates = data.candidates;
            this.parseCandidateIdentifiers();
            if (data.wajaran) {{
              this.state.currentWajaran = {{
                kawad: data.wajaran.wajaranMinKawad,
                ikatan: data.wajaran.wajaranMinIkatan,
                overall: data.wajaran.wajaranMinOverall,
                wajaranKawad: data.wajaran.wajaranKawad,
                wajaranBM: data.wajaran.wajaranBantuMula,
                wajaranIkatan: data.wajaran.wajaranIkatan
              }};
              this.syncSliderInputs();
            }}
            this.recalculateAllStats();
            this.renderCandidatesTable();
            this.populateCandidateDropdown();
            this.renderTop5Podium();
            this.updateCharts();
          }}
          if (syncBadge) {{
            syncBadge.className = 'header-badge green';
            syncBadge.innerHTML = '<div class="pulse-dot"></div><span>Sistem Aktif • Segerak Google Sheets</span>';
          }}
        }} catch(err) {{
          console.warn('Guna data terbina (Offline/Preview Mode):', err);
          if (syncBadge) {{
            syncBadge.className = 'header-badge green';
            syncBadge.innerHTML = '<div class="pulse-dot"></div><span>Sistem Sedia (Data Terbina)</span>';
          }}
        }}
      }},

      bindNavEvents() {{
        document.querySelectorAll('.tab-btn').forEach(btn => {{
          btn.addEventListener('click', (e) => {{
            const tabId = e.currentTarget.getAttribute('data-tab');
            this.switchTab(tabId);
          }});
        }});

        document.getElementById('btn-quick-sync')?.addEventListener('click', () => {{
          this.refreshLiveData(false);
        }});

        document.getElementById('btn-quick-top5')?.addEventListener('click', () => {{
          this.switchTab('tab-analytics');
          const el = document.querySelector('.top5-section');
          if (el) el.scrollIntoView({{ behavior: 'smooth' }});
        }});
      }},

      switchTab(tabId) {{
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(p => p.classList.remove('active'));
        
        const targetBtn = document.querySelector(`[data-tab="${{tabId}}"]`);
        const targetPane = document.getElementById(tabId);
        
        if (targetBtn) targetBtn.classList.add('active');
        if (targetPane) targetPane.classList.add('active');
        this.state.activeTab = tabId;

        if (tabId === 'tab-analytics') {{
          setTimeout(() => this.updateCharts(), 100);
        }}
      }},

      updateAuthVisuals() {{
        const authPill = document.getElementById('nav-auth-pill');
        const loginScreen = document.getElementById('screen-admin-login');
        const panelScreen = document.getElementById('screen-admin-panel');
        const csvBtn = document.getElementById('btn-csv-export');
        const manageCard = document.getElementById('admin-candidate-manage-card');

        if (this.state.isAdminLoggedIn) {{
          if (authPill) {{
            authPill.className = 'auth-pill logged-in';
            authPill.innerHTML = '<i class="fa-solid fa-user-shield"></i> URUS SETIA AKTIF';
            authPill.style.display = 'inline-flex';
          }}
          if (loginScreen) loginScreen.style.display = 'none';
          if (panelScreen) panelScreen.style.display = 'block';
          if (csvBtn) csvBtn.style.display = 'inline-flex';
          if (manageCard) manageCard.style.display = 'block';
          document.querySelectorAll('.btn-table-manage').forEach(b => b.style.display = 'inline-flex');
        }} else {{
          if (authPill) {{
            authPill.className = 'auth-pill';
            authPill.style.display = 'none';
          }}
          if (loginScreen) loginScreen.style.display = 'block';
          if (panelScreen) panelScreen.style.display = 'none';
          if (csvBtn) csvBtn.style.display = 'none';
          if (manageCard) manageCard.style.display = 'none';
          document.querySelectorAll('.btn-table-manage').forEach(b => b.style.display = 'none');
        }}
      }},

      recalculateAllStats() {{
        const w = this.state.currentWajaran;
        let evaluated = 0;
        let passCount = 0;
        let condCount = 0;
        let failCount = 0;
        let absentCount = 0;
        let withdrawCount = 0;
        let sumKawad = 0, sumBM = 0, sumIkatan = 0, sumOverall = 0;

        this.state.candidates.forEach(c => {{
          if (c.catatan && (c.catatan.includes('TARIK DIRI'))) {{
            withdrawCount++;
            c.isTarikDiri = true;
            c.isPass = false;
            c.statusText = 'TARIK DIRI';
            return;
          }}

          if (c.isAbsent || (c.catatan && (c.catatan.includes('TH') || c.catatan.includes('TIDAK HADIR')))) {{
            absentCount++;
            c.isAbsent = true;
            c.isPass = false;
            c.statusText = 'TH';
            return;
          }}

          const rawK = parseFloat(c.rawKawad) || 0;
          const rawBM = parseFloat(c.rawBantuMula) || 0;
          const rawIK = parseFloat(c.rawIkatan) || 0;

          if (rawK > 0 || rawBM > 0 || rawIK > 0) {{
            evaluated++;
            sumKawad += rawK;
            sumBM += rawBM;
            sumIkatan += rawIK;

            const overall = (rawK * w.wajaranKawad) + (rawBM * w.wajaranBM) + (rawIK * w.wajaranIkatan);
            c.rawOverall = overall;
            c.overall = (overall * 100).toFixed(1) + '%';
            sumOverall += overall;

            const avgSkill = (rawBM + rawIK) / 2.0;
            const passK = rawK >= w.kawad;
            const passSkill = avgSkill >= w.ikatan;
            const passOverall = overall >= w.overall;

            c.statusText = (passK ? 'L' : 'G') + (passSkill ? 'L' : 'G') + (passOverall ? 'L' : 'G');
            
            if (c.statusText === 'LLL' || (passK && passSkill && passOverall)) {{
              c.isPass = true;
              passCount++;
            }} else if (overall >= 0.50) {{
              c.isPass = false;
              condCount++;
            }} else {{
              c.isPass = false;
              failCount++;
            }}
          }}
        }});

        const total = this.state.candidates.length;
        const passRate = total > 0 ? ((passCount / total) * 100).toFixed(1) : 0;

        const elTotal = document.getElementById('stat-macro-total');
        if (elTotal) elTotal.innerText = total;
        const elEval = document.getElementById('stat-macro-eval');
        if (elEval) elEval.innerText = evaluated;
        const elPendingPill = document.getElementById('stat-macro-pending-pill');
        if (elPendingPill) elPendingPill.innerText = `${{total - evaluated}} Belum Dinilai`;
        const elPass = document.getElementById('stat-macro-passrate');
        if (elPass) elPass.innerText = passRate + '%';

        if (evaluated > 0) {{
          document.getElementById('avg-score-kawad').innerText = ((sumKawad / evaluated) * 100).toFixed(1) + '%';
          document.getElementById('avg-score-bm').innerText = ((sumBM / evaluated) * 100).toFixed(1) + '%';
          document.getElementById('avg-score-ikatan').innerText = ((sumIkatan / evaluated) * 100).toFixed(1) + '%';
          document.getElementById('avg-score-overall').innerText = ((sumOverall / evaluated) * 100).toFixed(1) + '%';
        }}

        const elSimRate = document.getElementById('sim-rate-val');
        if (elSimRate) elSimRate.innerText = passRate + '%';
        const elSimPass = document.getElementById('sim-pass-val');
        if (elSimPass) elSimPass.innerText = `${{passCount}} / ${{total}}`;
        const elSimCond = document.getElementById('sim-cond-val');
        if (elSimCond) elSimCond.innerText = condCount;
        const elSimFail = document.getElementById('sim-fail-val');
        if (elSimFail) elSimFail.innerText = failCount;

        this.renderTop5Podium();
        this.updateCharts();
      }},

      renderCandidatesTable() {{
        const tbody = document.getElementById('table-candidates-body');
        if (!tbody) return;

        const searchQuery = (document.getElementById('input-candidate-search')?.value || '').toLowerCase();
        const filterUnit = document.getElementById('select-unit')?.value || 'ALL';
        const filterKumpulan = document.getElementById('select-kumpulan')?.value || 'ALL';
        const filterJantina = document.getElementById('select-jantina')?.value || 'ALL';
        const filterStatus = document.getElementById('select-status')?.value || 'ALL';

        const filtered = this.state.candidates.filter(c => {{
          const matchSearch = (c.nama || '').toLowerCase().includes(searchQuery) ||
                              (c.noGiliran || '').toLowerCase().includes(searchQuery) ||
                              (c.sekolah || '').toLowerCase().includes(searchQuery);
          
          const matchUnit = filterUnit === 'ALL' || c.unit === filterUnit;
          const matchKumpulan = filterKumpulan === 'ALL' || c.kumpulan === filterKumpulan;
          const matchJantina = filterJantina === 'ALL' || c.jantina === filterJantina;

          let matchStatus = true;
          if (filterStatus === 'PASS') {{
            matchStatus = c.statusText === 'LLL';
          }} else if (filterStatus === 'CONDITIONAL') {{
            matchStatus = c.statusText !== 'LLL' && !c.isAbsent && !c.isTarikDiri && (c.rawOverall >= 0.5);
          }} else if (filterStatus === 'FAIL') {{
            matchStatus = c.statusText !== 'LLL' && !c.isAbsent && !c.isTarikDiri && c.rawOverall < 0.5 && (c.rawOverall > 0);
          }} else if (filterStatus === 'PENDING') {{
            matchStatus = (!c.rawOverall || c.rawOverall === 0) && !c.isAbsent && !c.isTarikDiri;
          }} else if (filterStatus === 'ABSENT') {{
            matchStatus = c.isAbsent || c.statusText === 'TH' || (c.catatan && c.catatan.includes('TIDAK HADIR'));
          }} else if (filterStatus === 'WITHDRAW') {{
            matchStatus = c.isTarikDiri || c.statusText === 'TARIK DIRI' || (c.catatan && c.catatan.includes('TARIK DIRI'));
          }}

          return matchSearch && matchUnit && matchKumpulan && matchJantina && matchStatus;
        }});

        tbody.innerHTML = '';
        if (filtered.length === 0) {{
          tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:36px; color:var(--slate-500); font-weight:600;"><i class="fa-solid fa-magnifying-glass" style="font-size:24px; color:var(--slate-300); margin-bottom:8px; display:block;"></i>Tiada rekod calon yang sepadan dengan carian atau penapis anda.</td></tr>';
          return;
        }}

        filtered.forEach(c => {{
          let badgeHtml = '<span class="status-badge pending">Belum Dinilai</span>';
          if (c.isTarikDiri || c.statusText === 'TARIK DIRI' || (c.catatan && c.catatan.includes('TARIK DIRI'))) {{
            badgeHtml = '<span class="status-badge withdraw"><i class="fa-solid fa-person-walking-arrow-right"></i> Tarik Diri</span>';
          }} else if (c.statusText === 'TH' || c.isAbsent || (c.catatan && c.catatan.includes('TIDAK HADIR'))) {{
            badgeHtml = '<span class="status-badge absent"><i class="fa-solid fa-user-slash"></i> Tidak Hadir (TH)</span>';
          }} else if (c.statusText === 'LLL') {{
            badgeHtml = '<span class="status-badge pass"><i class="fa-solid fa-circle-check"></i> Lulus (LLL)</span>';
          }} else if (c.rawOverall >= 0.50) {{
            badgeHtml = `<span class="status-badge conditional"><i class="fa-solid fa-triangle-exclamation"></i> Bersyarat (${{c.statusText}})</span>`;
          }} else if (c.rawOverall > 0) {{
            badgeHtml = `<span class="status-badge fail"><i class="fa-solid fa-circle-xmark"></i> Gagal (${{c.statusText}})</span>`;
          }}

          const unitClass = c.unit === 'TKRS' ? 'tkrs' : 'krs';

          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td><span class="candidate-id-badge">${{c.noGiliran}}</span></td>
            <td>
              <div style="font-weight:700; color:var(--slate-900); font-size:13.5px;">${{c.nama}}</div>
              <div style="font-size:12px; color:var(--slate-500); margin-top:2px;">${{c.sekolah}}</div>
            </td>
            <td><span class="unit-badge ${{unitClass}}">${{c.unit}}</span></td>
            <td><strong>${{c.kumpulan}}</strong></td>
            <td><strong style="font-family:var(--font-mono); font-size:13.5px; color:var(--blue-600);">${{c.overall || '0.0%'}}</strong></td>
            <td>${{badgeHtml}}</td>
            <td style="text-align:center;">
              <div style="display:inline-flex; gap:6px;">
                <button class="btn-table-action btn-slip" data-id="${{c.noGiliran}}" title="Papar & Cetak Slip Keputusan Rasmi">
                  <i class="fa-solid fa-file-invoice"></i> Slip
                </button>
                <button class="btn-table-action btn-table-manage" data-id="${{c.noGiliran}}" title="Urus Status Calon" style="${{this.state.isAdminLoggedIn ? 'display:inline-flex;' : 'display:none;'}}">
                  <i class="fa-solid fa-user-gear"></i> Urus
                </button>
              </div>
            </td>
          `;
          tbody.appendChild(tr);
        }});

        // Bind table action buttons
        tbody.querySelectorAll('.btn-slip').forEach(btn => {{
          btn.addEventListener('click', (e) => {{
            const id = e.currentTarget.getAttribute('data-id');
            this.openSlipModal(id);
          }});
        }});

        tbody.querySelectorAll('.btn-table-manage').forEach(btn => {{
          btn.addEventListener('click', (e) => {{
            const id = e.currentTarget.getAttribute('data-id');
            this.switchTab('tab-admin');
            const select = document.getElementById('select-candidate-id');
            if (select) {{
              select.value = id;
              document.getElementById('admin-candidate-manage-card')?.scrollIntoView({{ behavior: 'smooth' }});
            }}
          }});
        }});
      }},

      renderTop5Podium() {{
        const tkrsContainer = document.getElementById('top5-tkrs-container');
        const krsContainer = document.getElementById('top5-krs-container');
        if (!tkrsContainer || !krsContainer) return;

        const getTop5 = (unit) => {{
          return this.state.candidates
            .filter(c => c.unit === unit && !c.isAbsent && !c.isTarikDiri && (c.rawOverall || 0) > 0)
            .sort((a, b) => (b.rawOverall || 0) - (a.rawOverall || 0))
            .slice(0, 5);
        }};

        const renderGrid = (list, container) => {{
          container.innerHTML = '';
          if (list.length === 0) {{
            container.innerHTML = '<div style="grid-column:1/-1; text-align:center; padding:24px; color:var(--slate-500); font-weight:600;">Belum ada calon dinilai dalam kategori ini. Markah akan dipaparkan secara automatik sebaik sahaja penguji memasukkan markah di AppSheet.</div>';
            return;
          }}

          list.forEach((c, idx) => {{
            const rank = idx + 1;
            const card = document.createElement('div');
            card.className = `top5-card rank-${{rank}}`;
            
            let badgeIcon = `${{rank}}`;
            if (rank === 1) badgeIcon = '<i class="fa-solid fa-crown"></i>';
            else if (rank === 2) badgeIcon = '<i class="fa-solid fa-medal"></i>';
            else if (rank === 3) badgeIcon = '<i class="fa-solid fa-award"></i>';

            card.innerHTML = `
              <div class="top5-badge">${{badgeIcon}}</div>
              <div>
                <span class="candidate-id-badge" style="font-size:11px;">${{c.noGiliran}}</span>
                <div class="top5-name">${{c.nama}}</div>
                <div class="top5-school">${{c.sekolah}}</div>
              </div>
              <div class="top5-score-box">
                <span style="font-size:11.5px; font-weight:700; color:var(--slate-500);">Markah Keseluruhan:</span>
                <span class="top5-score">${{c.overall}}</span>
              </div>
              <button class="btn-table-action btn-slip" data-id="${{c.noGiliran}}" style="margin-top:10px; width:100%; justify-content:center;">
                <i class="fa-solid fa-file-invoice"></i> Papar Slip Rasmi
              </button>
            `;
            container.appendChild(card);
          }});

          container.querySelectorAll('.btn-slip').forEach(b => {{
            b.addEventListener('click', (e) => {{
              const id = e.currentTarget.getAttribute('data-id');
              this.openSlipModal(id);
            }});
          }});
        }};

        renderGrid(getTop5('TKRS'), tkrsContainer);
        renderGrid(getTop5('KRS'), krsContainer);
      }},

      bindTop5Events() {{
        const btnTKRS = document.getElementById('btn-top5-tkrs');
        const btnKRS = document.getElementById('btn-top5-krs');
        const tkrsGrid = document.getElementById('top5-tkrs-container');
        const krsGrid = document.getElementById('top5-krs-container');

        btnTKRS?.addEventListener('click', () => {{
          btnTKRS.classList.add('active');
          btnKRS.classList.remove('active');
          tkrsGrid.style.display = 'grid';
          krsGrid.style.display = 'none';
        }});

        btnKRS?.addEventListener('click', () => {{
          btnKRS.classList.add('active');
          btnTKRS.classList.remove('active');
          krsGrid.style.display = 'grid';
          tkrsGrid.style.display = 'none';
        }});
      }},

      openSlipModal(noGiliran) {{
        const c = this.state.candidates.find(x => x.noGiliran === noGiliran);
        if (!c) return;

        const w = this.state.currentWajaran;
        const rawK = parseFloat(c.rawKawad) || 0;
        const rawBM = parseFloat(c.rawBantuMula) || 0;
        const rawIK = parseFloat(c.rawIkatan) || 0;
        const overall = (rawK * w.wajaranKawad) + (rawBM * w.wajaranBM) + (rawIK * w.wajaranIkatan);

        document.getElementById('slip-val-nogiliran').innerText = c.noGiliran;
        document.getElementById('slip-val-unit').innerText = `${{c.unit}} (${{c.unit === 'TKRS' ? 'KOPERAL' : 'SARJAN'}})`;
        document.getElementById('slip-val-nama').innerText = c.nama;
        document.getElementById('slip-val-sekolah').innerText = c.sekolah;
        document.getElementById('slip-val-kumpulan').innerText = `Kumpulan ${{c.kumpulan}}`;
        document.getElementById('slip-val-jantina').innerText = c.jantina === 'L' ? 'Lelaki' : 'Perempuan';

        document.getElementById('slip-score-raw-kawad').innerText = (rawK * 100).toFixed(1) + '%';
        document.getElementById('slip-score-weight-kawad').innerText = (rawK * w.wajaranKawad * 100).toFixed(1) + '%';

        document.getElementById('slip-score-raw-bm').innerText = (rawBM * 100).toFixed(1) + '%';
        document.getElementById('slip-score-weight-bm').innerText = (rawBM * w.wajaranBM * 100).toFixed(1) + '%';

        document.getElementById('slip-score-raw-ikatan').innerText = (rawIK * 100).toFixed(1) + '%';
        document.getElementById('slip-score-weight-ikatan').innerText = (rawIK * w.wajaranIkatan * 100).toFixed(1) + '%';

        document.getElementById('slip-score-total').innerText = (overall * 100).toFixed(1) + '%';

        const statusCell = document.getElementById('slip-score-status');
        if (c.statusText === 'LLL') {{
          statusCell.innerHTML = '<span class="status-badge pass"><i class="fa-solid fa-circle-check"></i> LULUS RASMI</span>';
        }} else if (c.isAbsent) {{
          statusCell.innerHTML = '<span class="status-badge absent">TIDAK HADIR</span>';
        }} else if (c.isTarikDiri) {{
          statusCell.innerHTML = '<span class="status-badge withdraw">TARIK DIRI</span>';
        }} else if (overall >= 0.50) {{
          statusCell.innerHTML = '<span class="status-badge conditional">LULUS BERSYARAT</span>';
        }} else {{
          statusCell.innerHTML = '<span class="status-badge fail">GAGAL</span>';
        }}

        const modal = document.getElementById('modal-slip');
        if (modal) modal.classList.add('active');
      }},

      bindSlipModalEvents() {{
        const modal = document.getElementById('modal-slip');
        document.getElementById('btn-close-slip')?.addEventListener('click', () => {{
          modal?.classList.remove('active');
        }});
        document.getElementById('btn-cancel-slip')?.addEventListener('click', () => {{
          modal?.classList.remove('active');
        }});
        modal?.addEventListener('click', (e) => {{
          if (e.target === modal) modal.classList.remove('active');
        }});

        document.getElementById('btn-print-slip')?.addEventListener('click', () => {{
          window.print();
        }});
      }},

      initCharts() {{
        const ctx1 = document.getElementById('chartCategoryGender')?.getContext('2d');
        if (ctx1) {{
          this.state.charts.categoryGender = new Chart(ctx1, {{
            type: 'doughnut',
            data: {{
              labels: ['TKRS Lelaki', 'TKRS Perempuan', 'KRS Lelaki', 'KRS Perempuan'],
              datasets: [{{
                data: [90, 71, 90, 54],
                backgroundColor: ['#d97706', '#f59e0b', '#1e3a8a', '#3b82f6'],
                hoverOffset: 6,
                borderWidth: 3,
                borderColor: '#ffffff'
              }}]
            }},
            options: {{
              responsive: true,
              maintainAspectRatio: false,
              plugins: {{
                legend: {{ position: 'bottom', labels: {{ boxWidth: 14, font: {{ family: 'Plus Jakarta Sans', size: 12, weight: '600' }} }} }}
              }},
              cutout: '64%'
            }}
          }});
        }}

        const ctx2 = document.getElementById('chartModulePerformance')?.getContext('2d');
        if (ctx2) {{
          this.state.charts.modulePerf = new Chart(ctx2, {{
            type: 'bar',
            data: {{
              labels: ['Kawad Kaki (60%)', 'Bantu Mula (20%)', 'Ikatan (20%)', 'Keseluruhan'],
              datasets: [
                {{
                  label: 'TKRS (Sekolah Rendah)',
                  data: [0, 0, 0, 0],
                  backgroundColor: '#d97706',
                  borderRadius: 6
                }},
                {{
                  label: 'KRS (Sekolah Menengah)',
                  data: [0, 0, 0, 0],
                  backgroundColor: '#1e3a8a',
                  borderRadius: 6
                }}
              ]
            }},
            options: {{
              responsive: true,
              maintainAspectRatio: false,
              scales: {{
                y: {{
                  beginAtZero: true,
                  max: 100,
                  ticks: {{ callback: v => v + '%', font: {{ family: 'Plus Jakarta Sans', size: 12 }} }}
                }},
                x: {{
                  ticks: {{ font: {{ family: 'Plus Jakarta Sans', size: 12, weight: '600' }} }}
                }}
              }},
              plugins: {{
                legend: {{ position: 'bottom', labels: {{ boxWidth: 14, font: {{ family: 'Plus Jakarta Sans', size: 12, weight: '600' }} }} }}
              }}
            }}
          }});
        }}

        const ctx3 = document.getElementById('chartTopSchools')?.getContext('2d');
        if (ctx3) {{
          this.state.charts.topSchools = new Chart(ctx3, {{
            type: 'bar',
            data: {{
              labels: [],
              datasets: [{{
                label: 'Bilangan Calon',
                data: [],
                backgroundColor: '#2563eb',
                borderRadius: 5
              }}]
            }},
            options: {{
              indexAxis: 'y',
              responsive: true,
              maintainAspectRatio: false,
              scales: {{
                x: {{ beginAtZero: true, ticks: {{ stepSize: 1, font: {{ family: 'Plus Jakarta Sans', size: 12 }} }} }},
                y: {{ ticks: {{ font: {{ family: 'Plus Jakarta Sans', size: 11.5, weight: '600' }} }} }}
              }},
              plugins: {{
                legend: {{ display: false }}
              }}
            }}
          }});
        }}

        const ctx4 = document.getElementById('chartPassStatus')?.getContext('2d');
        if (ctx4) {{
          this.state.charts.passStatus = new Chart(ctx4, {{
            type: 'doughnut',
            data: {{
              labels: ['Lulus (LLL)', 'Lulus Bersyarat', 'Gagal', 'Belum Dinilai', 'Tidak Hadir / Tarik Diri'],
              datasets: [{{
                data: [0, 0, 0, 305, 0],
                backgroundColor: ['#059669', '#d97706', '#dc2626', '#94a3b8', '#64748b'],
                hoverOffset: 6,
                borderWidth: 3,
                borderColor: '#ffffff'
              }}]
            }},
            options: {{
              responsive: true,
              maintainAspectRatio: false,
              plugins: {{
                legend: {{ position: 'bottom', labels: {{ boxWidth: 14, font: {{ family: 'Plus Jakarta Sans', size: 12, weight: '600' }} }} }}
              }},
              cutout: '60%'
            }}
          }});
        }}

        this.updateCharts();
      }},

      updateCharts() {{
        if (!this.state.charts || !this.state.charts.categoryGender) return;

        let tkrsL = 0, tkrsP = 0, krsL = 0, krsP = 0;
        let sumK_TKRS = 0, sumBM_TKRS = 0, sumIK_TKRS = 0, sumTot_TKRS = 0, evalTKRS = 0;
        let sumK_KRS = 0, sumBM_KRS = 0, sumIK_KRS = 0, sumTot_KRS = 0, evalKRS = 0;
        let passLLL = 0, passCond = 0, failCount = 0, pendingCount = 0, absentOrWithdraw = 0;
        const schoolMap = {{}};

        this.state.candidates.forEach(c => {{
          const isTKRS = c.unit === 'TKRS';
          const isL = c.jantina === 'L';

          if (isTKRS) {{
            if (isL) tkrsL++; else tkrsP++;
          }} else {{
            if (isL) krsL++; else krsP++;
          }}

          if (c.sekolah) {{
            schoolMap[c.sekolah] = (schoolMap[c.sekolah] || 0) + 1;
          }}

          if (c.isAbsent || c.isTarikDiri || c.statusText === 'TH' || c.statusText === 'TARIK DIRI') {{
            absentOrWithdraw++;
            return;
          }}

          const rawK = parseFloat(c.rawKawad) || 0;
          const rawBM = parseFloat(c.rawBantuMula) || 0;
          const rawIK = parseFloat(c.rawIkatan) || 0;
          const rawTot = parseFloat(c.rawOverall) || 0;

          if (rawK > 0 || rawBM > 0 || rawIK > 0) {{
            if (isTKRS) {{
              evalTKRS++;
              sumK_TKRS += rawK; sumBM_TKRS += rawBM; sumIK_TKRS += rawIK; sumTot_TKRS += rawTot;
            }} else {{
              evalKRS++;
              sumK_KRS += rawK; sumBM_KRS += rawBM; sumIK_KRS += rawIK; sumTot_KRS += rawTot;
            }}

            if (c.statusText === 'LLL') passLLL++;
            else if (rawTot >= 0.50) passCond++;
            else failCount++;
          }} else {{
            pendingCount++;
          }}
        }});

        if (this.state.charts.categoryGender) {{
          this.state.charts.categoryGender.data.datasets[0].data = [tkrsL, tkrsP, krsL, krsP];
          this.state.charts.categoryGender.update();
        }}

        if (this.state.charts.modulePerf) {{
          const avgTKRS = [
            evalTKRS > 0 ? ((sumK_TKRS / evalTKRS) * 100).toFixed(1) : 0,
            evalTKRS > 0 ? ((sumBM_TKRS / evalTKRS) * 100).toFixed(1) : 0,
            evalTKRS > 0 ? ((sumIK_TKRS / evalTKRS) * 100).toFixed(1) : 0,
            evalTKRS > 0 ? ((sumTot_TKRS / evalTKRS) * 100).toFixed(1) : 0
          ];
          const avgKRS = [
            evalKRS > 0 ? ((sumK_KRS / evalKRS) * 100).toFixed(1) : 0,
            evalKRS > 0 ? ((sumBM_KRS / evalKRS) * 100).toFixed(1) : 0,
            evalKRS > 0 ? ((sumIK_KRS / evalKRS) * 100).toFixed(1) : 0,
            evalKRS > 0 ? ((sumTot_KRS / evalKRS) * 100).toFixed(1) : 0
          ];

          this.state.charts.modulePerf.data.datasets[0].data = avgTKRS;
          this.state.charts.modulePerf.data.datasets[1].data = avgKRS;
          this.state.charts.modulePerf.update();
        }}

        if (this.state.charts.topSchools) {{
          const sortedSchools = Object.keys(schoolMap)
            .map(k => ({{ name: k, count: schoolMap[k] }}))
            .sort((a, b) => b.count - a.count)
            .slice(0, 10);

          this.state.charts.topSchools.data.labels = sortedSchools.map(s => s.name);
          this.state.charts.topSchools.data.datasets[0].data = sortedSchools.map(s => s.count);
          this.state.charts.topSchools.update();
        }}

        if (this.state.charts.passStatus) {{
          this.state.charts.passStatus.data.datasets[0].data = [passLLL, passCond, failCount, pendingCount, absentOrWithdraw];
          this.state.charts.passStatus.update();
        }}
      }},

      bindFilterEvents() {{
        const searchInput = document.getElementById('input-candidate-search');
        const filterUnit = document.getElementById('select-unit');
        const filterKumpulan = document.getElementById('select-kumpulan');
        const filterJantina = document.getElementById('select-jantina');
        const filterStatus = document.getElementById('select-status');

        [searchInput, filterUnit, filterKumpulan, filterJantina, filterStatus].forEach(el => {{
          if (el) {{
            el.addEventListener('input', () => this.renderCandidatesTable());
            el.addEventListener('change', () => this.renderCandidatesTable());
          }}
        }});

        document.getElementById('btn-csv-export')?.addEventListener('click', () => {{
          this.exportToCSV();
        }});
      }},

      exportToCSV() {{
        let csv = "No Giliran,Nama Calon,Unit,Jantina,Kumpulan,Sekolah,Jumlah Markah,Status Keputusan\\n";
        this.state.candidates.forEach(c => {{
          csv += "\\"" + c.noGiliran + "\\",\\"" + c.nama + "\\",\\"" + c.unit + "\\",\\"" + c.jantina + "\\",\\"" + c.kumpulan + "\\",\\"" + c.sekolah + "\\",\\"" + c.overall + "\\",\\"" + c.statusText + "\\"\\n";
        }});
        
        const blob = new Blob([csv], {{ type: 'text/csv;charset=utf-8;' }});
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.setAttribute('href', url);
        link.setAttribute('download', `Analisis_Pentauliahan_KRS_TKRS_JB_2026_${{new Date().toISOString().slice(0,10)}}.csv`);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      }},

      populateCandidateDropdown(filterQuery = '') {{
        const select = document.getElementById('select-candidate-id');
        const countBadge = document.getElementById('manage-filter-count');
        if (!select) return;

        const q = (filterQuery || '').toLowerCase().trim();
        const currentVal = select.value;

        const filtered = this.state.candidates.filter(c => {{
          if (!q) return true;
          return (c.nama || '').toLowerCase().includes(q) ||
                 (c.sekolah || '').toLowerCase().includes(q) ||
                 (c.noGiliran || '').toLowerCase().includes(q);
        }});

        select.innerHTML = '<option value="">-- Pilih Calon (' + filtered.length + ' calon dijumpai) --</option>';
        
        filtered.forEach(c => {{
          const opt = document.createElement('option');
          opt.value = c.noGiliran;
          opt.textContent = `${{c.noGiliran}} • ${{c.nama}} (${{c.sekolah}})`;
          select.appendChild(opt);
        }});

        if (currentVal && filtered.some(c => c.noGiliran === currentVal)) {{
          select.value = currentVal;
        }}

        if (countBadge) {{
          countBadge.innerText = `Menjumpai ${{filtered.length}} daripada ${{this.state.candidates.length}} calon`;
        }}
      }},

      bindAdminEvents() {{
        const formAuth = document.getElementById('form-admin-auth');
        formAuth?.addEventListener('submit', async (e) => {{
          e.preventDefault();
          const pin = document.getElementById('input-admin-pin').value;
          const errAlert = document.getElementById('auth-error-alert');
          errAlert.style.display = 'none';

          try {{
            const res = await runBackendAction('verifyAdminPIN', {{ pin: pin }});
            if (res.success) {{
              this.state.isAdminLoggedIn = true;
              sessionStorage.setItem('pentauliahan_admin_auth', 'true');
              this.updateAuthVisuals();
            }} else {{
              errAlert.innerText = res.message || 'PIN Admin tidak sah. Sila cuba lagi.';
              errAlert.style.display = 'block';
            }}
          }} catch (err) {{
            if (pin === 'seketejb26') {{
              this.state.isAdminLoggedIn = true;
              sessionStorage.setItem('pentauliahan_admin_auth', 'true');
              this.updateAuthVisuals();
            }} else {{
              errAlert.innerText = 'PIN Admin tidak sah: ' + err.message;
              errAlert.style.display = 'block';
            }}
          }}
        }});

        document.getElementById('btn-logout')?.addEventListener('click', () => {{
          this.state.isAdminLoggedIn = false;
          sessionStorage.removeItem('pentauliahan_admin_auth');
          this.updateAuthVisuals();
        }});

        const sliderBindings = [
          {{ id: 'range-wajaran-kawad', textId: 'text-wajaran-kawad', key: 'wajaranKawad' }},
          {{ id: 'range-wajaran-bm', textId: 'text-wajaran-bm', key: 'wajaranBM' }},
          {{ id: 'range-wajaran-ikatan', textId: 'text-wajaran-ikatan', key: 'wajaranIkatan' }},
          {{ id: 'range-wajaran-min-kawad', textId: 'text-wajaran-min-kawad', key: 'kawad' }},
          {{ id: 'range-wajaran-min-ikatan', textId: 'text-wajaran-min-ikatan', key: 'ikatan' }},
          {{ id: 'range-wajaran-min-overall', textId: 'text-wajaran-min-overall', key: 'overall' }}
        ];

        sliderBindings.forEach(s => {{
          const rangeEl = document.getElementById(s.id);
          const textEl = document.getElementById(s.textId);
          rangeEl?.addEventListener('input', (e) => {{
            const val = parseFloat(e.target.value);
            textEl.innerText = val + '%';
            this.state.currentWajaran[s.key] = val / 100.0;
            
            const totalW = (this.state.currentWajaran.wajaranKawad + this.state.currentWajaran.wajaranBM + this.state.currentWajaran.wajaranIkatan) * 100;
            const badgeW = document.getElementById('badge-wajaran-total');
            if (badgeW) {{
              badgeW.innerText = `Jumlah Wajaran: ${{Math.round(totalW)}}%`;
              badgeW.className = Math.round(totalW) === 100 ? 'status-badge pass' : 'status-badge fail';
            }}

            this.recalculateAllStats();
            this.renderCandidatesTable();
          }});
        }});

        document.getElementById('btn-save-wajaran')?.addEventListener('click', () => {{
          this.saveWajaranToGoogleSheet();
        }});

        document.getElementById('btn-repair-formulas')?.addEventListener('click', () => {{
          this.repairVlookupFormulas();
        }});

        document.getElementById('btn-install-triggers')?.addEventListener('click', () => {{
          this.installTriggers();
        }});
      }},

      syncSliderInputs() {{
        const w = this.state.currentWajaran;
        if (document.getElementById('range-wajaran-kawad')) {{
          document.getElementById('range-wajaran-kawad').value = w.wajaranKawad * 100;
          document.getElementById('text-wajaran-kawad').innerText = (w.wajaranKawad * 100) + '%';
        }}
        if (document.getElementById('range-wajaran-bm')) {{
          document.getElementById('range-wajaran-bm').value = w.wajaranBM * 100;
          document.getElementById('text-wajaran-bm').innerText = (w.wajaranBM * 100) + '%';
        }}
        if (document.getElementById('range-wajaran-ikatan')) {{
          document.getElementById('range-wajaran-ikatan').value = w.wajaranIkatan * 100;
          document.getElementById('text-wajaran-ikatan').innerText = (w.wajaranIkatan * 100) + '%';
        }}
        if (document.getElementById('range-wajaran-min-kawad')) {{
          document.getElementById('range-wajaran-min-kawad').value = w.kawad * 100;
          document.getElementById('text-wajaran-min-kawad').innerText = (w.kawad * 100) + '%';
        }}
        if (document.getElementById('range-wajaran-min-ikatan')) {{
          document.getElementById('range-wajaran-min-ikatan').value = w.ikatan * 100;
          document.getElementById('text-wajaran-min-ikatan').innerText = (w.ikatan * 100) + '%';
        }}
        if (document.getElementById('range-wajaran-min-overall')) {{
          document.getElementById('range-wajaran-min-overall').value = w.overall * 100;
          document.getElementById('text-wajaran-min-overall').innerText = (w.overall * 100) + '%';
        }}
      }},

      async saveWajaranToGoogleSheet() {{
        const statusBox = document.getElementById('wajaran-action-status');
        statusBox.style.display = 'block';
        statusBox.style.background = '#eff6ff';
        statusBox.style.color = '#1e40af';
        statusBox.innerText = 'Sedang mengemas kini tetapan wajaran ke Google Sheet...';

        const config = {{
          wajaranMinKawad: this.state.currentWajaran.kawad,
          wajaranMinIkatan: this.state.currentWajaran.ikatan,
          wajaranMinOverall: this.state.currentWajaran.overall,
          wajaranKawad: this.state.currentWajaran.wajaranKawad,
          wajaranBantuMula: this.state.currentWajaran.wajaranBM,
          wajaranIkatan: this.state.currentWajaran.wajaranIkatan
        }};

        try {{
          const res = await runBackendAction('updatePassingWajaran', {{ config: config, pin: 'seketejb26' }});
          statusBox.style.background = '#dcfce7';
          statusBox.style.color = '#166534';
          statusBox.innerText = '✅ ' + (res.message || res);
        }} catch(err) {{
          statusBox.style.background = '#fee2e2';
          statusBox.style.color = '#991b1b';
          statusBox.innerText = '❌ Ralat: ' + err.message;
        }}
      }},

      async repairVlookupFormulas() {{
        const statusBox = document.getElementById('wajaran-action-status');
        statusBox.style.display = 'block';
        statusBox.style.background = '#eff6ff';
        statusBox.style.color = '#1e40af';
        statusBox.innerText = 'Sedang menyelaraskan formula VLOOKUP Google Sheet...';

        try {{
          const res = await runBackendAction('repairAllFormulasAndFormat');
          statusBox.style.background = '#dcfce7';
          statusBox.style.color = '#166534';
          statusBox.innerText = '✅ ' + (res.message || res);
        }} catch(err) {{
          statusBox.style.background = '#fee2e2';
          statusBox.style.color = '#991b1b';
          statusBox.innerText = '❌ Ralat: ' + err.message;
        }}
      }},

      async installTriggers() {{
        const statusBox = document.getElementById('wajaran-action-status');
        statusBox.style.display = 'block';
        statusBox.style.background = '#eff6ff';
        statusBox.style.color = '#1e40af';
        statusBox.innerText = 'Sedang memasang trigger automasi Google Sheet...';

        try {{
          const res = await runBackendAction('setupAutoSyncTriggers');
          statusBox.style.background = '#dcfce7';
          statusBox.style.color = '#166534';
          statusBox.innerText = '✅ ' + (res.message || res);
        }} catch(err) {{
          statusBox.style.background = '#fee2e2';
          statusBox.style.color = '#991b1b';
          statusBox.innerText = '❌ Ralat: ' + err.message;
        }}
      }},

      bindCandidateManageEvents() {{
        const form = document.getElementById('form-manage-candidate');
        const searchManage = document.getElementById('input-manage-search');
        const statusBox = document.getElementById('candidate-action-status');

        searchManage?.addEventListener('input', (e) => {{
          this.populateCandidateDropdown(e.target.value);
        }});

        form?.addEventListener('submit', async (e) => {{
          e.preventDefault();
          const noGiliran = document.getElementById('select-candidate-id').value;
          const statusType = document.getElementById('select-candidate-action').value;
          const newName = document.getElementById('input-candidate-newname').value;

          if (!noGiliran) {{
            alert('Sila pilih calon terlebih dahulu.');
            return;
          }}

          statusBox.style.display = 'block';
          statusBox.style.background = '#eff6ff';
          statusBox.style.color = '#1e40af';
          statusBox.innerText = `Sedang mengemas kini status calon ${{noGiliran}}...`;

          const payload = {{
            noGiliran: noGiliran,
            newStatus: statusType,
            newName: newName,
            catatan: statusType
          }};

          try {{
            const res = await runBackendAction('updateCandidateStatusRecord', {{ payload: payload, pin: 'seketejb26' }});
            statusBox.style.background = '#dcfce7';
            statusBox.style.color = '#166534';
            statusBox.innerText = '✅ ' + (res.message || res);
            
            const c = this.state.candidates.find(x => x.noGiliran === noGiliran);
            if (c) {{
              c.catatan = statusType;
              if (newName && statusType === 'TUKAR PESERTA') c.nama = newName;
              if (statusType === 'TIDAK HADIR') {{
                c.isAbsent = true;
                c.isTarikDiri = false;
                c.statusText = 'TH';
              }} else if (statusType === 'TARIK DIRI') {{
                c.isTarikDiri = true;
                c.isAbsent = false;
                c.statusText = 'TARIK DIRI';
              }} else {{
                c.isAbsent = false;
                c.isTarikDiri = false;
              }}
            }}
            this.recalculateAllStats();
            this.renderCandidatesTable();
          }} catch(err) {{
            statusBox.style.background = '#fee2e2';
            statusBox.style.color = '#991b1b';
            statusBox.innerText = '❌ Ralat: ' + err.message;
          }}
        }});
      }}
    }};

    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', () => App.init());
    }} else {{
      App.init();
    }}
  </script>
</body>
</html>
"""
    return html

# Write GAS Index.html
gas_html = build_html(is_gas=True)
with open('03_Google_Apps_Script/Index.html', 'w', encoding='utf-8') as f:
    f.write(gas_html)
print(f"✓ Saved 03_Google_Apps_Script/Index.html ({len(gas_html):,} bytes)")

# Write Netlify index.html
netlify_html = build_html(is_gas=False)
with open('04_Web_App_Netlify/index.html', 'w', encoding='utf-8') as f:
    f.write(netlify_html)
print(f"✓ Saved 04_Web_App_Netlify/index.html ({len(netlify_html):,} bytes)")
