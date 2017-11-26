# -*- coding: utf-8 -*-
# File name : fihistgram1.py
# Date      : 2017/11/23
# Author    : Huiqun Lin
# Ver       : 0.1
#-----------------------------------------------

import numpy as np
from PIL import Image,ImageOps 
import cv2
from matplotlib import pyplot as plt

class run:
	def __init__(self):
		#img = Image.open("img/kitten_blurred.jpg")

		# grayscale 変換
		#gray = ImageOps.grayscale( img )

		img = cv2.imread("img/kitten_blurred.jpg")
		# グレースケール変換
		gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

		# 方法1(NumPyでヒストグラムの算出)
		hist, bins = np.histogram(gray.ravel(),256,[0,256])

		# 方法2(OpenCVでヒストグラムの算出)
		#hist = cv2.calcHist([img],[0],None,[256],[0,256])

		# ヒストグラムの中身表示
		print(hist)

		# グラフの作成
		plt.xlim(0, 255)
		plt.plot(hist)
		plt.xlabel("Pixel value", fontsize=20)
		plt.ylabel("Number of pixels", fontsize=20)
		plt.grid()
		plt.show()

		# 表示させるため apt-get install -y imagemagick
		#img.show( )

if __name__ == '__main__':
	run()
