# -*- coding: utf-8 -*-
# File name : mgraphtype.py
# Date      : 2017/10/26
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import mbase
from mbase import mBase

# クラスの説明
# このクラスは、グラフを描くための例
class run(mBase):

#関数リスト
	def __init__(self):
		com_list = [
			['折れ線','mgraphplot'],
			['散布図','mgraphscatter'],
			['棒グラフ','mgraphbar'],
			['QQプロット','mgraphqq'],
			['円グラフ','mgraphpie'],
			['極座標','imgraphpolar'],
			['ヒストグラム','mgraphhistgram'],
			['箱ひげ図','mgraphboxplot'],
			['3D',''],
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
	
	
