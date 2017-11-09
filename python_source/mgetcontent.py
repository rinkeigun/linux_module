# -*- coding: utf-8 -*-
# File name : mcontent.py
# Date      : 2017/11/04
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import mbase
from mbase import mBase

# クラスの説明
# このクラスは、ファイルを取り扱う例
class run(mBase):

#関数リスト
	def __init__(self):
		com_list = [
			['ページ全体','fwholepage'],
			['タグ','fgettag'],
			['属性','fgetattrs'],
			['ファイルの取得','fgetfiles'],
			['JavaScript','mjavascript'],
			['CSS','mcss'],
			['画像','mwebimage'],
			['音声','msound'],
			['映像','mmovie'],
			['サイト全体','mwholesite'],
			['インターネット','minternet'],
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
	
	
