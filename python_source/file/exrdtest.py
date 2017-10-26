from xlrd import open_workbook

wb = open_workbook('sample.xls', formatting_info = True)

#シート名を出力
print(wb.sheet_by_index(0).name)
sheet = wb.sheet_by_name("Newsheet_1")
# cell インデックスの値をどう取るか
#シート内の行数、列数
print(sheet.nrows)
print(sheet.ncols)
row_list = []
for row in range( sheet.nrows ):
	col_list = []
	for col in range(sheet.ncols):
		#セルの値を取得し、出力
		print( sheet.cell(row,col).value)
cell = sheet.cell ( 5, 1)
print( "cell.xl_index is ", cell.xf_index )
fmt = wb.xf_list[cell.xf_index]
print( type(fmt) )
fmt.dump()
