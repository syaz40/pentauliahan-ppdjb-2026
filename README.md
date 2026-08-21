# Sistem Pengurusan & Dashboard Pentauliahan KRS / TKRS PPD Johor Bahru 2026

Projek ini mengandungi ekosistem penuh bagi Ujian Kenaikan Pangkat Sarjan KRS (Sekolah Menengah) dan Koperal TKRS (Sekolah Rendah) Daerah Johor Bahru yang berlangsung pada 22 Ogos 2026.

---

## 📂 Struktur Direktori Projek

```text
📁 APPSHEET PENTAULIAHAN/
│
├── 📄 README.md                                # Panduan direktori & ringkasan projek ini
├── 📄 .gitignore                               # Konfigurasi pengabaian Git
│
├── 📁 01_Dokumen_Kertas_Kerja/                 # Kertas kerja rasmi, instrumen ujian & imbasan scan
│   ├── 00_SEJARAH_PERBUALAN_LENGKAP_PROJECT.md # Rekod kronologi penuh perbualan & pembangunan projek
│   ├── kertas kerja sarjan koperal 2026.docx   # Kertas kerja asal program
│   ├── CamScanner 19-08-2026 10.20.pdf         # Instrumen & borang pemarkahan scan
│   └── camscanner_pages/                       # Imbasan visual setiap muka surat instrumen
│
├── 📁 02_Database_Excel/                       # Pangkalan data Excel backend & formula VLOOKUP
│   ├── PENTAULIAHAN_BACKEND_REVISED.xlsx       # Fail Excel master rasmi yang telah dibetulkan
│   ├── backend_pentauliahan.xlsx               # Fail Excel asal
│   └── live_google_sheet.xlsx                  # Salinan data Google Sheet live
│
├── 📁 03_Google_Apps_Script/                   # Kod aplikasi pengeluaran Google Apps Script (GAS)
│   ├── Code.gs                                 # Enjin backend Apps Script (doGet, API, Hydration)
│   ├── Index.html                              # Frontend Web App lengkap (Bootstrap, Chart.js, Modals)
│   ├── appsscript.json                         # Konfigurasi manifest GAS
│   └── .clasp.json                             # Tetapan clasp deploy
│
├── 📁 04_Web_App_Netlify/                      # Kod pengeluaran untuk hosting di Netlify
│   ├── index.html                              # Web app standalone sedia terbit
│   └── netlify.toml                            # Konfigurasi headers & keselamatan Netlify
│
├── 📁 05_Automasi_AppSheet/                    # Panduan automasi & integrasi borang AppSheet
│   └── Panduan_Automasi_AppSheet.md
│
├── 📁 06_Aset_Media_&_Rakaman/                 # Aset grafik, logo rasmi & video demo
│   ├── Logos/                                  # Logo PPD JB (Hitam/Putih) & Logo KRS
│   └── Rakaman_Video/                          # Video demonstrasi & rakaman sesi ujian sistem
│
└── 📁 07_Arkib_&_Skrip_Diagnostik/             # Arkib komprehensif skrip & fail sokongan
    ├── 01_Backup_GAS_Terdahulu/                # Salinan asal GAS sebelum pengoptimuman
    ├── 02_Kod_Sumber_Modular/                  # Arkib kod modular awal (HTML/JS/CSS berasingan)
    ├── 03_Data_Dump_JSON/                      # JSON dump statistik & fail kamus kata
    ├── 04_Skrip_Diagnostik_Excel/              # Skrip Python analisis formula & pengesahan VLOOKUP
    └── 05_Skrip_Migrasi_&_Pengekstrakan_Web/   # Skrip pemprosesan teks, pemisahan modul & ujian
```

---

## 🚀 Komponen Utama

1. **Google Apps Script Web App (`03_Google_Apps_Script/`)**
   - Berfungsi sebagai web app terus dari Google Drive / Sheet sekolah.
   - Mengandungi ciri Server Hydration, Live Google Sheet Sync, Carian Calon, Cetakan Slip Rasmi, 5 Terbaik & Simulator Ambang Kelulusan.

2. **Netlify Deployment (`04_Web_App_Netlify/`)**
   - Versi Web Dashboard berprestasi tinggi untuk capaian awam/pentadbir melalui URL Netlify tersendiri.

3. **Pangkalan Data Excel (`02_Database_Excel/`)**
   - Struktur jadual piawai mengikut skema markah 5 stesen pengujian (Kawad Kaki, Kawad Senjata/Bantu Mula, Ikatan & Tali Temali, Asas Kebombaan/Ujian Bertulis, Ketatanegaraan).
