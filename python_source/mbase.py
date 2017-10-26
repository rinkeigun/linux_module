# -*- coding: utf-8 -*-
# File name : mbase.py
# Date      : 2017/10/26
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

# クラスの説明
# このクラスは、メニューの基本クラスとする
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
		for nl in self.lst:
			print( nl )
	# 動作説明 
	def mexp(self):
		print( '操作説明' )
	# コマンド入力部分 
	def mcommand(self):
		self.com = input('>>')
	# 処理
	def mexcute(self):
		if self.com == 'a':
			print('a')
		elif self.com == 'b':
			print('b')
		else:
			self.mview()
	def __del__(self):
		print( 'クラスが終了するときに呼び出される' )
# mBaseの終わり

# テストプログラムはこれより下に書く
if __name__ == '__main__':
	com_list = [
		'動作',
		'２つ目'
	]
	b = mBase(com_list)
	
	
