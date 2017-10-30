# -*- coding: utf-8 -*-
# File name : mgraph.py
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
			['グラフの種類','mgraphtype'],
			['線の太さ、色','mline'],
			['マーカー','mmarker'],
			['凡例、タイトル、ラベル',''],
			['複数グラフ',''],
			['3D','m3d'],
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
	
	
