# 環境変数
# C:\Users\myname\AppData\Local\Programs\Python\Python36
# C:\Users\myname\AppData\Local\Programs\Python\Python36\Scripts

# pip install wxpython

# python wxpy.py
# pyinstaller wxpy.py -> wxpy.exe



import wx

class SampleApp(wx.App):
    def OnInit(self):
        self.init_frame()
        return True

    def init_frame(self):
        self.frm_main = wx.Frame(None)
        self.frm_main.SetTitle("Hello, wxPython!")
        self.frm_main.SetSize((400, 200))
        self.frm_main.Show()

if __name__ == "__main__":
    app = SampleApp(False)
    app.MainLoop()
