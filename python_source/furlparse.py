# -*- coding: utf-8 -*-
# File name : furlparse.py
# Date      : 2017/11/07
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

from urllib.parse import urlparse
from urllib.parse import urljoin

class run:

	def __init__(self):
		url =  "http://www.no1iot.com/index.php?aaa=bbb" 
		url = urlparse( "http://www.no1iot.com/index.php?aaa=bbb" )
		print( type(url) )
		print( url )
		print( "scheme   : " + url.scheme )
		print( "netloc   : " + url.netloc )
		print( "path     : " + url.path )
		print( "params   : " + url.params )
		print( "query    : " + url.query )
		print( "fragment : " + url.fragment )
		url = urljoin( "http://www.no1iot.com/index.php?aaa=bbb", "index2.php" )
		print( url )
		#print( url.ParseResult['scheme'] )

if __name__ == '__main__':
	run()
