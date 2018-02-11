# _*_ coding: utf-8 _*_
# 引数にパスワードを入力してください

from bs4 import BeautifulSoup
import requests
import sys


payload = {
    'identity': 'huiqun.lin@gmail.com',
    'password': sys.argv[1]
}

# authenticity_tokenの取得
s = requests.Session()
#r = s.get('https://www.shufti.jp/users/login')
#soup = BeautifulSoup(r.text)
#auth_token = soup.find(attrs={'name': 'authenticity_token'}).get('value')
#payload['authenticity_token'] = auth_token

# ログイン
#method="post"なら、data=ディクショナリ
#method="get"なら、params=ディクショナリ
s.post('https://www.shufti.jp/users/login', data=payload)
r = s.get('https://www.shufti.jp/jobs/search/business/research')
soup = BeautifulSoup(r.text)

print(soup)
