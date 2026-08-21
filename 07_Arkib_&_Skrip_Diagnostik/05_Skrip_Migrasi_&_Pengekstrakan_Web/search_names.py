with open(r"i:\Other computers\My computer\Desktop\ANTIGRAVITY PROJECT\APPSHEET PENTAULIAHAN\00_SEJARAH_PERBUALAN_LENGKAP_PROJECT.md", "r", encoding="utf-8") as f:
    text = f.read()

for m in ['Dashboard.html', 'ModalAutomasi', 'ModalBaikiFormula', 'ModalKehadiran', 'ModalMengenai', 'ModalWajaran']:
    count = text.count(m)
    print(f"{m}: {count} occurrences")
