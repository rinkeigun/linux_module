# scraping-img-1.py
 
import requests # urlを読み込むためrequestsをインポート
from bs4 import BeautifulSoup # htmlを読み込むためBeautifulSoupをインポート
import re
import os

 
URL = 'https://www.freepik.com/free-icons' # URL入力
 
soup = BeautifulSoup(requests.get(URL).content,'lxml') # bsでURL内を解析
 
for link in soup.find_all('a', href=re.compile("free-icons/")): # imgタグを取得しlinkに格納
    category = BeautifulSoup(requests.get(link.get('href')).content,'lxml') # bsでURL内を解析
    folder   = link.string
    images = [] # 画像リストの配列
    paging = category.find('div', class_="paging")  # imgタグを取得しlinkに格納
    max_page = paging.find_all("li")[len(paging.find_all("li"))-1].a
    url = max_page.get('href').split('&')
    page_str = url[1].split('=')
    for page_no in range(1,int(max_page.string)):
        page_str[1] = str(page_no)
        print(page_no)
        print(url)
        url[1] = '='.join(page_str)
        new_link = '&'.join(url)
        print(new_link)
        img_page = BeautifulSoup(requests.get(new_link).content,'lxml') # bsでURL内を解析
    #    for paging_li in paging.find_all("li"): # imgタグを取得しlinkに格納
    #        print( paging_li.a )
    #        #print( paging.ul.li.string )

        for cat_link in img_page.find_all('img', class_="preview"): # imgタグを取得しlinkに格納
            print ( cat_link.get('src').split('?')[0] )
            images.append(cat_link.get('src').split('?')[0])
 
    path = 'img/'+folder
    if not os.path.exists(path): os.makedirs(path)
    for target in images: # imagesからtargetに入れる
        re = requests.get(target)
        with open(path+'/' + target.split('/')[-1], 'wb') as f: # imgフォルダに格納
            f.write(re.content) # .contentにて画像データとして書き込む

print("ok") # 確認