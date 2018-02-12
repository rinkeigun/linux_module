# -*- coding: utf-8 -*-

import re
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
#from cStringIO import StringIO
from io import StringIO

#space = re.compile(ur"[ 　]+")
space = re.compile(u"[ 　]+")

def convert_pdf_to_txt(path, txtname, buf=True):
    rsrcmgr = PDFResourceManager()
    if buf:
        outfp = StringIO()
    else:
        #outfp = file(txtname, 'w')
        outfp = open(txtname, 'w')
    codec = 'utf-8'
    laparams = LAParams()
    laparams.detect_vertical = True
    device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams)

    #fp = file(path, 'rb')
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fp):
        print(page)
        interpreter.process_page(page)
    fp.close()
    device.close()
    if buf:
        text = re.sub(space, "", outfp.getvalue())
        print (text)
    outfp.close()


convert_pdf_to_txt("TEST.pdf", "test.txt", False)
