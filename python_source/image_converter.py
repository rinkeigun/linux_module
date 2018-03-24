#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pyinstall --icon="iconfile.icon" --onefile --noconsole image_converter.py

from __future__ import unicode_literals

import wx
from PIL import Image
import glob
import os
import json
import codecs


class myWindow(wx.Frame):
    def __init__(self,parent,id):
        x = 640
        y = 400

        x1 = x/2
        y1 = 320
        y2 = y - y1
        
        #JSON ファイルの読み込み
        #f = open('itemlist.json', 'r')
        f = codecs.open('itemlist.json', 'r', 'utf-8')
#        self.json_dict = json.load(f)
        in_str = f.read()
        self.json_dict = json.loads(in_str)

        title = self.json_dict['IMAGE_CONVERTER'] + "(" + self.json_dict['VERSION_INFO'] + ")"
        wx.Frame.__init__(self, parent,id, title, size=(x, y))

        icon = wx.Icon('frame.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        panel1 = wx.Panel(self, wx.ID_ANY, pos=(0, 0), size=(x1, y1))
        panel2 = wx.Panel(self, wx.ID_ANY, pos=(x1, 0), size=(x1, y1))
        panel3 = wx.Panel(self, wx.ID_ANY, pos=(0, y1), size=(2*x1, y2))
        panel1.SetBackgroundColour('#FF0000')
        panel2.SetBackgroundColour('#FFFF00')
        panel3.SetBackgroundColour('#00FF00')

        # 入力用フォルダー
        in_folder_l  = wx.StaticText(panel1, wx.ID_ANY, self.json_dict['IN_FOLDER_L'])
        self.in_folder_t  = wx.TextCtrl(panel1, wx.ID_ANY, pos=self.get_next_pos(in_folder_l))
        in_folder_b  = wx.Button(panel1, wx.ID_ANY, self.json_dict['IN_FOLDER_B'], pos=self.get_next_pos2(self.in_folder_t))
        in_folder_b.Bind(wx.EVT_BUTTON, self.in_folder_f)

        # 入力用ファイル
        in_file_l    = wx.StaticText(panel1, wx.ID_ANY, self.json_dict['IN_FILE_L'], pos=self.get_next_pos(self.in_folder_t))
        self.in_file_t    = wx.TextCtrl(panel1, wx.ID_ANY, pos=self.get_next_pos(in_file_l))

        # 出力用フォルダ
        out_folder_l = wx.StaticText(panel1, wx.ID_ANY, self.json_dict['OUT_FOLDER_L'], pos=self.get_next_pos(self.in_file_t))
        self.out_folder_t = wx.TextCtrl(panel1, wx.ID_ANY, pos=self.get_next_pos(out_folder_l))
        out_folder_b = wx.Button(panel1, wx.ID_ANY, self.json_dict['OUT_FOLDER_B'],pos=self.get_next_pos2(self.out_folder_t))
        out_folder_b.Bind(wx.EVT_BUTTON, self.out_folder_f)


        #layout1 = wx.BoxSizer(wx.VERTICAL)
        #layout1.Add(in_folder_l)
        #layout1.Add(in_file_l)

        #layout1.Add(in_folder_t)
        #layout1.Add(in_folder_b)
        #layout2.Add(out_folder_t)
        #layout2.Add(out_folder_b)

        # イメージ種別
        self.image_type_l = wx.StaticText(panel2, wx.ID_ANY, '')
        self.image_type_l.SetLabel("bmp")
        self.image_type_l.Hide()

        #radiobutton_1 = wx.RadioButton(panel2, wx.ID_ANY, 'ラジオボタン１', style=wx.RB_GROUP)
        #radiobutton_2 = wx.RadioButton(panel2, wx.ID_ANY, 'ラジオボタン２') 
        lblList = [ 'bmp', 'jpg', 'png', 'gif', 'tiff', 'ico' ]
        self.rbox = wx.RadioBox(panel2, label = self.json_dict['IMAGE_TYPE_L'],  choices = lblList,
            majorDimension = 1, style = wx.RA_SPECIFY_ROWS) 
        self.rbox.Bind(wx.EVT_RADIOBOX,self.onRadioBox) 
        

        #panel22 = wx.Panel(panel2)
        #panel22.SetBackgroundColour('#ededed')

        # 開始
        start_b = wx.Button(panel2, wx.ID_ANY, self.json_dict['START_B'], pos=self.get_next_pos(self.rbox))
        start_b.Bind(wx.EVT_BUTTON, self.start_f)

        # 終了
        end_b = wx.Button(panel2, wx.ID_ANY, self.json_dict['END_B'], pos=self.get_next_pos2(start_b))
        end_b.Bind(wx.EVT_BUTTON, self.end_f)


        boxsizer = wx.BoxSizer(wx.VERTICAL)
        #layout2.Add(start_b, flag=wx.GROW)
        #layout2.Add(end_b, flag=wx.GROW)
        boxsizer.Add(start_b)
        boxsizer.Add(end_b)

         
        #panel1.SetSizer(layout1)
        panel2.SetSizer(boxsizer)

        self.slider = wx.Slider(panel3, style=wx.SL_LABELS)

    def get_next_pos(self, element):
        pos_x, pos_y = element.GetPosition()
        size_x, size_y = element.GetSize()
        return(0, pos_y+size_y+10)

    def get_next_pos2(self, element):
        pos_x, pos_y = element.GetPosition()
        size_x, size_y = element.GetSize()
        return(size_x, pos_y)

    def in_folder_f(self, event):
#        dialog = wx.FileDialog(None, u'ファイルを選択してください')
        dialog = wx.DirDialog(None, self.json_dict['SELECT_FOLDER'])
        if dialog.ShowModal() == wx.ID_CANCEL:
            return
        pathname = dialog.GetPath()
        self.in_folder_t.SetValue(pathname)
        return
        
    def out_folder_f(self, event):
        dialog = wx.DirDialog(None, self.json_dict['SELECT_FOLDER'])
        if dialog.ShowModal() == wx.ID_CANCEL:
            return
        pathname = dialog.GetPath()
        self.out_folder_t.SetValue(pathname)
        return 
        
    def onRadioBox(self, event):
        print (self.rbox.GetStringSelection())
        self.image_type_l.SetLabel(self.rbox.GetStringSelection())
        return 

    def start_f(self, event):
        #１．入力フォルダー欄からパスを取得
        in_path = self.out_folder_t.GetValue()
        
        #２．取得できない場合は、現在フォルダーを入力パスに設定
        if in_path == "" :
        	in_path = u".\\"
        	
        #３．入力ファイル欄からファイル名を取得
        in_file = self.in_file_t.GetValue()
        
        #４．取得できない場合、パスにあるファイルを全対象とする
        in_file_list = []
        if in_file == "":
            in_file_list = glob.glob(self.in_folder_t.GetValue()+"\\*")
        else:
            in_file_list = [ self.in_folder_t + "\\" + self.in_file_t ]
            
        #５．出力フォルダー欄からパスを取得
        out_folder = self.out_folder_t.GetValue()
        
        #６．取得できない場合現フォルダーを出力パスに設定
        if out_folder == "":
            out_folder = u".\\"

        #７．ラジオリストからラジオ値を取得し、出力ファイル種別を特定
        file_type = self.image_type_l.GetLabel()

        
        #８．４までで取得したファイル一覧で下記の繰り返し処理を行う
        
        num = len( in_file_list )
        i = 0
        for file in in_file_list:
            #９．入力と出力のファイルが同じ種別かつ入出力先が同じの場合、処理しない
            #１０．変換を行う
            
            i += 1
            self.convert(file, file_type, out_folder)
            self.slider.SetValue( i / num *100 )
            
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



if __name__ == '__main__':
    application = wx.App()
    frame = myWindow(parent = None, id=wx.ID_ANY)

    frame.Show()
    application.MainLoop()