/**
 * =========================================================================
 * SISTEM PENGURUSAN PENTAULIAHAN KRS & TKRS DAERAH JOHOR BAHRU 2026
 * PUSAT KAWALAN, API REAL-TIME, AUTHENTICATION ADMIN & SHEET SYNC ENGINE
 * =========================================================================
 */

// PIN Lalai Pentadbir
var DEFAULT_ADMIN_PIN = "seketejb26";
var SPREADSHEET_ID = "1_YmAJ6XVfBREx4_NDTUWRMXAL1Jgi-1vSFS2528dtW0";

/**
 * Menu Khas Google Sheets apabila fail dibuka
 */
function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('🏛️ PENTAULIAHAN 2026')
    .addItem('🌐 Buka Web App Portal Rasmi', 'openWebAppDirectly')
    .addItem('📊 Buka Pusat Kawalan Eksekutif (Modal)', 'openDashboardModal')
    .addSeparator()
    .addItem('⚡ Baiki Semua Formula VLOOKUP & Markah', 'runRepairFromMenu')
    .addItem('🔄 Segerakkan Markah Penguji Masa Nyata', 'runSyncFromMenu')
    .addItem('🤖 Pasang Automasi Trigger (Auto-Sync)', 'runTriggerFromMenu')
    .addSeparator()
    .addItem('ℹ️ Mengenai Sistem & Skema PPDJB', 'showMengenaiAlert')
    .addToUi();
}

/**
 * Endpoint Utama Web App (doGet) & API Router Universal (Netlify & GAS)
 */
function doGet(e) {
  if (e && e.parameter && (e.parameter.action || e.parameter.format === 'json')) {
    return handleApiRequest(e.parameter.action || 'getDashboardData', e.parameter);
  }

  var template = HtmlService.createTemplateFromFile('Index');
  try {
    template.initialData = getDashboardData();
  } catch (err) {
    template.initialData = null;
  }
  return template.evaluate()
    .setTitle('Portal Eksekutif Pentauliahan Sarjan KRS & Koperal TKRS — PPD Johor Bahru 2026')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1, maximum-scale=1');
}

/**
 * Endpoint POST untuk panggilan API dari Netlify / Luar
 */
function doPost(e) {
  var action = '';
  var params = {};
  if (e && e.postData && e.postData.contents) {
    try {
      var body = JSON.parse(e.postData.contents);
      action = body.action || '';
      params = body.params || body;
    } catch(err) {
      action = e.parameter ? e.parameter.action : '';
      params = e.parameter || {};
    }
  } else if (e && e.parameter) {
    action = e.parameter.action || '';
    params = e.parameter;
  }
  return handleApiRequest(action, params);
}

function handleApiRequest(action, params) {
  var responseData = {};
  params = params || {};

  // Ekstrak payload dalam pelbagai format (JSON string, nested object, atau flat parameter)
  var payload = {};
  if (params.payload) {
    if (typeof params.payload === 'string') {
      try { payload = JSON.parse(params.payload); } catch(e) { payload = {}; }
    } else {
      payload = params.payload;
    }
  } else if (params.noBadan) {
    payload = params;
  }

  var pin = params.pin || payload.pin || 'seketejb26';

  try {
    if (action === 'getDashboardData' || !action) {
      responseData = { success: true, result: getDashboardData() };
    } else if (action === 'verifyAdminPIN') {
      responseData = { success: true, result: verifyAdminPIN(pin) };
    } else if (action === 'updatePassingWajaran') {
      var config = params.config || payload.config || {};
      responseData = { success: true, result: updatePassingWajaran(config, pin) };
    } else if (action === 'updateCandidateStatusRecord') {
      responseData = { success: true, result: updateCandidateStatusRecord(payload, pin) };
    } else if (action === 'repairAllFormulasAndFormat') {
      responseData = { success: true, result: repairAllFormulasAndFormat() };
    } else if (action === 'setupAutoSyncTriggers') {
      responseData = { success: true, result: setupAutoSyncTriggers() };
    } else {
      responseData = { success: false, error: 'Tindakan API tidak dikenali: ' + action };
    }
  } catch(err) {
    responseData = { success: false, error: err.toString() };
  }

  return ContentService.createTextOutput(JSON.stringify(responseData))
    .setMimeType(ContentService.MimeType.JSON);
}

