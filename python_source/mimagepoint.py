# -*- coding: utf-8 -*-
# File name : mimagepoint.py
# Date      : 2017/11/19
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import mbase
from mbase import mBase

# クラスの説明
# このクラスは、画像変形を取り扱う例
class run(mBase):

#関数リスト
	def __init__(self):
		com_list = [
			['変形（拡大）',''],
			['変形（縮小）',''],
			['変形',''],
			['アフィン変換',''],
			['射影変換',''],
			['移動',''],
			['オフセット','fioffset'],
			['左右反転','fileft2right'],
			['上下反転','fitop2buttom'],
			['回転',''],
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
	
	
