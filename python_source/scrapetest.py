from urllib.request import urlopen
html = urlopen( "http://www.no1iot.com/" )
print( html.read())
