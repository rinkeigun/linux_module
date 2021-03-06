# -*- coding: utf-8 -*-
# File name : mimage.py
# Date      : 2017/11/19
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import mbase
from mbase import mBase

# クラスの説明
# このクラスは、画像を取り扱う例
class run(mBase):

#関数リスト
	def __init__(self):
		com_list = [
			['画像フォーマット','mimageformat'],
			['画像基本','mimagebase'],
			['画像変形','mimagepoint'],
			['画像色','mimagecolor'],
			['画像処理','mimageprocess'],
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
	
	
