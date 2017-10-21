# coding: UTF-8 #
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sqlite3
import datetime
import time

url = "http://www.nikkei.com/markets/kabu/"

while 1: 
	if datetime.datetime.now().minute != 5:
		time.sleep(58)
		continue	
	while datetime.datetime.now().second != 59:
		time.sleep(1)
	time.sleep(1)
	time_ = datetime.datetime.now().strftime( "%Y/%m/%d %H:%M:%S")
	html = urlopen( url )

	soup = BeautifulSoup( html, "html5lib" )
	span = soup.find_all( "span" )

	nikkei_heikin = ""

	for tag in span:
		try:
			string_ = tag.get("class").pop(0)
			if string_ in "mkc-stock_prices":
				nikkei_heikin = tag.string
				break
		except:
			pass
	connector = sqlite3.connect("sqlite_test.db")
	sql = "create table IF NOT EXISTS test_table ( datetime text, price text )"
	connector.execute( sql )
	sql = 'insert into test_table values( "%s" , "%s" )' % (time_ , nikkei_heikin )
	connector.execute( sql )
	
	connector.commit()
	connector.close()
	print (nikkei_heikin)
