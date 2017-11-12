# -*- coding: utf-8 -*-
# File name : mdb.py
# Date      : 2017/10/29
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import mbase
from mbase import mBase

# クラスの説明
# このクラスは、データベースを取り扱う例
class run(mBase):

#関数リスト
	def __init__(self):
		com_list = [
			['mysql','mmysql'],
			['posgresql','mposgresql'],
			['oracle','moracle'],
			['sqlite','fsqlite'],
		]
		mBase.__init__(self, com_list)
		

	def __str__(self):
		print('str')

	def __del__(self):
		print( 'クラスが終了するときに呼び出される' )
# mBaseの終わり

# テストプログラムはこれより下に書く
if __name__ == '__main__':
	mMain()
	
	
