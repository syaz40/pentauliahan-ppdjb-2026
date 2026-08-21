import os
import json
import urllib.request
import urllib.error
import sys

sys.stdout.reconfigure(encoding='utf-8')

appdata_path = os.path.expandvars(r'%APPDATA%\netlify\Config\config.json')
with open(appdata_path, 'r') as f:
    cfg = json.load(f)

users = cfg.get('users', {})
user_id = cfg.get('userId')
user_data = users.get(user_id, {})
token = user_data.get('auth', {}).get('token')

site_id = "77fe0d38-c1f2-4a2f-b7f9-c320a9d7117e"
deploy_id = "6a88732aba6d400a8100b606"

url = f"https://api.netlify.com/api/v1/sites/{site_id}/deploys/{deploy_id}/restore"
req = urllib.request.Request(url, method='POST', headers={
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
})

try:
    with urllib.request.urlopen(req) as resp:
        res_data = json.loads(resp.read().decode('utf-8'))
        print("[BERJAYA] Deploy telah diterbitkan ke Production!")
        print("Site URL:", res_data.get('ssl_url') or res_data.get('url'))
        print("Published Deploy State:", res_data.get('state'))
        print("Published Deploy ID:", res_data.get('id'))
except urllib.error.HTTPError as e:
    print(f"HTTP Error {e.code}: {e.read().decode('utf-8')}")
except Exception as e:
    print("Error:", e)