function getActiveWajaranConfig() {
  var props = PropertiesService.getScriptProperties();
  return {
    wajaranMinKawad: parseFloat(props.getProperty('WAJARAN_MIN_KAWAD') || props.getProperty('THRESHOLD_KAWAD') || '0.70'),
    wajaranMinIkatan: parseFloat(props.getProperty('WAJARAN_MIN_IKATAN') || props.getProperty('THRESHOLD_IKATAN') || '0.50'),
    wajaranMinOverall: parseFloat(props.getProperty('WAJARAN_MIN_OVERALL') || props.getProperty('THRESHOLD_OVERALL') || '0.70'),
    wajaranKawad: parseFloat(props.getProperty('WAJARAN_KAWAD') || '0.60'),
    wajaranBantuMula: parseFloat(props.getProperty('WAJARAN_BANTU_MULA') || '0.20'),
    wajaranIkatan: parseFloat(props.getProperty('WAJARAN_IKATAN') || '0.20')
  };
}

function getDashboardData() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  if (!ss) {
    try {
      ss = SpreadsheetApp.openById(SPREADSHEET_ID);
    } catch(e) {}
  }

  var cfg = getActiveWajaranConfig();
  var sheetTKRS = ss ? ss.getSheetByName('ANALISIS_TKRS') : null;
  var sheetKRS = ss ? ss.getSheetByName('ANALISIS_KRS') : null;
  var sheetTKRSKawad = ss ? ss.getSheetByName('MARKAH_TKRS_KAWAD') : null;
  var sheetKRSKawad = ss ? ss.getSheetByName('MARKAH_KRS_KAWAD') : null;

  // Ambil data dan tapis baris kosong (kolum Sekolah mestilah ada nilai)
  var rawDataTKRS = sheetTKRS && sheetTKRS.getLastRow() >= 3 ? sheetTKRS.getRange(3, 1, sheetTKRS.getLastRow() - 2, 12).getValues() : [];
  var rawDataKRS = sheetKRS && sheetKRS.getLastRow() >= 3 ? sheetKRS.getRange(3, 1, sheetKRS.getLastRow() - 2, 12).getValues() : [];
  // PEMBETULAN: Tapis baris kosong supaya getLastRow() tidak mengira baris kosong sebagai calon
  var dataTKRS = rawDataTKRS.filter(function(row) { return row[3] && String(row[3]).trim() !== ''; });
  var dataKRS = rawDataKRS.filter(function(row) { return row[3] && String(row[3]).trim() !== ''; });
  var dataTKRSKawad = sheetTKRSKawad && sheetTKRSKawad.getLastRow() >= 2 ? sheetTKRSKawad.getRange(2, 1, sheetTKRSKawad.getLastRow() - 1, 10).getValues() : [];
  var dataKRSKawad = sheetKRSKawad && sheetKRSKawad.getLastRow() >= 2 ? sheetKRSKawad.getRange(2, 1, sheetKRSKawad.getLastRow() - 1, 10).getValues() : [];

  var stats = {
    timestamp: new Date().toLocaleTimeString('ms-MY', { hour: '2-digit', minute: '2-digit', second: '2-digit' }),
    totalCandidates: dataTKRS.length + dataKRS.length,
    totalTKRS: dataTKRS.length,
    totalKRS: dataKRS.length,
    totalSchools: 0,
    evaluatedCount: 0,
    pendingCount: 0,
    absentCount: 0,
    tarikDiriCount: 0,
    tukarPesertaCount: 0,
    passCountTKRS: 0,
    failCountTKRS: 0,
    passCountKRS: 0,
    failCountKRS: 0,
    totalPassCount: 0,
    totalFailCount: 0,
    passRate: 0,
    avgKawadTKRS: 0,
    avgBantuMulaTKRS: 0,
    avgIkatanTKRS: 0,
    avgOverallTKRS: 0,
    avgKawadKRS: 0,
    avgBantuMulaKRS: 0,
    avgIkatanKRS: 0,
    avgOverallKRS: 0,
    maleTKRS: 0,
    femaleTKRS: 0,
    maleKRS: 0,
    femaleKRS: 0,
    schoolStats: {},
    kumpulanStats: {
      total: 0,
      tkrs: {},
      krs: {}
    },
    wajaran: cfg,
    candidates: []
  };

  var schoolSet = {};
  var sumKawadTKRS = 0, sumBMTKRS = 0, sumIkatanTKRS = 0, sumOverallTKRS = 0, evaluatedTKRS = 0;
  var sumKawadKRS = 0, sumBMKRS = 0, sumIkatanKRS = 0, sumOverallKRS = 0, evaluatedKRS = 0;

  // Demografi Kumpulan TKRS & KRS
  dataTKRSKawad.forEach(function(row) {
    var jantina = String(row[5] || '').toUpperCase();
    var kumpulan = String(row[7] || '').trim();
    if (kumpulan) {
      if (!stats.kumpulanStats.tkrs[kumpulan]) stats.kumpulanStats.tkrs[kumpulan] = { total: 0, male: 0, female: 0 };
      stats.kumpulanStats.tkrs[kumpulan].total++;
      if (jantina === 'L' || jantina === 'LELAKI') stats.kumpulanStats.tkrs[kumpulan].male++;
      else if (jantina === 'P' || jantina === 'PEREMPUAN') stats.kumpulanStats.tkrs[kumpulan].female++;
    }
  });

  dataKRSKawad.forEach(function(row) {
    var jantina = String(row[5] || '').toUpperCase();
    var kumpulan = String(row[7] || '').trim();
    if (kumpulan) {
      if (!stats.kumpulanStats.krs[kumpulan]) stats.kumpulanStats.krs[kumpulan] = { total: 0, male: 0, female: 0 };
      stats.kumpulanStats.krs[kumpulan].total++;
      if (jantina === 'L' || jantina === 'LELAKI') stats.kumpulanStats.krs[kumpulan].male++;
      else if (jantina === 'P' || jantina === 'PEREMPUAN') stats.kumpulanStats.krs[kumpulan].female++;
    }
  });

  stats.kumpulanStats.total = Object.keys(stats.kumpulanStats.tkrs).length + Object.keys(stats.kumpulanStats.krs).length;

  // Pemprosesan Data Calon TKRS
  dataTKRS.forEach(function(row, idx) {
    var noGiliran = row[1];
    var nama = row[2];
    var sekolah = row[3];
    var jantina = row[4];
    var kawad = typeof row[6] === 'number' ? row[6] : 0;
    var bantuMula = typeof row[7] === 'number' ? row[7] : 0;
    var ikatan = typeof row[8] === 'number' ? row[8] : 0;
    var overall = typeof row[9] === 'number' ? row[9] : 0;
    var statusText = String(row[10] || '');
    var catatan = String(row[11] || '');

    if (sekolah) schoolSet[sekolah] = true;
    var isEvaluated = (kawad > 0 || bantuMula > 0 || ikatan > 0);
    var isAbsent = catatan.toUpperCase().indexOf('TH') !== -1 || catatan.toUpperCase().indexOf('TIDAK HADIR') !== -1;
    var isTarikDiri = catatan.toUpperCase().indexOf('TARIK DIRI') !== -1;
    var isTukar = catatan.toUpperCase().indexOf('GANTIAN') !== -1 || catatan.toUpperCase().indexOf('TUKAR') !== -1;

    if (isAbsent) stats.absentCount++;
    if (isTarikDiri) stats.tarikDiriCount++;
    if (isTukar) stats.tukarPesertaCount++;

    var j = String(jantina).toUpperCase();
    if (j === 'L' || j === 'LELAKI') stats.maleTKRS++;
    else if (j === 'P' || j === 'PEREMPUAN') stats.femaleTKRS++;

    if (sekolah) {
      if (!stats.schoolStats[sekolah]) stats.schoolStats[sekolah] = { total: 0, tkrs: 0, krs: 0, male: 0, female: 0 };
      stats.schoolStats[sekolah].total++;
      stats.schoolStats[sekolah].tkrs++;
      if (j === 'L' || j === 'LELAKI') stats.schoolStats[sekolah].male++;
      else if (j === 'P' || j === 'PEREMPUAN') stats.schoolStats[sekolah].female++;
    }

    var bmIkatanAvg = (bantuMula + ikatan) / 2;
    var isPass = (kawad >= cfg.wajaranMinKawad && bmIkatanAvg >= cfg.wajaranMinIkatan && overall >= cfg.wajaranMinOverall);
    if (statusText === 'LLL' || isPass) {
      stats.passCountTKRS++;
      stats.totalPassCount++;
    } else {
      stats.failCountTKRS++;
      stats.totalFailCount++;
    }

    if (isEvaluated) {
      evaluatedTKRS++;
      stats.evaluatedCount++;
      sumKawadTKRS += kawad;
      sumBMTKRS += bantuMula;
      sumIkatanTKRS += ikatan;
      sumOverallTKRS += overall;
    } else {
      stats.pendingCount++;
    }

    stats.candidates.push({
      unit: 'TKRS',
      pangkat: 'Koperal',
      rowIdx: idx + 3,
      noGiliran: noGiliran,
      nama: nama,
      jantina: jantina,
      sekolah: sekolah,
      kawad: (kawad * 100).toFixed(1) + '%',
      bantuMula: (bantuMula * 100).toFixed(1) + '%',
      ikatan: (ikatan * 100).toFixed(1) + '%',
      overall: (overall * 100).toFixed(1) + '%',
      rawKawad: kawad,
      rawBantuMula: bantuMula,
      rawIkatan: ikatan,
      rawOverall: overall,
      isPass: isPass,
      statusText: statusText,
      catatan: catatan,
      isEvaluated: isEvaluated,
      isAbsent: isAbsent,
      isTarikDiri: isTarikDiri,
      isTukar: isTukar
    });
  });

  // Pemprosesan Data Calon KRS
  dataKRS.forEach(function(row, idx) {
    var noGiliran = row[1];
    var nama = row[2];
    var sekolah = row[3];
    var jantina = row[4];
    var kawad = typeof row[6] === 'number' ? row[6] : 0;
    var bantuMula = typeof row[7] === 'number' ? row[7] : 0;
    var ikatan = typeof row[8] === 'number' ? row[8] : 0;
    var overall = typeof row[9] === 'number' ? row[9] : 0;
    var statusText = String(row[10] || '');
    var catatan = String(row[11] || '');

    if (sekolah) schoolSet[sekolah] = true;
    var isEvaluated = (kawad > 0 || bantuMula > 0 || ikatan > 0);
    var isAbsent = catatan.toUpperCase().indexOf('TH') !== -1 || catatan.toUpperCase().indexOf('TIDAK HADIR') !== -1;
    var isTarikDiri = catatan.toUpperCase().indexOf('TARIK DIRI') !== -1;
    var isTukar = catatan.toUpperCase().indexOf('GANTIAN') !== -1 || catatan.toUpperCase().indexOf('TUKAR') !== -1;

    if (isAbsent) stats.absentCount++;
    if (isTarikDiri) stats.tarikDiriCount++;
    if (isTukar) stats.tukarPesertaCount++;

    var jk = String(jantina).toUpperCase();
    if (jk === 'L' || jk === 'LELAKI') stats.maleKRS++;
    else if (jk === 'P' || jk === 'PEREMPUAN') stats.femaleKRS++;

    if (sekolah) {
      if (!stats.schoolStats[sekolah]) stats.schoolStats[sekolah] = { total: 0, tkrs: 0, krs: 0, male: 0, female: 0 };
      stats.schoolStats[sekolah].total++;
      stats.schoolStats[sekolah].krs++;
      if (jk === 'L' || jk === 'LELAKI') stats.schoolStats[sekolah].male++;
      else if (jk === 'P' || jk === 'PEREMPUAN') stats.schoolStats[sekolah].female++;
    }

    var bmIkatanAvg = (bantuMula + ikatan) / 2;
    var isPass = (kawad >= cfg.wajaranMinKawad && bmIkatanAvg >= cfg.wajaranMinIkatan && overall >= cfg.wajaranMinOverall);
    if (statusText === 'LLL' || isPass) {
      stats.passCountKRS++;
      stats.totalPassCount++;
    } else {
      stats.failCountKRS++;
      stats.totalFailCount++;
    }

    if (isEvaluated) {
      evaluatedKRS++;
      stats.evaluatedCount++;
      sumKawadKRS += kawad;
      sumBMKRS += bantuMula;
      sumIkatanKRS += ikatan;
      sumOverallKRS += overall;
    } else {
      stats.pendingCount++;
    }

    stats.candidates.push({
      unit: 'KRS',
      pangkat: 'Sarjan',
      rowIdx: idx + 3,
      noGiliran: noGiliran,
      nama: nama,
      jantina: jantina,
      sekolah: sekolah,
      kawad: (kawad * 100).toFixed(1) + '%',
      bantuMula: (bantuMula * 100).toFixed(1) + '%',
      ikatan: (ikatan * 100).toFixed(1) + '%',
      overall: (overall * 100).toFixed(1) + '%',
      rawKawad: kawad,
      rawBantuMula: bantuMula,
      rawIkatan: ikatan,
      rawOverall: overall,
      isPass: isPass,
      statusText: statusText,
      catatan: catatan,
      isEvaluated: isEvaluated,
      isAbsent: isAbsent,
      isTarikDiri: isTarikDiri,
      isTukar: isTukar
    });
  });

  stats.totalSchools = Object.keys(schoolSet).length || 60;
  stats.passRate = stats.totalCandidates > 0 ? ((stats.totalPassCount / stats.totalCandidates) * 100).toFixed(1) : 0;

  if (evaluatedTKRS > 0) {
    stats.avgKawadTKRS = ((sumKawadTKRS / evaluatedTKRS) * 100).toFixed(1);
    stats.avgBantuMulaTKRS = ((sumBMTKRS / evaluatedTKRS) * 100).toFixed(1);
    stats.avgIkatanTKRS = ((sumIkatanTKRS / evaluatedTKRS) * 100).toFixed(1);
    stats.avgOverallTKRS = ((sumOverallTKRS / evaluatedTKRS) * 100).toFixed(1);
  }

  if (evaluatedKRS > 0) {
    stats.avgKawadKRS = ((sumKawadKRS / evaluatedKRS) * 100).toFixed(1);
    stats.avgBantuMulaKRS = ((sumBMKRS / evaluatedKRS) * 100).toFixed(1);
    stats.avgIkatanKRS = ((sumIkatanKRS / evaluatedKRS) * 100).toFixed(1);
    stats.avgOverallKRS = ((sumOverallKRS / evaluatedKRS) * 100).toFixed(1);
  }

  return stats;
}

