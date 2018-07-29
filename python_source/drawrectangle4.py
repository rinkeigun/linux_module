import wx
class myFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title,style = wx.NO_BORDER | wx.FRAME_SHAPED)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        image = wx.Image('icon\\qr.png')
        self.bitmap = image.ConvertToBitmap()

        self.SetClientSize(image.GetSize())
        #self.SetShape(wx.RegionFromBitmapColour(self.bitmap,wx.Color(255,255,255)))

    def OnPaint(self, event=None):
        deviceContext = wx.PaintDC(self)
        deviceContext.DrawBitmap(self.bitmap, 0, 0, True)

app = wx.App(False)
frame = myFrame(None, "none")
frame.Show()
app.MainLoop()