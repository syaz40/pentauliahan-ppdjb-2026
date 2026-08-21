import json

with open("full_system_dump.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for sheet in ["ANALISIS_TKRS", "ANALISIS_KRS", "JENIS_PENTAULIAHAN"]:
    print(f"================ {sheet} ================")
    print("Headers:", d[sheet]["headers"])
    print("Formulas:")
    for k, v in d[sheet]["formulas"].items():
        print(f"  {k} -> {v}")
    print("Preview Rows:")
    for row in d[sheet]["data_preview"]:
        print(" ", row)

