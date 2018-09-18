# -*- coding: utf-8 -*-

import wx
 
application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, 'テストフレーム', size=(300, 200))
 
panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour('#AFAFAF')
 
slider = wx.Slider(panel, style=wx.SL_LABELS)
 
print(slider.GetMin())
print(slider.GetMax())
slider.SetMin(100)
slider.SetMax(500)
 
layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(slider, flag=wx.GROW)
 
panel.SetSizer(layout)
 
frame.Show()
application.MainLoop()