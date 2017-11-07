# -*- coding: utf-8 -*-
# File name : furlrobot.py
# Date      : 2017/11/05
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#from urllib.request import urlopen
import urllib.robotparser

class run:

	def __init__(self):
		rp = urllib.robotparser.RobotFileParser()
		rp.set_url("http://www.no1iot.com/rebots.txt" )
		rp.read()
		#rrate = rp.request_rate('*')
		#rrate.requests
		#rrate.seconds
		#rp.crawl_delay('*')
		#rp.can_fetch('*','http://someurl.com/')

if __name__ == '__main__':
	run()
