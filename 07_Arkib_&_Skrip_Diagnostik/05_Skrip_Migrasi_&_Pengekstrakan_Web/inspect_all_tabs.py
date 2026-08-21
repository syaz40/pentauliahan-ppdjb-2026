import urllib.request
import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

sheet_id = '1_YmAJ6XVfBREx4_NDTUWRMXAL1Jgi-1vSFS2528dtW0'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/edit'

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='replace')
        
        # Look for bootstrapData or sheet metadata in HTML
        m = re.findall(r'(\d+),\"([^\"]+)\",\d+,\d+,\[', html)
        print(f"Matched tabs: {len(m)}")
        
        # Let's search for known tab names
        known_tabs = [
            "SENARAI_CALON", "ANALISIS_KESELURUHAN", "MARKAH_TKRS_KAWAD", 
            "MARKAH_TKRS_BANTU_MULA", "MARKAH_TKRS_IKATAN",
            "MARKAH_KRS_KAWAD", "MARKAH_KRS_BANTU_MULA", "MARKAH_KRS_IKATAN",
            "PENETAPAN_WAJARAN", "LOG_KEHADIRAN_CALON"
        ]
        for t in known_tabs:
            if t in html:
                print(f"Found known tab in sheet HTML: {t}")
                
except Exception as e:
    print('Error:', e)
