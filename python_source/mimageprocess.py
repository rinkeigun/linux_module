# -*- coding: utf-8 -*-
# File name : mimageprocess.py
# Date      : 2017/11/19
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import mbase
from mbase import mBase

# クラスの説明
# このクラスは、画像処理を取り扱う例
class run(mBase):

#関数リスト
	def __init__(self):
		com_list = [
			['ぼかし',''],
			['モザイク',''],
			['色反転',''],
			['マスク',''],
			['グレースケール','figrayscale'],
			['ヒストグラム(1ch)','fihistgram1'],
			['ヒストグラム(3ch)','fihistgram3'],
			['ヒストグラム(伸張化) ',''],
			['ヒストグラム(平坦化) ',''],
			['閾値',''],
			['キャニー法',''],
			['２値化',''],
			['カラー２値化',''],
			['切り取り',''],
			['輪郭と外接矩形',''],
			['エッジ検出',''],
			['直線検出',''],
			['円検出',''],
			['透明',''],
			['合成',''],
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
	
	
