# -*- coding: utf-8 -*-
# File name : mcontrol.py
# Date      : 2017/11/03
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import mbase
from mbase import mBase

# クラスの説明
# このクラスは、制御を取り扱う例
class run(mBase):

#関数リスト
	def __init__(self):
		com_list = [
			['if','mif'],
			['while','mwhile'],
			['for','mfor'],
			['break','mbreak'],
			['continue','mcontinue'],
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
	
	
