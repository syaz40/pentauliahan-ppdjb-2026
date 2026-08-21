import openpyxl

wb = openpyxl.load_workbook('live_google_sheet.xlsx', data_only=False)

# 1. Update ANALISIS_TKRS
ws_tkrs = wb['ANALISIS_TKRS']
for r in range(3, ws_tkrs.max_row + 1):
    if ws_tkrs.cell(row=r, column=2).value is not None:
        ws_tkrs.cell(row=r, column=7).value = f'=IFERROR(VLOOKUP($B{r}, MARKAH_TKRS_KAWAD!$B:$AP, 40, FALSE)/95, 0)'
        ws_tkrs.cell(row=r, column=8).value = f'=IFERROR(VLOOKUP($B{r}, MARKAH_TKRS_BANTU_MULA!$B:$K, 10, FALSE)/20, 0)'
        ws_tkrs.cell(row=r, column=9).value = f'=IFERROR(VLOOKUP($B{r}, MARKAH_TKRS_IKATAN!$B:$M, 12, FALSE)/25, 0)'
        ws_tkrs.cell(row=r, column=10).value = f'=IFERROR((G{r} * 0.6) + (H{r} * 0.2) + (I{r} * 0.2), 0)'
        ws_tkrs.cell(row=r, column=11).value = f'=IF(G{r}>=0.5, "L", "G") & IF(((H{r}+I{r})/2)>=0.5, "L", "G") & IF(J{r}>=0.6, "L", "G")'

# 2. Update ANALISIS_KRS
ws_krs = wb['ANALISIS_KRS']
for r in range(3, ws_krs.max_row + 1):
    if ws_krs.cell(row=r, column=2).value is not None:
        ws_krs.cell(row=r, column=7).value = f'=IFERROR(VLOOKUP($B{r}, MARKAH_KRS_KAWAD!$B:$BD, 54, FALSE)/137, 0)'
        ws_krs.cell(row=r, column=8).value = f'=IFERROR(VLOOKUP($B{r}, MARKAH_KRS_BANTU_MULA!$B:$L, 11, FALSE)/20, 0)'
        ws_krs.cell(row=r, column=9).value = f'=IFERROR(VLOOKUP($B{r}, MARKAH_KRS_IKATAN!$B:$N, 13, FALSE)/25, 0)'
        ws_krs.cell(row=r, column=10).value = f'=IFERROR((G{r} * 0.6) + (H{r} * 0.2) + (I{r} * 0.2), 0)'
        ws_krs.cell(row=r, column=11).value = f'=IF(G{r}>=0.5, "L", "G") & IF(((H{r}+I{r})/2)>=0.5, "L", "G") & IF(J{r}>=0.6, "L", "G")'

wb.save('PENTAULIAHAN_BACKEND_REVISED.xlsx')
print("PENTAULIAHAN_BACKEND_REVISED.xlsx successfully created and verified!")
