import wx
import win32gui
import time

class Desktop(wx.Frame):
    def __init__(self):
        super(Desktop,self).__init__(None,-1,'',style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP )
        self.AssociateHandle(win32gui.GetDesktopWindow())
        dc = wx.WindowDC(self)
        dc.SetPen(wx.Pen('red', 3))
#        wx.Pen((255,0,0), width=100)
#        wx.Pen().SetWidth(10)
#        wx.Pen().SetColour(2,0,0)

        dc.DrawLine(100,100,800,100)
        dc.DrawLine(800,100,800,800)
        dc.DrawLine(800,800,100,800)
        dc.DrawLine(100,800,100,100)
        #dc.DrawRectangle( 100, 100, 800, 800 )
        self.SetTransparent(255)
        #dc.SetTransparent(255)
        time.sleep(3)
        dc.Clear()


app = wx.App(0)
mf = Desktop()
app.MainLoop()