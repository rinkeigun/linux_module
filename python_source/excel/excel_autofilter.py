#!/usr/bin/env python
# -*- coding: utf-8 -*-

from win32com.client import DispatchEx
xl = DispatchEx("Excel.Application")
xl.Workbooks.Open("D:\\sourcetree\\python_source\\excel\\workbook1.xlsx")
#xl.ActiveWorkbook.ActiveSheet.Columns("1:3").AutoFilter(1)
xl.ActiveWorkbook.ActiveSheet.Range("A5:C5").AutoFilter(1)
#xl.ActiveWorkbook.ActiveSheet.Range("A5:C5").AutoFilter(1)
xl.ActiveWorkbook.Close(SaveChanges=1)
xl.Quit()
del (xl)