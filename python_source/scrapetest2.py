# -*- coding: utf-8 -*-
import requests
from chardet.universaldetector import UniversalDetector
headers = {"User-Agent":"hoge"}
url = "http://www.no1iot.com"
resp = requests.get( url, timeout=1, headers=headers)
#print(UniversalDetector().feed(resp.text))
print(resp.text)
