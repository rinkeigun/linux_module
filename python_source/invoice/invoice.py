# -*- coding: utf-8 -*-
# File name : invoice.py
# Date      : 2018/02/09
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

import glob
import os
from xlrd import open_workbook
import xlwt
from xlutils.copy import copy
import calendar
import datetime

A = 0
B = 1
C = 2
D = 3
E = 4
F = 5
G = 6
H = 7
I = 8
J = 9
K = 10
L = 11
M = 12
N = 13
O = 14
P = 15
Q = 16
R = 17
S = 18
T = 19

# 出勤時間により請求書の生成
class run:

	def __init__(self):
		
		# 10. 初期化
		datalist = {}
		timeRecordDir = "input/record/*"
		controlFile   = "input/controlfile.xlsx"
		templateFile  = "input/template.xlsx"
		outputDir = "output"
		
		# 20. ファイルの読込
		timefiles = glob.glob( timeRecordDir )

		# 30. ファイル種別判定
		for file in timefiles:
			# ファイルの拡張子取得
			root, ext = os.path.splitext(file)

			# ファイル名を小文字にする
			ext = ext.lower()
			if ext == ".xlsx":
				self.readEmpData( file, datalist )
			elif ext == ".pdf":
				print( "file type is pdf" )
				continue
			elif ext == ".bmp":
				print( "file type bmp" )
				continue
			elif ext == ".tiff":
				print( "file type tiff" )
				continue
			elif ext == ".jpg":
				print( "file type jpg" )
				continue
			else:
				print( file +" :unknow file type!" )
				continue
			
			# 40. 管理データの読込
			self.controldata( controlFile, datalist)

			# 50. 新しいファイルの生成、書き込み
			self.createinvoice(templateFile, datalist, outputDir)


	# 出勤ファイルからデータを読込
	def readEmpData( self, file, datalist ):
		# workbook
		#wb = open_workbook( file, formatting_info = True )
		wb = open_workbook( file )

		# シート名を取得
		sheet = wb.sheet_by_index(0)
		sheetname = sheet.name
		
		# データの取得
		datalist['name']    = ( 13, B, sheet.cell(0, B).value)
		datalist[u"年月"]   = ( 0, 0, sheetname)
		datalist[u"総時間"] = ( 13, D, sheet.cell(32, D).value)
		return (0)

	# 管理ファイルから名前が同じのデータを追加
	def controldata(self, controlfile, datalist):

		# 対象社員の名前
		name = datalist['name'][2]

		# workbook
		#wb = open_workbook( controlfile, formatting_info = True )
		wb = open_workbook( controlfile )

		# シート名を取得
		sheet = wb.sheet_by_index(0)
		
		# 名前で行を走査
		print( sheet.nrows ) 
		for row in range( sheet.nrows ):
			if sheet.cell(row, A).value == name :
				# データの取得
				datalist[u"注文書番号"]    = ( 1, G, sheet.cell(row, N).value)
				datalist[u"取引先名"]    = ( 2, B, sheet.cell(row, F).value)
				ym = datalist[u"年月"][2]
				v = str(int(sheet.cell(row, T).value))
				monthstr = ym[:4] + "/" + ym[4:] + u"/"
				tmp, maxday = calendar.monthrange(int(ym[:4]), int(ym[4:]))
				thisday = 1 
				if len(v) == 0:
					during = monthstr + "1-" + monthstr + str(maxday)
					thisday = maxday
					v = u"/月末"
					
				else:
					#lastmonthstr = ym[:4] + "/" + int(ym[4:]) + u"/"
					#during = monthstr + str(v+1) + "-" + monthstr + str(v)
					thisday = int(v)
					v = str(v)
				thismonth = datetime.date( int(ym[:4]), int(ym[4:]), thisday)
				dd = datetime.timedelta(days=-maxday)
				lastmonth = thismonth + dd 
				print( lastmonth, thismonth )
				#datalist[u"請求日"]    = ( 2, G, sheet.cell(row, T).value)
				datalist[u"請求日"]    = ( 2, G, v)

				# 総時間、下限時間、上限時間により不足、超過時間の算出
				totaltime = datalist[u"総時間"] [2]
				project = sheet.cell(row, J).value
				bottom = sheet.cell(row, O).value
				top    = sheet.cell(row, P).value
				kadou, over = self.calovertime( totaltime, bottom, top )
				
				#datalist[u"社員名"]  =  datalist[u"社員名"][2] + kikan, anjianmei( kadou ) 
				#datalist[u"name"]  =  datalist[u"name"][2] + u":(" + kadou + u")"
				name = name + ":"+ datetime.datetime.strftime(lastmonth, "%Y/%m/%d") + "-" + datetime.datetime.strftime(thismonth, "%Y/%m/%d") + project+ u"(" + str(kadou) + u")"
				datalist[u"社員名"]  =  (13, B, name )
				datalist[u"総時間"]  = ( 13, D, 1)
				datalist[u"単価"]    = ( 13, F, sheet.cell(row, S).value)
				datalist[u"超過時間"] = ( 14, B, u"超過時間:" + str(over))
				datalist[u"数量"]    = ( 14, D, over)
				datalist[u"時給"]    = ( 14, F, sheet.cell(row, Q).value)
				datalist[u"合計金額"]    = ( 10, C, xlwt.Formula('G24'))
				datalist[u"金額14"]    = ( 13, G, xlwt.Formula('ROUND(D14*F14, 0)'))
				datalist[u"金額15"]    = ( 14, G, xlwt.Formula('ROUND(D15*F15, 0)'))
				datalist[u"金額16"]    = ( 15, G, xlwt.Formula('ROUND(D16*F16, 0)'))
				datalist[u"金額17"]    = ( 16, G, xlwt.Formula('ROUND(D17*F17, 0)'))
				datalist[u"金額18"]    = ( 17, G, xlwt.Formula('ROUND(D18*F18, 0)'))
				datalist[u"金額19"]    = ( 18, G, xlwt.Formula('ROUND(D19*F19, 0)'))
				datalist[u"金額20"]    = ( 19, G, xlwt.Formula('ROUND(D20*F20, 0)'))
				datalist[u"金額21"]    = ( 20, G, xlwt.Formula('ROUND(D21*F21, 0)'))
				datalist[u"小計"]    = ( 21, G, xlwt.Formula('SUM(G14:G21)'))
				datalist[u"消費税等"]    = ( 22, G, xlwt.Formula('ROUNDDOWN(G22*0.08, 0)'))
				datalist[u"合計"]    = ( 23, G, xlwt.Formula('SUM(G22:G23)'))

		return (0)

	# 総時間、下限、上限から超過時間の算出
	def calovertime( self, totaltime, bottom, top ):
		over = 0
		if totaltime < bottom:
			over = totaltime - bottom
			totaltime = tobbom
		elif totaltime > top:
			over = totaltime - top
			totaltime = top
		return( int(totaltime), int(over))
			
	# テンプレートファイルにデータを書き出し、ファイルを保存 
	def createinvoice(self, templatefile, datalist, outputDir):
		# 出力ファイル名
		file = outputDir + "/" + datalist[u"年月"][2] + "_" + datalist["name"][2] + ".xlsx"
		datalist.pop(u"年月")
		datalist.pop(u"name")

		# ファイルのオープン
		#book = xlwt.Workbook( templatefile )
		#bk = open_workbook( templatefile, formatting_info = True )
		bk = open_workbook( templatefile )
		book = copy( bk )

		# シートの特定
		#sheet = book.add_sheet( u"請求書")
		#sheet = book.get_sheet( u"請求書")
		sheet = book.get_sheet(0)

		# 内容の書き換え
		for d in datalist.values():
			print( d )
			sheet.write( d[0], d[1], d[2])

		# シートの書式設定
		sheet.col(A).width = 20
		sheet.col(C).width = 5000

		# テンプレートファイルのコピー
		book.save( file )

#-----------------------------------------------------------
if __name__ == '__main__':
	run()
