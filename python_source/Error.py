from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
#from bs4 import BeautifulSoup
# これで日本語入力できる

try:
#	html = urlopen( "http://www.google.com/" )
	html = urlopen( "http://hahaahnoiot.com/" )
except HTTPError as e:
	print(e)
except URLError as e:
	print("The server could not be found!")
except :
	print("上記以外のエラー!")
else:
	print("It worked")
#bsObj = BeautifulSoup(html.read())
#print( bsObj.title )
