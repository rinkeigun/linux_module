# -*- coding: utf-8 -*-
# File name : mscraping.py
# Date      : 2017/11/03
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import mbase
from mbase import mBase

# クラスの説明
# このクラスは、ウェブスクレピングを取り扱う例
class run(mBase):

#関数リスト
	def __init__(self):
		com_list = [
			['API調査','mwebapi'],
			['robots.txt',''],
			['URL構造-基本','furlbase'],
			['URL構造-一時的な場所に保存','furlretrieve'],
			['URL構造-request','furlrequest'],
			['URL構造-一覧ページ',''],
			['URL構造-詳細ページ',''],
			['アクセス方法-GET',''],
			['アクセス方法-POST','furlpost'],
			['アクセス方法-HEADER','furlheader'],
			['アクセス方法-認証',''],
			['例外','furlexcept'],
			['ページ構造確認',''],
			['内容の取得','mgetcontent'],
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
	
	
