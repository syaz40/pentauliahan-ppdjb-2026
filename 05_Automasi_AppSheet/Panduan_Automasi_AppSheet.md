# PANDUAN AUTOMATIK APPSHEET & GOOGLE APPS SCRIPT
## SISTEM PENTAULIAHAN KRS & TKRS DAERAH JOHOR BAHRU 2026

---

## 🤖 1. AUTOMASI VIRTUAL COLUMNS (PENGIRAAN PANTAS DALAM APPSHEET)

Untuk mengelakkan kelewatan (*lag*) formula Google Sheet di padang, masukkan Virtual Columns ini dalam jadual `ANALISIS_TKRS` dan `ANALISIS_KRS` di AppSheet:

### A. Virtual Columns Jadual `ANALISIS_TKRS`:
1. **`[v_Markah_Kawad]`** (Type: Decimal)
   ```appsheet
   LOOKUP([_THISROW].[ID_PESERTA], "MARKAH_TKRS_KAWAD", "ID_PESERTA", "MARKAH KAWAD")
   ```
2. **`[v_Markah_Bantu_Mula]`** (Type: Decimal)
   ```appsheet
   LOOKUP([_THISROW].[ID_PESERTA], "MARKAH_TKRS_BANTU_MULA", "ID_PESERTA", "MARKAHBANTUMULA10")
   ```
3. **`[v_Markah_Ikatan]`** (Type: Decimal)
   ```appsheet
   LOOKUP([_THISROW].[ID_PESERTA], "MARKAH_TKRS_IKATAN", "ID_PESERTA", "MARKAHIKATAN10")
   ```
4. **`[v_Peratus_Keseluruhan]`** (Type: Percent)
   ```appsheet
   (([v_Markah_Kawad] / 95) * 0.6) + (([v_Markah_Bantu_Mula] / 20) * 0.2) + (([v_Markah_Ikatan] / 25) * 0.2)
   ```
5. **`[v_Status_Kelulusan]`** (Type: Enum / Text)
   ```appsheet
   IFS(
     AND(([v_Markah_Kawad] / 95) >= 0.5, ((([v_Markah_Bantu_Mula] / 20) + ([v_Markah_Ikatan] / 25)) / 2) >= 0.5, [v_Peratus_Keseluruhan] >= 0.6), "LULUS PENTAULIAHAN KOPERAL",
     TRUE, "GAGAL / BELUM LENGKAP"
   )
   ```

---

### B. Virtual Columns Jadual `ANALISIS_KRS`:
1. **`[v_Markah_Kawad]`** (Type: Decimal)
   ```appsheet
   LOOKUP([_THISROW].[ID_PESERTA], "MARKAH_KRS_KAWAD", "ID_PESERTA", "MARKAH KAWAD")
   ```
2. **`[v_Markah_Bantu_Mula]`** (Type: Decimal)
   ```appsheet
   LOOKUP([_THISROW].[ID_PESERTA], "MARKAH_KRS_BANTU_MULA", "ID_PESERTA", "MARKAHBANTUMULA10")
   ```
3. **`[v_Markah_Ikatan]`** (Type: Decimal)
   ```appsheet
   LOOKUP([_THISROW].[ID_PESERTA], "MARKAH_KRS_IKATAN", "ID_PESERTA", "MARKAHIKATAN10")
   ```
4. **`[v_Peratus_Keseluruhan]`** (Type: Percent)
   ```appsheet
   (([v_Markah_Kawad] / 137) * 0.6) + (([v_Markah_Bantu_Mula] / 20) * 0.2) + (([v_Markah_Ikatan] / 25) * 0.2)
   ```
5. **`[v_Status_Kelulusan]`** (Type: Enum / Text)
   ```appsheet
   IFS(
     AND(([v_Markah_Kawad] / 137) >= 0.5, ((([v_Markah_Bantu_Mula] / 20) + ([v_Markah_Ikatan] / 25)) / 2) >= 0.5, [v_Peratus_Keseluruhan] >= 0.6), "LULUS PENTAULIAHAN SARJAN",
     TRUE, "GAGAL / BELUM LENGKAP"
   )
   ```

---

## ⚡ 2. AUTOMASI BOT (APPSHEET AUTOMATION)

### Bot 1: Notifikasi Pengesahan Selesai Ujian
* **Event:** Data Change $\rightarrow$ Adds & Updates pada jadual `MARKAH_TKRS_KAWAD` / `MARKAH_KRS_KAWAD`.
* **Action:** Send a notification / Send an email kepada Ketua Hakim Kawad & Urus Setia.

### Bot 2: Penjanaan Slip Keputusan / Sijil PDF Automatik
* **Event:** Bila `[v_Status_Kelulusan]` bertukar kepada `"LULUS PENTAULIAHAN..."`
* **Task:** Create a new file (PDF Document) menggunakan template Sijil Pentauliahan Daerah Johor Bahru 2026.
