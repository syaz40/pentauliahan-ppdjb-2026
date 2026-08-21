import json

with open("detailed_analysis.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for name, info in data.items():
    print("=" * 60)
    print(f"SHEET NAME: {name}")
    print(f"Total Rows: {info['total_data_rows']} | Total Columns: {info['total_columns']}")
    print(f"Headers ({len(info['headers'])}):")
    for i, h in enumerate(info['headers'], 1):
        print(f"  {i}. {h}")
    if info['formulas']:
        print("Formulas found:")
        for h, form in info['formulas'].items():
            print(f"  - [{h}]: {form}")
    if info['sample']:
        print("Sample Row 1:")
        print(" ", json.dumps(info['sample'][0], ensure_ascii=False))
print("=" * 60)
