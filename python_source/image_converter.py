#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pyinstaller --icon="iconfile.icon" --onefile --noconsole image_converter.py

# Panel Structure
# rootPanel
#    + CompoPanel
#    |    + LeftPanel
#    |    |    + InPanel
#    |    |    + FilePanel
#    |    |    + OutPanel
#    |    + RightPanel
#    |         + ImagePanel
#    |         + CommandPanel
#    + SliderPanel

from __future__ import unicode_literals

import wx
from PIL import Image
import glob
import os
import json
import codecs


class myWindow(wx.Frame):
    def __init__(self,parent,id):
        self.parent = parent
        x = 640
        y = 320

        x1 = x/2
        y1 = 320
        y2 = y - y1
        
        #JSON ファイルの読み込み
        #f = open('itemlist.json', 'r')
        f = codecs.open('itemlist.json', 'r', 'utf-8')
        in_str = f.read()
        self.json_dict = json.loads(in_str)

        title = self.json_dict['IMAGE_CONVERTER'] + "(" + self.json_dict['VERSION_INFO'] + ")"
        wx.Frame.__init__(self, parent,id, title, size=(x, y))

        icon = wx.Icon('frame.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        self.root_panel = wx.Panel(self, wx.ID_ANY, pos=(0, 0), size=(x1, y1))

        self.compo_panel = CompoPanel(self.root_panel, self.json_dict, self.start_f, self.end_f)
        self.slider_panel = SliderPanel(self.root_panel)
  
        root_layout = wx.BoxSizer(wx.VERTICAL)
        root_layout.Add(self.compo_panel, 0, wx.GROW | wx.LEFT | wx.RIGHT, border=20)
        root_layout.Add(self.slider_panel, 0, wx.GROW | wx.ALL, border=10)
        self.root_panel.SetSizer(root_layout)
        root_layout.Fit(self.root_panel)

        
    def setSliderValue(self, i, num):
        self.slider_panel.setValue(i, num)

    def start_f(self, event):
    
        in_path, in_file, out_folder, file_type = self.compo_panel.get()
        #１．入力フォルダー欄からパスを取得
        #in_path = self.out_folder_t.GetValue()
        
        #２．取得できない場合は、現在フォルダーを入力パスに設定
        if in_path == "" :
        	in_path = u".\\"
        	
        #３．入力ファイル欄からファイル名を取得
        #in_file = self.in_file_t.GetValue()
        
        #４．取得できない場合、パスにあるファイルを全対象とする
        in_file_list = []
        if in_file == "":
            in_file_list = glob.glob(in_path+"\\*")
        else:
            in_file_list = [ in_path + "\\" + in_file ]
            
        #５．出力フォルダー欄からパスを取得
        #out_folder = self.out_folder_t.GetValue()
        
        #６．取得できない場合現フォルダーを出力パスに設定
        if out_folder == "":
            out_folder = u".\\"

        #７．ラジオリストからラジオ値を取得し、出力ファイル種別を特定
        #file_type = self.image_type_l.GetLabel()

        
        #８．４までで取得したファイル一覧で下記の繰り返し処理を行う
        
        num = len( in_file_list )
        i = 0
        for file in in_file_list:
            #９．入力と出力のファイルが同じ種別かつ入出力先が同じの場合、処理しない
            #１０．変換を行う
            
            i += 1
            self.convert(file, file_type, out_folder)
            self.setSliderValue( i, num )
            
            #１１．出力ファイル名は、基本的に元ファイル名と同じで拡張子が異なる
            #１２．変換対象ファイルは、１つの場合かつ出力フォルダー欄にファイル名まで指定してある場合その名前を使う
        return

    def convert(self, file, file_type, out_folder):
        path, ext = os.path.splitext( os.path.basename(file) )
        try:
            kitten = Image.open(file)
        except OSError as e:
            print(e.args[0])
            print(e.errno)
            print(e.strerror)
            print(e.args)
            print(e)
            #print(sys.exc_info())
            print(file)
            return
        outfile = out_folder + "\\" + path + "." + file_type
        print(outfile)
        
        kitten.save( outfile )
        kitten.close()
        return
    
    def end_f(self, event):
        self.Close(True)

        
class CompoPanel(wx.Panel):
    """
    操作部分
    """
  
    def __init__(self, parent, dict, start_f, end_f):
      
        super().__init__(parent, wx.ID_ANY)
        
        self.left_panel = LeftPanel(self, dict)
        self.right_panel = RightPanel(self, dict, start_f, end_f)
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(self.left_panel, 1, flag=wx.EXPAND | wx.ALL, border=5)
        layout.Add(self.right_panel, 1, flag=wx.EXPAND | wx.ALL, border=5)
        self.SetSizer(layout)
        
    def get(self):
        in_foler, in_file, out_folder = self.left_panel.get()
        image_type = self.right_panel.get()
        return (in_foler, in_file, out_folder, image_type)
        
    def end_f(self, event):
        self.parent.end_f(event)

class SliderPanel(wx.Panel):
    """
    スライダーを表示する部分
    """
  
    def __init__(self, parent):
      
        super().__init__(parent, wx.ID_ANY)
        
        layout = wx.BoxSizer(wx.HORIZONTAL)
        self.slider = wx.Slider(self, style=wx.SL_LABELS)
        layout.Add( self.slider, proportion=1)
        self.SetSizer(layout)
        
    def setValue(self, i, num):
        self.slider.SetValue( i / num *100 )



class LeftPanel(wx.Panel):
    """
    画面左辺を表示する部分
    """
  
    def __init__(self, parent, dict):
      
        super().__init__(parent, wx.ID_ANY)
          
        self.in_panel = InPanel(self, dict)
        self.file_panel = FilePanel(self, dict)
        self.out_panel = OutPanel(self, dict)
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.in_panel, 1, flag=wx.EXPAND | wx.TOP, border=10)
        layout.Add(self.file_panel, 1)
        layout.Add(self.out_panel, 1)
        self.SetSizer(layout)
    def get(self):
        return( self.in_panel.get(), self.file_panel.get(), self.out_panel.get())

