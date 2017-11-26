# -*- coding: utf-8 -*-
# File name : fitop2buttom.py
# Date      : 2017/11/19
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import numpy as np
from PIL import Image, ImageDraw

class run:
	def __init__(self):
		kitten = Image.open("img/kitten_blurred.jpg")
		top2buttom = kitten.transpose( Image.FLIP_LEFT_RIGHT)
		top2buttom.save('img/left2right.jpg')	

if __name__ == '__main__':
	run()
