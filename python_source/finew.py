# -*- coding: utf-8 -*-
# File name : finew.py
# Date      : 2017/11/19
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

from PIL import Image

class run:
	def __init__(self):
		kitten = Image.open("img/kitten_blurred.jpg")
		img2 = Image.new('RGBA', kitten.size )
		print( "size : %d, %d" % img2.size )
		print( "mode : " + img2.mode )

if __name__ == '__main__':
	run()
