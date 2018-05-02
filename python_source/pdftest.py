# -*- coding: utf-8 -*-

import re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
#from pdfminer.pdfpage import PDFPage
#import io as StringIO
#from cStringIO import StringIO
from io import StringIO
import re

#space = re.compile(ur'[ 　]+')

def convert_pdf_to_txt(path, txtname, buf=True):
    rsrcmgr = PDFResourceManager()
    if buf:
        outfp = StringIO()
    else:
        outfp = file(txtname, 'w')
    codec = 'utf-8'
    laparams = LAParams()
    laparams.detect_vertical = True
#    device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams)
    device = TextConverter(rsrcmgr, outfp,  laparams=laparams)

    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    fp.close()
    device.close()
    if buf:
        text = re.sub(space, "", outfp.getvalue())
        print (text)
    outfp.close()


convert_pdf_to_txt("5.pdf", "test.txt")