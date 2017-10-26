# -*- coding: utf-8 -*-

import xlwt
import datetime

#新しいブック
book = xlwt.Workbook()

#シート
newsheet_1 = book.add_sheet('Newsheet_1')

#セルへの書き込み、行列を直接指定
newsheet_1.write(0,0,'A1')

#行指定移動
newsheet_1_row_1 = newsheet_1.row(1)

#列のみ指定の書き込み
newsheet_1_row_1.write(0, 'A2')
newsheet_1_row_1.write(1, 'b2')

#列幅
newSheet_1_column_1 = newsheet_1.col(2)
newSheet_1_column_1.width = 5000

# Alignment
c_align = xlwt.Alignment()
c_align.horz = xlwt.Alignment.HORZ_CENTER


# 背景
c_pattern = xlwt.Pattern()
c_pattern.pattern = xlwt.Pattern.SOLID_PATTERN
c_pattern.pattern_fore_colour = 0x16

#Font
c_font_1 = xlwt.Font()
c_font_1.bold = True
c_font_1.colour_index = 0x35
c_style_1 = xlwt.XFStyle()
c_style_1.font = c_font_1
c_style_1.num_format_str = 'yyyy-mm-dd'

c_font_2 = xlwt.Font()
c_font_2.name = 'Arial'
c_style_2 = xlwt.XFStyle()
c_style_2.font = c_font_2
c_style_2.alignment = c_align
c_style_2.pattern = c_pattern

# 上書きはダメ？
#Exception: Attempt to overwrite cell: sheetname='Newsheet_1' rowx=1 colx=0

newsheet_1.write(3, 0, datetime.date.today() , c_style_1)
newsheet_1.write(4, 0, 'Font-Arial', c_style_2)


# ボーダー設定
c_border = xlwt.Borders()
c_border.top    = xlwt.Borders.MEDIUM
c_border.bottom = xlwt.Borders.THICK
c_border.left   = xlwt.Borders.THIN
#c_border.right = xlwt.Borders.THICK
c_style = xlwt.XFStyle()
c_style.borders = c_border

newsheet_1.write(5,1, 'Bordr', c_style)
book.save('sample.xls')

