from urllib.request import urlopen
from urllib.error import HTTPError
#from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen( url )
	except HTTPError as e:
		print(e)
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		#title = bsObj.body.h1
		title = bsObj.title
	except AttributeError as e:
		return None
	return title

title = getTitle( "http://no1iot.com/" )
if title == None:
	print( "Title could not be found!")
else:
	print( title )
