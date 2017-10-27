#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
#import urllib
#from urllib3.request import urlopen
from urllib.request import urlopen
from BeautifulSoup import BeautifulSoup
 
url = "http://www.yahoo.co.jp"
#htmlfp = request.urlopen(url)
htmlfp = urlopen(url)
html = htmlfp.read().decode("utf-8", "replace")
htmlfp.close()
 
soup = BeautifulSoup(html, "html5lib")
#soup = BeautifulSoup(html, 'lxml')
for link in soup.findAll("a"):
	print (link)
