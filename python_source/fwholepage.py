# -*- coding: utf-8 -*-
# File name : fwholepage.py
# Date      : 2017/11/08
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

from urllib.request import urlopen
from bs4 import BeautifulSoup

class run:
	def __init__(self):
		html = urlopen( "http://www.google.com/" )
		bsObj = BeautifulSoup(html.read())
		print( bsObj )

# テストプログラムはこれより下に書く
if __name__ == '__main__':
        run()

