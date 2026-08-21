import json

with open(r"C:\Users\SKSRITEBRAUGURU1\.gemini\antigravity-ide\brain\03aac6d1-d22e-4888-92f8-729db7079142\.system_generated\steps\1486\content.md", "r", encoding="utf-8") as f:
    raw = f.read()

data = json.loads(raw)
print("Keys in data:", data.keys())
print("totalCandidates:", data.get('totalCandidates'))
print("totalTKRS:", data.get('totalTKRS'))
print("totalKRS:", data.get('totalKRS'))
print("candidates count:", len(data.get('candidates', [])))
print("School stats count:", len(data.get('schoolStats', {})))
