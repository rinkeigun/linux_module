# -*- coding: utf-8 -*-
# File name : fioffset.py
# Date      : 2017/11/24
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

#import numpy as np
from PIL import Image, ImageDraw, ImageChops
from fivbase import fivbase

class run(fivbase):
	def __init__(self):
		kitten = Image.open("img/kitten_blurred.jpg")
		img1 =ImageChops.offset(kitten, 250, 250)
		lst = [kitten, img1]
		#lst = [img1, kitten]
		# 表示させるため apt-get install -y imagemagick
		fivbase.__init__(self, lst)	

if __name__ == '__main__':
	run()
