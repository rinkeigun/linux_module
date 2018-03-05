# coding = utf-8

import subprocess
import os

subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE')

# parameter
subprocess.Popen([r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE', r'D:\2017-12\RPAソフト.ods'])
subprocess.Popen(['start', r'D:\2017-12\RPAツール比較・評価テンプレート.xlsx'], shell=True)

#フォルダーを開く
subprocess.Popen(['explorer' , r'D:\2018-03'])

#標準出力を受け取る
p = subprocess.Popen("DIR", shell = True, stdout = subprocess.PIPE)
print(p.returncode)
print(p.communicate()[0].decode('sjis'))
#print(type(p.communicate()[0]))

#引数設定
NAME='ABC.jpg' # 適当な画像ファイル名を設定して下さい
returncode = subprocess.call(['C:\Windows\System32\mspaint.exe', NAME])
print(returncode)

NAME = 'Booke1.xls' # 適当なファイル名を設定して下さい
returncode = subprocess.call(['cmd.exe', '/C', 'start', NAME])
#returncode = subprocess.call(['cmd.exe', '/C', NAME])
print(returncode)

NAME = 'Booke1.xls' # 適当なファイル名を設定して下さい
os.system('start '+NAME) 
