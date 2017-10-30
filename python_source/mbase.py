# -*- coding: utf-8 -*-
# File name   : mbase.py
# Date        : 2017/10/26
# Last Modify : 2017/10/29
# Author      : Huiqun Lin
# Ver         : 0.2
#-----------------------------------------------

# クラスの説明
# このクラスは、メニューの基本クラスとする
import importlib

class mBase:

#関数リスト
	def __init__(self, lst):
		# クラスの初期化
		self.com = ''
		self.lst = lst
		self.mview()

	def __str__(self):
		print('str')

	# 1画面の表示 
	def mview(self):
		self.mlist()
		self.mexp()
		self.mcommand()
		self.mexcute()

	# リスト
	def mlist(self):
		i = 0
		for nl in self.lst:
			i+=1
			print( str(i) + ':'+nl[0] )
	# 動作説明 
	def mexp(self):
		print( '操作説明' )
	# コマンド入力部分 
	def mcommand(self):
		self.com = input('>>')
	# 処理
	def mexcute(self):
		i = 0
		for nl in self.lst:
			i+=1
			print( self.com + str(i) +':'+ nl[1] )
			if int(self.com) == i:
				print( nl[1] )
				obj = importlib.import_module(nl[1])
				obj.run()
		#self.mview()
	def __del__(self):
		print( 'クラスが終了するときに呼び出される' )
# mBaseの終わり

# テストプログラムはこれより下に書く
if __name__ == '__main__':
	com_list = [
		['動作', 'dousa'],
		['２つ目', '2me']
	]
	b = mBase(com_list)
