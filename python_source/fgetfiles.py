#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name : fgetfile.py
# Date      : 2017/11/09
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

import requests
import time

from bs4 import BeautifulSoup

BASE_URL = u"http://seanlahman.com/"
EXTENSIONs = [
	u"csv.zip",
]

# 書き込みモードの設定：1 binary, 0 not binary
binary = 0
if 1:
	binary = 1 
	
#EXTENSION = u"csv.zip"

urls = [
	u"http://seanlahman.com/baseball-archive/statistics/",
]


class run:
	def __init__(self):
		for url in urls:

			download_urls = []
			r = requests.get(url)
			soup = BeautifulSoup(r.content)
			links = soup.findAll('a')

			# URLの抽出
			for link in links:
				href = link.get('href')
	
				for EXTENSION in EXTENSIONs:
					if href and EXTENSION in href:
						download_urls.append(href)

			# ファイルのダウンロード（ひとまず3件に制限）
			#for download_url in download_urls[:3]:
			for download_url in download_urls:

				# 一秒スリープ
				time.sleep(1)

				file_name = download_url.split("/")[-1]

			if BASE_URL in download_url:
				r = requests.get(download_url)
			else:
				r = requests.get(BASE_URL + download_url)

			# ファイルの保存
			w_mode = 'w'
			if binary == 1:
				w_mode ='wb' 
			if r.status_code == 200:
				f = open(file_name, w_mode)
				f.write(r.content)
				f.close()

# テストプログラムはこれより下に書く
if __name__ == '__main__':
	run()

