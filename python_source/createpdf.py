# coding:utf-8

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import sys

#sys.setdefaultencoding("utf-8")

xmargin = 8.4*mm
ymargin = 8.8*mm
swidth  = 48.3*mm
sheight = 25.4*mm

def draw_label(c, x, y, data):
  c.setLineWidth(0.5)
  c.rect(x, y, 48.3*mm, 25.4*mm, stroke=1, fill=0)
  c.drawString(x, y, str(data))

c = canvas.Canvas("test.pdf",pagesize=A4)
for i in xrange(44):
  #オフセット位置
  x = xmargin + swidth * (i%4)
  y = ymargin + sheight * (10-(i//4))
  #ラベル印刷
  #draw_label(c, x, y, u"日本語"+str(i).encode('utf-8'))
  a = u"日本語"
  print( type(a ))

  #draw_label(c, x, y, u"日本語"+str(i))
  draw_label(c, x, y, i)

# 一ページ分を確定して、PDFデータをファイルに格納
c.showPage()
c.save()

