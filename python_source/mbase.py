# -*- coding: utf-8 -*-
# File name   : mbase.py
# Date        : 2017/10/26
# Last Modify : 2017/11/03
# Author      : Huiqun Lin
# Ver         : 0.3
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
		print( '-------------------------------------------------' )
		print( '操作説明' )
		print( 'q:終了 b:戻る' )
		print( '-------------------------------------------------' )
	# コマンド入力部分 
	def mcommand(self):
		self.com = input('>>')
	# 入力を処理 
	def mexcute(self):
		# 画面をクリア
		print('\033[2J')

		# 終了
		try:
			if self.com.lower() == 'q':
				exit ()
			elif self.com.lower() == 'b':
				return ()
			else:
				i = 0
				for nl in self.lst:
					i+=1
					if int(self.com) == i:
						obj = importlib.import_module(nl[1])
						obj.run()
				self.mview()
		except ImportError as e:
			print('importモジュールが未定義')
			self.mview()
		
	def __del__(self):
		pass
# mBaseの終わり

# テストプログラムはこれより下に書く
if __name__ == '__main__':
	com_list = [
		['動作', 'dousa'],
		['２つ目', '2me']
	]
	b = mBase(com_list)