class RightPanel(wx.Panel):
    """
    上部の右辺を表示する部分
    """
  
    def __init__(self, parent, dict, start_f, end_f):
      
        super().__init__(parent, wx.ID_ANY)
        
        self.image_panel = ImagePanel(self, dict)
        command_panel = CommandPanel(self, dict, start_f, end_f)
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.image_panel, 1, flag=wx.EXPAND | wx.TOP, border=10) #60
        layout.Add(command_panel, 1, flag= wx.TOP, border=5) #57
        self.SetSizer(layout)
    
    def get(self):
        return ( self.image_panel.get())
        
    def end_f(self, event):
        self.parent.end_f(event)

class InPanel(wx.Panel):
    """
    入力フォルダーを指定する部分
    """
  
    def __init__(self, parent, dict):
      
        super().__init__(parent, wx.ID_ANY)
        self.dict = dict

        x_pos = 350
        # 入力用フォルダー
        in_folder_l  = wx.StaticText(self, wx.ID_ANY, dict['IN_FOLDER_L'])
        self.in_folder_t  = wx.TextCtrl(self, wx.ID_ANY, pos=(0, 20), size=(x_pos,25))
        btnBmap = wx.ArtProvider.GetBitmap(wx.ART_FIND)
        in_folder_b = wx.BitmapButton(self, wx.ID_ANY, btnBmap, pos=(x_pos,20), size=(26,26))
        in_folder_b.SetToolTip(wx.ToolTip(dict['IN_FOLDER_B']))
        #in_folder_b  = wx.Button(self, wx.ID_ANY, dict['IN_FOLDER_B'], pos=(x_pos,20))
        in_folder_b.Bind(wx.EVT_BUTTON, self.in_folder_f)

    def get(self):
        return self.in_folder_t.GetValue()
        
    def in_folder_f(self, event):
        dialog = wx.DirDialog(None, self.dict['SELECT_FOLDER'])
        if dialog.ShowModal() == wx.ID_CANCEL:
            return
        pathname = dialog.GetPath()
        self.in_folder_t.SetValue(pathname)
        return



