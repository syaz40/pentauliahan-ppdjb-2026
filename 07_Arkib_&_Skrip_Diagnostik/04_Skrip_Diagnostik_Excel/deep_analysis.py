import openpyxl
import json

wb = openpyxl.load_workbook("backend_pentauliahan.xlsx", data_only=False)
wb_vals = openpyxl.load_workbook("backend_pentauliahan.xlsx", data_only=True)

detailed_report = {}

for sheet_name in wb.sheetnames:
    ws = wb[sheet_name]
    ws_v = wb_vals[sheet_name]
    
    # Extract non-empty headers from row 1
    headers = []
    for c in range(1, ws.max_column + 1):
        h_val = ws_v.cell(row=1, column=c).value
        headers.append(str(h_val).strip() if h_val is not None else f"Col_{c}")
        
    # Count rows with actual data
    row_count = 0
    formulas = {}
    id_candidates = []
    
    for r in range(2, ws.max_row + 1):
        row_vals = [ws_v.cell(row=r, column=c).value for c in range(1, len(headers) + 1)]
        if any(v is not None and str(v).strip() != "" for v in row_vals):
            row_count += 1
            
    # Check formulas across columns
    for c, h in enumerate(headers, 1):
        col_formulas = []
        for r in range(2, min(ws.max_row + 1, 15)):
            val = ws.cell(row=r, column=c).value
            if val and str(val).startswith('='):
                col_formulas.append(str(val))
        if col_formulas:
            formulas[h] = col_formulas[0]
            
    # Sample first 2 rows
    sample_data = []
    for r in range(2, min(ws.max_row + 1, 4)):
        row_data = {}
        for c, h in enumerate(headers, 1):
            val = ws_v.cell(row=r, column=c).value
            row_data[h] = str(val) if val is not None else ""
        if any(row_data.values()):
            sample_data.append(row_data)

    detailed_report[sheet_name] = {
        "total_data_rows": row_count,
        "total_columns": len(headers),
        "headers": headers,
        "formulas": formulas,
        "sample": sample_data
    }

with open("detailed_analysis.json", "w", encoding="utf-8") as f:
    json.dump(detailed_report, f, ensure_ascii=False, indent=2)

print("Detailed analysis saved to detailed_analysis.json")