/* =========================================================================
   PENGURUSAN WAJARAN, STATUS CALON & PEMBAIKAN SPREADSHEET
   ========================================================================= */

function updatePassingWajaran(config, pin) {
  if (pin) {
    var auth = verifyAdminPIN(pin);
    if (!auth.success) throw new Error("PIN Admin tidak sah.");
  }

  var props = PropertiesService.getScriptProperties();
  props.setProperty('WAJARAN_MIN_KAWAD', String(config.wajaranMinKawad || config.thresholdKawad || '0.70'));
  props.setProperty('WAJARAN_MIN_IKATAN', String(config.wajaranMinIkatan || config.thresholdIkatan || '0.50'));
  props.setProperty('WAJARAN_MIN_OVERALL', String(config.wajaranMinOverall || config.thresholdOverall || '0.70'));
  props.setProperty('WAJARAN_KAWAD', String(config.wajaranKawad || '0.60'));
  props.setProperty('WAJARAN_BANTU_MULA', String(config.wajaranBantuMula || '0.20'));
  props.setProperty('WAJARAN_IKATAN', String(config.wajaranIkatan || '0.20'));

  repairAndOptimizeSpreadsheet();
  return "Wajaran Komponen & Wajaran Kelayakan berjaya dikemas kini ke Google Sheet! (Wajaran: Kawad " + Math.round(config.wajaranKawad*100) + "%, BM " + Math.round(config.wajaranBantuMula*100) + "%, Ikatan " + Math.round(config.wajaranIkatan*100) + "% | Wajaran Minimum Lulus: Kawad " + Math.round((config.wajaranMinKawad||config.thresholdKawad||0.7)*100) + "%, BM+Ikatan " + Math.round((config.wajaranMinIkatan||config.thresholdIkatan||0.5)*100) + "%, Keseluruhan " + Math.round((config.wajaranMinOverall||config.thresholdOverall||0.7)*100) + "%)";
}

