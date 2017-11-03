# -*- coding: utf-8 -*-
# File name : mtype.py
# Date      : 2017/11/03
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import mbase
from mbase import mBase

# クラスの説明
# このクラスは、型を取り扱う例
class run(mBase):

#関数リスト
	def __init__(self):
		com_list = [
			['ブール','mtext'],
			['数値','mini'],
			['イテレータ','mxml'],
			['シーケンス','mjson'],
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
	
	
