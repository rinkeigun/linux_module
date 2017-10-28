import urllib 
import copy
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#targetUrl = "http://en.wikipedia.org"
targetUrl = "http://www.nisshin-sci.co.jp"
pages = set()
def getLinks(pageUrl):
    global pages
    urlStr = targetUrl+pageUrl
    print(urlStr)
    html = urlopen(urlStr)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print(bsObj.h1.get_text())
        #print(bsObj.find(id ="mw-content-text").findAll("p")[0])
        #print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")
    
    #for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
    for link in bsObj.findAll("a", href=re.compile("^(/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                to_str = copy.copy(newPage)
                print("----------------\n"+urllib.parse.unquote(to_str.encode('ascii')))
                #print("----------------\n"+urllib.parse.unquote(to_str.encode('raw_unicode_escape')).decode('utf-8'))
                #print("----------------\n"+newPage)
                #print("----------------\n"+u(newPage))
                pages.add(newPage)
                getLinks(newPage)
getLinks("") 
