# -*- coding: utf-8 -*-
# File name : fgetwholesite.py
# Date      : 2017/11/12
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

import urllib 
import copy
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re
import sqlite3
import datetime
import sys

pages = set()
class run:
	def __init__(self):
		#targetUrl = "http://en.wikipedia.org"
		#targetUrl = "http://innov-soft.co.jp"
		# 取得したいサイト
		self.targetUrl = "http://yahoo.co.jp"

		#　自サイトのurlのバックアップ
		self.myurl = urlparse( self.targetUrl).netloc

		# DBの接続
		self.connector = sqlite3.connect('mydata.db')

		# errorの出力テーブルを作成
		sql = "create table IF NOT EXISTS errorManager (edt datetime, eCode text, eType text, eMessage text)"
		self.connector.execute( sql )
		
		# 内部urlを記憶するテーブルを生成
		sql = "create table IF NOT EXISTS internalURL (edt datetime, url text)"
		self.connector.execute( sql )
		self.connector.commit()
		self.getLinks(self.targetUrl)
		#self.getLinks("")
	def getLinks(self, pageUrl):
		global pages
		#urlStr = self.targetUrl+"/"+pageUrl
		urlStr = pageUrl
		print(urlStr)
		html = urlopen(urlStr)
		bsObj = BeautifulSoup(html, "html.parser")
		try:
			#print(bsObj.h1.get_text())
			print(bsObj.title.get_text())
			#print(bsObj.find(id ="mw-content-text").findAll("p")[0])
			#print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
		except AttributeError:
			print("This page is missing something! No worries though!")
    
			#for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
			#for link in bsObj.findAll("a", href=re.compile("^(/)")):
		for link in bsObj.findAll("a"):
			try:
				print( link.attrs )
				if 'href' in link.attrs:
					url = urlparse( link.attrs['href'] )
					if self.myurl in url.netloc:
						print( type(url) )
						print( url )
						print( "scheme   : " + url.scheme )
						print( "netloc   : " + url.netloc )
						print( "path     : " + url.path )
						print( "params   : " + url.params )
						print( "query    : " + url.query )
						print( "fragment : " + url.fragment )

						#if link.attrs['href'] == 'javascript:void(0);':
						#	return()
						#if link.attrs['href'] == '#yjContentsStart':
						#	return()
						if link.attrs['href'] not in pages:
							#We have encountered a new page
							newPage = link.attrs['href']
							to_str = copy.copy(newPage)
							#print("----------------\n"+urllib.parse.unquote(to_str.encode('ascii')))
							#print("----------------\n"+urllib.parse.unquote(to_str.encode('raw_unicode_escape')).decode('utf-8'))
							print("----------------\n"+newPage)
							#print("----------------\n"+u(newPage))
							sql = "insert into internalURL values( '%s', '%s')" % ( datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"), newPage)
							self.connector.execute( sql )
							self.connector.commit()
							pages.add(newPage)
							self.getLinks(newPage)
			except KeyboardInterrupt:
				sys.exit()
			except ValueError as e:
				sql = "insert into errorManager values( '%s', '%s', '%s', '%s')" % ( datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"), e.errno, e.strerror, e.args)
				self.connector.execute( sql )
				self.connector.commit()
				continue
			except:
				#sql = "insert into errorManager values( '%s', '%s', '%s', '%s')" % ( datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 'a', 'a', sys.exc_info())
				sql = "insert into errorManager values( '%s', '%s', '%s', '%s')" % ( datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 'a', 'a', 'b')
				print( sql )
				self.connector.execute( sql )
				self.connector.commit()
				continue
	def __del__(self):
		self.connector.close()
					

if __name__ == '__main__':
        run()

