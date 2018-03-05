import subprocess
subprocess.Popen(r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE')

# parameter
subprocess.Popen([r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE', r'D:\2017-12\RPAソフト.ods'])
subprocess.Popen(['start', r'D:\2017-12\RPAツール比較・評価テンプレート.xlsx'], shell=True)

#フォルダーを開く
subprocess.Popen(['explorer' , r'D:\2018-03'])
