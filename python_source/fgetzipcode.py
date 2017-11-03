# -*- coding: utf-8 -*-
# File name : fgetzipcode.py
# Date      : 2017/11/03
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

import json
import requests
import sqlite3

class run:
	def __init__(self):
		self.url = 'http://zipcloud.ibsnet.co.jp/api/search'
		self.excute()

	def excute(self):
		if 1:
		#try:
			i_code = 1520 
			connector = sqlite3.connect("zipcode20171103.db")
			sql = "create table IF NOT EXISTS zipcodejp (zipcode text, address1 text, address2 text, address3 text, kana1 text, kana2 text, kana3 text, prefcode text, message text)"
			connector.execute( sql )
			while i_code < 9999999:
				zipcode = '%07d'%i_code
				print ('zipcode  : ' + zipcode)
				query = {
					'zipcode': zipcode,
       		 		}

				r = requests.get(self.url, params=query) 
				#print ('status  : ' + str(r.json()['status']))
				#print (json.dumps(r.json(), sort_keys=True, indent=2))
				if r.json()['results'] is not None:
					data = r.json()['results'][0]
					zipcode = data['zipcode']
					address1 = data['address1']
					address2 = data['address2']
					address3 = data['address3']
					kana1 = data['kana1']
					kana2 = data['kana2']
					kana3 = data['kana3']
					prefcode = data['prefcode']
					message = r.json()['message']
					sql = "insert into zipcodejp values('%s', '%s', '%s', '%s', '%s','%s','%s','%s','%s')" % (zipcode,address1,address2,address3,kana1,kana2,kana3,prefcode, message)
					connector.execute( sql )
					connector.commit()
				i_code += 1	
			connector.close()
#		except:
#			print('test')

	def __del__(self):
		pass
# テストプログラムはこれより下に書く
if __name__ == '__main__':
        run()

