# -*- coding: utf-8 -*-
# File name : fishow.py
# Date      : 2017/11/19
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import numpy as np
from PIL import Image, ImageDraw

class run:
	def __init__(self):
		kitten = Image.open("img/kitten_blurred.jpg")
		# 表示させるため apt-get install -y imagemagick
		kitten.show( )

if __name__ == '__main__':
	run()
