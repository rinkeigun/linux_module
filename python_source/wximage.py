import wx
import time

class bucky(wx.Frame):

	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300,200))
		panel = wx.Panel(self)

		i = 0
		while 1:
			bmp = "creek.bmp"
			if i%2 == 1:
				bmp = "creek.bmp"
			else:
				bmp = "ushi.bmp"
			pic = wx.Image(bmp, wx.BITMAP_TYPE_BMP).ConvertToBitmap()
			self.button=wx.BitmapButton(panel, -1, pic, pos=(10,10))
			#self.Bind(wx.EVT_BUTTON, self.doMe, self.button)
			self.button.SetDefault()
			i += 1
			time.sleep(1)
			break

	def doMe(self, event):
		self.Destroy()

if __name__ == '__main__':
	app=wx.App()
	frame=bucky(parent=None, id=-1)
	frame.Show()
	app.MainLoop()