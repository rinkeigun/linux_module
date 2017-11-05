# -*- coding: utf-8 -*-
# File name : furlretrieve.py
# Date      : 2017/11/05
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

from urllib.request import urlopen
from urllib.request import urlretrieve

class run:

	def __init__(self):
		req, headers = urlretrieve( "http://www.no1iot.com/" )
		print( req )
		print( headers )
		html = open( req )
		print( html.read())

if __name__ == '__main__':
	run()
