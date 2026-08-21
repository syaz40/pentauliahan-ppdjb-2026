import json

with open("tables_detail.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for sname, info in d.items():
    print("=" * 60)
    print(f"SHEET: {sname}")
    print("Headers count:", len(info["headers"]))
    print("Headers:", info["headers"])
    if info["row2_formulas"]:
        print("Row 2 Formulas:", info["row2_formulas"])
    else:
        print("No formulas on row 2")
