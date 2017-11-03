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
			['型','mtype'],
			['文字列','mstring'],
			['リスト','mlists'],
			['演算子','moperator'],
			['制御','mcontrol'],
			['関数','mfunction'],
			['クラス','mclass'],
			['例外','mexception'],
			['パッケージ、モジュール','mmodule'],
			['スクレイピング','mscraping'],
			['画像','mimage'],
			['ファイル処理','mfile'],
			['DB','mdb'],
			['グラフ','mgraph'],

			['音声','mvoice'],
			['機械学習','mmachinelearning'],
		]
		mBase.__init__(self, com_list)
		

	def __str__(self):
		print('str')

	def __del__(self):
		pass
# mBaseの終わり

# テストプログラムはこれより下に書く
if __name__ == '__main__':
	mMain()
	
	
