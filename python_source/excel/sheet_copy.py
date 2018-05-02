from win32com.client import Dispatch

path1 = 'D:\\sourcetree\\python_source\\excel\\workbook1.xlsx'
path2 = 'D:\\sourcetree\\python_source\\excel\\workbook2.xlsx'

xl = Dispatch("Excel.Application")
xl.Visible = True  # You can remove this line if you don't want the Excel application to be visible

wb1 = xl.Workbooks.Open(Filename=path1)
wb2 = xl.Workbooks.Open(Filename=path2)

ws1 = wb1.Worksheets(1)
ws1.Copy(Before=wb2.Worksheets(1))

wb2.Close(SaveChanges=True)
xl.Quit()
