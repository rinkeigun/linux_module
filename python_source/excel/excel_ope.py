#!/usr/bin/env python
# -*- coding: utf-8 -*-

import win32com.client

"""
Excelの操作
"""

# Excelのインスタンスを用意
xlApp = win32com.client.Dispatch("Excel.Application")

# Excelを閉じる
xlApp.Quit()

"""
ブックの操作
"""

# ブックを開く（読み取り専用）
wb = xlApp.Workbooks.Open("sample.xls", ReadOnly="True")

# ブックを別名保存する
# ファイル名を指定すると、カレント・ディレクトリに保存する。フルパスでの指定も可能。
# 読み取り専用で開くダイアログを表示しない
# Excel95-97形式
wb.SaveAs("sample.xls", ReadOnlyRecommended="False", FileFormat=xlExcel9795)

# ブックを閉じる
# - True: 保存して閉じる
# - False: 保存しないで閉じる
wb.Close(True)

"""
シートの操作
"""
# シートを追加
ws = wb.Worksheets.Add()

# シートを末尾(<シート数>個目のシートの後)に移動。
# 第1パラメータの`None`が無いと動かない。これで数日ハマった。。。
ws.Move(None, wb.Worksheets(wb.Worksheets.Count))

# コピーも同様。
ws.Copy(None, wb.Worksheets(1))

# シート名の変更
ws.Name = "sample2"

# シートの表示倍率を変更 [%]
ws.PageSetup.Zoom = 70

# 列の幅の変更
# A列からG列について、それぞれの列幅をWorksheet'origin'の同じ列の幅に設定する
for i in ws.Range("A:G"):
    i.ColumnWidth = wb.Worksheets("origin").Columns(i.Column).ColumnWidth

# オートフィルタ
# 3～7行目にオートフィルタを設定する(3行目にフィルタのドロップダウン▼マークがつく)
ws.Rows("3:7").AutoFilter()

# 配列で入力する
# オートフィルタの列名入力等に便利。
str_array = ["name 1", "name 2", "name 3", "name 4"]
ws.Range("A1:A4").Value = str_array


"""
セル範囲の操作
"""
# 列の挿入
# 1列目の左に、1列分を挿入
ws.Columns(1).Insert()

# 行の挿入
# 3行目の上に、5行分を挿入
ws.Rows("3:7").Insert()

# 行の削除
ws.Rows("1:6").Delete()

# セル範囲の内容を削除
ws.Range("A:C").ClearContents()

# セル範囲の背景色を変更
ws.Range("A1:D8").Interior.ColorIndex = 24 # Ice Blue : 24

# セル範囲の文字色を変更
ws.Rows("2:6").Font.ColorIndex = 1 # black : 1

# copy contents
ws.UsedRange.Copy(ws.Range("A1"))

# 値の貼り付け
ws.Range("A1:C3").PasteSpecial(Paste=xlPasteValues) # xlPasteValues = 

# セルに文字列として入力されている数字を、数字として使いたい場合、int()を使う。
# print出力のためには、さらにstr()を使う
print("B1:" + str(int(ws.Cells(1, 2).Value))

# セル範囲に一括入力する例
for i in ws.Range("B1:B10"):
    if ws.Cells(i.Row, 1).Value == None: # A列が空だったら
        i.Value = i.Row                  # B列に行番号を入力

# 並べ替え
# セル(1,1)から(10,10)が対象
# 1列目をキーとする
# 昇順
# 1行目をヘッダとする
sortTable = ws.Range(ws.Cells(1, 1), ws.Cells(10, 10))
sortTable.Sort(Key1 = sortTable.Columns(1), \
    Order1 = xlAscending, \
    Header = xlYes, \
    Orientation = xlSortRows)

"""
セルの操作
"""
# 数式を入力
ws.Range("D1").Formula = "=VLOOKUP($C1,data!$A$3:$I$10,2,0)"

# セルの値がエラーかどうかチェック
if ws.Range("A1").Errors.Item(1).Value == True: # xlEvaluateToError = 1
    ws.Range("B1").Value = "ERROR!"