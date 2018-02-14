# apt-get install tesseract-ocr-jpn
from PIL import Image
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
	Image.open("a.png"),
	lang="jpn+eng",
	builder = pyocr.builders.TextBuilder(    tesseract_layout=4)
	#builder = pyocr.builders.LineBoxBuilder( tesseract_layout=6)
)
print (txt)

out = cv2.imread("a.png")
for d in txt:
	print (d.content)
	print (d.position)
	cv2.rectangle(out, d.position[0], d.position[1], (0, 0, 225), 2)

cv2.imshow('image', out)
cv2.waitKey(0)
cv2.destroyAllWindows()
