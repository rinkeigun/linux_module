# -*- coding: utf-8 -*-
# File name : mimagebase.py
# Date      : 2017/11/19
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import mbase
from mbase import mBase

# クラスの説明
# このクラスは、画像基本を取り扱う例
class run(mBase):

#関数リスト
	def __init__(self):
		com_list = [
			['生成（新規）','fiopen'],
			['生成（読み込み）','finew'],
			['画像の配列化','fidata'],
			['表示','fishow'],
			['保存','fisave'],
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
	
	
