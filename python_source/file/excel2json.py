from __future__ import unicode_literals
from xlrd import open_workbook
import json
import codecs

#wb = open_workbook(u'画像コンバータ設計書.xlsx', formatting_info = True)
wb = open_workbook(u'画像コンバータ設計書.xlsx')

#シート名を出力
sheet = wb.sheet_by_name(u"2.ItemList")
# cell インデックスの値をどう取るか
#シート内の行数、列数
print(sheet.nrows)
print(sheet.ncols)
# list
row_list = []
#dict
row_dict = {}
#for row in range( sheet.nrows ):
for row in  range( sheet.nrows ):
    if row < 2:
    	continue
    print(row, ",",sheet.cell(row,12).value,":",type(sheet.cell(row,2).value))
    row_dict[sheet.cell(row,12).value] = sheet.cell(row,2).value
#	col_list = []
#	for col in range(sheet.ncols):
#		print(row, ",", col,":",sheet.cell(row,col).value)
#		#セルの値を取得し、出力
#		print( sheet.cell(row,col).value)
#cell = sheet.cell ( 5, 1)
#print( "cell.xl_index is ", cell.xf_index )
#fmt = wb.xf_list[cell.xf_index]
#print( type(fmt) )
#fmt.dump()

print('-----辞書型から JSON 形式の文字列へ変換-----')
json_str = json.dumps(row_dict, sort_keys=True, ensure_ascii=False, indent=2)
print(json_str)

#print('json_str:{}'.format(type(json_str)))
#print('-----JSON 形式の文字列から辞書型へ変換-----')
#json_dict2 = json.loads(json_str)
#print('json_dict2:{}'.format(type(json_dict2)))
#JSON データの書き込み
#f2 = open('test2.json', 'w')
f2 = codecs.open('test2.json', 'w', 'utf-8')
#json.dump(json_dict2, f2)
#json.dump(json_str, f2)
f2.write(json_str)
#with open("utf8.json", "w") as fh:
#f2.write(json_str.encode("utf-8"))
