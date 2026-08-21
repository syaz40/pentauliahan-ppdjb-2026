import openpyxl
import json
import sys

def inspect_workbook(file_path):
    wb = openpyxl.load_workbook(file_path, data_only=False)
    wb_values = openpyxl.load_workbook(file_path, data_only=True)
    
    summary = {
        "sheet_names": wb.sheetnames,
        "sheets": {}
    }
    
    for name in wb.sheetnames:
        sheet = wb[name]
        sheet_val = wb_values[name]
        
        max_row = sheet.max_row
        max_col = sheet.max_column
        
        # Get headers (row 1)
        headers = []
        for col_idx in range(1, max_col + 1):
            val = sheet_val.cell(row=1, column=col_idx).value
            headers.append(str(val) if val is not None else f"Unnamed_{col_idx}")
            
        # Get first 3 sample data rows
        sample_rows = []
        for r in range(2, min(max_row + 1, 6)):
            row_data = {}
            for col_idx, h in enumerate(headers, start=1):
                raw_formula = sheet.cell(row=r, column=col_idx).value
                val = sheet_val.cell(row=r, column=col_idx).value
                if str(raw_formula).startswith('='):
                    row_data[h] = f"FORMULA: {raw_formula} -> VAL: {val}"
                else:
                    row_data[h] = val
            sample_rows.append(row_data)
            
        # Check for formula columns
        formula_cols = {}
        for col_idx, h in enumerate(headers, start=1):
            for r in range(2, min(max_row + 1, 20)):
                raw = sheet.cell(row=r, column=col_idx).value
                if str(raw).startswith('='):
                    formula_cols[h] = str(raw)
                    break
                    
        summary["sheets"][name] = {
            "max_row": max_row,
            "max_column": max_col,
            "headers": headers,
            "formula_columns": formula_cols,
            "sample_rows": sample_rows
        }
        
    with open("analysis_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2, default=str)
        
    print("Inspection complete! Found sheets:", wb.sheetnames)

if __name__ == "__main__":
    inspect_workbook("backend_pentauliahan.xlsx")
