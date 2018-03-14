from pywinauto import application
import time

app = application.Application()
app.start("notepad.exe")
app.Notepad.wait('visible')
#time.sleep(3)
app.Notepad.edit.TypeKeys('Hello world')
app.Notepad.MenuSelect(u'ファイル(&F)->名前を付けて保存(&A)...')

# 動作を分けてはだめ？
#app.Notepad.MenuSelect(u'ファイル(&F)')[u'名前を付けて保存(&A)...']
#app.Notepad.MenuSelect(u'ファイル(&F)')
#app.Notepad.MenuSelect(u'名前を付けて保存(&A)...')

app[u'名前を付けて保存'].edit.SetText('tamesi.txt')
app[u'無題.*メモ帳'].CaptureAsImage().save('auto_capture.png')
app[u'名前を付けて保存'][u'保存(&S)'].Click()
