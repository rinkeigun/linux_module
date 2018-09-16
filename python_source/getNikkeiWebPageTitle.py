# -*- coding: utf-8 -*-
#import urllib as myurllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.nikkei.com/"

#html = myurllib.urlopen( url )
html = urlopen( url )

#soup = BeautifulSoup( html, "htmlparser" )
soup = BeautifulSoup( html, "html5lib" )

title_tag = soup.title

title = title_tag.string

print( title_tag )
print( title)
