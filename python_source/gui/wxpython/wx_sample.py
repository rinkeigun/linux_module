import wx

app = wx.App()

frame = wx.Frame(None, wx.ID_ANY, "テスト", size=(500, 500))
frame.SetBackgroundColour("black")

panel = wx.Panel(frame, wx.ID_ANY, pos=(0,0), size=(100, 500))
panel.SetBackgroundColour("blue")

panel_2 = wx.Panel(frame, wx.ID_ANY, pos=(100,0), size=(100, 500))
panel_2.SetBackgroundColour("green")

frame.Show()
app.MainLoop()
