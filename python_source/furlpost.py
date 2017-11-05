# -*- coding: utf-8 -*-
# File name : furlpost.py
# Date      : 2017/11/05
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

from urllib.request import urlopen
from urllib.request import Request
from urllib.parse   import urlencode
import chardet

class run:

	def __init__(self):
		url =  "http://www.innov-soft.co.jp/sendmail.php" 
		values =  {'name':'wo',
			'mail':'huiqun.lin@gmail.com',
			'tel':'080-9667-2468',
			'title':'愛を語ろう',
			'body':'愛している',
			} 
		data = urlencode( values )
		data = data.encode( 'ascii' )
		req = Request( url, data )
		with urlopen( req ) as resp:
			#print( resp.read())
			#data = ''.join(resp.read())
			#data = ''.join(resp.readlines())
			data = resp.read()
			guess =chardet.detect(data)
			unicode_data = data.decode( guess['encoding'] )
			print( unicode_data )

#-----------------------------------------------------------
if __name__ == '__main__':
	run()
