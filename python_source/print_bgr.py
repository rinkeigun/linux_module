import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('kitten_blurred.jpg')
 
# show image format (basically a 3-d array of pixel color info, in BGR format)
print(img)
