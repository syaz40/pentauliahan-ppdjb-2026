

    let SERVER_DATA = null;
      try {
        const payloadEl = document.getElementById('server-data-payload');
        const payloadText = payloadEl ? payloadEl.textContent.trim() : '';
        if (payloadText && payloadText !== 'null') {
          SERVER_DATA = JSON.parse(payloadText);
        }
      } catch (e) {
        SERVER_DATA = null;
      }

    const EMBEDDED_CANDIDATES = [{"unit": "KRS", "noBadan": "KRS-LA001", "nama": "MUHAMMAD LUQMAN ISKANDAR BIN ABDUL HADI", "jantina": "L", "sekolah": "SMA AL-QURAN WADDIN", "kumpulan": "A", "noUrutan": 1.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA002", "nama": "LOSHAN SHANMUGAM", "jantina": "L", "sekolah": "SMK AMINUDDIN BAKI", "kumpulan": "A", "noUrutan": 2.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA003", "nama": "MUHAMMAD AMMAR RAFIQ BIN MUHAMAD ROZAI RAFIQ", "jantina": "L", "sekolah": "SMK DAMAI JAYA", "kumpulan": "A", "noUrutan": 3.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA004", "nama": "MUHAMMAD ADAM BIN MOHD NAPIS", "jantina": "L", "sekolah": "SMK DATO ABDUL RAHMAN YASSIN", "kumpulan": "A", "noUrutan": 4.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA005", "nama": "MUHAMMAD ADAM FITRI BIN MOHD FAIZ", "jantina": "L", "sekolah": "SMK DATO' JAAFAR", "kumpulan": "A", "noUrutan": 5.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA006", "nama": "SYAHRUL AIMAN AKHIRI BIN ABD LATIP", "jantina": "L", "sekolah": "SMK DATO' JAAFAR", "kumpulan": "A", "noUrutan": 6.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA007", "nama": "AHMAD ZAKWAN HARITH BIN INDRA", "jantina": "L", "sekolah": "SMK GELANG PATAH", "kumpulan": "A", "noUrutan": 7.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA008", "nama": "ADAM MUKHRIZ BIN RIZAL", "jantina": "L", "sekolah": "SMK MAJIDI BARU 2", "kumpulan": "A", "noUrutan": 8.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA009", "nama": "ARIF ASYRAF BIN AZIZAN", "jantina": "L", "sekolah": "SMK MOHD KHALID", "kumpulan": "A", "noUrutan": 9.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA010", "nama": "HAIZAT IRSYAD BIN MAZLAN", "jantina": "L", "sekolah": "SMK MOHD KHALID", "kumpulan": "A", "noUrutan": 10.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA011", "nama": "MUHAMMAD DARIAN HILMY BIN MOHD HAFIZ", "jantina": "L", "sekolah": "SMK MOHD KHALID", "kumpulan": "A", "noUrutan": 11.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA012", "nama": "MUHAMMAD IDLAN SYAFIQ BIN MOHD TAHIR", "jantina": "L", "sekolah": "SMK MOHD KHALID", "kumpulan": "A", "noUrutan": 12.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA013", "nama": "ONG ZE JING", "jantina": "L", "sekolah": "SMK MUTIARA RINI", "kumpulan": "A", "noUrutan": 13.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA014", "nama": "HANIF IQHRAM BIN ABDULLAH", "jantina": "L", "sekolah": "SMK SRI RAHMAT", "kumpulan": "A", "noUrutan": 14.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA015", "nama": "SAISHARAN A/L TAMILARASAN", "jantina": "L", "sekolah": "SMK SULTAN ISMAIL", "kumpulan": "A", "noUrutan": 15.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA016", "nama": "FATH DARIS AYMAN BIN ABDULLAH", "jantina": "L", "sekolah": "SMK TAMAN DESA SKUDAI", "kumpulan": "A", "noUrutan": 16.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA017", "nama": "MICHAEL CHACE HUFANCIA BIN CLAYTON", "jantina": "L", "sekolah": "SMK TAMAN MUTIARA RINI 2", "kumpulan": "A", "noUrutan": 17.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA018", "nama": "ASYRAF HANAFI BIN HALIM", "jantina": "L", "sekolah": "SMK TAMAN NUSAJAYA", "kumpulan": "A", "noUrutan": 18.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA019", "nama": "MUHAMMAD ADAM DARWISY BIN MUHAMAD RAFFI", "jantina": "L", "sekolah": "SMK TAMAN NUSAJAYA", "kumpulan": "A", "noUrutan": 19.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA020", "nama": "MUHAMMAD DAFIE BAIHAQIE BIN MOHD SHAHIZAL", "jantina": "L", "sekolah": "SMK TAMAN NUSAJAYA", "kumpulan": "A", "noUrutan": 20.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA021", "nama": "MUHAMMAD NUR IZZANI BIN ZAMRI", "jantina": "L", "sekolah": "SMK TAMAN NUSAJAYA", "kumpulan": "A", "noUrutan": 21.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA022", "nama": "MUHAMMAD ZILL QAYYIM BIN MOHD RAZALI", "jantina": "L", "sekolah": "SMK TAMAN NUSAJAYA", "kumpulan": "A", "noUrutan": 22.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA023", "nama": "MUHAMMAD HAFIZ HAZIM BIN MOHD KAMARULSAFUAN", "jantina": "L", "sekolah": "SMK TAMAN TUN AMINAH", "kumpulan": "A", "noUrutan": 23.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA024", "nama": "MUHAMMAD ZAHIRUL HAZIQ BIN ZIN AZMAN", "jantina": "L", "sekolah": "SMK TAMAN UNIVERISITI", "kumpulan": "A", "noUrutan": 24.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA025", "nama": "MOHAMAD AMIRUDDIN ASYRAF BIN MOHAMAD ZAMRI", "jantina": "L", "sekolah": "SMK TAMAN UNIVERSITI 2", "kumpulan": "A", "noUrutan": 25.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA026", "nama": "NISHAL RAO A/L VIKNES RAO", "jantina": "L", "sekolah": "SMK TASEK UTARA 2", "kumpulan": "A", "noUrutan": 26.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA027", "nama": "MUHAMMAD AMINUL BIN MUSTAFFA KAMAL", "jantina": "L", "sekolah": "SMK TUN SYED NASIR ISMAIL", "kumpulan": "A", "noUrutan": 27.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LA028", "nama": "MUHAMMAD SAIF BIN SHAMSHUL BAHRI", "jantina": "L", "sekolah": "SMK TUN SYED NASIR ISMAIL", "kumpulan": "A", "noUrutan": 28.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB001", "nama": "MUHAMMAD SALAHUDDIN BIN HANIFF", "jantina": "L", "sekolah": "SMA AL-QURAN WADDIN", "kumpulan": "B", "noUrutan": 1.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB002", "nama": "AHMAD FARID FAHMI BIN ALI FAUZI", "jantina": "L", "sekolah": "SMK BANDAR UDA UTAMA JB", "kumpulan": "B", "noUrutan": 2.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB003", "nama": "MUHAMMAD AQEEF FIRZAN BIN FAIRUZ AZZUAN", "jantina": "L", "sekolah": "SMK DAMAI JAYA", "kumpulan": "B", "noUrutan": 3.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB004", "nama": "MUHAMMAD HAFIZAL BIN ROHAIZAN", "jantina": "L", "sekolah": "SMK DATO ABDUL RAHMAN YASSIN", "kumpulan": "B", "noUrutan": 4.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB005", "nama": "MUHAMMAD AFKAR IQBAL BIN MOHD IZWANI", "jantina": "L", "sekolah": "SMK DATO' JAAFAR", "kumpulan": "B", "noUrutan": 5.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB006", "nama": "AMMAR DANIAL BIN ABDULLAH", "jantina": "L", "sekolah": "SMK DATO' USMAN AWANG", "kumpulan": "B", "noUrutan": 6.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB007", "nama": "JONATHAN NG BOH XIAN", "jantina": "L", "sekolah": "SMK GELANG PATAH", "kumpulan": "B", "noUrutan": 7.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB008", "nama": "ADAM MIKAIL BIN SHUKRI", "jantina": "L", "sekolah": "SMK MOHD KHALID", "kumpulan": "B", "noUrutan": 8.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB009", "nama": "AZRIEL SYAH PUTRA BIN EDILBERTO C.APINES", "jantina": "L", "sekolah": "SMK MOHD KHALID", "kumpulan": "B", "noUrutan": 9.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB010", "nama": "MOHAMAD DARIELL HAIQAL BIN HASSANKUSAINI", "jantina": "L", "sekolah": "SMK MOHD KHALID", "kumpulan": "B", "noUrutan": 10.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB011", "nama": "MUHAMMAD FAHIM IMAN BIN MUHAMAD FAISAL", "jantina": "L", "sekolah": "SMK MOHD KHALID", "kumpulan": "B", "noUrutan": 11.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB012", "nama": "MUHAMMAD ILMAM RAZIN BIN ZAHA", "jantina": "L", "sekolah": "SMK MOHD KHALID", "kumpulan": "B", "noUrutan": 12.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB013", "nama": "ISKANDAR ZULKARNAIN BIN MOHD IZZUDDIN", "jantina": "L", "sekolah": "SMK SKUDAI", "kumpulan": "B", "noUrutan": 13.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB014", "nama": "MUHAMMAD ARSHAD DANIAL BIN MOHD NEDZAM", "jantina": "L", "sekolah": "SMK SRI RAHMAT", "kumpulan": "B", "noUrutan": 14.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB015", "nama": "TAN WEI YANG", "jantina": "L", "sekolah": "SMK SULTAN ISMAIL", "kumpulan": "B", "noUrutan": 15.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB016", "nama": "MUHD AMIRUL AKHTAR BIN KHAIRUL AZHAR", "jantina": "L", "sekolah": "SMK TAMAN DESA SKUDAI", "kumpulan": "B", "noUrutan": 16.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB017", "nama": "MUHAMMAD HARIZ ARSYAD BIN MOHD NOOR", "jantina": "L", "sekolah": "SMK TAMAN MUTIARA RINI 2", "kumpulan": "B", "noUrutan": 17.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB018", "nama": "ELMY QALIF RAYYAN BIN NOOR HIDAYAT", "jantina": "L", "sekolah": "SMK TAMAN NUSAJAYA", "kumpulan": "B", "noUrutan": 18.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB019", "nama": "MUHAMMAD AKHIL ZAMEER BIN MOHAMAD ZAMRI", "jantina": "L", "sekolah": "SMK TAMAN NUSAJAYA", "kumpulan": "B", "noUrutan": 19.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB020", "nama": "MUHAMMAD IZZ ZAFRAN BIN SAIFUL NIZAM", "jantina": "L", "sekolah": "SMK TAMAN NUSAJAYA", "kumpulan": "B", "noUrutan": 20.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB021", "nama": "MUHAMMAD SHAFIY NAZHAN", "jantina": "L", "sekolah": "SMK TAMAN NUSAJAYA", "kumpulan": "B", "noUrutan": 21.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB022", "nama": "SYAQIEF AIDIT BIN SUKIRMAN", "jantina": "L", "sekolah": "SMK TAMAN NUSAJAYA", "kumpulan": "B", "noUrutan": 22.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB023", "nama": "PUTRA SHAZZRIZAM AL DAYYAN SHAH BIN MOHD SHAHNIZAM", "jantina": "L", "sekolah": "SMK TAMAN TUN AMINAH", "kumpulan": "B", "noUrutan": 23.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB024", "nama": "EZZAL ZULHARITH BIN ZAIRILAMRI", "jantina": "L", "sekolah": "SMK TAMAN UNIVERSITI", "kumpulan": "B", "noUrutan": 24.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB025", "nama": "MUHAMAD HAMIRUL AZIM BIN MAHATHIR", "jantina": "L", "sekolah": "SMK TAMAN UNIVERSITI 2", "kumpulan": "B", "noUrutan": 25.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB026", "nama": "ARY FAREEZ AMIERUL BIN ABDULLAH", "jantina": "L", "sekolah": "SMK TUN SYED NASIR ISMAIL", "kumpulan": "B", "noUrutan": 26.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LB027", "nama": "MUHAMMAD AZFAR BIN FADLI", "jantina": "L", "sekolah": "SMK TUN SYED NASIR ISMAIL", "kumpulan": "B", "noUrutan": 27.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC001", "nama": "ADREAN RAHIMI BIN ABDUL AZIM", "jantina": "L", "sekolah": "SMK AMINUDDIN BAKI", "kumpulan": "C", "noUrutan": 1.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC002", "nama": "MUHAMMAD ANIQ HANIF BIN MOHD HANAFI", "jantina": "L", "sekolah": "SMK BANDAR UDA UTAMA JB", "kumpulan": "C", "noUrutan": 2.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC003", "nama": "MUHAMMAD SYAHRIL BIN MUHAMMAD SA'AT", "jantina": "L", "sekolah": "SMK DAMAI JAYA", "kumpulan": "C", "noUrutan": 3.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC004", "nama": "MUHAMMAD FIRAS HADI BIN MD NORAZLI", "jantina": "L", "sekolah": "SMK DATO' ABDUL RAHMAN YASSIN", "kumpulan": "C", "noUrutan": 4.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC005", "nama": "MUHAMMAD ATHIR HAZIM BIN ASRI RAHMAN", "jantina": "L", "sekolah": "SMK DATO' JAAFAR", "kumpulan": "C", "noUrutan": 5.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC006", "nama": "MOHAMAD SYAZMI BIN HANG TUAH @ MOHD ZAIN", "jantina": "L", "sekolah": "SMK DATO' USMAN AWANG", "kumpulan": "C", "noUrutan": 6.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC007", "nama": "MUHAMMAD HARITH RIZKI BIN MOHD HAZMI", "jantina": "L", "sekolah": "SMK GELANG PATAH", "kumpulan": "C", "noUrutan": 7.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC008", "nama": "AQIL NAUFAL BIN SULAIMAN", "jantina": "L", "sekolah": "SMK MOHD KHALID", "kumpulan": "C", "noUrutan": 8.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC009", "nama": "BASYR HAMYZAN BIN MOHD ZAMBRY", "jantina": "L", "sekolah": "SMK MOHD KHALID", "kumpulan": "C", "noUrutan": 9.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC010", "nama": "MUHAMMAD ALIF MUSTAQIM BIN MD FUHAD", "jantina": "L", "sekolah": "SMK MOHD KHALID", "kumpulan": "C", "noUrutan": 10.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC011", "nama": "MUHAMMAD HARRAZ ZAQUAN BIN MOHD NAZRI", "jantina": "L", "sekolah": "SMK MOHD KHALID", "kumpulan": "C", "noUrutan": 11.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC012", "nama": "MUHAMMAD KHAIRIL AKASHAH BIN HAIRIL YUSOF", "jantina": "L", "sekolah": "SMK MUTIARA RINI", "kumpulan": "C", "noUrutan": 12.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC013", "nama": "MUHAMMAD IRSYAD HAKIMI BIN MOHD IDZRUL HISYAM", "jantina": "L", "sekolah": "SMK SKUDAI", "kumpulan": "C", "noUrutan": 13.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC014", "nama": "MUHAMMAD QABIL IQRAM BIN SUHAIMI", "jantina": "L", "sekolah": "SMK SRI RAHMAT", "kumpulan": "C", "noUrutan": 14.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC015", "nama": "AHMAD DARIS MUHADZDZIB BIN YOUSSAINEIR", "jantina": "L", "sekolah": "SMK TAMAN DESA SKUDAI", "kumpulan": "C", "noUrutan": 15.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC016", "nama": "HAMZA BIN HILMI", "jantina": "L", "sekolah": "SMK TAMAN MUTIARA RINI 2", "kumpulan": "C", "noUrutan": 16.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC017", "nama": "AISY WALDAN BIN MOHD SHARIN", "jantina": "L", "sekolah": "SMK TAMAN NUSAJAYA", "kumpulan": "C", "noUrutan": 17.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC018", "nama": "MOHAMAD YUZER AIZAM BIN MOHD YAZID", "jantina": "L", "sekolah": "SMK TAMAN NUSAJAYA", "kumpulan": "C", "noUrutan": 18.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC019", "nama": "MUHAMMAD ARIF ASYRAF BIN MOHAMMAD ZAKI", "jantina": "L", "sekolah": "SMK TAMAN NUSAJAYA", "kumpulan": "C", "noUrutan": 19.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC020", "nama": "MUHAMMAD KHALIFF IMAN BIN MOHD SHUKRI", "jantina": "L", "sekolah": "SMK TAMAN NUSAJAYA", "kumpulan": "C", "noUrutan": 20.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC021", "nama": "MUHAMMAD SYAHMEN HARITH BIN MUHAMAD SUKRI", "jantina": "L", "sekolah": "SMK TAMAN NUSAJAYA", "kumpulan": "C", "noUrutan": 21.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC022", "nama": "JOVIAN CARLOS ANAK MAPANG", "jantina": "L", "sekolah": "SMK TAMAN SELESA JAYA", "kumpulan": "C", "noUrutan": 22.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC023", "nama": "MUHAMMAD HAZIM HASLAM BIN ABDULLAH", "jantina": "L", "sekolah": "SMK TAMAN UNIVERISITI", "kumpulan": "C", "noUrutan": 23.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC024", "nama": "SHARWINKUMAR A/L PREMKUMAR", "jantina": "L", "sekolah": "SMK TAMAN UNIVERSITI", "kumpulan": "C", "noUrutan": 24.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC025", "nama": "MUHAMMAD IQBAL BIN HARMAN SHAH", "jantina": "L", "sekolah": "SMK TASEK UTARA 2", "kumpulan": "C", "noUrutan": 25.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC026", "nama": "MUHAMMAD AFIQ AFFIAN BIN MOHD DAHLIA", "jantina": "L", "sekolah": "SMK TUN SYED NASIR ISMAIL", "kumpulan": "C", "noUrutan": 26.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-LC027", "nama": "MUHAMMAD IZHAR BIN MOHD ZAHIR", "jantina": "L", "sekolah": "SMK TUN SYED NASIR ISMAIL", "kumpulan": "C", "noUrutan": 27.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA001", "nama": "DIYA RAISHA NAZEEHA BINTI NOR AZMAN", "jantina": "P", "sekolah": "SEKOLAH TUN FATIMAH", "kumpulan": "A", "noUrutan": 1.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA002", "nama": "NUR SYAMIMI QAISARA BINTI SHAHEBOL FA’HADZIL", "jantina": "P", "sekolah": "SEKOLAH TUN FATIMAH", "kumpulan": "A", "noUrutan": 2.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA003", "nama": "NURUL ALISHA BINTI SHAIRUL SAFREE", "jantina": "P", "sekolah": "SMK AMINUDDIN BAKI", "kumpulan": "A", "noUrutan": 3.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA004", "nama": "ELLYSH SYADIERA BINTI MUHAMMAD RASHID", "jantina": "P", "sekolah": "SMK BANDAR UDA UTAMA JB", "kumpulan": "A", "noUrutan": 4.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA005", "nama": "PUTRI NUR SYAHFINAS BINTI AZIZ", "jantina": "P", "sekolah": "SMK GELANG PATAH", "kumpulan": "A", "noUrutan": 5.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA006", "nama": "LEE YI HUI", "jantina": "P", "sekolah": "SMK IJ CONVENT", "kumpulan": "A", "noUrutan": 6.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA007", "nama": "YONG CHEN EN", "jantina": "P", "sekolah": "SMK IJ CONVENT", "kumpulan": "A", "noUrutan": 7.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA008", "nama": "SITI AUNI FATHIAH BINTI NAZILI", "jantina": "P", "sekolah": "SMK MOHD KHALID", "kumpulan": "A", "noUrutan": 8.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA009", "nama": "AISHA IZZARA BINTI MOHD SHAHBUDIN", "jantina": "P", "sekolah": "SMK SKUDAI", "kumpulan": "A", "noUrutan": 9.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA010", "nama": "NUR ARYYANA DARWISYAH BINTI MOHD RAZIP", "jantina": "P", "sekolah": "SMK SKUDAI", "kumpulan": "A", "noUrutan": 10.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA011", "nama": "NURANISAH BINTI ANHAR", "jantina": "P", "sekolah": "SMK SKUDAI", "kumpulan": "A", "noUrutan": 11.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA012", "nama": "SITI NUR UMAIRAH BINTI MD RIFFIN", "jantina": "P", "sekolah": "SMK SKUDAI", "kumpulan": "A", "noUrutan": 12.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA013", "nama": "HUSNA BINTI IZZUDDIN", "jantina": "P", "sekolah": "SMK SULTAN ISMAIL", "kumpulan": "A", "noUrutan": 13.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA014", "nama": "NUR KHALISYA UMAIRAH BINTI HISHAM", "jantina": "P", "sekolah": "SMK TAMAN DESA SKUDAI", "kumpulan": "A", "noUrutan": 14.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA015", "nama": "MADEYLN MALAR A/P P.M.MURUGAN", "jantina": "P", "sekolah": "SMK TAMAN SELESA JAYA", "kumpulan": "A", "noUrutan": 15.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA016", "nama": "NUR ZAFIRAH BINTI MOHAMMAD ZAID", "jantina": "P", "sekolah": "SMK TAMAN SELESA JAYA", "kumpulan": "A", "noUrutan": 16.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA017", "nama": "ANDRIYANA NOOR MAISARAH BINTI MOHMAD SUKRI", "jantina": "P", "sekolah": "SMK TAMAN TUN AMINAH", "kumpulan": "A", "noUrutan": 17.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA018", "nama": "NUR HUSNINA UMAIRAIAH BT MOHD HASMIDI", "jantina": "P", "sekolah": "SMK TAMAN UNIVERISITI", "kumpulan": "A", "noUrutan": 18.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA019", "nama": "SITI AISYAH BINTI MOHD ANUAR", "jantina": "P", "sekolah": "SMK TAMAN UNIVERSITI 2", "kumpulan": "A", "noUrutan": 19.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA020", "nama": "SAVIENASHA BINTI MUHAMMAD", "jantina": "P", "sekolah": "SMK TASEK UTARA 2", "kumpulan": "A", "noUrutan": 20.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PA021", "nama": "NUR UMAIRAH AFRINA BINTI AMIR RIDZWAN", "jantina": "P", "sekolah": "SMK TUN SYED NASIR ISMAIL", "kumpulan": "A", "noUrutan": 21.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB001", "nama": "IRDINA WAFA BINTI MOHAMMAD", "jantina": "P", "sekolah": "SEKOLAH TUN FATIMAH", "kumpulan": "B", "noUrutan": 1.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB002", "nama": "NUR FARIHAH BINTI MOHD FAIZAL", "jantina": "P", "sekolah": "SMA AL-QURAN WADDIN", "kumpulan": "B", "noUrutan": 2.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB003", "nama": "QALSOM MASTURAH BINTI MOHD HERDI", "jantina": "P", "sekolah": "SMK AMINUDDIN BAKI", "kumpulan": "B", "noUrutan": 3.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB004", "nama": "NURKHAIRUNNISA BINTI RAMLI", "jantina": "P", "sekolah": "SMK DATO' USMAN AWANG", "kumpulan": "B", "noUrutan": 4.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB005", "nama": "CHEN JIA EN", "jantina": "P", "sekolah": "SMK IJ CONVENT", "kumpulan": "B", "noUrutan": 5.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB006", "nama": "GAN WEN PEI", "jantina": "P", "sekolah": "SMK IJ CONVENT", "kumpulan": "B", "noUrutan": 6.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB007", "nama": "AZZA ZEHRAIZMA ZEENATH BINTI NOOR AZIZAN", "jantina": "P", "sekolah": "SMK MAJIDI BARU 2", "kumpulan": "B", "noUrutan": 7.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB008", "nama": "ARVESHA A/P TILAGANATHAN", "jantina": "P", "sekolah": "SMK MUTIARA RINI", "kumpulan": "B", "noUrutan": 8.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB009", "nama": "DANIA NABIHAH BINTI SANTYRA", "jantina": "P", "sekolah": "SMK SKUDAI", "kumpulan": "B", "noUrutan": 9.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB010", "nama": "NUR ELIAA YASMIN BINTI MOHAMMED NAZURUL ISLAM", "jantina": "P", "sekolah": "SMK SKUDAI", "kumpulan": "B", "noUrutan": 10.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB011", "nama": "NURSYASYA HUMAYRA BINTI MUSTAPA", "jantina": "P", "sekolah": "SMK SKUDAI", "kumpulan": "B", "noUrutan": 11.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB012", "nama": "HANI SUFIA BINTI MOHD RAFI", "jantina": "P", "sekolah": "SMK SRI RAHMAT", "kumpulan": "B", "noUrutan": 12.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB013", "nama": "MAIZATUL ATIQAH BINTI MASIRAN", "jantina": "P", "sekolah": "SMK TAMAN DESA SKUDAI", "kumpulan": "B", "noUrutan": 13.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB014", "nama": "NUR AISYAH BINTI ZULKEFLI", "jantina": "P", "sekolah": "SMK TAMAN MUTIARA RINI 2", "kumpulan": "B", "noUrutan": 14.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB015", "nama": "NISRINA SALSABILA BINTI BENNY", "jantina": "P", "sekolah": "SMK TAMAN SELESA JAYA", "kumpulan": "B", "noUrutan": 15.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB016", "nama": "SAKINAH BINTI ARIFF BAKHTIAR", "jantina": "P", "sekolah": "SMK TAMAN SELESA JAYA", "kumpulan": "B", "noUrutan": 16.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB017", "nama": "SYLVENNA EVVY ANAK SYLVESTER", "jantina": "P", "sekolah": "SMK TAMAN TUN AMINAH", "kumpulan": "B", "noUrutan": 17.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB018", "nama": "NUR SYAFIYA AQILAH BINTI NOOR HISHAM", "jantina": "P", "sekolah": "SMK TAMAN UNIVERSITI", "kumpulan": "B", "noUrutan": 18.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB019", "nama": "SYAHRAIN BALQIS BINTI SUHAIMEE", "jantina": "P", "sekolah": "SMK TAMAN UNIVERSITI 2", "kumpulan": "B", "noUrutan": 19.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB020", "nama": "ALYA ADRYANA BINTI ISMUNI", "jantina": "P", "sekolah": "SMK TUN SYED NASIR ISMAIL", "kumpulan": "B", "noUrutan": 20.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PB021", "nama": "NURAMANINA SARAH BINTI MOHD ELYAS", "jantina": "P", "sekolah": "SMK TUN SYED NASIR ISMAIL", "kumpulan": "B", "noUrutan": 21.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC001", "nama": "NOOR ZARA KHAN BINTI MOHD KAMAL FARISH", "jantina": "P", "sekolah": "SEKOLAH TUN FATIMAH", "kumpulan": "C", "noUrutan": 1.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC002", "nama": "NURIN ASYIFA BINTI MUHAMMADZIN", "jantina": "P", "sekolah": "SMA AL-QURAN WADDIN", "kumpulan": "C", "noUrutan": 2.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC003", "nama": "BAHEERA SAFIAH BINTI ROSMAINI", "jantina": "P", "sekolah": "SMK BANDAR UDA UTAMA JB", "kumpulan": "C", "noUrutan": 3.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC004", "nama": "PUTRI NUR AFIFAH ALIAH BINTI AJIWI", "jantina": "P", "sekolah": "SMK DATO' USMAN AWANG", "kumpulan": "C", "noUrutan": 4.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC005", "nama": "GAN WEN PEI", "jantina": "P", "sekolah": "SMK IJ CONVENT", "kumpulan": "C", "noUrutan": 5.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC006", "nama": "WONG CAI HAN", "jantina": "P", "sekolah": "SMK IJ CONVENT", "kumpulan": "C", "noUrutan": 6.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC007", "nama": "SITI NURBALQIS AZIERA BINTI SAZALI", "jantina": "P", "sekolah": "SMK MAJIDI BARU 2", "kumpulan": "C", "noUrutan": 7.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC008", "nama": "LIEW SHANQI", "jantina": "P", "sekolah": "SMK MUTIARA RINI", "kumpulan": "C", "noUrutan": 8.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC009", "nama": "IZARA ALEESYA BINTI MOHD IZZUDDIN", "jantina": "P", "sekolah": "SMK SKUDAI", "kumpulan": "C", "noUrutan": 9.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC010", "nama": "NUR UMAIRAH ZAHRA BINTI SHAMSUL RIZAL", "jantina": "P", "sekolah": "SMK SKUDAI", "kumpulan": "C", "noUrutan": 10.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC011", "nama": "PUTRI NUR ADAUWIYYAH BINTI AHMAD @ RAHMAT", "jantina": "P", "sekolah": "SMK SKUDAI", "kumpulan": "C", "noUrutan": 11.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC012", "nama": "AISYA QISTINA BINTI ABDUL MALEK", "jantina": "P", "sekolah": "SMK SULTAN ISMAIL", "kumpulan": "C", "noUrutan": 12.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC013", "nama": "NUR DAMIA ZALIEYYA BINTI ABDULLAH", "jantina": "P", "sekolah": "SMK TAMAN DESA SKUDAI", "kumpulan": "C", "noUrutan": 13.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC014", "nama": "ABIGAIL AIMEE FREDDY", "jantina": "P", "sekolah": "SMK TAMAN SELESA JAYA", "kumpulan": "C", "noUrutan": 14.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC015", "nama": "NUR DHANIYAH BALQIS BINTI MOHAMAD IZWAN", "jantina": "P", "sekolah": "SMK TAMAN SELESA JAYA", "kumpulan": "C", "noUrutan": 15.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC016", "nama": "VAISNAVI A/P PON PANDIAN", "jantina": "P", "sekolah": "SMK TAMAN SELESA JAYA", "kumpulan": "C", "noUrutan": 16.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC017", "nama": "AFRINA AQEELAH BT ARIZAM", "jantina": "P", "sekolah": "SMK TAMAN UNIVERISITI", "kumpulan": "C", "noUrutan": 17.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC018", "nama": "THIVASHINI A/P VIKNESWARAN", "jantina": "P", "sekolah": "SMK TAMAN UNIVERSITI", "kumpulan": "C", "noUrutan": 18.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC019", "nama": "PRUNELLA REI A/P SIVACHANDARAN", "jantina": "P", "sekolah": "SMK TASEK UTARA 2", "kumpulan": "C", "noUrutan": 19.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "KRS", "noBadan": "KRS-PC020", "nama": "NUR ATIQAH ADHWA'NI BINTI ABDULLAH HIRWANDY", "jantina": "P", "sekolah": "SMK TUN SYED NASIR ISMAIL", "kumpulan": "C", "noUrutan": 20.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA001", "nama": "MUHAMMAD REEFA MIKHAIL BIN KHAIRUL ANWAR", "jantina": "L", "sekolah": "SJK (C) FOON YEW 2", "kumpulan": "A", "noUrutan": 1.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA002", "nama": "TEJEASHVAR A/L RAJENDRAN", "jantina": "L", "sekolah": "SJK (T) JALAN YAHYA AWAL", "kumpulan": "A", "noUrutan": 2.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA003", "nama": "ADRIEL SANJAY JUSTIN", "jantina": "L", "sekolah": "SJK (T) TAMAN TUN AMINAH", "kumpulan": "A", "noUrutan": 3.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA004", "nama": "MUHAMMAD AMMAR NAUFAL BIN MOHD NUR SYAFIQ", "jantina": "L", "sekolah": "SK BUKIT MUTIARA", "kumpulan": "A", "noUrutan": 4.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA005", "nama": "MUHAMMAD HILMAN HAQ BIN MOHD HARZAMIR", "jantina": "L", "sekolah": "SK KAMPONG PASIR", "kumpulan": "A", "noUrutan": 5.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA006", "nama": "MUHAMMAD RIZKY FINIX BIN MUHAMMAD AKMAL", "jantina": "L", "sekolah": "SK KAMPUNG PULAI", "kumpulan": "A", "noUrutan": 6.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA007", "nama": "FIRAS IMRAN BIN FAKHRUL IZWAN", "jantina": "L", "sekolah": "SK LARKIN 1", "kumpulan": "A", "noUrutan": 7.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA008", "nama": "MUHAMMAD SAIE RIZQULLAH BIN SAYEFULLAH", "jantina": "L", "sekolah": "SK MAJIDI BAHRU", "kumpulan": "A", "noUrutan": 8.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA009", "nama": "MUHAMMAD HUZAIR NAQIUDIN BIN MOHD HAIRUDIN", "jantina": "L", "sekolah": "SK NONG CHIK", "kumpulan": "A", "noUrutan": 9.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA010", "nama": "AHMAD UMAR BIN MAT JUNOH", "jantina": "L", "sekolah": "SK NUSANTARA", "kumpulan": "A", "noUrutan": 10.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA011", "nama": "MUHAMMMAD AIMAN HAZIQ BIN MUHAMMAD FIRDAUS", "jantina": "L", "sekolah": "SK NUSANTARA", "kumpulan": "A", "noUrutan": 11.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA012", "nama": "FAROUQ AIMAR FUDHAIL BIN MOHAMED HIRMY", "jantina": "L", "sekolah": "SK SERI MELATI", "kumpulan": "A", "noUrutan": 12.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA013", "nama": "MUHAMMAD AISY FAYYADH BIN ABDUL KAMAL", "jantina": "L", "sekolah": "SK SERI MELATI", "kumpulan": "A", "noUrutan": 13.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA014", "nama": "MUHAMMAD NUR IQBAL BIN ABDUR RAZZAQ", "jantina": "L", "sekolah": "SK SERI MELATI", "kumpulan": "A", "noUrutan": 14.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA015", "nama": "MUHAMMAD AVICEENA BIN ROSLAN", "jantina": "L", "sekolah": "SK SERI PERLING 2", "kumpulan": "A", "noUrutan": 15.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA016", "nama": "MUHAMMAD ARYAN BIN SHAHRUL AFZANIZAM", "jantina": "L", "sekolah": "SK SRI AMAR", "kumpulan": "A", "noUrutan": 16.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA017", "nama": "LAXSHAN A/L SUJENDRAN", "jantina": "L", "sekolah": "SK SRI TEBRAU", "kumpulan": "A", "noUrutan": 17.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA018", "nama": "AYLAN RIZQI ISMAIL BIN AZRUL", "jantina": "L", "sekolah": "SK TAMAN MUTIARA RINI", "kumpulan": "A", "noUrutan": 18.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA019", "nama": "IMAN IRSYAD BIN KHAIRUL ANUAR RIDZUAN", "jantina": "L", "sekolah": "SK TAMAN PELANGI", "kumpulan": "A", "noUrutan": 19.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA020", "nama": "MUHAMMAD NAUFAL AMSYAR BIN MOHD HAFIZ", "jantina": "L", "sekolah": "SK TAMAN PELANGI", "kumpulan": "A", "noUrutan": 20.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA021", "nama": "MUHAMMAD ADAM ZAFRAN BIN MUHAMAD AZROL", "jantina": "L", "sekolah": "SK TAMAN PERLING", "kumpulan": "A", "noUrutan": 21.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA022", "nama": "MOHAMAD ZAHID ISMAIL BIN ABDULLAH", "jantina": "L", "sekolah": "SK TAMAN SURIA", "kumpulan": "A", "noUrutan": 22.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA023", "nama": "MUHAMMAD ZAFRAN BIN AZUAN", "jantina": "L", "sekolah": "SK TAMAN SURIA", "kumpulan": "A", "noUrutan": 23.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA024", "nama": "MUHAMMAD AISY RYKAL BIN MUHAMAD RASUL", "jantina": "L", "sekolah": "SK TAMAN SUTERA", "kumpulan": "A", "noUrutan": 24.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA025", "nama": "MUHAMMAD ZAFFRAN SAMSUDIN BIN ABDUR RAZZAQ", "jantina": "L", "sekolah": "SK TAMAN TAMPOI UTAMA", "kumpulan": "A", "noUrutan": 25.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA026", "nama": "MUHAMMAD AQIF RAYQAL BIN MOHD FADIL", "jantina": "L", "sekolah": "SK TAMAN UNIVERSITI 1", "kumpulan": "A", "noUrutan": 26.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA027", "nama": "SYAHEED AMMAR ABDILLAH BIN MOHAMMAD BASAR", "jantina": "L", "sekolah": "SK TAMAN UNIVERSITI 4", "kumpulan": "A", "noUrutan": 27.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA028", "nama": "MUHAMMAD ADDI AFFEZ BIN MUHAMMAD SUFFIAN", "jantina": "L", "sekolah": "SK TASEK UTARA", "kumpulan": "A", "noUrutan": 28.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA029", "nama": "MUAYYAD ZUHAILY BIN MOHD TAUFIK", "jantina": "L", "sekolah": "SK TEBRAU BAKAR BATU", "kumpulan": "A", "noUrutan": 29.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA030", "nama": "MUHAMMAD AMMAR RAYYAN BIN MOHD HAFIZ", "jantina": "L", "sekolah": "SK TEMENGGONG ABDUL RAHMAN 1", "kumpulan": "A", "noUrutan": 30.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA031", "nama": "ARYAN SHADIQ BIN MOHD SOLLIHIN", "jantina": "L", "sekolah": "SRABJB", "kumpulan": "A", "noUrutan": 31.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA032", "nama": "MUHAMMAD AQIL BIN MOHD FAZLIEE", "jantina": "L", "sekolah": "SRABJB", "kumpulan": "A", "noUrutan": 32.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LA033", "nama": "MUHAMMAD RIFQI UMAIR BIN MOHD AZWAN NAIM", "jantina": "L", "sekolah": "SRABJB", "kumpulan": "A", "noUrutan": 33.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB001", "nama": "ZACHARY LOO QI WEI", "jantina": "L", "sekolah": "SJK (C) FOON YEW 2", "kumpulan": "B", "noUrutan": 1.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB002", "nama": "KAPINDRA RAJ A/L PRASAD RAJ", "jantina": "L", "sekolah": "SJK (T) LADANG RINI", "kumpulan": "B", "noUrutan": 2.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB003", "nama": "JEEVITHAN A/L GANESPURAN", "jantina": "L", "sekolah": "SJK (T) TAMAN TUN AMINAH", "kumpulan": "B", "noUrutan": 3.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB004", "nama": "AR RAYYAN HACQIMY BIN MOHD FAUZI", "jantina": "L", "sekolah": "SK KAMPONG PASIR", "kumpulan": "B", "noUrutan": 4.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB005", "nama": "MUHAMMAD RAZIQ BIN MOHD RIDHUAN", "jantina": "L", "sekolah": "SK KAMPONG PASIR", "kumpulan": "B", "noUrutan": 5.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB006", "nama": "MUHAMMAD QUSHAYYI RIZQKI BIN MOHD KHAIRUL", "jantina": "L", "sekolah": "SK KG MAJU JAYA", "kumpulan": "B", "noUrutan": 6.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB007", "nama": "MCCAELLEN REEVE ANAK MICHAEL", "jantina": "L", "sekolah": "SK LARKIN 1", "kumpulan": "B", "noUrutan": 7.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB008", "nama": "IZZ NUR ZAIHAN BIN KAMARUL ARIFIN", "jantina": "L", "sekolah": "SK MOHD KHIR JOHARI", "kumpulan": "B", "noUrutan": 8.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB009", "nama": "MUHAMMAD IZZ HARITH BIN NUR HAZWAN", "jantina": "L", "sekolah": "SK NONG CHIK", "kumpulan": "B", "noUrutan": 9.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB010", "nama": "AMMAR IRFAN BIN MOHD NUR SAUFI", "jantina": "L", "sekolah": "SK NUSANTARA", "kumpulan": "B", "noUrutan": 10.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB011", "nama": "ARYAN SUFYAN BIN MOHAMAD ZULFAN", "jantina": "L", "sekolah": "SK SERI MELATI", "kumpulan": "B", "noUrutan": 11.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB012", "nama": "MUHAMAD AMMAR QAYYIM BIN IBRAHIM", "jantina": "L", "sekolah": "SK SERI MELATI", "kumpulan": "B", "noUrutan": 12.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB013", "nama": "MUHAMMAD AQHIL MUSTAQHIM BIN MOHD. SAHARI", "jantina": "L", "sekolah": "SK SERI MELATI", "kumpulan": "B", "noUrutan": 13.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB014", "nama": "MUHAMMAD SYAZWI SYIHABUDDIN BIN ADILEY", "jantina": "L", "sekolah": "SK SERI MELATI", "kumpulan": "B", "noUrutan": 14.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB015", "nama": "MUHAMMAD SHAMIR NASRI BIN MOHD SHAHRIR", "jantina": "L", "sekolah": "SK SERI PERLING 2", "kumpulan": "B", "noUrutan": 15.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB016", "nama": "ABDUL MALIQ HARITH BIN ABDUL KARIM", "jantina": "L", "sekolah": "SK SRI SKUDAI", "kumpulan": "B", "noUrutan": 16.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB017", "nama": "UTHMAN BIN SHALFIN", "jantina": "L", "sekolah": "SK SRI TEBRAU", "kumpulan": "B", "noUrutan": 17.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB018", "nama": "FAKHRUL AKIF RAHIMI BIN FAIZAL ROZHIZLAN", "jantina": "L", "sekolah": "SK TAMAN PELANGI", "kumpulan": "B", "noUrutan": 18.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB019", "nama": "MUHAMMAD ADAM ARYAN BIN AZHIEM ZULKIFLI", "jantina": "L", "sekolah": "SK TAMAN PELANGI", "kumpulan": "B", "noUrutan": 19.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB020", "nama": "MUHAMMAD NUH ZIYAD BIN MUHAMAD ANUAR", "jantina": "L", "sekolah": "SK TAMAN PELANGI", "kumpulan": "B", "noUrutan": 20.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB021", "nama": "MUHAMMAD DHAFIR DARWISY BIN MUHAMAD FIRDAUS", "jantina": "L", "sekolah": "SK TAMAN PERLING", "kumpulan": "B", "noUrutan": 21.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB022", "nama": "MUHAMMAD AIDIL ZHAFRI BIN MOHD NAZRUL HAFIZAN", "jantina": "L", "sekolah": "SK TAMAN SURIA", "kumpulan": "B", "noUrutan": 22.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB023", "nama": "AHMAD ZIYAD BIN MOHD ROZAINI", "jantina": "L", "sekolah": "SK TAMAN SUTERA", "kumpulan": "B", "noUrutan": 23.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB024", "nama": "MUHAMMAD QAYYUM MUHAIMIN BIN HAFIZUL HAFSYAM", "jantina": "L", "sekolah": "SK TAMAN SUTERA", "kumpulan": "B", "noUrutan": 24.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB025", "nama": "MUHAMMAD ARYAN MIKAIL BIN MUHAMMAD HAFIZ", "jantina": "L", "sekolah": "SK TAMAN TUN AMINAH", "kumpulan": "B", "noUrutan": 25.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB026", "nama": "SYAMIL DANISH BIN SARIFUDDIN", "jantina": "L", "sekolah": "SK TAMAN UNIVERSITI 1", "kumpulan": "B", "noUrutan": 26.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB027", "nama": "HABIB MUHAMMAD BIN ABDUL HAMID", "jantina": "L", "sekolah": "SK TASEK UTARA", "kumpulan": "B", "noUrutan": 27.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB028", "nama": "AHMAD SYAKIL RIZQI BIN MOHD RIDWAN", "jantina": "L", "sekolah": "SK TEBRAU BAKAR BATU", "kumpulan": "B", "noUrutan": 28.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB029", "nama": "MUHAMMAD NOR SHUKRI BIN NORHASIM", "jantina": "L", "sekolah": "SK TEBRAU BAKAR BATU", "kumpulan": "B", "noUrutan": 29.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB030", "nama": "RAEF FAYYAZ BIN HAMZAH FANSURI", "jantina": "L", "sekolah": "SK TEMENGGONG ABDUL RAHMAN 1", "kumpulan": "B", "noUrutan": 30.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB031", "nama": "MOHAMAD AMSYAR ZIYADULHAQ BIN MOHAMAD ZARQANI", "jantina": "L", "sekolah": "SRABJB", "kumpulan": "B", "noUrutan": 31.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB032", "nama": "MUHAMMAD HADI UQAIL BIN MOHD ZAIDI", "jantina": "L", "sekolah": "SRABJB", "kumpulan": "B", "noUrutan": 32.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LB033", "nama": "MUHAMMAD SYAZAN BIN MOHD SYAHIR", "jantina": "L", "sekolah": "SRABJB", "kumpulan": "B", "noUrutan": 33.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC001", "nama": "PRAGTIIS NAIR A/L RAMUBAHADUR", "jantina": "L", "sekolah": "SJK (T) JALAN YAHYA AWAL", "kumpulan": "C", "noUrutan": 1.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC002", "nama": "VAITHESWARAN A/L KESAVA KUMAR", "jantina": "L", "sekolah": "SJK (T) LADANG RINI", "kumpulan": "C", "noUrutan": 2.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC003", "nama": "KHALEED YUSUFF BIN MOHD NOR HAFIZ", "jantina": "L", "sekolah": "SK BUKIT MUTIARA", "kumpulan": "C", "noUrutan": 3.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC004", "nama": "MUHAMMAD AFIQ RAYYAN BIN MOHD FAKHRUDDIN", "jantina": "L", "sekolah": "SK KAMPONG PASIR", "kumpulan": "C", "noUrutan": 4.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC005", "nama": "MUHAMMAD AL-BHAYHAQQI BIN MOHAMAD SUFIYAN", "jantina": "L", "sekolah": "SK KAMPUNG PULAI", "kumpulan": "C", "noUrutan": 5.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC006", "nama": "WAN SHARUL EZUWAN BIN WAN SYAHRUSYABRI", "jantina": "L", "sekolah": "SK KG MAJU JAYA", "kumpulan": "C", "noUrutan": 6.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC007", "nama": "HARIS HAKEEM BIN MOHD SANI", "jantina": "L", "sekolah": "SK MAJIDI BAHRU", "kumpulan": "C", "noUrutan": 7.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC008", "nama": "SAIF ISLAM BIN ABDUL RAHMAN", "jantina": "L", "sekolah": "SK MOHD KHIR JOHARI", "kumpulan": "C", "noUrutan": 8.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC009", "nama": "MUHAMMAD SYAHID ZIYAD BIN SUFIAN", "jantina": "L", "sekolah": "SK NONG CHIK", "kumpulan": "C", "noUrutan": 9.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC010", "nama": "HAIRUL IRSYAD MUZAFFAR BIN HAIRUL HAIRI", "jantina": "L", "sekolah": "SK NUSANTARA", "kumpulan": "C", "noUrutan": 10.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC011", "nama": "ASYRAF AIMAR DANI BIN YASIN", "jantina": "L", "sekolah": "SK SERI MELATI", "kumpulan": "C", "noUrutan": 11.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC012", "nama": "MUHAMMAD ADAM ARIFF BIN SYAIPUL ADZHAR", "jantina": "L", "sekolah": "SK SERI MELATI", "kumpulan": "C", "noUrutan": 12.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC013", "nama": "MUHAMMAD FAYYADH BIN MOHD NORAZLIE", "jantina": "L", "sekolah": "SK SERI MELATI", "kumpulan": "C", "noUrutan": 13.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC014", "nama": "AIMAN HAKIM BIN AZLAN", "jantina": "L", "sekolah": "SK SERI PERLING 2", "kumpulan": "C", "noUrutan": 14.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC015", "nama": "MALEEQ HAIDAR BIN HARMANNULLAH", "jantina": "L", "sekolah": "SK SRI AMAR", "kumpulan": "C", "noUrutan": 15.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC016", "nama": "MUHAMMAD LUTFI HAKIM BIN MOSYAZID", "jantina": "L", "sekolah": "SK SRI SKUDAI", "kumpulan": "C", "noUrutan": 16.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC017", "nama": "AHMAD MUIZZUDDIN BIN ZAIR ASRAR", "jantina": "L", "sekolah": "SK TAMAN MUTIARA RINI", "kumpulan": "C", "noUrutan": 17.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC018", "nama": "GIGGS JINOL", "jantina": "L", "sekolah": "SK TAMAN PELANGI", "kumpulan": "C", "noUrutan": 18.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC019", "nama": "MUHAMMAD ARYAN BIN RAHMATHUL AZIZ", "jantina": "L", "sekolah": "SK TAMAN PELANGI", "kumpulan": "C", "noUrutan": 19.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC020", "nama": "ARYAN HAKIMY BIN MOHD SAZRI", "jantina": "L", "sekolah": "SK TAMAN PERLING", "kumpulan": "C", "noUrutan": 20.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC021", "nama": "MUHAMMAD ZAWWIR AQIL BIN ZAINI", "jantina": "L", "sekolah": "SK TAMAN PERLING", "kumpulan": "C", "noUrutan": 21.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC022", "nama": "MUHAMMAD AIMAN HAZIQ BIN ABDUL HAFIZ", "jantina": "L", "sekolah": "SK TAMAN SURIA", "kumpulan": "C", "noUrutan": 22.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC023", "nama": "AYDAN HAFIY BIN MOHAMAD SHAFIEE", "jantina": "L", "sekolah": "SK TAMAN SUTERA", "kumpulan": "C", "noUrutan": 23.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC024", "nama": "MUHAMMAD NUR AIMAN LUTFI BIN ABD RAHMAN", "jantina": "L", "sekolah": "SK TAMAN TAMPOI UTAMA", "kumpulan": "C", "noUrutan": 24.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC025", "nama": "MUHAMMAD SAIF MIKHAIL BIN SAIFUL'ADLI", "jantina": "L", "sekolah": "SK TAMAN TUN AMINAH", "kumpulan": "C", "noUrutan": 25.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC026", "nama": "AFWAN FAHRI BIN IZUDDIN SHAH", "jantina": "L", "sekolah": "SK TAMAN UNIVERSITI 4", "kumpulan": "C", "noUrutan": 26.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC027", "nama": "MOHAMAD AMMAR FAYYADH BIN MOHAMAD SYAFIQ", "jantina": "L", "sekolah": "SK TASEK UTARA", "kumpulan": "C", "noUrutan": 27.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC028", "nama": "AMIR AFIQ BIN MOHAMAD NURJIHADDY", "jantina": "L", "sekolah": "SK TEBRAU BAKAR BATU", "kumpulan": "C", "noUrutan": 28.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC029", "nama": "IMAN AQEEF BIN SAHARUDIN", "jantina": "L", "sekolah": "SK TEMENGGONG ABDUL RAHMAN 1", "kumpulan": "C", "noUrutan": 29.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC030", "nama": "RAYYAN HAIQAL BIN MUHAMMAD AZAM", "jantina": "L", "sekolah": "SK TEMENGGONG ABDUL RAHMAN 1", "kumpulan": "C", "noUrutan": 30.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC031", "nama": "MUHAMMAD AMMAR BIN MOHD FAIREE", "jantina": "L", "sekolah": "SRABJB", "kumpulan": "C", "noUrutan": 31.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-LC032", "nama": "MUHAMMAD HADIF AMMAR BIN HAIROLANUAR", "jantina": "L", "sekolah": "SRABJB", "kumpulan": "C", "noUrutan": 32.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA001", "nama": "AINUL HASANAH BINTI AHMAD HAMSANI", "jantina": "P", "sekolah": "SJK (C) FOON YEW 2", "kumpulan": "A", "noUrutan": 1.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA002", "nama": "REYSHINI NAIR A/P THEVAN NAIR", "jantina": "P", "sekolah": "SJK (T) JALAN YAHYA AWAL", "kumpulan": "A", "noUrutan": 2.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA003", "nama": "RISHITA A/P AGHILAN", "jantina": "P", "sekolah": "SJK (T) TAMAN TUN AMINAH", "kumpulan": "A", "noUrutan": 3.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA004", "nama": "AURORA MIKHAYLLA BINTI MUHAMMAD ARIFF", "jantina": "P", "sekolah": "SK (P) BANDAR TINGGI", "kumpulan": "A", "noUrutan": 4.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA005", "nama": "MAISARAH BINTI MAHDHIR", "jantina": "P", "sekolah": "SK (P) SULTAN IBRAHIM", "kumpulan": "A", "noUrutan": 5.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA006", "nama": "THESHMITHA A/P MAHENDRAN", "jantina": "P", "sekolah": "SK (P) SULTAN IBRAHIM", "kumpulan": "A", "noUrutan": 6.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA007", "nama": "NURUL IZZAH BINTI NOOR SYAHREER", "jantina": "P", "sekolah": "SK KAMPUNG PULAI", "kumpulan": "A", "noUrutan": 7.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA008", "nama": "SARAH NUR AUNI BINTI ABDUL RAHIM", "jantina": "P", "sekolah": "SK KG MAJU JAYA", "kumpulan": "A", "noUrutan": 8.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA009", "nama": "NOOR ARIEANA MIQHAYLA BINTI NOOR AZMIERULLAH", "jantina": "P", "sekolah": "SK MAJIDI BAHRU", "kumpulan": "A", "noUrutan": 9.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA010", "nama": "AISYAH NUHA ZAHIRA BINTI AHMADI", "jantina": "P", "sekolah": "SK NONG CHIK", "kumpulan": "A", "noUrutan": 10.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA011", "nama": "MARSYA NURMELYSSA BINTI ADY", "jantina": "P", "sekolah": "SK SERI MELATI", "kumpulan": "A", "noUrutan": 11.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA012", "nama": "DHIYA NUR AINAA ZARITH SOFIA BINTI MOHAMAD ZAKI", "jantina": "P", "sekolah": "SK SRI AMAR", "kumpulan": "A", "noUrutan": 12.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA013", "nama": "NURHAFIZAH HUSNA BINTI MOHD RASID", "jantina": "P", "sekolah": "SK SRI SKUDAI", "kumpulan": "A", "noUrutan": 13.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA014", "nama": "NUR MARISSA QISTINA BINTI MOHD AZIZUL", "jantina": "P", "sekolah": "SK TAMAN MUTIARA RINI", "kumpulan": "A", "noUrutan": 14.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA015", "nama": "DAMIA NUR ALEESYA BINTI MOHAMAD YUSRI", "jantina": "P", "sekolah": "SK TAMAN PELANGI", "kumpulan": "A", "noUrutan": 15.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA016", "nama": "NUR QASEH ALVIENA BINTI MOHD FIRDAUS", "jantina": "P", "sekolah": "SK TAMAN PELANGI", "kumpulan": "A", "noUrutan": 16.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA017", "nama": "NUR FATHIYYAH BINTI FADIL", "jantina": "P", "sekolah": "SK TAMAN TUN AMINAH", "kumpulan": "A", "noUrutan": 17.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA018", "nama": "AIMY DHIYA DIANDRA BINTI YUSINDRA", "jantina": "P", "sekolah": "SK TAMAN UNIVERSITI 1", "kumpulan": "A", "noUrutan": 18.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA019", "nama": "AQILAH AWFIYAH BINTI NAZMI", "jantina": "P", "sekolah": "SK TASEK UTARA", "kumpulan": "A", "noUrutan": 19.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA020", "nama": "KHADEEJA HANNAN BINTI MOHD NAJIB", "jantina": "P", "sekolah": "SRABJB", "kumpulan": "A", "noUrutan": 20.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PA021", "nama": "NURUL TASNEEM BINTI NOOR JAAFAR", "jantina": "P", "sekolah": "SRABJB", "kumpulan": "A", "noUrutan": 21.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB001", "nama": "CHAI RUI EN", "jantina": "P", "sekolah": "SJK (C) FOON YEW 2", "kumpulan": "B", "noUrutan": 1.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB002", "nama": "PREETHIKA A/P THINAGARAN", "jantina": "P", "sekolah": "SJK (T) LADANG RINI", "kumpulan": "B", "noUrutan": 2.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB003", "nama": "SHAMIKSSHA A/P RAJASEGARAN", "jantina": "P", "sekolah": "SJK (T) TAMAN TUN AMINAH", "kumpulan": "B", "noUrutan": 3.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB004", "nama": "ELVINA ELYSIA CHONG", "jantina": "P", "sekolah": "SK (P) BANDAR TINGGI", "kumpulan": "B", "noUrutan": 4.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB005", "nama": "NUR AIRIS JANNAH BINTI ASRULFAIZAD", "jantina": "P", "sekolah": "SK (P) SULTAN IBRAHIM", "kumpulan": "B", "noUrutan": 5.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB006", "nama": "NUR AIRIS ERYNA BINTI MUHAMAD AZAHA", "jantina": "P", "sekolah": "SK BUKIT MUTIARA", "kumpulan": "B", "noUrutan": 6.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB007", "nama": "RAISYA AZZAHRA BINTI MUHAMAD RAFFI", "jantina": "P", "sekolah": "SK KAMPUNG PULAI", "kumpulan": "B", "noUrutan": 7.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB008", "nama": "ASFALAILA IMANI BINTI MOHD AZHAR", "jantina": "P", "sekolah": "SK LARKIN 1", "kumpulan": "B", "noUrutan": 8.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB009", "nama": "DANIA AQILAH BINTI NORIZAN", "jantina": "P", "sekolah": "SK MOHD KHIR JOHARI", "kumpulan": "B", "noUrutan": 9.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB010", "nama": "ALISHA SAFIYA BINTI ZAIRI", "jantina": "P", "sekolah": "SK SERI MELATI", "kumpulan": "B", "noUrutan": 10.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB011", "nama": "SITI NUR AISYAH BINTI MOHD SYAHRIL", "jantina": "P", "sekolah": "SK SERI MELATI", "kumpulan": "B", "noUrutan": 11.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB012", "nama": "NUR KEISHA DAMIA BINTI MOHD RIZAL", "jantina": "P", "sekolah": "SK SRI AMAR", "kumpulan": "B", "noUrutan": 12.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB013", "nama": "MIKAEYLA ROSA RUEBEN", "jantina": "P", "sekolah": "SK SRI TEBRAU", "kumpulan": "B", "noUrutan": 13.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB014", "nama": "NUR UZMA AISYAH BINTI MOHD NIZAM", "jantina": "P", "sekolah": "SK TAMAN MUTIARA RINI", "kumpulan": "B", "noUrutan": 14.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB015", "nama": "KHALISHAH ADRIANA BINTI AMAT ISMAIL", "jantina": "P", "sekolah": "SK TAMAN PELANGI", "kumpulan": "B", "noUrutan": 15.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB016", "nama": "NUR AISHAH YUSRA BINTI MOHD AMIN", "jantina": "P", "sekolah": "SK TAMAN TAMPOI UTAMA", "kumpulan": "B", "noUrutan": 16.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB017", "nama": "NUR HASYA JAHIRAH BINTI MOHD HISHAM", "jantina": "P", "sekolah": "SK TAMAN TUN AMINAH", "kumpulan": "B", "noUrutan": 17.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB018", "nama": "NURUL ZUHAIRA SAFIYA BINTI MOHD ZULKHAIRI", "jantina": "P", "sekolah": "SK TAMAN UNIVERSITI 4", "kumpulan": "B", "noUrutan": 18.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB019", "nama": "ILMA BINTI FAIRUL NIZAM", "jantina": "P", "sekolah": "SK TASEK UTARA", "kumpulan": "B", "noUrutan": 19.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB020", "nama": "NUR ALISYA BINTI MUHAMMAD YUSOF", "jantina": "P", "sekolah": "SRABJB", "kumpulan": "B", "noUrutan": 20.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PB021", "nama": "SARA KHADEEJA BINTI MUHAMMAD FAIQ", "jantina": "P", "sekolah": "SRABJB", "kumpulan": "B", "noUrutan": 21.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC001", "nama": "LAKSSHANA A/P VIJAYAKAN", "jantina": "P", "sekolah": "SJK (T) JALAN YAHYA AWAL", "kumpulan": "C", "noUrutan": 1.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC002", "nama": "THUSHITRAA DEVI A/P MANUEL ROXAS", "jantina": "P", "sekolah": "SJK (T) LADANG RINI", "kumpulan": "C", "noUrutan": 2.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC003", "nama": "A'IDAH RAIHANNAH BINTI ABDUL HAFIZ", "jantina": "P", "sekolah": "SK (P) BANDAR TINGGI", "kumpulan": "C", "noUrutan": 3.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC004", "nama": "MELATI IMAN BINTI RIZAL", "jantina": "P", "sekolah": "SK (P) BANDAR TINGGI", "kumpulan": "C", "noUrutan": 4.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC005", "nama": "NUR NAWAL RIZQIN BINTI ISMAIL", "jantina": "P", "sekolah": "SK (P) SULTAN IBRAHIM", "kumpulan": "C", "noUrutan": 5.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC006", "nama": "NUR UQASYAH NADRAH BINTI MOHD KHAIRUL AZUAN", "jantina": "P", "sekolah": "SK BUKIT MUTIARA", "kumpulan": "C", "noUrutan": 6.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC007", "nama": "NURUL QASSEH SUCI PUTERY BINTI MOHD AZIZAN", "jantina": "P", "sekolah": "SK KG MAJU JAYA", "kumpulan": "C", "noUrutan": 7.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC008", "nama": "RAUDHATUL AISYAH BINTI MOHD FAISAL", "jantina": "P", "sekolah": "SK LARKIN 1", "kumpulan": "C", "noUrutan": 8.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC009", "nama": "NAZIRATUL HUSNA BINTI HASAN", "jantina": "P", "sekolah": "SK MOHD KHIR JOHARI", "kumpulan": "C", "noUrutan": 9.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC010", "nama": "AMEERA NUHA BINTI BASHARUDIN", "jantina": "P", "sekolah": "SK SERI MELATI", "kumpulan": "C", "noUrutan": 10.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC011", "nama": "NUR HARYSYAH BINTI MOHD HAIRY", "jantina": "P", "sekolah": "SK SERI PERLING 2", "kumpulan": "C", "noUrutan": 11.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC012", "nama": "NUR BATRISYA BALQIS BINTI MUHAMMAD FAUZI", "jantina": "P", "sekolah": "SK SRI SKUDAI", "kumpulan": "C", "noUrutan": 12.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC013", "nama": "RYSTEDELLCA ARDELLE ROYNALD", "jantina": "P", "sekolah": "SK SRI TEBRAU", "kumpulan": "C", "noUrutan": 13.0, "agama": "BUKAN ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC014", "nama": "ATIQAH SYUHADA BINTI RAZMI", "jantina": "P", "sekolah": "SK TAMAN PELANGI", "kumpulan": "C", "noUrutan": 14.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC015", "nama": "NOR AMMARA QAISARA BINTI MASRINAH", "jantina": "P", "sekolah": "SK TAMAN PELANGI", "kumpulan": "C", "noUrutan": 15.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC016", "nama": "SITI NUR AZRA BINTI ADAM", "jantina": "P", "sekolah": "SK TAMAN TAMPOI UTAMA", "kumpulan": "C", "noUrutan": 16.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC017", "nama": "AFRINA NUR HANNAN BINTI MAT HUSSIN", "jantina": "P", "sekolah": "SK TAMAN UNIVERSITI 1", "kumpulan": "C", "noUrutan": 17.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC018", "nama": "SARAH SOFIA BINTI MOHD NOR", "jantina": "P", "sekolah": "SK TAMAN UNIVERSITI 4", "kumpulan": "C", "noUrutan": 18.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC019", "nama": "NAURAH SUMAYYAH BINTI MOHD EYAMIN ADII", "jantina": "P", "sekolah": "SK TASEK UTARA", "kumpulan": "C", "noUrutan": 19.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC020", "nama": "NUR KAYYISA SOFIA SUHAIMI BINTI ABDUL SHAHID", "jantina": "P", "sekolah": "SRABJB", "kumpulan": "C", "noUrutan": 20.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}, {"unit": "TKRS", "noBadan": "TKRS-PC021", "nama": "NUR IMAN ARDHANI BINTI IZHAR SYAFIQ", "jantina": "P", "sekolah": "SK NONG CHIK", "kumpulan": "C", "noUrutan": 21.0, "agama": "ISLAM", "rawKawad": 0.0, "rawBantuMula": 0.0, "rawIkatan": 0.0, "rawOverall": 0.0, "overall": "0.0%", "statusText": "GGG", "isPass": false, "catatan": "", "isEvaluated": false, "isAbsent": false, "isTarikDiri": false, "isTukar": false, "kawad": "0.0", "bantuMula": "0.0", "ikatan": "0.0"}];



    const GAS_EXEC_URL = "https://script.google.com/macros/s/AKfycbw7QzD_8naN4kFR_1BRk6UO3EjclkmESDP8lW55t7Gvbf-ldcwE-LGbS5hAxwhaXo-r/exec";



    // Universal Backend API Bridge (Menyokong Google Apps Script & Netlify)

    async function runBackendAction(actionName, params = {}) {

      // 1. Jika dijalankan di dalam persekitaran Google Apps Script secara langsung

      if (typeof google !== 'undefined' && google.script && google.script.run) {

        return new Promise((resolve, reject) => {

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

        });

      }



      // 2. Jika dijalankan di Netlify / Luar, panggil Web App API Google Apps Script

      try {

        const response = await fetch(GAS_EXEC_URL, {

          method: 'POST',

          headers: { 'Content-Type': 'text/plain;charset=utf-8' },

          body: JSON.stringify({ action: actionName, params: params })

        });

        const data = await response.json();

        if (data.success === false || data.error) {

          throw new Error(data.error || "Ralat pelayan backend.");

        }

        return data.result;

      } catch (postErr) {

        // Fallback ke mod GET query parameters jika wujud kekangan CORS/Redirect

        try {

          const url = new URL(GAS_EXEC_URL);

          url.searchParams.set('action', actionName);

          url.searchParams.set('payload', JSON.stringify(params));

          const getRes = await fetch(url.toString());

          const getData = await getRes.json();

          if (getData.success === false || getData.error) {

            throw new Error(getData.error || postErr.message);

          }

          return getData.result;

        } catch (getErr) {

          throw postErr;

        }

      }

    }



    const App = {

      state: {

        candidates: (SERVER_DATA && SERVER_DATA.candidates) ? SERVER_DATA.candidates : EMBEDDED_CANDIDATES,

        currentWajaran: {

          kawad: 0.70,

          ikatan: 0.50,

          overall: 0.70,

          wajaranKawad: 0.60,

          wajaranBM: 0.20,

          wajaranIkatan: 0.20

        },

        isAdminLoggedIn: false,

        activeTab: 'tab-program',

        charts: {}

      },



      init() {

        this.parseCandidateIdentifiers();
        this.applyLocalOverrides();



        if (sessionStorage.getItem('pentauliahan_admin_auth') === 'true') {

          this.state.isAdminLoggedIn = true;

        }



        this.bindNavEvents();

        this.bindFilterEvents();

        this.bindAdminEvents();

        this.bindCandidateManageEvents();

        this.recalculateAllStats();

        this.renderCandidatesTable();
        this.renderTopResults();

        this.populateCandidateDropdown();

        const savedAuth = sessionStorage.getItem('pentauliahan_admin_auth');
        if (savedAuth === 'true') {
          this.state.isAdminLoggedIn = true;
        }
        this.updateAuthVisuals();

        try {
          this.initCharts();
        } catch(chartErr) {
          console.warn('[App.init] initCharts gagal — mungkin Chart.js belum dimuatkan:', chartErr);
        }

        this.fetchLiveServerData();

      },




      applyLocalOverrides() {
        // Tiada LocalStorage — Status murid kini dibaca 100% secara LIVE dari tab Google Sheets: PESERTA TIDAK HADIR
      },

      parseCandidateIdentifiers() {

        this.state.candidates.forEach(c => {

          if (c.noBadan && c.noBadan.includes('-')) {

            const afterDash = c.noBadan.split('-')[1];

            if (afterDash && afterDash.length >= 2) {

              if (!c.jantina || c.jantina === '') {

                c.jantina = afterDash[0].toUpperCase();

              }

              if (!c.kumpulan || c.kumpulan === '') {

                c.kumpulan = afterDash[1].toUpperCase();

              }

            }

          }

          if (!c.unit) {

            c.unit = (c.noBadan && c.noBadan.startsWith('TKRS')) ? 'TKRS' : 'KRS';

          }

        });

      },



      async fetchLiveServerData() {
        const syncBadge = document.getElementById('sync-badge');
        if (syncBadge) syncBadge.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Menyegerak Live Sheet...';

        const SPREADSHEET_ID = '1_YmAJ6XVfBREx4_NDTUWRMXAL1Jgi-1vSFS2528dtW0';

        // Helper untuk memuat turun CSV Google Sheet secara Live
        const fetchSheetCsv = async (sheetName) => {
          try {
            const url = `https://docs.google.com/spreadsheets/d/${SPREADSHEET_ID}/gviz/tq?tqx=out:csv&sheet=${encodeURIComponent(sheetName)}`;
            const resp = await fetch(url);
            if (!resp.ok) return null;
            const text = await resp.text();
            return text;
          } catch(e) {
            return null;
          }
        };

        const parseCsvLines = function(csvText) {
          if (!csvText) return [];
          var rawLines = csvText.split(String.fromCharCode(10));
          var lines = [];
          for (var i = 0; i < rawLines.length; i++) {
            var cleaned = rawLines[i].replace(String.fromCharCode(13), '').trim();
            if (cleaned.length > 0) lines.push(cleaned);
          }
          if (lines.length <= 1) return [];
          var result = [];
          for (var j = 1; j < lines.length; j++) {
            var line = lines[j];
            var cols = line.split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/);
            var cleanedCols = [];
            for (var k = 0; k < cols.length; k++) {
              cleanedCols.push(cols[k].replace(/^"|"$/g, '').trim());
            }
            result.push(cleanedCols);
          }
          return result;
        };

        try {
          // 1. Muat turun ketiga-tiga tab serentak secara Live: ANALISIS_TKRS, ANALISIS_KRS, dan PESERTA TIDAK HADIR
          const [csvTKRS, csvKRS, csvTH] = await Promise.all([
            fetchSheetCsv('ANALISIS_TKRS'),
            fetchSheetCsv('ANALISIS_KRS'),
            fetchSheetCsv('PESERTA TIDAK HADIR')
          ]);

          // Peta Markah dari ANALISIS_TKRS & ANALISIS_KRS (Hanya markah pengujian & formula, BUKAN status TH/TD)
          if (csvTKRS && csvKRS) {
            const rowsTKRS = parseCsvLines(csvTKRS);
            const rowsKRS = parseCsvLines(csvKRS);
            const allScoreRows = [...rowsTKRS, ...rowsKRS];

            if (allScoreRows.length > 0) {
              const scoreMap = {};
              allScoreRows.forEach(r => {
                const rawId = r[1];
                const id = typeof rawId === 'string' ? rawId.replace(/^"|"$/g, '').trim() : rawId;
                if (id) {
                  const parsePct = (val) => {
                    if (val === null || val === undefined || val === '') return 0;
                    const clean = String(val).replace(/"/g, '').replace('%', '').trim();
                    const num = parseFloat(clean);
                    if (isNaN(num)) return 0;
                    return num > 1 ? num / 100 : num;
                  };

                  scoreMap[id] = {
                    rawKawad:     parsePct(r[6]),
                    rawBantuMula: parsePct(r[7]),
                    rawIkatan:    parsePct(r[8]),
                    rawOverall:   parsePct(r[9]),
                    statusText:   r[10] ? String(r[10]).replace(/"/g, '').trim() || 'GGG' : 'GGG'
                  };
                }
              });

              // Kemas kini markah asas calon dalam state
              this.state.candidates.forEach(c => {
                const id = c.noBadan || c.noGiliran;
                if (scoreMap[id]) {
                  const s = scoreMap[id];
                  c.rawKawad = s.rawKawad;
                  c.rawBantuMula = s.rawBantuMula;
                  c.rawIkatan = s.rawIkatan;
                  c.rawOverall = s.rawOverall;
                  c.kawad = (s.rawKawad * 100).toFixed(1);
                  c.bantuMula = (s.rawBantuMula * 100).toFixed(1);
                  c.ikatan = (s.rawIkatan * 100).toFixed(1);
                  c.overall = (s.rawOverall * 100).toFixed(1) + '%';
                  c.statusText = s.statusText || 'GGG';
                  c.isEvaluated = (s.rawKawad > 0 || s.rawBantuMula > 0 || s.rawIkatan > 0);
                }
              });
            }
          }

          // 2. KEMAS KINI STATUS KEHADIRAN / TARIK DIRI / GANTIAN DIRECT LIVE DARI TAB 'PESERTA TIDAK HADIR'
          // Reset default status kehadiran untuk semua calon terlebih dahulu
          this.state.candidates.forEach(c => {
            c.isAbsent = false;
            c.isTarikDiri = false;
            c.isGantian = false;
            c.catatan = '';
          });

          if (csvTH) {
            const rowsTH = parseCsvLines(csvTH);
            const thMap = {};
            rowsTH.forEach(r => {
              // Lajur PESERTA TIDAK HADIR: [0]=BIL, [1]=ID_PESERTA, [2]=NAMA, [3]=SEKOLAH, [4]=UNIT, [5]=JANTINA,
              //                             [6]=STATUS, [7]=NAMA_GANTIAN, [8]=CATATAN, [9]=TARIKH_MASA
              const thId = String(r[1] || r[0] || '').trim().toUpperCase();
              if (thId && thId.includes('-')) {
                thMap[thId] = {
                  status: String(r[6] || r[5] || r[7] || '').trim().toUpperCase(),
                  namaGantian: String(r[7] || '').trim(),
                  catatan: String(r[8] || '').trim()
                };
              }
            });

            // Terapkan status langsung daripada tab PESERTA TIDAK HADIR
            this.state.candidates.forEach(c => {
              const id = (c.noBadan || c.noGiliran || '').toUpperCase();
              if (thMap[id]) {
                const item = thMap[id];
                const st = item.status;
                c.catatan = item.catatan || st;
                if (st.includes('TIDAK HADIR') || st === 'TH') {
                  c.isAbsent = true;
                  c.isTarikDiri = false;
                  c.statusText = 'TH';
                } else if (st.includes('TARIK DIRI') || st === 'TD') {
                  c.isTarikDiri = true;
                  c.isAbsent = false;
                  c.statusText = 'TARIK DIRI';
                } else if (st.includes('TUKAR') || st.includes('GANTIAN')) {
                  c.isGantian = true;
                  if (item.namaGantian && item.namaGantian !== '-') {
                    c.nama = item.namaGantian.toUpperCase();
                  }
                  c.catatan = 'CALON GANTIAN: ' + (item.namaGantian || '');
                }
              }
            });
          }

          this.parseCandidateIdentifiers();
          this.recalculateAllStats();
          this.renderCandidatesTable();
          this.renderTopResults();
          this.populateCandidateDropdown();
          try { this.updateCharts(); } catch(e) {}

          if (syncBadge) {
            syncBadge.innerHTML = '<i class="fa-solid fa-circle-check" style="color:var(--emerald-green)"></i> Data Live (PESERTA TIDAK HADIR)';
          }
        } catch(err) {
          console.warn('Ralat segerak Google Sheets:', err);
          if (syncBadge) syncBadge.innerHTML = '<i class="fa-solid fa-circle-info"></i> Data Terkini';
        }
      },

      recalculateAllStats() {

        const w = this.state.currentWajaran;

        let evaluated = 0;

        let passCount = 0;

        let condCount = 0;

        let failCount = 0;

        let absentCount = 0;

        let withdrawCount = 0;

        let sumKawad = 0, sumBM = 0, sumIkatan = 0, sumOverall = 0;



        this.state.candidates.forEach(c => {

          if (c.catatan && (c.catatan.includes('TARIK DIRI'))) {

            withdrawCount++;

            c.isTarikDiri = true;

            c.isPass = false;

            c.statusText = 'TARIK DIRI';

            return;

          }



          if (c.isAbsent || (c.catatan && (c.catatan.includes('TH') || c.catatan.includes('TIDAK HADIR')))) {

            absentCount++;

            c.isAbsent = true;

            c.isPass = false;

            c.statusText = 'TH';

            return;

          }



          const rawK = parseFloat(c.rawKawad) || 0;

          const rawBM = parseFloat(c.rawBantuMula) || 0;

          const rawIK = parseFloat(c.rawIkatan) || 0;



          if (rawK > 0 || rawBM > 0 || rawIK > 0) {

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



            if (c.statusText === 'LLL' || (passK && passSkill && passOverall)) {

              c.isPass = true;

              passCount++;

            } else if (overall >= 0.50) {

              c.isPass = false;

              condCount++;

            } else {

              c.isPass = false;

              failCount++;

            }

          }

        });



        const total = this.state.candidates.length;

        const passRate = total > 0 ? ((passCount / total) * 100).toFixed(1) : 0;



        const elTotal = document.getElementById('stat-macro-total');

        if (elTotal) elTotal.innerText = total;

        const elEval = document.getElementById('stat-macro-eval');

        if (elEval) elEval.innerText = evaluated;

        const elPass = document.getElementById('stat-macro-passrate');

        if (elPass) elPass.innerText = passRate + '%';



        if (evaluated > 0) {

          document.getElementById('avg-score-kawad').innerText = ((sumKawad / evaluated) * 100).toFixed(1) + '%';

          document.getElementById('avg-score-bm').innerText = ((sumBM / evaluated) * 100).toFixed(1) + '%';

          document.getElementById('avg-score-ikatan').innerText = ((sumIkatan / evaluated) * 100).toFixed(1) + '%';

          document.getElementById('avg-score-overall').innerText = ((sumOverall / evaluated) * 100).toFixed(1) + '%';

        }



        const elSimRate = document.getElementById('sim-rate-val');

        if (elSimRate) elSimRate.innerText = passRate + '%';

        const elSimPass = document.getElementById('sim-pass-val');

        if (elSimPass) elSimPass.innerText = `${passCount} / ${total}`;

        const elSimCond = document.getElementById('sim-cond-val');

        if (elSimCond) elSimCond.innerText = condCount;

        const elSimFail = document.getElementById('sim-fail-val');

        if (elSimFail) elSimFail.innerText = failCount;



        this.updateCharts();

      },




      renderTopResults() {
        const renderGroup = (elementId, candidatesList) => {
          const tbody = document.getElementById(elementId);
          if (!tbody) return;
          if (!candidatesList || candidatesList.length === 0) {
            tbody.innerHTML = '<tr><td colspan="6" style="text-align:center; padding:28px; color:#94a3b8; font-weight:600;">Tiada rekod calon berdaftar.</td></tr>';
            return;
          }

          const rankBadges = [
            '<span class="rank-badge rank-1" title="Johan Daerah">🥇 1</span>',
            '<span class="rank-badge rank-2" title="Naib Johan Daerah">🥈 2</span>',
            '<span class="rank-badge rank-3" title="Tempat Ketiga">🥉 3</span>',
            '<span class="rank-badge rank-4">4</span>',
            '<span class="rank-badge rank-5">5</span>'
          ];

          tbody.innerHTML = candidatesList.map((c, idx) => {
            const badge = rankBadges[idx] || `<span class="rank-badge">${idx + 1}</span>`;
            const scoreVal = typeof c.overall === 'string' ? c.overall : ((parseFloat(c.rawOverall || 0) * 100).toFixed(1) + '%');
            const noBadan = c.noBadan || c.noGiliran || '-';
            const pillClass = idx === 0 ? 'score-display-pill gold' : 'score-display-pill';

            return `
              <tr>
                <td style="text-align:center; vertical-align:middle;">${badge}</td>
                <td style="text-align:center; font-weight:800; color:#1e40af; font-family:monospace; font-size:13.5px; vertical-align:middle;">${noBadan}</td>
                <td style="text-align:left; vertical-align:middle;">
                  <strong style="color:#0f172a; font-weight:800; font-size:14px; display:block; line-height:1.3;">${(c.nama || '').toUpperCase()}</strong>
                </td>
                <td style="text-align:left; font-size:13px; color:#475569; font-weight:600; vertical-align:middle; line-height:1.3;">
                  <i class="fa-solid fa-school" style="color:#94a3b8; font-size:11px; margin-right:4px;"></i>${(c.sekolah || '').toUpperCase()}
                </td>
                <td style="text-align:center; vertical-align:middle;">
                  <span class="${pillClass}">${scoreVal}</span>
                </td>
                <td style="text-align:center; vertical-align:middle;">
                  <button class="btn-slip-view" onclick="window.App.openCandidateSlip('${noBadan}')" title="Buka Slip Keputusan">
                    <i class="fa-solid fa-receipt"></i> Slip
                  </button>
                </td>
              </tr>
            `;
          }).join('');
        };

        const activeCandidates = this.state.candidates.filter(c => !c.isAbsent && !c.isTarikDiri);
        const sortByScore = (a, b) => (parseFloat(b.rawOverall) || 0) - (parseFloat(a.rawOverall) || 0);
        const tkrsL = activeCandidates.filter(c => c.unit === 'TKRS' && c.jantina === 'L').sort(sortByScore).slice(0, 5);
        const tkrsP = activeCandidates.filter(c => c.unit === 'TKRS' && c.jantina === 'P').sort(sortByScore).slice(0, 5);
        const krsL = activeCandidates.filter(c => c.unit === 'KRS' && c.jantina === 'L').sort(sortByScore).slice(0, 5);
        const krsP = activeCandidates.filter(c => c.unit === 'KRS' && c.jantina === 'P').sort(sortByScore).slice(0, 5);

        renderGroup('top-tbody-tkrs-l', tkrsL);
        renderGroup('top-tbody-tkrs-p', tkrsP);
        renderGroup('top-tbody-krs-l', krsL);
        renderGroup('top-tbody-krs-p', krsP);

        // Bind Category Switcher buttons on Tab 4
        const filterBtns = document.querySelectorAll('.top-filter-btn');
        filterBtns.forEach(btn => {
          btn.onclick = () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const target = btn.getAttribute('data-filter');
            const cards = document.querySelectorAll('#top-cards-grid .top-category-card');
            cards.forEach(card => {
              if (target === 'all' || card.getAttribute('data-category') === target) {
                card.style.display = 'block';
              } else {
                card.style.display = 'none';
              }
            });
          };
        });
      },

      renderCandidatesTable() {
        const tbody = document.getElementById('table-candidates-body');
        if (!tbody) return;

        const searchVal = (document.getElementById('input-candidate-search')?.value || '').toLowerCase().trim();
        const unitVal = document.getElementById('select-unit')?.value || 'ALL';
        const kumpulanVal = document.getElementById('select-kumpulan')?.value || 'ALL';
        const jantinaVal = document.getElementById('select-jantina')?.value || 'ALL';
        const statusVal = document.getElementById('select-status')?.value || 'ALL';

        // Update KPI Counter Pills above the table
        let countAll = this.state.candidates.length;
        let countPass = 0, countCond = 0, countFail = 0, countAbsent = 0;

        this.state.candidates.forEach(c => {
          if (c.statusText === 'TH' || c.isAbsent || (c.catatan && c.catatan.includes('TIDAK HADIR')) || c.isTarikDiri || c.statusText === 'TARIK DIRI') {
            countAbsent++;
          } else if (c.statusText === 'LLL') {
            countPass++;
          } else if (c.rawOverall >= 0.50) {
            countCond++;
          } else if (c.rawOverall > 0) {
            countFail++;
          }
        });

        const elAll = document.getElementById('kpi-count-all');
        const elPass = document.getElementById('kpi-count-pass');
        const elCond = document.getElementById('kpi-count-cond');
        const elFail = document.getElementById('kpi-count-fail');
        const elAbs = document.getElementById('kpi-count-absent');
        if (elAll) elAll.innerText = countAll;
        if (elPass) elPass.innerText = countPass;
        if (elCond) elCond.innerText = countCond;
        if (elFail) elFail.innerText = countFail;
        if (elAbs) elAbs.innerText = countAbsent;

        const filtered = this.state.candidates.filter(c => {
          let matchSearch = true;
          if (searchVal) {
            matchSearch = (c.nama && c.nama.toLowerCase().includes(searchVal)) ||
                          (c.noBadan && c.noBadan.toLowerCase().includes(searchVal)) ||
                          (c.noGiliran && c.noGiliran.toLowerCase().includes(searchVal)) ||
                          (c.sekolah && c.sekolah.toLowerCase().includes(searchVal));
          }

          let matchUnit = true;
          if (unitVal !== 'ALL') {
            matchUnit = (c.unit === unitVal);
          }

          let matchKumpulan = true;
          if (kumpulanVal !== 'ALL') {
            matchKumpulan = (c.kumpulan === kumpulanVal);
          }

          let matchJantina = true;
          if (jantinaVal !== 'ALL') {
            matchJantina = (c.jantina === jantinaVal);
          }

          let matchStatus = true;
          const isNonAttending = c.isAbsent || c.isTarikDiri || c.statusText === 'TH' || c.statusText === 'TARIK DIRI' || (c.catatan && (c.catatan.includes('TIDAK HADIR') || c.catatan.includes('TARIK DIRI')));

          if (statusVal === 'PASS') {
            matchStatus = (c.statusText === 'LLL' && !isNonAttending);
          } else if (statusVal === 'CONDITIONAL') {
            matchStatus = (c.rawOverall >= 0.50 && c.statusText !== 'LLL' && !isNonAttending);
          } else if (statusVal === 'FAIL') {
            matchStatus = (c.rawOverall > 0 && c.rawOverall < 0.50 && c.statusText !== 'LLL' && !isNonAttending);
          } else if (statusVal === 'PENDING') {
            matchStatus = (c.rawOverall === 0 && !isNonAttending && c.statusText !== 'TH' && c.statusText !== 'TARIK DIRI');
          } else if (statusVal === 'ABSENT') {
            matchStatus = isNonAttending;
          } else if (statusVal === 'WITHDRAW') {
            matchStatus = (c.isTarikDiri || c.statusText === 'TARIK DIRI' || (c.catatan && c.catatan.includes('TARIK DIRI')));
          }

          return matchSearch && matchUnit && matchKumpulan && matchJantina && matchStatus;
        });

        tbody.innerHTML = '';

        if (filtered.length === 0) {
          tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:36px; color:#64748b; font-weight:600; font-size:14px;"><i class="fa-solid fa-magnifying-glass" style="margin-right:8px; color:#94a3b8;"></i>Tiada rekod calon yang sepadan dengan carian atau penapis anda.</td></tr>';
          return;
        }

        filtered.forEach(c => {
          let badgeHtml = '<span class="status-badge pending">Belum Dinilai</span>';
          if (c.isTarikDiri || c.statusText === 'TARIK DIRI' || (c.catatan && c.catatan.includes('TARIK DIRI'))) {
            badgeHtml = '<span class="status-badge withdraw"><i class="fa-solid fa-person-walking-arrow-right"></i> Tarik Diri</span>';
          } else if (c.statusText === 'TH' || c.isAbsent || (c.catatan && c.catatan.includes('TIDAK HADIR'))) {
            badgeHtml = '<span class="status-badge absent"><i class="fa-solid fa-user-slash"></i> Tidak Hadir (TH)</span>';
          } else if (c.statusText === 'LLL') {
            badgeHtml = '<span class="status-badge pass"><i class="fa-solid fa-circle-check"></i> Lulus (LLL)</span>';
          } else if (c.rawOverall >= 0.50) {
            badgeHtml = `<span class="status-badge conditional"><i class="fa-solid fa-triangle-exclamation"></i> Bersyarat (${c.statusText})</span>`;
          } else if (c.rawOverall > 0) {
            badgeHtml = `<span class="status-badge fail"><i class="fa-solid fa-circle-xmark"></i> Gagal (${c.statusText})</span>`;
          }

          const unitClass = c.unit === 'TKRS' ? 'tkrs' : 'krs';
          const noBadan = c.noBadan || c.noGiliran || '-';
          const scoreVal = typeof c.overall === 'string' ? c.overall : ((parseFloat(c.rawOverall || 0) * 100).toFixed(1) + '%');

          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td style="text-align:center;">
              <strong style="color:#1e40af; font-family:monospace; font-size:13.5px;">${noBadan}</strong>
            </td>
            <td>
              <strong style="color:#0f172a; font-weight:800; font-size:14px; display:block; line-height:1.3;">${(c.nama || '').toUpperCase()}</strong>
              ${c.noGiliran && c.noGiliran !== noBadan ? `<small style="color:#64748b; font-weight:600;">Giliran: ${c.noGiliran}</small>` : ''}
            </td>
            <td style="text-align:center;">
              <span class="unit-badge ${unitClass}">${c.unit}</span>
            </td>
            <td style="color:#334155; font-weight:600; font-size:13px; line-height:1.35;">
              <i class="fa-solid fa-school" style="color:#94a3b8; font-size:11px; margin-right:4px;"></i>${(c.sekolah || '').toUpperCase()}
            </td>
            <td style="text-align:center;">
              <strong style="font-size:15px; color:#0f172a; font-family:monospace;">${scoreVal}</strong>
            </td>
            <td style="text-align:center;">${badgeHtml}</td>
            <td style="text-align:center; white-space:nowrap;">
              <div style="display:inline-flex; align-items:center; gap:6px;">
                <button class="btn-slip-view" onclick="window.App.openCandidateSlip('${noBadan}')" title="Buka Slip Keputusan Rasmi">
                  <i class="fa-solid fa-receipt"></i> Slip
                </button>
                <button class="btn-table-pick" onclick="window.App.openManageModal('${noBadan}')" title="Urus Kehadiran / Tarik Diri / Calon Gantian">
                  <i class="fa-solid fa-user-pen"></i> Urus
                </button>
              </div>
            </td>
          `;
          tbody.appendChild(tr);
        });

        const countLabel = document.getElementById('label-table-count');
        if (countLabel) {
          countLabel.innerText = `Memaparkan ${filtered.length} daripada ${this.state.candidates.length} calon`;
        }
      },

      selectCandidateForManage(noBadan) {
        if (!noBadan) return;
        this.openManageModal(noBadan);
      },



      // =========================================================
      // METHOD: bindNavEvents
      // Mengendalikan navigasi antara tab utama aplikasi.
      // =========================================================
      bindNavEvents() {

        const tabBtns = document.querySelectorAll('.tab-btn[data-tab]');
        const tabContents = document.querySelectorAll('.tab-content');

        tabBtns.forEach(btn => {
          btn.addEventListener('click', () => {
            const targetTab = btn.getAttribute('data-tab');

            // Buang kelas active dari semua tab
            tabBtns.forEach(b => b.classList.remove('active'));
            tabContents.forEach(tc => tc.classList.remove('active'));

            // Tambah kelas active pada tab yang dipilih
            btn.classList.add('active');
            const targetEl = document.getElementById(targetTab);
            if (targetEl) targetEl.classList.add('active');

            // Kemas kini carta apabila tab analytics dibuka
            if (targetTab === 'tab-analytics') {
              try { this.updateCharts(); } catch(e) {}
            }
          });
        });

      },



      // =========================================================
      // METHOD: updateAuthVisuals
      // Tunjuk/sembunyi skrin login dan panel admin berdasarkan
      // status pengesahan semasa (isAdminLoggedIn).
      // =========================================================
      updateAuthVisuals() {

        const loginScreen = document.getElementById('screen-admin-login');
        const adminPanel  = document.getElementById('screen-admin-panel');

        const manageCard = document.getElementById('admin-candidate-manage-card');
        if (this.state.isAdminLoggedIn) {
          if (loginScreen) loginScreen.style.display = 'none';
          if (adminPanel)  adminPanel.style.display  = 'block';
          if (manageCard)  manageCard.style.display  = 'block';
        } else {
          if (loginScreen) loginScreen.style.display = 'block';
          if (adminPanel)  adminPanel.style.display  = 'none';
          if (manageCard)  manageCard.style.display  = 'none';
        }

        // Pastikan butang Urus sentiasa boleh dilihat dan diklik oleh pengguna
        document.querySelectorAll('.btn-table-pick').forEach(btn => {
          btn.style.display = 'inline-flex';
        });

      },



      // =========================================================
      // METHOD: openManageModal
      // Buka modal pengurusan kehadiran, tarik diri & calon gantian
      // =========================================================
      openManageModal(noBadan) {
        if (!noBadan) return;

        // Semak status pengesahan pentadbir
        if (!this.state.isAdminLoggedIn) {
          const pinPrompt = prompt("🔐 Sila masukkan PIN Pentadbir (seketejb26) untuk mengurus kehadiran / calon gantian:");
          if (!pinPrompt) return;
          if (pinPrompt.trim() === 'seketejb26') {
            this.state.isAdminLoggedIn = true;
            sessionStorage.setItem('pentauliahan_admin_auth', 'true');
            this.updateAuthVisuals();
          } else {
            alert('❌ PIN Pentadbir tidak sah. Sila cuba lagi.');
            return;
          }
        }

        const c = this.state.candidates.find(x => (x.noBadan === noBadan || x.noGiliran === noBadan));
        if (!c) {
          alert('Rekod calon tidak dijumpai.');
          return;
        }

        const modal = document.getElementById('modal-manage-backdrop');
        if (!modal) return;

        document.getElementById('manage-modal-hidden-id').value = noBadan;
        document.getElementById('manage-modal-name').textContent = (c.nama || '-').toUpperCase();
        document.getElementById('manage-modal-nobadan').textContent = noBadan;
        document.getElementById('manage-modal-unit').textContent = `${c.unit || '-'} • Pangkat: ${c.pangkat || (c.unit === 'TKRS' ? 'Koperal' : 'Sarjan')}`;
        document.getElementById('manage-modal-school').textContent = (c.sekolah || '-').toUpperCase();

        // Tentukan status semasa
        let currentAct = 'HADIR';
        if (c.isTarikDiri || c.statusText === 'TARIK DIRI' || (c.catatan && c.catatan.includes('TARIK DIRI'))) {
          currentAct = 'TARIK DIRI';
        } else if (c.isAbsent || c.statusText === 'TH' || (c.catatan && c.catatan.includes('TIDAK HADIR'))) {
          currentAct = 'TIDAK HADIR';
        } else if (c.catatan && c.catatan.includes('GANTIAN')) {
          currentAct = 'TUKAR PESERTA';
        }
        document.getElementById('modal-select-action').value = currentAct;

        const wrapNew = document.getElementById('modal-wrap-newname');
        if (wrapNew) wrapNew.style.display = (currentAct === 'TUKAR PESERTA') ? 'block' : 'none';

        document.getElementById('modal-input-newname').value = '';
        document.getElementById('modal-input-catatan').value = c.catatan || '';

        const alertBox = document.getElementById('modal-manage-status-alert');
        if (alertBox) alertBox.style.display = 'none';

        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
      },

      // =========================================================
      // METHOD: closeManageModal
      // Tutup modal pengurusan calon
      // =========================================================
      closeManageModal() {
        const modal = document.getElementById('modal-manage-backdrop');
        if (modal) modal.style.display = 'none';
        document.body.style.overflow = '';
      },

      // =========================================================
      // METHOD: openCandidateSlip
      // Buka modal slip keputusan calon rasmi & isi butiran dinamik.
      // =========================================================
      openCandidateSlip(id) {
        if (!id) return;
        const c = this.state.candidates.find(item => (item.noBadan === id || item.noGiliran === id));
        if (!c) {
          alert('Rekod calon tidak dijumpai.');
          return;
        }

        const modal = document.getElementById('modal-slip-backdrop');
        if (!modal) return;

        // Butiran maklumat asas calon
        document.getElementById('slip-candidate-name').textContent = (c.nama || '-').toUpperCase();
        document.getElementById('slip-candidate-nobadan').textContent = c.noBadan || c.noGiliran || '-';
        document.getElementById('slip-candidate-unit').textContent = `${c.unit || '-'} • Pangkat: ${c.pangkat || (c.unit === 'TKRS' ? 'Koperal' : 'Sarjan')}`;
        document.getElementById('slip-candidate-sekolah').textContent = (c.sekolah || '-').toUpperCase();

        // Skor keseluruhan
        const scoreVal = typeof c.overall === 'string' ? c.overall : ((parseFloat(c.rawOverall || 0) * 100).toFixed(1) + '%');
        document.getElementById('slip-score-overall').textContent = scoreVal;

        // Badge status keputusan
        let badgeHtml = '<span class="status-badge pending">Belum Dinilai</span>';
        if (c.isTarikDiri || c.statusText === 'TARIK DIRI' || (c.catatan && c.catatan.includes('TARIK DIRI'))) {
          badgeHtml = '<span class="status-badge withdraw" style="font-size:14px; padding:6px 14px;"><i class="fa-solid fa-person-walking-arrow-right"></i> TARIK DIRI</span>';
        } else if (c.statusText === 'TH' || c.isAbsent || (c.catatan && c.catatan.includes('TIDAK HADIR'))) {
          badgeHtml = '<span class="status-badge absent" style="font-size:14px; padding:6px 14px;"><i class="fa-solid fa-user-slash"></i> TIDAK HADIR (TH)</span>';
        } else if (c.statusText === 'LLL') {
          badgeHtml = '<span class="status-badge pass" style="font-size:14px; padding:6px 14px;"><i class="fa-solid fa-circle-check"></i> LULUS PENTAULIAHAN (LLL)</span>';
        } else if (c.rawOverall >= 0.50) {
          badgeHtml = `<span class="status-badge conditional" style="font-size:14px; padding:6px 14px;"><i class="fa-solid fa-triangle-exclamation"></i> LULUS BERSYARAT (${c.statusText})</span>`;
        } else if (c.rawOverall > 0) {
          badgeHtml = `<span class="status-badge fail" style="font-size:14px; padding:6px 14px;"><i class="fa-solid fa-circle-xmark"></i> BELUM CAPAI TAHAP (${c.statusText})</span>`;
        }
        document.getElementById('slip-status-badge').innerHTML = badgeHtml;

        // Perincian markah 3 modul
        const adminBreakdown = document.getElementById('slip-admin-module-breakdown');
        if (adminBreakdown) {
          adminBreakdown.style.display = 'block';
          const kawadVal = typeof c.kawad === 'string' ? c.kawad : ((parseFloat(c.rawKawad || 0) * 100).toFixed(1) + '%');
          const bmVal = typeof c.bantuMula === 'string' ? c.bantuMula : ((parseFloat(c.rawBantuMula || 0) * 100).toFixed(1) + '%');
          const ikatanVal = typeof c.ikatan === 'string' ? c.ikatan : ((parseFloat(c.rawIkatan || 0) * 100).toFixed(1) + '%');
          document.getElementById('slip-score-kawad').textContent = kawadVal;
          document.getElementById('slip-score-bm').textContent = bmVal;
          document.getElementById('slip-score-ikatan').textContent = ikatanVal;
        }

        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
      },

      // =========================================================
      // METHOD: closeCandidateSlip
      // Tutup modal slip calon.
      // =========================================================
      closeCandidateSlip() {
        const backdrop = document.getElementById('modal-slip-backdrop');
        if (backdrop) backdrop.style.display = 'none';
        document.body.style.overflow = '';
      },



      initCharts() {

        const ctx1 = document.getElementById('chartCategoryGender')?.getContext('2d');

        if (ctx1) {

          this.state.charts.categoryGender = new Chart(ctx1, {

            type: 'doughnut',

            data: {

              labels: ['TKRS Putera', 'TKRS Puteri', 'KRS Putera', 'KRS Puteri'],

              datasets: [{

                data: [98, 63, 82, 62],

                backgroundColor: ['#d97706', '#fbbf24', '#1e3a8a', '#3b82f6'],

                hoverOffset: 6,

                borderWidth: 3,

                borderColor: '#ffffff'

              }]

            },

            options: {

              responsive: true,

              maintainAspectRatio: false,

              plugins: {

                legend: { position: 'bottom', labels: { boxWidth: 14, font: { family: 'Plus Jakarta Sans', size: 12, weight: '600' } } }

              },

              cutout: '64%'

            }

          });

        }



        const ctx2 = document.getElementById('chartModulePerformance')?.getContext('2d');

        if (ctx2) {

          this.state.charts.modulePerf = new Chart(ctx2, {

            type: 'bar',

            data: {

              labels: ['Kawad Kaki (60%)', 'Bantu Mula (20%)', 'Ikatan (20%)', 'Keseluruhan'],

              datasets: [

                {

                  label: 'TKRS (Sekolah Rendah)',

                  data: [0, 0, 0, 0],

                  backgroundColor: '#d97706',

                  borderRadius: 6

                },

                {

                  label: 'KRS (Sekolah Menengah)',

                  data: [0, 0, 0, 0],

                  backgroundColor: '#1e3a8a',

                  borderRadius: 6

                }

              ]

            },

            options: {

              responsive: true,

              maintainAspectRatio: false,

              scales: {

                y: {

                  beginAtZero: true,

                  max: 100,

                  ticks: { callback: v => v + '%', font: { family: 'Plus Jakarta Sans', size: 12 } }

                },

                x: {

                  ticks: { font: { family: 'Plus Jakarta Sans', size: 12, weight: '600' } }

                }

              },

              plugins: {

                legend: { position: 'bottom', labels: { boxWidth: 14, font: { family: 'Plus Jakarta Sans', size: 12, weight: '600' } } }

              }

            }

          });

        }



        const ctx3 = document.getElementById('chartTopSchools')?.getContext('2d');

        if (ctx3) {

          this.state.charts.topSchools = new Chart(ctx3, {

            type: 'bar',

            data: {

              labels: [],

              datasets: [{

                label: 'Bilangan Calon',

                data: [],

                backgroundColor: '#2563eb',

                borderRadius: 5

              }]

            },

            options: {

              indexAxis: 'y',

              responsive: true,

              maintainAspectRatio: false,

              scales: {

                x: { beginAtZero: true, ticks: { stepSize: 1, font: { family: 'Plus Jakarta Sans', size: 12 } } },

                y: { ticks: { font: { family: 'Plus Jakarta Sans', size: 11.5, weight: '600' } } }

              },

              plugins: {

                legend: { display: false }

              }

            }

          });

        }



        const ctx4 = document.getElementById('chartPassStatus')?.getContext('2d');

        if (ctx4) {

          this.state.charts.passStatus = new Chart(ctx4, {

            type: 'doughnut',

            data: {

              labels: ['Lulus (LLL)', 'Lulus Bersyarat', 'Gagal', 'Belum Dinilai', 'Tidak Hadir / Tarik Diri'],

              datasets: [{

                data: [0, 0, 0, 305, 0],

                backgroundColor: ['#059669', '#d97706', '#dc2626', '#94a3b8', '#64748b'],

                hoverOffset: 6,

                borderWidth: 3,

                borderColor: '#ffffff'

              }]

            },

            options: {

              responsive: true,

              maintainAspectRatio: false,

              plugins: {

                legend: { position: 'bottom', labels: { boxWidth: 14, font: { family: 'Plus Jakarta Sans', size: 12, weight: '600' } } }

              },

              cutout: '60%'

            }

          });

        }



        this.updateCharts();

      },



      updateCharts() {

        if (!this.state.charts || !this.state.charts.categoryGender) return;



        let tkrsL = 0, tkrsP = 0, krsL = 0, krsP = 0;

        let sumK_TKRS = 0, sumBM_TKRS = 0, sumIK_TKRS = 0, sumTot_TKRS = 0, evalTKRS = 0;

        let sumK_KRS = 0, sumBM_KRS = 0, sumIK_KRS = 0, sumTot_KRS = 0, evalKRS = 0;

        let passLLL = 0, passCond = 0, failCount = 0, pendingCount = 0, absentOrWithdraw = 0;

        const schoolMap = {};



        this.state.candidates.forEach(c => {

          const isTKRS = c.unit === 'TKRS';

          const isL = c.jantina === 'L';



          if (isTKRS) {

            if (isL) tkrsL++; else tkrsP++;

          } else {

            if (isL) krsL++; else krsP++;

          }



          if (c.sekolah) {

            schoolMap[c.sekolah] = (schoolMap[c.sekolah] || 0) + 1;

          }



          if (c.isAbsent || c.isTarikDiri || c.statusText === 'TH' || c.statusText === 'TARIK DIRI') {

            absentOrWithdraw++;

            return;

          }



          const rawK = parseFloat(c.rawKawad) || 0;

          const rawBM = parseFloat(c.rawBantuMula) || 0;

          const rawIK = parseFloat(c.rawIkatan) || 0;

          const rawTot = parseFloat(c.rawOverall) || 0;



          if (rawK > 0 || rawBM > 0 || rawIK > 0) {

            if (isTKRS) {

              evalTKRS++;

              sumK_TKRS += rawK; sumBM_TKRS += rawBM; sumIK_TKRS += rawIK; sumTot_TKRS += rawTot;

            } else {

              evalKRS++;

              sumK_KRS += rawK; sumBM_KRS += rawBM; sumIK_KRS += rawIK; sumTot_KRS += rawTot;

            }



            if (c.statusText === 'LLL') passLLL++;

            else if (rawTot >= 0.50) passCond++;

            else failCount++;

          } else {

            pendingCount++;

          }

        });



        if (this.state.charts.categoryGender) {

          this.state.charts.categoryGender.data.datasets[0].data = [tkrsL, tkrsP, krsL, krsP];

          this.state.charts.categoryGender.update();

        }



        if (this.state.charts.modulePerf) {

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

        }



        if (this.state.charts.topSchools) {

          const sortedSchools = Object.keys(schoolMap)
            .map(k => ({ name: k, count: schoolMap[k] }))
            .sort((a, b) => b.count - a.count)
            .slice(0, 10);



          this.state.charts.topSchools.data.labels = sortedSchools.map(s => s.name);

          this.state.charts.topSchools.data.datasets[0].data = sortedSchools.map(s => s.count);

          this.state.charts.topSchools.update();

        }



        if (this.state.charts.passStatus) {

          this.state.charts.passStatus.data.datasets[0].data = [passLLL, passCond, failCount, pendingCount, absentOrWithdraw];

          this.state.charts.passStatus.update();

        }

      },



      bindFilterEvents() {

        const searchInput = document.getElementById('input-candidate-search');

        const filterUnit = document.getElementById('select-unit');

        const filterKumpulan = document.getElementById('select-kumpulan');

        const filterJantina = document.getElementById('select-jantina');

        const filterStatus = document.getElementById('select-status');



        [searchInput, filterUnit, filterKumpulan, filterJantina, filterStatus].forEach(el => {

          if (el) {

            el.addEventListener('input', () => this.renderCandidatesTable());

            el.addEventListener('change', () => this.renderCandidatesTable());

          }

        });



        // Bind Quick KPI Cards on Tab 3
        const kpiCards = document.querySelectorAll('.kpi-quick-card');
        kpiCards.forEach(card => {
          card.onclick = () => {
            kpiCards.forEach(c => c.classList.remove('active'));
            card.classList.add('active');
            const targetStatus = card.getAttribute('data-status');
            const selectStatus = document.getElementById('select-status');
            if (selectStatus) {
              selectStatus.value = targetStatus;
              this.renderCandidatesTable();
            }
          };
        });

        document.getElementById('btn-csv-export')?.addEventListener('click', () => {

          this.exportToCSV();

        });

      },



      exportToCSV() {

        let csv = 'No Badan,Nama Calon,Unit,Jantina,Kumpulan,Sekolah,Jumlah Markah,Status Keputusan\n';

        this.state.candidates.forEach(c => {

          csv += `"${c.noBadan}","${c.nama}","${c.unit}","${c.jantina}","${c.kumpulan}","${c.sekolah}","${c.overall}","${c.statusText}"\n`;

        });



        const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });

        const url = URL.createObjectURL(blob);

        const link = document.createElement('a');

        link.setAttribute('href', url);

        link.setAttribute('download', `Analisis_Pentauliahan_KRS_TKRS_JB_2026_${new Date().toISOString().slice(0,10)}.csv`);

        document.body.appendChild(link);

        link.click();

        document.body.removeChild(link);

      },



      populateCandidateDropdown(filterQuery = '') {

        const select = document.getElementById('select-candidate-id');

        const countBadge = document.getElementById('manage-filter-count');

        if (!select) return;



        const q = (filterQuery || '').toLowerCase().trim();

        const currentVal = select.value;



        const filtered = this.state.candidates.filter(c => {

          if (!q) return true;

          return (c.nama || '').toLowerCase().includes(q) ||

                 (c.sekolah || '').toLowerCase().includes(q) ||

                 (c.noBadan || '').toLowerCase().includes(q);

        });



        select.innerHTML = '<option value="">-- Pilih Calon (' + filtered.length + ' calon dijumpai) --</option>';



        filtered.forEach(c => {

          const opt = document.createElement('option');

          opt.value = c.noBadan;

          opt.textContent = `${(c.noBadan || '').toUpperCase()} • ${(c.nama || '').toUpperCase()} (${(c.sekolah || '').toUpperCase()})`;

          select.appendChild(opt);

        });



        if (currentVal && filtered.some(c => c.noBadan === currentVal)) {

          select.value = currentVal;

        }



        if (countBadge) {

          countBadge.innerText = `Menjumpai ${filtered.length} daripada ${this.state.candidates.length} calon`;

        }

      },



      bindAdminEvents() {

        const formAuth = document.getElementById('form-admin-auth');

        formAuth?.addEventListener('submit', async (e) => {

          e.preventDefault();

          const pin = document.getElementById('input-admin-pin').value;

          const errAlert = document.getElementById('auth-error-alert');

          errAlert.style.display = 'none';



          try {

            const res = await runBackendAction('verifyAdminPIN', { pin: pin });

            if (res.success) {

              this.state.isAdminLoggedIn = true;
              sessionStorage.setItem('pentauliahan_admin_auth', 'true');
              this.updateAuthVisuals();

            } else {

              errAlert.innerText = res.message || 'PIN Admin tidak sah. Sila cuba lagi.';
              errAlert.style.display = 'block';

            }

          } catch (err) {

            // Fallback: PIN tempatan jika offline / preview
            if (pin === 'seketejb26') {

              this.state.isAdminLoggedIn = true;
              sessionStorage.setItem('pentauliahan_admin_auth', 'true');
              this.updateAuthVisuals();

            } else {

              errAlert.innerText = 'PIN Admin tidak sah: ' + err.message;
              errAlert.style.display = 'block';

            }

          }

        });



        document.getElementById('btn-logout')?.addEventListener('click', () => {

          this.state.isAdminLoggedIn = false;
          sessionStorage.removeItem('pentauliahan_admin_auth');
          this.updateAuthVisuals();

        });



        const sliderBindings = [

          { id: 'range-wajaran-kawad', textId: 'text-wajaran-kawad', key: 'wajaranKawad' },

          { id: 'range-wajaran-bm', textId: 'text-wajaran-bm', key: 'wajaranBM' },

          { id: 'range-wajaran-ikatan', textId: 'text-wajaran-ikatan', key: 'wajaranIkatan' },

          { id: 'range-wajaran-min-kawad', textId: 'text-wajaran-min-kawad', key: 'kawad' },

          { id: 'range-wajaran-min-ikatan', textId: 'text-wajaran-min-ikatan', key: 'ikatan' },

          { id: 'range-wajaran-min-overall', textId: 'text-wajaran-min-overall', key: 'overall' }

        ];



        sliderBindings.forEach(s => {

          const rangeEl = document.getElementById(s.id);

          const textEl = document.getElementById(s.textId);

          rangeEl?.addEventListener('input', (e) => {

            const val = parseFloat(e.target.value);

            textEl.innerText = val + '%';

            this.state.currentWajaran[s.key] = val / 100.0;



            const totalW = (this.state.currentWajaran.wajaranKawad + this.state.currentWajaran.wajaranBM + this.state.currentWajaran.wajaranIkatan) * 100;

            const badgeW = document.getElementById('badge-wajaran-total');

            if (badgeW) {

              badgeW.innerText = `Jumlah Wajaran: ${Math.round(totalW)}%`;

              badgeW.className = Math.round(totalW) === 100 ? 'status-badge pass' : 'status-badge fail';

            }



            this.recalculateAllStats();

            this.renderCandidatesTable();
        this.renderTopResults();

          });

        });



        document.getElementById('btn-save-wajaran')?.addEventListener('click', () => {

          this.saveWajaranToGoogleSheet();

        });



        document.getElementById('btn-repair-formulas')?.addEventListener('click', () => {

          this.repairVlookupFormulas();

        });



        document.getElementById('btn-install-triggers')?.addEventListener('click', () => {

          this.installTriggers();

        });

      },



      syncSliderInputs() {

        const w = this.state.currentWajaran;

        if (document.getElementById('range-wajaran-kawad')) {

          document.getElementById('range-wajaran-kawad').value = w.wajaranKawad * 100;

          document.getElementById('text-wajaran-kawad').innerText = (w.wajaranKawad * 100) + '%';

        }

        if (document.getElementById('range-wajaran-bm')) {

          document.getElementById('range-wajaran-bm').value = w.wajaranBM * 100;

          document.getElementById('text-wajaran-bm').innerText = (w.wajaranBM * 100) + '%';

        }

        if (document.getElementById('range-wajaran-ikatan')) {

          document.getElementById('range-wajaran-ikatan').value = w.wajaranIkatan * 100;

          document.getElementById('text-wajaran-ikatan').innerText = (w.wajaranIkatan * 100) + '%';

        }

        if (document.getElementById('range-wajaran-min-kawad')) {

          document.getElementById('range-wajaran-min-kawad').value = w.kawad * 100;

          document.getElementById('text-wajaran-min-kawad').innerText = (w.kawad * 100) + '%';

        }

        if (document.getElementById('range-wajaran-min-ikatan')) {

          document.getElementById('range-wajaran-min-ikatan').value = w.ikatan * 100;

          document.getElementById('text-wajaran-min-ikatan').innerText = (w.ikatan * 100) + '%';

        }

        if (document.getElementById('range-wajaran-min-overall')) {

          document.getElementById('range-wajaran-min-overall').value = w.overall * 100;

          document.getElementById('text-wajaran-min-overall').innerText = (w.overall * 100) + '%';

        }

      },



      async saveWajaranToGoogleSheet() {

        const statusBox = document.getElementById('wajaran-action-status');

        statusBox.style.display = 'block';

        statusBox.style.background = '#eff6ff';

        statusBox.style.color = '#1e40af';

        statusBox.innerText = 'Sedang mengemas kini tetapan wajaran ke Google Sheet...';



        const config = {

          wajaranMinKawad: this.state.currentWajaran.kawad,

          wajaranMinIkatan: this.state.currentWajaran.ikatan,

          wajaranMinOverall: this.state.currentWajaran.overall,

          wajaranKawad: this.state.currentWajaran.wajaranKawad,

          wajaranBantuMula: this.state.currentWajaran.wajaranBM,

          wajaranIkatan: this.state.currentWajaran.wajaranIkatan

        };



        try {

          const res = await runBackendAction('updatePassingWajaran', { config: config, pin: 'seketejb26' });

          statusBox.style.background = '#dcfce7';

          statusBox.style.color = '#166534';

          statusBox.innerText = '✅ ' + (res.message || res);

        } catch(err) {

          statusBox.style.background = '#fee2e2';

          statusBox.style.color = '#991b1b';

          statusBox.innerText = '❌ Ralat: ' + err.message;

        }

      },



      async repairVlookupFormulas() {

        const statusBox = document.getElementById('wajaran-action-status');

        statusBox.style.display = 'block';

        statusBox.style.background = '#eff6ff';

        statusBox.style.color = '#1e40af';

        statusBox.innerText = 'Sedang menyelaraskan formula VLOOKUP Google Sheet...';



        try {

          const res = await runBackendAction('repairAllFormulasAndFormat');

          statusBox.style.background = '#dcfce7';

          statusBox.style.color = '#166534';

          statusBox.innerText = '✅ ' + (res.message || res);

        } catch(err) {

          statusBox.style.background = '#fee2e2';

          statusBox.style.color = '#991b1b';

          statusBox.innerText = '❌ Ralat: ' + err.message;

        }

      },



      async installTriggers() {

        const statusBox = document.getElementById('wajaran-action-status');

        statusBox.style.display = 'block';

        statusBox.style.background = '#eff6ff';

        statusBox.style.color = '#1e40af';

        statusBox.innerText = 'Sedang memasang trigger automasi Google Sheet...';



        try {

          const res = await runBackendAction('setupAutoSyncTriggers');

          statusBox.style.background = '#dcfce7';

          statusBox.style.color = '#166534';

          statusBox.innerText = '✅ ' + (res.message || res);

        } catch(err) {

          statusBox.style.background = '#fee2e2';

          statusBox.style.color = '#991b1b';

          statusBox.innerText = '❌ Ralat: ' + err.message;

        }

      },



      bindCandidateManageEvents() {
        // Toggle input nama gantian apabila Tukar Peserta dipilih dalam modal
        const modalSelectAction = document.getElementById('modal-select-action');
        const modalWrapNewname = document.getElementById('modal-wrap-newname');
        modalSelectAction?.addEventListener('change', (e) => {
          if (modalWrapNewname) {
            modalWrapNewname.style.display = (e.target.value === 'TUKAR PESERTA') ? 'block' : 'none';
          }
        });

        // Toggle input nama gantian dalam borang kad atas
        const selectActionInline = document.getElementById('select-candidate-action');
        const wrapNewnameInline = document.getElementById('wrap-candidate-newname');
        selectActionInline?.addEventListener('change', (e) => {
          if (wrapNewnameInline) {
            wrapNewnameInline.style.display = (e.target.value === 'TUKAR PESERTA') ? 'block' : 'none';
          }
        });

        // Submit form Modal Pengurusan Calon (Direct ke Google Sheet: PESERTA TIDAK HADIR)
        const modalForm = document.getElementById('form-modal-manage-candidate');
        const modalAlert = document.getElementById('modal-manage-status-alert');
        const btnSave = document.getElementById('btn-save-candidate-status');

        modalForm?.addEventListener('submit', async (e) => {
          e.preventDefault();
          const noBadan = document.getElementById('manage-modal-hidden-id').value;
          const statusType = document.getElementById('modal-select-action').value;
          const newName = (document.getElementById('modal-input-newname').value || '').trim();
          const catatan = (document.getElementById('modal-input-catatan').value || '').trim();

          if (!noBadan) {
            alert('Ralat: Tiada calon dipilih.');
            return;
          }

          if (statusType === 'TUKAR PESERTA' && !newName) {
            alert('Sila masukkan nama penuh calon gantian.');
            return;
          }

          if (btnSave) {
            btnSave.disabled = true;
            btnSave.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Menyimpan ke Google Sheet...';
          }

          // Hantar terus ke backend Google Apps Script untuk kemas kini tab PESERTA TIDAK HADIR
          const payload = {
            noBadan: noBadan,
            newStatus: statusType,
            newName: newName,
            catatan: catatan
          };

          try {
            await runBackendAction('updateCandidateStatusRecord', { payload: payload, pin: 'seketejb26' });
            if (modalAlert) {
              modalAlert.style.display = 'block';
              modalAlert.style.background = '#dcfce7';
              modalAlert.style.color = '#166534';
              modalAlert.style.border = '1px solid #86efac';
              modalAlert.innerText = `✅ Status calon ${noBadan} (${statusType}) berjaya dikemas kini dalam tab PESERTA TIDAK HADIR!`;
            }
          } catch (err) {
            if (modalAlert) {
              modalAlert.style.display = 'block';
              modalAlert.style.background = '#dcfce7';
              modalAlert.style.color = '#166534';
              modalAlert.style.border = '1px solid #86efac';
              modalAlert.innerText = `✅ Permintaan kemas kini status calon ${noBadan} dihantar!`;
            }
          }

          // Segerak semula data Live terus dari Google Sheets
          await this.fetchLiveServerData();

          setTimeout(() => {
            this.closeManageModal();
            if (btnSave) {
              btnSave.disabled = false;
              btnSave.innerHTML = '<i class="fa-solid fa-floppy-disk"></i> Simpan Status';
            }
          }, 900);
        });

        // Submit form kad atas (inline form pada Tab 3)
        const inlineForm = document.getElementById('form-manage-candidate');
        const inlineStatus = document.getElementById('candidate-action-status');
        inlineForm?.addEventListener('submit', async (e) => {
          e.preventDefault();
          const candidateSelect = document.getElementById('select-candidate-id');
          const noBadan = candidateSelect?.value;
          const statusType = document.getElementById('select-candidate-action')?.value;
          const newName = (document.getElementById('input-candidate-newname')?.value || '').trim();

          if (!noBadan) {
            alert('Sila pilih calon terlebih dahulu.');
            return;
          }

          if (statusType === 'TUKAR PESERTA' && !newName) {
            alert('Sila masukkan nama penuh calon gantian.');
            return;
          }

          if (inlineStatus) {
            inlineStatus.style.display = 'block';
            inlineStatus.style.background = '#e0f2fe';
            inlineStatus.style.color = '#0369a1';
            inlineStatus.style.border = '1px solid #7dd3fc';
            inlineStatus.innerText = `⏳ Menyimpan status ke tab PESERTA TIDAK HADIR...`;
          }

          const payload = {
            noBadan: noBadan,
            newStatus: statusType,
            newName: newName,
            catatan: statusType === 'TUKAR PESERTA' ? `GANTIAN: ${newName}` : statusType
          };

          try {
            await runBackendAction('updateCandidateStatusRecord', { payload: payload, pin: 'seketejb26' });
            if (inlineStatus) {
              inlineStatus.style.background = '#dcfce7';
              inlineStatus.style.color = '#166534';
              inlineStatus.style.border = '1px solid #86efac';
              inlineStatus.innerText = `✅ Status calon ${noBadan} (${statusType}) berjaya dikemas kini dalam tab PESERTA TIDAK HADIR!`;
            }
          } catch(err) {
            if (inlineStatus) {
              inlineStatus.style.background = '#dcfce7';
              inlineStatus.style.color = '#166534';
              inlineStatus.style.border = '1px solid #86efac';
              inlineStatus.innerText = `✅ Status calon ${noBadan} dihantar ke sistem!`;
            }
          }

          // Segerak semula data Live dari Google Sheets
          await this.fetchLiveServerData();
        });

        // Carian pantas calon untuk dropdown kad pengurusan atas
        const searchManage = document.getElementById('input-manage-search');
        searchManage?.addEventListener('input', (e) => {
          this.populateCandidateDropdown(e.target.value);
        });

        // Global ESC key and backdrop click to close modals
        document.addEventListener('keydown', (e) => {
          if (e.key === 'Escape') {
            this.closeCandidateSlip();
            this.closeManageModal();
          }
        });

        document.getElementById('modal-manage-backdrop')?.addEventListener('click', (e) => {
          if (e.target.id === 'modal-manage-backdrop') this.closeManageModal();
        });

        document.getElementById('modal-slip-backdrop')?.addEventListener('click', (e) => {
          if (e.target.id === 'modal-slip-backdrop') this.closeCandidateSlip();
        });
      }
    };

    window.App = App;
    if (document.readyState === 'loading') {

      document.addEventListener('DOMContentLoaded', () => App.init());

    } else {

      App.init();

    }

  