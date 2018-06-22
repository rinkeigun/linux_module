# apt-get install tesseract-ocr-jpn
from PIL import Image
import sys
import pyocr
import pyocr.builders
import numpy as np
import cv2


'''
pagesegmode values are:
0 = Orientation and script detection (OSD) only.
1 = Automatic page segmentation with OSD.
2 = Automatic page segmentation, but no OSD, or OCR
3 = Fully automatic page segmentation, but no OSD. (Default)
4 = Assume a single column of text of variable sizes.
5 = Assume a single uniform block of vertically aligned text.
6 = Assume a single uniform block of text.
7 = Treat the image as a single text line.
8 = Treat the image as a single word.
9 = Treat the image as a single word in a circle.
10 = Treat the image as a single character.
'''



filename = sys.argv[1]
print( filename )

tools = pyocr.get_available_tools()
if len(tools) == 0:
	print("No OCR tool found")
	sys.exit(1)
tool = tools[0]
#a = pyocr.builders.TextBuilder(tesseract_layout=4)
a = pyocr.builders.WordBoxBuilder(tesseract_layout=6 )
#a = pyocr.builders.LineBoxBuilder(tesseract_layout=6)

txt = tool.image_to_string(
	Image.open(filename),
	lang="jpn+eng",
	builder = a
)
print (txt)


out = cv2.imread(filename)
for d in txt:
	print (d.content)
	print (d.position)
	cv2.rectangle(out, d.position[0], d.position[1], (0, 0, 225), 2)

cv2.imshow('image', out)
cv2.waitKey(0)
cv2.destroyAllWindows()