// Alias untuk keserasian
function updatePassingThresholds(config, pin) {
  return updatePassingWajaran(config, pin);
}

function updateCandidateStatusRecord(payload, pin) {
  if (pin) {
    var auth = verifyAdminPIN(pin);
    if (!auth.success) throw new Error("PIN Admin tidak sah.");
  }

  var ss = SpreadsheetApp.getActiveSpreadsheet();
  if (!ss) {
    try { ss = SpreadsheetApp.openById(SPREADSHEET_ID); } catch(e) {}
  }
  if (!ss) throw new Error("Spreadsheet tidak dijumpai.");

  var noBadan = String(payload.noBadan || payload.noGiliran || '').trim();
  var newStatus = String(payload.newStatus || '').trim().toUpperCase();
  var newName = String(payload.newName || '').trim().toUpperCase();
  var catatan = String(payload.catatan || '').trim();

  if (!noBadan) throw new Error("No Badan peserta diperlukan.");

  var isTKRS = noBadan.toUpperCase().indexOf('TKRS') !== -1;
  var sheetName = isTKRS ? 'ANALISIS_TKRS' : 'ANALISIS_KRS';
  var sheet = ss.getSheetByName(sheetName);
  var originalName = '';
  var originalSchool = '';
  var originalJantina = '';

  // Dapatkan maklumat asas calon daripada sheet markah (untuk nama, sekolah, jantina)
  if (sheet) {
    var data = sheet.getDataRange().getValues();
    for (var i = 2; i < data.length; i++) {
      if (String(data[i][1]).trim().toUpperCase() === noBadan.toUpperCase()) {
        originalName = String(data[i][2] || '');
        originalSchool = String(data[i][3] || data[i][5] || '');
        originalJantina = String(data[i][4] || '');
        if (newName && newStatus.indexOf('TUKAR') !== -1) {
          sheet.getRange(i + 1, 3).setValue(newName); // Tukar nama di Kolum C jika calon gantian
        }
        break;
      }
    }
  }

  // KEMAS KINI SHEET 'PESERTA TIDAK HADIR' (SUMBER TUNGGAL STATUS KEHADIRAN / TARIK DIRI)
  var thSheet = ss.getSheetByName('PESERTA TIDAK HADIR');
  if (!thSheet) {
    thSheet = ss.insertSheet('PESERTA TIDAK HADIR');
  }

  // Pastikan Header wujud dalam 'PESERTA TIDAK HADIR'
  if (thSheet.getLastRow() < 1) {
    var thHeaders = [
      'BIL',
      'ID_PESERTA',
      'NAMA CALON',
      'SEKOLAH',
      'UNIT',
      'JANTINA',
      'STATUS KEHADIRAN / TINDAKAN',
      'NAMA CALON GANTIAN',
      'CATATAN / SEBAB',
      'TARIKH & MASA KEMAS KINI'
    ];
    thSheet.appendRow(thHeaders);
    var hRange = thSheet.getRange(1, 1, 1, thHeaders.length);
    hRange.setBackground('#0f172a')
          .setFontColor('#ffffff')
          .setFontWeight('bold')
          .setHorizontalAlignment('center');
    thSheet.setFrozenRows(1);
  }

  var nowStr = Utilities.formatDate(new Date(), Session.getScriptTimeZone() || 'Asia/Kuala_Lumpur', 'yyyy-MM-dd HH:mm:ss');
  var thData = thSheet.getDataRange().getValues();
  var foundRowIndex = -1;

  // Cari kedudukan baris calon dalam PESERTA TIDAK HADIR
  for (var r = 1; r < thData.length; r++) {
    if (String(thData[r][1]).trim().toUpperCase() === noBadan.toUpperCase()) {
      foundRowIndex = r + 1;
      break;
    }
  }

  if (newStatus === 'HADIR') {
    // Jika status ditukar kepada HADIR semula, padam baris dari PESERTA TIDAK HADIR
    if (foundRowIndex !== -1) {
      thSheet.deleteRow(foundRowIndex);
    }
  } else {
    // Jika status adalah TIDAK HADIR / TARIK DIRI / TUKAR PESERTA
    if (foundRowIndex !== -1) {
      // Kemas kini baris sedia ada
      thSheet.getRange(foundRowIndex, 3).setValue((newName && newStatus.indexOf('TUKAR') !== -1) ? newName : originalName);
      thSheet.getRange(foundRowIndex, 4).setValue(originalSchool);
      thSheet.getRange(foundRowIndex, 5).setValue(isTKRS ? 'TKRS' : 'KRS');
      thSheet.getRange(foundRowIndex, 6).setValue(originalJantina);
      thSheet.getRange(foundRowIndex, 7).setValue(newStatus);
      thSheet.getRange(foundRowIndex, 8).setValue((newName && newStatus.indexOf('TUKAR') !== -1) ? newName : '-');
      thSheet.getRange(foundRowIndex, 9).setValue(catatan || '-');
      thSheet.getRange(foundRowIndex, 10).setValue(nowStr);
    } else {
      // Tambah baris baharu
      var newBil = thData.length;
      thSheet.appendRow([
        newBil,
        noBadan,
        originalName,
        originalSchool,
        isTKRS ? 'TKRS' : 'KRS',
        originalJantina,
        newStatus,
        (newName && newStatus.indexOf('TUKAR') !== -1) ? newName : '-',
        catatan || '-',
        nowStr
      ]);
    }
  }

  return "Status calon " + noBadan + " berjaya dikemas kini kepada [" + newStatus + "] dalam tab PESERTA TIDAK HADIR!";
}

function repairAndOptimizeSpreadsheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  if (!ss) {
    try { ss = SpreadsheetApp.openById(SPREADSHEET_ID); } catch(e) {}
  }
  if (!ss) return "Spreadsheet tidak disambungkan.";

  var cfg = getActiveWajaranConfig();
  var sheetTKRS = ss.getSheetByName('ANALISIS_TKRS');
  if (sheetTKRS) {
    var lastRowTKRS = sheetTKRS.getLastRow();
    if (lastRowTKRS >= 3) {
      var numRows = lastRowTKRS - 2;
      var fKawad = [], fBM = [], fIkatan = [], fTotal = [], fStatus = [];
      for (var i = 3; i <= lastRowTKRS; i++) {
        fKawad.push(['=IFERROR(VLOOKUP($B' + i + ', MARKAH_TKRS_KAWAD!$B:$AP, 40, FALSE)/95, 0)']);
        fBM.push(['=IFERROR(VLOOKUP($B' + i + ', MARKAH_TKRS_BANTU_MULA!$B:$K, 9, FALSE)/20, 0)']);
        fIkatan.push(['=IFERROR(VLOOKUP($B' + i + ', MARKAH_TKRS_IKATAN!$B:$M, 11, FALSE)/25, 0)']);
        fTotal.push(['=IFERROR((G' + i + ' * ' + cfg.wajaranKawad + ') + (H' + i + ' * ' + cfg.wajaranBantuMula + ') + (I' + i + ' * ' + cfg.wajaranIkatan + '), 0)']);
        fStatus.push(['=IF(G' + i + '>=' + cfg.wajaranMinKawad + ', "L", "G") & IF(((H' + i + '+I' + i + ')/2)>=' + cfg.wajaranMinIkatan + ', "L", "G") & IF(J' + i + '>=' + cfg.wajaranMinOverall + ', "L", "G")']);
      }
      sheetTKRS.getRange(3, 7, numRows, 1).setFormulas(fKawad);
      sheetTKRS.getRange(3, 8, numRows, 1).setFormulas(fBM);
      sheetTKRS.getRange(3, 9, numRows, 1).setFormulas(fIkatan);
      sheetTKRS.getRange(3, 10, numRows, 1).setFormulas(fTotal);
      sheetTKRS.getRange(3, 11, numRows, 1).setFormulas(fStatus);
      sheetTKRS.getRange(3, 7, numRows, 4).setNumberFormat('0.00%');
    }
  }

  var sheetKRS = ss.getSheetByName('ANALISIS_KRS');
  if (sheetKRS) {
    var lastRowKRS = sheetKRS.getLastRow();
    if (lastRowKRS >= 3) {
      var numRowsK = lastRowKRS - 2;
      var fKawadK = [], fBMK = [], fIkatanK = [], fTotalK = [], fStatusK = [];
      for (var k = 3; k <= lastRowKRS; k++) {
        fKawadK.push(['=IFERROR(VLOOKUP($B' + k + ', MARKAH_KRS_KAWAD!$B:$BD, 54, FALSE)/137, 0)']);
        fBMK.push(['=IFERROR(VLOOKUP($B' + k + ', MARKAH_KRS_BANTU_MULA!$B:$K, 10, FALSE)/20, 0)']);
        fIkatanK.push(['=IFERROR(VLOOKUP($B' + k + ', MARKAH_KRS_IKATAN!$B:$M, 12, FALSE)/25, 0)']);
        fTotalK.push(['=IFERROR((G' + k + ' * ' + cfg.wajaranKawad + ') + (H' + k + ' * ' + cfg.wajaranBantuMula + ') + (I' + k + ' * ' + cfg.wajaranIkatan + '), 0)']);
        fStatusK.push(['=IF(G' + k + '>=' + cfg.wajaranMinKawad + ', "L", "G") & IF(((H' + k + '+I' + k + ')/2)>=' + cfg.wajaranMinIkatan + ', "L", "G") & IF(J' + k + '>=' + cfg.wajaranMinOverall + ', "L", "G")']);
      }
      sheetKRS.getRange(3, 7, numRowsK, 1).setFormulas(fKawadK);
      sheetKRS.getRange(3, 8, numRowsK, 1).setFormulas(fBMK);
      sheetKRS.getRange(3, 9, numRowsK, 1).setFormulas(fIkatanK);
      sheetKRS.getRange(3, 10, numRowsK, 1).setFormulas(fTotalK);
      sheetKRS.getRange(3, 11, numRowsK, 1).setFormulas(fStatusK);
      sheetKRS.getRange(3, 7, numRowsK, 4).setNumberFormat('0.00%');
    }
  }

  try {
    SpreadsheetApp.getActiveSpreadsheet().toast('✅ Formula markah & wajaran berjaya diselaraskan!', 'Pentauliahan 2026', 4);
  } catch(e) {}

  return "Semua formula ANALISIS_TKRS & ANALISIS_KRS telah berjaya diselaraskan mengikut wajaran semasa!";
}

