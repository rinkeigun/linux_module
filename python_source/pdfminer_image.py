# pdfminer.six
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTImage,  LTFigure
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
import io as StringIO
from PIL import Image


def extract_images(document):
    """PDF ドキュメントから画像形式のデータだけを抽出する"""

    # Create a PDF resource manager object that stores shared resources.
    rsrcmgr = PDFResourceManager()
    # Create a PDF device object.
    device = PDFPageAggregator(rsrcmgr, laparams=LAParams())
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    contents = []

    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
        layout = device.get_result()

        contents.extend(travarse(layout))

    return [to_pil_image(ltImage) for ltImage in contents]


def travarse(layout):
    """Layout オブジェクトを再帰的に走査して LTImage オブジェクトのみを list で返す"""

    images = []

    for obj in layout:
        if isinstance(obj, LTTextBox) or isinstance(obj, LTTextLine) or isinstance(obj, LTFigure):
            images.extend(travarse(obj))

        elif isinstance(obj, LTImage):
            images.append(obj)

    return images



def to_pil_image(ltImage):
    """Raw Binary を Image オブジェクトに変換"""

    #buffer = StringIO.StringIO()
    buffer = StringIO.BytesIO()
    string = ltImage.stream.get_rawdata()
    buffer.write(string)
    #buffer.write(ltImage.stream.get_rawdata())
    buffer.seek(0)
    img = Image.open(buffer)
    img.save( "img.png")
    return img 


fp = open("TEST.pdf", 'rb')
parser = PDFParser(fp)
document = PDFDocument(parser)
extract_images(document)
