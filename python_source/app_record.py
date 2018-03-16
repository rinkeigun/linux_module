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


stoper = False

class TestThread(threading.Thread):

    """docstring for TestThread"""

    def __init__(self, app):
        super(TestThread, self).__init__()
        self.app = app

    def run(self):
        #時間を取得
        d=datetime.datetime.now().isoformat()
        filerename=str(d)+'.avi'

        cameraCapture = cv2.VideoCapture(0)
        fps = 30
        size = (int(cameraCapture.get(3)),
            int(cameraCapture.get(4)))
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        filename = "output5.avi"
        videoWriter = cv2.VideoWriter(filename, fourcc, fps, size)


        #start=time()
        while (cameraCapture.isOpened()):
            ret, frame = cameraCapture.read()
            img = self.app.CaptureAsImage()
            frame = numpy.asarray(img)

            # 画面表示
            cv2.imshow('frame', frame)
 
            # 圧縮
            frame = cv2.resize(frame, (640, 480))
 
            # 書き込み
            videoWriter.write(frame)
			
            # キー待ち
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        videowriter.close()
        os.rename(filename,'%s'%(filerename))
        # 後処理
        cameraCapture.release()
        videoWriter.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':

    time.sleep(1)
    app = application.Application()
    app.start("notepad.exe")
    app.Notepad.wait('visible')
#    app[u'無題.*メモ帳'].CaptureAsImage().save('auto_capture.png')
    tmpapp = app[u'無題.*メモ帳']
    th_cl = TestThread(tmpapp)
    th_cl.start()

    #cap_app = AppCap(tmpapp)
    #.CaptureAsImage().save('auto_capture.png')

    time.sleep(1)
    app.Notepad.edit.TypeKeys('Hello world')
    time.sleep(1)

    app.Notepad.MenuSelect(u'ファイル(&F)->名前を付けて保存(&A)...')
    time.sleep(1)

    app[u'名前を付けて保存'].edit.SetText('tamesi.txt')
    time.sleep(1)
    app[u'名前を付けて保存'][u'保存(&S)'].Click()