function syncAndValidateAnalysis() {
  return repairAndOptimizeSpreadsheet();
}

function repairAllFormulasAndFormat() {
  var msg = repairAndOptimizeSpreadsheet();
  return { success: true, message: msg };
}

function syncAllExaminerScores() {
  var msg = repairAndOptimizeSpreadsheet();
  return { success: true, message: msg };
}

function setupAutoSyncTriggers() {
  var msg = setupAutoTriggers();
  return { success: true, message: msg };
}

function setupAutoTriggers() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  if (!ss) {
    try { ss = SpreadsheetApp.openById(SPREADSHEET_ID); } catch(e) {}
  }
  if (!ss) return "Spreadsheet tidak dijumpai.";

  var triggers = ScriptApp.getProjectTriggers();
  for (var i = 0; i < triggers.length; i++) {
    ScriptApp.deleteTrigger(triggers[i]);
  }

  ScriptApp.newTrigger('repairAndOptimizeSpreadsheet')
    .forSpreadsheet(ss)
    .onChange()
    .create();

  return "Trigger automasi masa nyata berjaya dipasang dan aktif!";
}

/* =========================================================================
   PENGENDALI MENU SPREADSHEET
   ========================================================================= */

function openWebAppDirectly() {
  var url = ScriptApp.getService().getUrl();
  if (!url) {
    SpreadsheetApp.getUi().alert(
      '🌐 Pautan Web App',
      'Sila buat "Deploy as Web App" terlebih dahulu pada bahagian Deploy > New Deployment di Google Apps Script.\n\nSelepas itu, Web App boleh diakses terus melalui pautan URL rasmi.',
      SpreadsheetApp.getUi().ButtonSet.OK
    );
    return;
  }
  var html = HtmlService.createHtmlOutput(
    '<div style="font-family:Segoe UI, sans-serif; padding:20px; text-align:center;">' +
    '<h3 style="color:#0f172a; margin-bottom:12px;">🌐 Web App Portal Rasmi</h3>' +
    '<p style="color:#475569; font-size:14px; margin-bottom:20px;">Klik butang di bawah untuk membuka portal pentauliahan dalam tab baru:</p>' +
    '<a href="' + url + '" target="_blank" style="display:inline-block; background:#2563eb; color:#fff; padding:12px 24px; text-decoration:none; border-radius:8px; font-weight:600; box-shadow:0 4px 6px -1px rgba(37,99,235,0.2);">🚀 Buka Portal Web App</a>' +
    '<p style="color:#94a3b8; font-size:11px; margin-top:20px;">PPD Johor Bahru © 2026</p>' +
    '</div>'
  ).setWidth(450).setHeight(220);
  SpreadsheetApp.getUi().showModalDialog(html, '🌐 Web App Portal Pentauliahan 2026');
}

