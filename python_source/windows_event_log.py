# coding: UTF-8
import csv
import re

# CSVファイルを開いてリストに読み込む
with open('eventlog.csv','r',encoding='utf8') as csvf:
    in_reader = csv.reader(csvf)
    tmp_list = list(in_reader)

# ソートの前に0:13:54のような時刻の頭が一桁の時間を2桁に補正する
pre_mk = re.compile(r'\s(\d{1}):')
for j in range(len(tmp_list)):
    tmp_list[j][0] = pre_mk.sub(r' 0\1:',tmp_list[j][0])

# 日付・時刻の昇順にソートしなおす
sl = sorted(tmp_list,key = lambda X:X[0])

is_started_dic = {} # 日別に最初の起動時刻を記録したらTRUE
in_day = '' # カレントの日付キーを保持する
day_dic = {} # 日別に初回起動時刻（start）と最終終了時刻（stop）を保持する

# 日別に初回起動時刻と最終終了時刻を更新する
dtpat = re.compile(r'(\d{4}/\d{2}/\d{2})\s+(\d+):(\d+):(\d+)')
for i in range(len(sl)):
    mo = dtpat.search(sl[i][0])
    if(mo):
        if(mo.group(1) not in is_started_dic):
            is_started_dic.setdefault(mo.group(1),False)
            
        if(sl[i][1] == '6005' or sl[i][1] == '7001'):
            in_day = mo.group(1)
            if(is_started_dic.get(mo.group(1),False) == False):
                is_started_dic[mo.group(1)] = True
                day_dic.setdefault(mo.group(1),{}).setdefault('start',sl[i][0])
                day_dic[mo.group(1)].setdefault('stop','')
        else:
            day_dic[in_day]['stop'] = sl[i][0]

# 結果をCSVに書き出す
with open('output.csv','w',newline='') as outcsv:
    csvwriter = csv.writer(outcsv)
    csvwriter.writerow(['年月日','初回起動','最終終了'])
    for k,v in day_dic.items():
        csvwriter.writerow([k,v['start'],v['stop']])
    outcsv.close()