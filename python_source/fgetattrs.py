#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name : fgetattrs.py
# Date      : 2017/11/08
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------
 
from urllib.request import urlopen
from bs4 import BeautifulSoup
 
class run:
	def __init__(self):
		url = "http://www.yahoo.co.jp"
		htmlfp = urlopen(url)
		html = htmlfp.read().decode("utf-8", "replace")
		htmlfp.close()
 
		soup = BeautifulSoup(html, "html5lib")
		# findAll 条件にあうタグを全て探してくれる
		for link in soup.findAll("a", href='https://about.yahoo.co.jp/'):
			print (link)
			print (link.text)
			print (link.attrs)
			print (link.attrs['href'])

# テストプログラムはこれより下に書く
if __name__ == '__main__':
        run()

