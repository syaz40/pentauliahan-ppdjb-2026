import os

def fix_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find exportToCSV() { ... const blob = new Blob
    idx1 = content.find('exportToCSV() {')
    idx2 = content.find('const blob = new Blob', idx1)
    if idx1 != -1 and idx2 != -1:
        new_block = (
            'exportToCSV() {\n'
            '        let csv = "No Giliran,Nama Calon,Unit,Jantina,Kumpulan,Sekolah,Jumlah Markah,Status Keputusan\\n";\n'
            '        this.state.candidates.forEach(c => {\n'
            '          csv += "\\"" + c.noGiliran + "\\",\\"" + c.nama + "\\",\\"" + c.unit + "\\",\\"" + c.jantina + "\\",\\"" + c.kumpulan + "\\",\\"" + c.sekolah + "\\",\\"" + c.overall + "\\",\\"" + c.statusText + "\\"\\n";\n'
            '        });\n        \n        '
        )
        content = content[:idx1] + new_block + content[idx2:]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully fixed exportToCSV in {file_path}")
    else:
        print(f"Could not find indices in {file_path}")

fix_csv('03_Google_Apps_Script/Index.html')
fix_csv('04_Web_App_Netlify/index.html')
