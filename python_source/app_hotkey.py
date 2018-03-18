#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import sys
import os
from time import time
import datetime
from pywinauto import application
import time
import numpy
import threading
import pyautogui

class TestThread(threading.Thread):

    """docstring for TestThread"""

    def __init__(self, app):
        super(TestThread, self).__init__()
        self.app = app

    def run(self):
        #時間を取得
        d=datetime.datetime.now().isoformat()
        filerename=(str(d)+'.avi').replace(":", "")

        #ファイル名
        filename = "output5.avi"
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        
        # 速度
        fps = 100
        
        #サイズが小さく設定すると画質が落ちる
        size = (1280,960)
        videoWriter = cv2.VideoWriter(filename, fourcc, fps, size)

        while (1):
            img = self.app.CaptureAsImage()
            frame = numpy.asarray(img)

            # 画面表示
            cv2.imshow('frame', frame)
 
            # 圧縮
            frame = cv2.resize(frame, size)
 
            # 書き込み
            videoWriter.write(frame)
			
            # キー待ち
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        videoWriter.release()
        os.rename(filename,'%s'%(filerename))
        # 後処理
        cv2.destroyAllWindows()

#コーデック名	引数	拡張子
#MP4S	('M', 'P', '4', 'S')	.mp4
#MP4V	('M', 'P', '4', 'V')	.mp4
#DIV3	('D', 'I', 'V', '3')	.avi
#DIVX	('D', 'I', 'V', 'X')	.avi
#I420	('I', '4', '2', '0')	.avi
#IYUV	('I', 'Y', 'U', 'V')	.avi
#MJPG	('M', 'J', 'P', 'G')	.avi
#PIM1	('P', 'I', 'M', '1')	.avi
#XVID	('X', 'V', 'I', 'D')	.avi
#dv25	('d', 'v', '2', '5')	.wmv
#dv50	('d', 'v', '5', '0')	.wmv
#dvc	('d', 'v', 'c', ' ')	.wmv
#dvh1	('d', 'v', 'h', '1')	.wmv
#dvhd	('d', 'v', 'h', 'd')	.wmv
#dvsd	('d', 'v', 's', 'd')	.wmv
#dvsl	('d', 'v', 's', 'l')	.wmv
#H263	('H', '2', '6', '3')	.wmv
#M4S2	('M', '4', 'S', '2')	.wmv
#MP43	('M', 'P', '4', '3')	.wmv
#MPG1	('M', 'P', 'G', '1')	.wmv
#MSS1	('M', 'S', 'S', '1')	.wmv
#MSS2	('M', 'S', 'S', '2')	.wmv
#WMV1	('W', 'M', 'V', '1')	.wmv
#WMV2	('W', 'M', 'V', '2')	.wmv
#WMV3	('W', 'M', 'V', '3')	.wmv
#WVC1	('W', 'V', 'C', '1')	.wmv
#mp4v	('m', 'p', '4', 'v')	.mov

if __name__ == '__main__':

    time.sleep(1)
    app_path = "notepad.exe"
    app = application.Application()
    app.start(app_path)
    print(app.Notepad.wait('visible'))
    
    spec_app = app.top_window()
#    app[u'無題.*メモ帳'].CaptureAsImage().save('auto_capture.png')
    tmpapp = app[u'無題.*メモ帳']
    th_cl = TestThread(spec_app)
    th_cl.start()

    #cap_app = AppCap(tmpapp)
    #.CaptureAsImage().save('auto_capture.png')

    time.sleep(1)
    app.Notepad.edit.TypeKeys(u'hotkeyによる操作開始')
    time.sleep(1)

    #app.Notepad.MenuSelect(u'ファイル(&F)->名前を付けて保存(&A)...')
    pyautogui.hotkey('alt', 'F')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'S')
    time.sleep(1)

    app[u'名前を付けて保存'].edit.SetText('tamesi.txt')
    time.sleep(1)
    app[u'名前を付けて保存'][u'保存(&S)'].Click()
    time.sleep(1)
    pyautogui.hotkey('alt', 'Y')


