# coding: utf-8
from datetime import datetime
from pywinauto import application
app = application.Application(backend="uia").start("notepad.exe")

dlg_spec = app['無題 - メモ帳']
dlg_spec.draw_outline()


# Notepad クラス (Notepad のウィンドウ) を探して日時を入力
#dlg_spec.Edit1.SetText(datetime.now())
#dlg_spec.Edit1.SetText("test")
#dialog = app[u"ファイル->名前を付けて保存"]


# メニューを選択
#app.Notepad.MenuSelect(u"ファイル->名前を付けて保存")
dlg_spec.MenuSelect(u"ファイル->名前を付けて保存")

# 「名前を付けて保存」のウィンドウを探す
dialog = app[u"名前を付けて保存"]
# ファイル名を設定
dialog.Edit1.SetText(u"datetime.txt")
# 保存ボタンをクリック
dialog.Button1.Click()

# すでにファイルが存在すれば上書きの確認が求められる
confirm = app[u"名前を付けて保存の確認"]
if confirm.Exists():  # 確認を求められたかどうか
    confirm.Button1.Click() # 上書きする

# キーストロークを使って終了させる
app.Notepad.TypeKeys("%FX") # 終了 (Alt+F X)
