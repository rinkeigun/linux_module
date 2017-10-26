# -*- coding: utf-8 -*-
# File name : mmain.py
# Date      : 2017/10/26
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import mbase
from mbase import mBase

# クラスの説明
# このクラスは、メニューの基本クラスとする
class mMain(mBase):

#関数リスト
	def __init__(self):
		com_list = [
			'動作',
			'２つ目',
			'３２つ目',
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
	
	
