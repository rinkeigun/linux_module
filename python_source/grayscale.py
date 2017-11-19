import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

#img = cv2.imread('img/isewtweetbg.jpg',0)
img = cv2.imread('img/isewtweetbg.jpg')
 
# show image format (basically a 3-d array of pixel color info, in BGR format)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#cv2.imshow("img", img)
 
# show image with matplotlib
plt.imshow(img)
plt.show()
#plt.imshow('image', img)
#plt.waitKey(0)
#keycode = cv2.waitKey(0)
#if keycode == ord('s'):
#	cv2.imwrite('gray_scale.png', img)
#cv2.destroyAllWindows()
#plt.destroyAllWindows()
#plt.show(img)
