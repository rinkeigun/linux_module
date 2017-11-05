# -*- coding: utf-8 -*-
# File name : furlheader.py
# Date      : 2017/11/05
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

from urllib.request import urlopen
from urllib.request import Request
from urllib.parse   import urlencode

class run:

	def __init__(self):
		url =  "http://www.innov-soft.co.jp/sendmail.php" 
		user_agent = 'Mosilla/5.0 (Windows NT 6.1; Win64; x64)'
		values =  {'name':'wo',
			'mail':'huiqun.lin@gmail.com',
			'tel':'080-9667-2468',
			'title':'愛を語ろう',
			'body':'愛している',
			} 
		headers = {'User-Agent':user_agent}
		data = urlencode( values )
		data = data.encode( 'ascii' )
		req = Request( url, data , headers)
		with urlopen( req ) as resp:
			print( resp.read())

if __name__ == '__main__':
	run()