class FilePanel(wx.Panel):
    """
    フィアルを指定する部分
    """
  
    def __init__(self, parent, dict):
      
        super().__init__(parent, wx.ID_ANY)
        
         # 入力用ファイル
        in_file_l    = wx.StaticText(self, wx.ID_ANY, dict['IN_FILE_L'])
        self.in_file_t    = wx.TextCtrl(self, wx.ID_ANY, pos=(0, 20), size=(350, 25))

    def get(self):
        return self.in_file_t.GetValue()
               
        
class OutPanel(wx.Panel):
    """
    出力を表示する部分
    """
  
    def __init__(self, parent, dict):
      
        super().__init__(parent, wx.ID_ANY)
        self.dict = dict
        
        # 出力用フォルダ
        x_pos = 350
        out_folder_l = wx.StaticText(self, wx.ID_ANY, dict['OUT_FOLDER_L'])
        self.out_folder_t = wx.TextCtrl(self, wx.ID_ANY, pos=(0, 20), size=(x_pos,25) )
        btnBmap = wx.ArtProvider.GetBitmap(wx.ART_FIND)
        out_folder_b = wx.BitmapButton(self, wx.ID_ANY, btnBmap, pos=(x_pos,20), size=(26,26))
        out_folder_b.SetToolTip(wx.ToolTip(dict['OUT_FOLDER_B']))
        #out_folder_b = wx.Button(self, wx.ID_ANY, dict['OUT_FOLDER_B'], pos=(250,20))
        out_folder_b.Bind(wx.EVT_BUTTON, self.out_folder_f)

    def get(self):
        return self.out_folder_t.GetValue()

    def out_folder_f(self, event):
        dialog = wx.DirDialog(None, self.dict['SELECT_FOLDER'])
        if dialog.ShowModal() == wx.ID_CANCEL:
            return
        pathname = dialog.GetPath()
        self.out_folder_t.SetValue(pathname)
        return 


class ImagePanel(wx.Panel):
    """
    画面上部に表示されるテキスト部分
    """
  
    def __init__(self, parent, dict):
      
        super().__init__(parent, wx.ID_ANY)
        # イメージ種別
        self.image_type_l = wx.StaticText(self, wx.ID_ANY, '')
        self.image_type_l.SetLabel("bmp")
        self.image_type_l.Hide()
        lblList = [ 'bmp', 'jpg', 'png', 'gif', 'tiff', 'ico' ]
        self.rbox = wx.RadioBox(self, label = dict['IMAGE_TYPE_L'],  choices = lblList,
            majorDimension = 2, style = wx.RA_SPECIFY_ROWS) 
        self.rbox.Bind(wx.EVT_RADIOBOX,self.onRadioBox) 
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(self.rbox, 1, flag=wx.EXPAND | wx.ALL, border=5)
        self.SetSizer(layout)

    def get(self):
        return self.image_type_l.GetLabel()

    def onRadioBox(self, event):
        print (self.rbox.GetStringSelection())
        self.image_type_l.SetLabel(self.rbox.GetStringSelection())
        return
        
        
class CommandPanel(wx.Panel):
    """
    画面上部に表示されるテキスト部分
    """
  
    def __init__(self, parent, dict, start_f, end_f):
      
        super().__init__(parent, wx.ID_ANY)

        layout = wx.GridSizer( 1,2,1,1) 
        # 開始
        start_b = wx.Button(self, wx.ID_ANY, dict['START_B'])
        start_b.Bind(wx.EVT_BUTTON, start_f)

        # 終了
        end_b = wx.Button(self, wx.ID_ANY, dict['END_B'])
        end_b.Bind(wx.EVT_BUTTON, end_f)
        
        layout.Add( start_b, flag= wx.LEFT, border=5 )
        layout.Add( end_b )
        self.SetSizer(layout)
        
        

if __name__ == '__main__':
    application = wx.App()
    frame = myWindow(parent = None, id=wx.ID_ANY)

    frame.Show()
    #wx.Window.Fit(frame)
    application.MainLoop()