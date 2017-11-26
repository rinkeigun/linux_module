# -*- coding: utf-8 -*-
# File name : moperator.py
# Date      : 2017/11/19
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import mbase
from mbase import mBase

# クラスの説明
# このクラスは、演算子を取り扱う例
class run(mBase):

#関数リスト
	def __init__(self):
		com_list = [
			['代数',''],
			['ビット',''],
			['代入',''],
			['比較',''],
			['論理',''],
			['ブール',''],
			['条件',''],
			['文字列',''],
			['演算子の優先順位',''],
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
	
	
