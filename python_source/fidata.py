# -*- coding: utf-8 -*-
# File name : fidata.py
# Date      : 2017/11/19
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

import numpy as np
from PIL import Image

class run:
	def __init__(self):
		kitten = Image.open("img/kitten_blurred.jpg")
		img2 = Image.new('RGBA', kitten.size )
		print( "size : %d, %d" % img2.size )
		print( "mode : " + img2.mode )

		img_pixels = []
		for y in range(img2.size[1]):
			for x in range(img2.size[0]):
				# getpixel((x,y))で左からx番目,上からy番目のピクセルの色を取得し、img_pixelsに追加する
				img_pixels.append(kitten.getpixel((x,y)))
				# あとで計算しやすいようにnumpyのarrayに変換しておく
		img_pixels = np.array(img_pixels)
		# pixel[100][10] の値を取得
		#print( img_pixels[100][10] )
		print( img_pixels )

		#pixel[100][10]への値のセット
		img2.putpixel( (100,10), (0,0,255) )

if __name__ == '__main__':
	run()
