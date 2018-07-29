import sys
from pytesseract import pytesseract
#pytesseract.run_tesseract(sys.argv[1], 'output', lang=None, boxes=False, config="hocr")
print( sys.argv[1])
pytesseract.run_tesseract(sys.argv[1], 'output', 'box', lang='jpn',  config="hocr")
