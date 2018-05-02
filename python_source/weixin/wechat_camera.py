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
# 导入模块
from wxpy import *
import sqlite3



# CV_FOURCC('D','I','B',' ')    = 無圧縮
# CV_FOURCC('P','I','M','1')    = MPEG-1 codec
# CV_FOURCC('M','J','P','G')    = motion-jpeg codec (does not work well)
# CV_FOURCC('M', 'P', '4', '2') = MPEG-4.2 codec
# CV_FOURCC('D', 'I', 'V', '3') = MPEG-4.3 codec
# CV_FOURCC('D', 'I', 'V', 'X') = MPEG-4 codec
# CV_FOURCC('U', '2', '6', '3') = H263 codec
# CV_FOURCC('I', '2', '6', '3') = H263I codec
# CV_FOURCC('F', 'L', 'V', '1') = FLV1 codec

class AppCap:
    def __init__(self):
        db = 'test.db3'
        tablename = 'wechat_control_t'
        connector = sqlite3.connect(db)

        filename, filerename, cameraCapture, videoWriter=self.camera_init()
        camera_flg = True
        flg = 1

        while (1):
            if flg == 0:
                time.sleep(4)
                if camera_flg == True:
                    # 後処理
                    cameraCapture.release()
                    videoWriter.release()
                    os.rename(filename,'%s'%(filerename))
                    cv2.destroyAllWindows()
                    camera_flg = False
                sql = "select flg from %s" % ( tablename )
                flg = connector.execute( sql ).fetchone()[0]
                continue
            else:
                if camera_flg == False:
                    filename, filerename, cameraCapture, videoWriter=self.camera_init()
                    camera_flg = True
            if cameraCapture.isOpened() == False:
                continue
            ret, frame = cameraCapture.read()

            # 画面表示
            cv2.imshow('frame', frame)

            # 圧縮
            frame = cv2.resize(frame, (640, 480))

            # 書き込み
            videoWriter.write(frame)

            # キー待ち
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            sql = "select flg from %s" % ( tablename )
            flg = connector.execute( sql ).fetchone()[0]
 
    def camera_init(self):
        #時間を取得
        d=datetime.datetime.now().isoformat()
        filerename=(str(d)+'.avi').replace(":", "")
        filename = 'output.avi'

        cameraCapture = cv2.VideoCapture(0)
        fps = 30
        size = (int(cameraCapture.get(3)),
            int(cameraCapture.get(4)))
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        videoWriter = cv2.VideoWriter(filename, fourcc, fps, size)
        
        return( filename, filerename, cameraCapture, videoWriter )


if __name__ == "__main__":

    # 初始化机器人，扫码登陆
    bot = Bot(cache_path=True, console_qr=True)

    @bot.register(except_self=False, enabled=True)
    def reply_my_friend(msg):
        db = 'test.db3'
        tablename = 'wechat_control_t'
        connector = sqlite3.connect(db)
        if msg.sender == msg.receiver:
            str_lower = msg.text.lower()
            if str_lower == 'h':
                str = 'h   : help\n'
                str += 'h s : status\n'
                str += 'c on/off : camera on/off'
                return str
            elif str_lower == 'h s':
                sql = "select flg from %s" % ( tablename )
                flg = connector.execute( sql ).fetchone()[0]
                if flg == 1:
                    return 'On'
                else:
                    return 'Off'
            elif 'c on' in str_lower:
                sql = "update %s set flg = %d " % ( tablename, 1 )
                connector.execute( sql )
                connector.commit()
            elif 'c off' in str_lower:
                sql = "update %s set flg = %d " % ( tablename, 0 )
                connector.execute( sql )
                connector.commit()
    cap_app = AppCap()

