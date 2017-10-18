#from PIL import Image
import sys
import pyocr
import pyocr.builders
import numpy as np
import cv2

tools = pyocr.get_available_tools()
if len(tools) == 0:
	print("No OCR tool found")
	sys.exit(1)
tool = tools[0]

txt = tool.image_to_string(
	Image.open("aaa.jpg"),
	lang="jpn+eng",
	builder = pyocr.builders.TextBuilder( tesseract_layout=6)
)
#print (txt)

out = cv2.imread("aaa.jpg")
for d in txt:
	print (d.content)
	print (d.position)
	cv2.rectangle(out, d.position[0], d.position[1], (0, 0, 225), 2)

cv.imshow('image', out)
cv.waitKey(0)
cv.destroyAllWindows()