function openDashboardModal() {
  var template = HtmlService.createTemplateFromFile('Index');
  try {
    template.initialData = getDashboardData();
  } catch (err) {
    template.initialData = null;
  }
  var html = template.evaluate()
    .setWidth(1150)
    .setHeight(700)
    .setTitle('Portal Eksekutif Pentauliahan Pangkat KRS & TKRS JB 2026');
  SpreadsheetApp.getUi().showModalDialog(html, '📊 Pusat Kawalan & Analisis Eksekutif');
}

function runRepairFromMenu() {
  var result = repairAndOptimizeSpreadsheet();
  SpreadsheetApp.getUi().alert('⚡ Pembaikan Formula Selesai', result, SpreadsheetApp.getUi().ButtonSet.OK);
}

function runSyncFromMenu() {
  var result = repairAndOptimizeSpreadsheet();
  SpreadsheetApp.getUi().alert('🔄 Segerak Markah Penguji', 'Semua markah penguji telah disegerakkan dan dikira semula secara automatik!\n\n' + result, SpreadsheetApp.getUi().ButtonSet.OK);
}

function runTriggerFromMenu() {
  var result = setupAutoTriggers();
  SpreadsheetApp.getUi().alert('🤖 Automasi Trigger', result, SpreadsheetApp.getUi().ButtonSet.OK);
}

