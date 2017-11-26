# -*- coding: utf-8 -*-
# File name : fiopen.py
# Date      : 2017/11/19
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

from PIL import Image

class run:
	def __init__(self):
		kitten = Image.open("img/kitten_blurred.jpg")
		print( "format : %s" % kitten.format )
		print( "size   : %d, %d" % kitten.size )
		print( "mode   : " + kitten.mode )

if __name__ == '__main__':
	run()
