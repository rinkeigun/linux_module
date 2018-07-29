import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Title", size=(300,150))
        self.InitializeComponents()

    def InitializeComponents(self):
        mainPanel = wx.Panel(self)
        button1 = wx.Button(mainPanel, -1, "Button 1")
        button2 = wx.Button(mainPanel, -1, "Button 2")
        button3 = wx.Button(mainPanel, -1, "Button 3")

        # Create a sizer.
#        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(button1)
        sizer.Add(button2)
        sizer.Add(button3)
        mainPanel.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    MyFrame().Show(True)
    app.MainLoop()