function showMengenaiAlert() {
  var msg = "🏛️ SISTEM PENGURUSAN PENTAULIAHAN KRS & TKRS DAERAH JOHOR BAHRU 2026\n\n" +
            "📌 Skema Pentauliahan:\n" +
            " • TKRS: Ujian Koperal TKRS (Tunas Kadet Remaja Sekolah)\n" +
            " • KRS: Ujian Sarjan KRS (Kadet Remaja Sekolah)\n\n" +
            "⚖️ Formula & Wajaran Markah Komponen:\n" +
            " • Kawad Kaki: 60% (Wajaran Utama)\n" +
            " • Bantu Mula: 20%\n" +
            " • Ikatan & Simpulan: 20%\n\n" +
            "🎯 Wajaran Minimum Kelayakan Pangkat:\n" +
            " • Wajaran Min. Kawad Kaki >= 70%\n" +
            " • Wajaran Min. Kemahiran (BM + Ikatan) >= 50%\n" +
            " • Wajaran Min. Keseluruhan >= 70%\n\n" +
            "PPD Johor Bahru © 2026 | Versi Sistem: 3.0 (Revamp Build 2026.08)";
  SpreadsheetApp.getUi().alert('ℹ️ Mengenai Sistem & Skema PPDJB', msg, SpreadsheetApp.getUi().ButtonSet.OK);
}


// Fungsi ditambah oleh AI: verifyAdminPIN
function verifyAdminPIN(pin) {
  var MASTER_PIN = 'seketejb26';
  return { success: pin === MASTER_PIN };
}
