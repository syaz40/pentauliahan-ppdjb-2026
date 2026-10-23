# Piawaian kod ANTIGRAVITY PROJECT (untuk Antigravity)

Fail ini diurus oleh _claude-sync (`_claude-sync/templat-projek`) — pinda di sana, bukan di sini. Salinan ringkas peraturan Claude dalam `~/.claude/rules/`. Peraturan dalam `AGENTS.md` projek mengatasi fail ini.

## Automatik pada setiap prompt (tanpa pemilik menyebut apa-apa)
1. **Permulaan sesi:** baca `AGENTS.md`/`CLAUDE.md` projek, `LOCKED_MODULES.md` jika ada, 3 entri teratas `HISTORY.md`, dan entri teratas `CLOUD PBD SYSTEM/work_files/history.md`. Jika entri teratas ditulis oleh ejen lain, sahkan terhadap kod dahulu.
2. **Setiap prompt:** pilih sendiri kemahiran paling sesuai (boleh lebih daripada satu) dan tulis satu baris `Kemahiran: …` di awal jawapan. Panduan:
   - reka bentuk / halaman / UI → `jurutera-frontend`, `frontend-design`, `ui-ux-pro-max` (+ `piawaian-antarabangsa`); tiru gaya laman → `skillui`
   - ujian pelayar / tangkapan skrin → `playwright-cli`
   - rosak / ralat → `baiki-isu`, `nyahpepijat-produksi`; keselamatan → `audit-keselamatan-produksi`
   - SEMAK → kemahiran projek `semak`; semak perubahan → `semak-kod`
   - perlahan → `optimasi-prestasi`; deploy → `devops-pengerahan`; projek baharu → `bina-mvp-produksi`, `sediakan-projek`
   - keputusan teknikal → `ketua-teknikal`; pelan → `scaffold`; teks pendek → `ghost`; dokumen pustaka terkini → MCP `context7`
   - animasi → `emil-design-eng`, `improve-animations`, `review-animations`; kemas akhir / elak rupa generik → `impeccable`, `design-taste-frontend`
   - kod terlalu panjang → `ponytail`; idea/pelan ciri → `brainstorming`, `writing-plans`; pepijat sukar → `systematic-debugging`
   - jualan/pemasaran → `copywriting`, `pricing`, `launch`, `seo-audit`, `cro`; media sosial → `post-writer-sms`, `caption-writer-sms`, `content-calendar-sms`
   - video → `remotion-*` atau `hyperframes`; teks Inggeris manusiawi → `humanizer`
3. **Selepas kerja bermakna:** tambah entri di atas `HISTORY.md` (tarikh, ejen, apa dibuat, fail diubah, ujian + keputusan, deploy, belum selesai) tanpa menunggu diminta.

## Gaya kod
- Ikut gaya fail sedia ada; jangan format semula fail yang tidak disentuh.
- Nama baharu ikut bahasa projek (BM jika projek guna BM). Teks pengguna dalam BM rasmi dan santun.
- Vanilla CSS; tiada pakej atau rangka kerja baharu tanpa kelulusan.
- UTF-8 tanpa BOM; semak tiada aksara rosak (`â€"`, `Ã©`) selepas sunting.
- Laluan dengan ruang mesti dalam tanda petik.
- Sunting `src/` dan jana semula; jangan sunting fail hasil build.

## Ujian
- Jalankan ujian/build sedia ada sebelum kata siap; laporkan keputusan sebenar dan apa yang belum diuji.
- Data ujian fiksyen sahaja; Firestore guna emulator atau projek ujian.
- Jangan ubah ujian supaya ia lulus.

## API dan ralat
- Sahkan identiti dan peranan di setiap endpoint; sahkan input di pelayan.
- Kod status HTTP yang betul; mesej ralat BM mudah kepada pengguna, butiran teknikal dalam log sahaja.
- Webhook bayaran: sahkan tandatangan, tolak ulang main, sahkan dengan API gateway, idempoten.

## Keselamatan
- Jangan baca atau paparkan `.env`, kunci, token, `service-account*.json`.
- Tiada data murid sebenar atau No. KP dalam contoh, ujian atau repo.
- Padam/alih fail, `git push --force`, `git reset --hard`, ubah data produksi: tunjuk pratonton dan tunggu "ya" pemilik.
