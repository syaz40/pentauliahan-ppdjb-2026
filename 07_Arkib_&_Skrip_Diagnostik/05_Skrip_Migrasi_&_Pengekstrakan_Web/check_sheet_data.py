import urllib.request
import urllib.parse
import sys
import csv

sys.stdout.reconfigure(encoding='utf-8')

sheet_id = '1_YmAJ6XVfBREx4_NDTUWRMXAL1Jgi-1vSFS2528dtW0'

# List of known gids or tab names
tabs = [
    ("MARKAH_TKRS_KAWAD", None),
    ("MARKAH_TKRS_BANTU_MULA", None),
    ("MARKAH_TKRS_IKATAN", "1354204171"),
    ("MARKAH_KRS_KAWAD", None),
    ("MARKAH_KRS_BANTU_MULA", None),
    ("MARKAH_KRS_IKATAN", None),
    ("ANALISIS_TKRS", None),
    ("ANALISIS_KRS", None),
    ("ANALISIS_KESELURUHAN", None)
]

for name, gid in tabs:
    if gid:
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
    else:
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={urllib.parse.quote(name)}"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8', errors='replace')
            lines = [l for l in content.strip().split('\n') if l.strip()]
            print(f"=== TAB: {name} (GID: {gid}) ===")
            print(f"Total Rows: {len(lines)}")
            if len(lines) > 0:
                print("Header:", lines[0][:120])
            if len(lines) > 1:
                print("Sample Row 1:", lines[1][:120])
            if len(lines) > 2:
                print("Sample Row 2:", lines[2][:120])
    except Exception as e:
        print(f"=== TAB: {name} -> Error: {e}")
    print()
