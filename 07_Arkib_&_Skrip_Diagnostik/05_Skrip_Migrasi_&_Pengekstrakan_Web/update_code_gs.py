with open(r"i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\03_Google_Apps_Script\Code.gs", "r", encoding="utf-8") as f:
    code = f.read()

# Update doGet
old_doget = """function doGet(e) {
  if (e && e.parameter && e.parameter.format === 'json') {
    var data = getDashboardData();
    return ContentService.createTextOutput(JSON.stringify(data))
      .setMimeType(ContentService.MimeType.JSON);
  }
  
  var template = HtmlService.createTemplateFromFile('Index');
  template.page = 'WebDashboard';
  return template.evaluate()
    .setTitle('Dashboard Pentauliahan Pangkat & Analisis Keputusan — PPD Johor Bahru 2026')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}"""

new_doget = """function doGet(e) {
  if (e && e.parameter && e.parameter.format === 'json') {
    var data = getDashboardData();
    return ContentService.createTextOutput(JSON.stringify(data))
      .setMimeType(ContentService.MimeType.JSON);
  }
  
  return HtmlService.createHtmlOutputFromFile('Index')
    .setTitle('Dashboard Pentauliahan Pangkat & Analisis Keputusan — PPD Johor Bahru 2026')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}"""

# Update modal references from 'Index' to 'Modals'
import re
code = code.replace(old_doget, new_doget)
code = re.sub(r"var template = HtmlService\.createTemplateFromFile\('Index'\);(\s*template\.page = '(?:Dashboard|ModalKehadiran|ModalWajaran|ModalBaikiFormula|ModalAutomasi|ModalMengenai)';)",
              r"var template = HtmlService.createTemplateFromFile('Modals');\1",
              code)

with open(r"i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\03_Google_Apps_Script\Code.gs", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated Code.gs successfully!")
