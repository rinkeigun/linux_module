# -*- coding: utf-8 -*-
# File name : 
# Date :
# Author :
#-----------------------------------------------

# クラスの説明
class FirstClass:

#関数リスト
	def __init__(self):
		print( 'クラスの初期化' )
	def __str__(self):
		print('str')
	def myfunc(self):
		print( '何かを出力する' )
	def __del__(self):
		print( 'クラスが終了するときに呼び出される' )
# fistclassの終わり

# テストプログラムはこれより下に書く
if __name__ == '__main__':
	b = FirstClass()
	print(b)
	
	
