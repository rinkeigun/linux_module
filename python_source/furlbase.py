# -*- coding: utf-8 -*-
# File name : furlbase.py
# Date      : 2017/11/05
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

from urllib.request import urlopen

class run:

	def __init__(self):
		html = urlopen( "http://www.no1iot.com/" )
		print( html.read())

if __name__ == '__main__':
	run()
