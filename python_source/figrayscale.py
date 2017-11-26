# -*- coding: utf-8 -*-
# File name : figrayscale.py
# Date      : 2017/11/23
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import numpy as np
from PIL import Image,ImageOps 

class run:
	def __init__(self):
		kitten = Image.open("img/kitten_blurred.jpg")

		# grayscale 変換
		img = ImageOps.grayscale( kitten )

		# 表示させるため apt-get install -y imagemagick
		img.show( )

if __name__ == '__main__':
	run()
