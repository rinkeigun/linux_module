# -*- coding: utf-8 -*-
# File name   : fivbase.py
# Date        : 2017/11/23
# Author      : Huiqun Lin
# Ver         : 0.1
#-----------------------------------------------

# クラスの説明
# このクラスは、メニューの基本クラスとする

from PIL import Image

class fivbase:

#関数リスト
	def __init__(self, lst):
		# クラスの初期化
		#self.cnt = lst.count() 
		self.cnt = len(lst)
		#self.x = lst[0].width 
		#self.y = lst[0].height 
		self.x = 250 
		self.y = 200 
		self.lst = lst
		self.fview()

	def __str__(self):
		print('str')

	# 1画面の表示 
	def fview(self):
		self.flist()

	# リスト
	def flist(self):
		ve = self.visibleerea()
		ee = self.eacherea( )
		i = 0
		for img in self.lst:
			x1 = self.x * ee[i][0] 
			y1 = self.y * ee[i][1] 
			x2 = self.x * ee[i][2] 
			y2 = self.y * ee[i][3] 
			ve.paste( img.resize( (self.x, self.y), Image.NEAREST), (x1, y1, x2, y2) )	
			i+=1
		ve.show()

	# 描画領域用 ( cnt は最大4 )
	def ereainuse(self, cnt):
		if cnt <= 0:
			return (NONE)
		lst = []
		lst.append( (1,1) )
		lst.append( (2,1) )
		lst.append( (2,2) )
		lst.append( (2,2) )
		return( lst[cnt-1] )

	# 描画可能エリア
	def visibleerea(self):
		i,j = self.ereainuse( self.cnt )
		img = Image.new( 'RGB', (i*self.x, j*self.y))
		return ( img )	
		
	# 1領域用
	def oneerea(self, i, j):
		return (i, j, i+1, j+1)

	# 各描画領域
	def eacherea(self):
		erea_list = []
		erea_list.append( self.oneerea( 0, 0 ))
		erea_list.append( self.oneerea( 1, 0 ))
		erea_list.append( self.oneerea( 0, 1 ))
		erea_list.append( self.oneerea( 1, 1 ))
		return (erea_list)
		
	def __del__(self):
		pass
# fivbaseの終わり

# テストプログラムはこれより下に書く
if __name__ == '__main__':
	com_list = [
		#Image.new('RGB' , (100,100) ),
		Image.open('img/save.png' , 'r' ),
		Image.open('img/save.png' , 'r' ),
		Image.open('img/save.png' , 'r' ),
		Image.open('img/save.png' , 'r' ),
	]
	b = fivbase(com_list)
