# -*- coding: utf-8 -*-
# File name : furlrequest.py
# Date      : 2017/11/05
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

from urllib.request import urlopen
from urllib.request import Request

class run:

	def __init__(self):
		req = Request( "http://www.no1iot.com/" )
		#ftp = Request( "ftp://sample.com/" )
		print( req )
		with urlopen( req ) as resp:
			print( resp.read())

if __name__ == '__main__':
	run()
