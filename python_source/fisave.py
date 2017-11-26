# -*- coding: utf-8 -*-
# File name : fishow.py
# Date      : 2017/11/19
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

import numpy as np
from PIL import Image

class run:
	def __init__(self):
		kitten = Image.open("img/kitten_blurred.jpg")

		# イメージの表示
		kitten.show()
		kitten.save( 'img/save.png', 'png' )
		kitten.save( 'img/save.bmp', 'bmp' )
		kitten.save( 'img/save.gif', 'gif' )
		kitten.save( 'img/save.tiff', 'tiff' )

if __name__ == '__main__':
	run()
