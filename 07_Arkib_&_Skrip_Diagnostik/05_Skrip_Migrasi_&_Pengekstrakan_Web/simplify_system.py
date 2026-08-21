import os
import re

gas_dir = r"i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\03_Google_Apps_Script"
arkib_dir = r"i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\06_Arkib_Fail"

# 1. Move Modals.html to 06_Arkib_Fail
modals_path = os.path.join(gas_dir, "Modals.html")
if os.path.exists(modals_path):
    dest = os.path.join(arkib_dir, "Modals.html")
    if os.path.exists(dest):
        os.remove(dest)
    os.rename(modals_path, dest)
    print("Moved Modals.html to 06_Arkib_Fail!")

# 2. Update .claspignore to only include Code.gs, Index.html, appsscript.json
claspignore_path = os.path.join(gas_dir, ".claspignore")
with open(claspignore_path, "w", encoding="utf-8") as f:
    f.write("**/**\n!Code.gs\n!Index.html\n!appsscript.json\n")
print("Updated .claspignore!")

# 3. Update Code.gs to simplify and remove any HtmlService modals, replacing with native Sheet UI alerts/toasts
code_path = os.path.join(gas_dir, "Code.gs")
with open(code_path, "r", encoding="utf-8") as f:
    code = f.read()

# Replace modal callers with clean native sheet actions & alerts
new_menu_actions = """/* =========================================================================
   PENGURUSAN MENU TERSUAI GOOGLE SHEET (NATIVE, PANTAS & RINGAN)
   ========================================================================= */

function openWebAppDirectly() {
  var url = ScriptApp.getService().getUrl() || "https://script.google.com/macros/s/AKfycbwKhf-gMkAcDewG5MujfTWJPZWZ9Kf4AuacLlNbU4ghT6qnErd4wFFPNIa804HVlarJ/exec";
  var html = HtmlService.createHtmlOutput(
    '<div style="font-family:Plus Jakarta Sans, sans-serif; padding:20px; text-align:center;">' +
    '<h3 style="color:#1e3a8a; margin-bottom:10px;">🌐 Pusat Kawalan & Web App Rasmi</h3>' +
    '<p style="color:#64748b; font-size:13px; margin-bottom:20px;">Klik butang di bawah untuk membuka Web App Dashboard Eksekutif:</p>' +
    '<a href="' + url + '" target="_blank" style="display:inline-block; background:#1e3a8a; color:white; padding:12px 24px; border-radius:8px; text-decoration:none; font-weight:700; font-size:14px;">🚀 Buka Web App Rasmi</a>' +
    '</div>'
  ).setWidth(450).setHeight(200);
  SpreadsheetApp.getUi().showModalDialog(html, '🌐 Web App Pentauliahan 2026');
}

function showMengenaiAlert() {
  var ui = SpreadsheetApp.getUi();
  ui.alert(
    '🏛️ SISTEM PENGURUSAN PENTAULIAHAN KRS & TKRS PPDJB 2026',
    'Versi: 2.0 (Eksekutif Cloud Enterprise)\\n' +
    'Skema: Ujian Kenaikan Pangkat Sarjan KRS & Koperal TKRS\\n' +
    'Penyelarasan: 305 Calon (144 KRS • 161 TKRS) dari 60 Buah Sekolah\\n' +
    'PPD Johor Bahru • Hak Cipta Terpelihara 2026',
    ui.ButtonSet.OK
  );
}

function runRepairFromMenu() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  ss.toast('Sedang membaiki semua formula VLOOKUP & analisis markah...', '⚡ Diagnosis VLOOKUP', 5);
  var res = repairAllFormulasAndFormat();
  SpreadsheetApp.getUi().alert('⚡ Keputusan Baiki Formula', res.message, SpreadsheetApp.getUi().ButtonSet.OK);
}

function runSyncFromMenu() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  ss.toast('Sedang menyegerakkan markah penguji...', '🔄 Segerak Markah', 5);
  var res = syncAllExaminerScores();
  SpreadsheetApp.getUi().alert('🔄 Status Penyegerakan', res.message, SpreadsheetApp.getUi().ButtonSet.OK);
}

function runTriggerFromMenu() {
  var res = setupAutoSyncTriggers();
  SpreadsheetApp.getUi().alert('🤖 Automasi Trigger', res.message, SpreadsheetApp.getUi().ButtonSet.OK);
}
"""

# Update onOpen menu to point to new native actions
old_onopen_regex = r'function onOpen\(\)\s*\{.*?\.addToUi\(\);?\s*\}'
new_onopen = """function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('🏛️ PENTAULIAHAN 2026')
    .addItem('🌐 Buka Web App Dashboard Rasmi', 'openWebAppDirectly')
    .addSeparator()
    .addItem('⚡ Baiki Semua Formula VLOOKUP & Markah', 'runRepairFromMenu')
    .addItem('🔄 Segerakkan Markah Penguji Masa Nyata', 'runSyncFromMenu')
    .addItem('🤖 Pasang Automasi Trigger (Auto-Sync)', 'runTriggerFromMenu')
    .addSeparator()
    .addItem('ℹ️ Mengenai Sistem & Skema PPDJB', 'showMengenaiAlert')
    .addToUi();
}"""

code = re.sub(old_onopen_regex, new_onopen, code, flags=re.DOTALL)

# Replace the old modal block in Code.gs
old_modal_regex = r'/\* =+ \s* PENGURUSAN FLOATING WINDOW MODAL.*?(?=/\* =+\s* ENJIN DATA)'
code = re.sub(old_modal_regex, new_menu_actions + "\n", code, flags=re.DOTALL)

with open(code_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated Code.gs with simplified native Sheet menu actions!")
