import sys, io, shutil, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r'03_Google_Apps_Script\Index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix colspan 6 -> 5 for top-results empty state messages
old_cs6 = 'colspan="6" style="text-align:center; padding:28px; color:#94a3b8; font-weight:600;">Tiada rekod calon berdaftar.</td></tr>'
new_cs5 = 'colspan="5" style="text-align:center; padding:28px; color:#94a3b8; font-weight:600;">Tiada rekod calon berdaftar.</td></tr>'
count_cs = html.count(old_cs6)
html = html.replace(old_cs6, new_cs5)
print(f"[4] Fix colspan 6->5 dalam top-results empty msg: {count_cs} kejadian")

# Also fix candidates table colspan if any
old_cs7 = 'colspan="7"'
count_cs7 = html.count(old_cs7)
print(f"  Candidates colspan=7: {count_cs7} (tidak perlu ubah - ada 6 kolumn sekarang: NoBadan, Nama, Unit, Sekolah, Status, Tindakan)")

# Sync to root and netlify
with open(r'03_Google_Apps_Script\Index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("\nSaved to 03_Google_Apps_Script\Index.html")

# Sync ke root dan Netlify
shutil.copy(r'03_Google_Apps_Script\Index.html', r'index.html')
shutil.copy(r'03_Google_Apps_Script\Index.html', r'04_Web_App_Netlify\index.html')

s1 = os.path.getsize(r'03_Google_Apps_Script\Index.html')
s2 = os.path.getsize(r'index.html')
s3 = os.path.getsize(r'04_Web_App_Netlify\index.html')
print(f"Sync: {s1}={s2}={s3} -> {'OK semua sama' if s1==s2==s3 else 'ERROR berbeza!'}")

# FINAL VERIFICATION
print()
print("=" * 60)
print("PENGESAHAN AKHIR - Kolumn Markah yang tinggal:")
print("=" * 60)
for word in ['<th>Markah', 'Markah (%)', 'scoreVal', 'pillClass']:
    count = html.count(word)
    status = "MASIH ADA - semak!" if count > 0 else "BERSIH (tiada)"
    print(f"  '{word}': {count} kejadian -> {status}")
    if count > 0 and count < 5:
        idx = html.find(word)
        while idx != -1:
            # Get line number
            line_no = html[:idx].count('\n') + 1
            print(f"    Baris {line_no}: {html[max(0,idx-50):idx+100].strip()!r}")
            idx = html.find(word, idx+1)
