#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tesseract.exe のインストール
# PATHの追加
# 

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
from PIL import ImageGrab
import pyperclip
import csv

import pyocr
import pyocr.builders
from PIL import Image



def wait_element_view(img, wait_time=1, confidence=0.999):
    for it in range(1, wait_time):
        if pyautogui.locateCenterOnScreen(img, confidence=confidence) is None: 
            time.sleep(1)
            continue
        else:
            break



if __name__ == '__main__':

    time.sleep(1)
    app_path = u'"C:\\Program Files\\photron\\WRPD19P_SMP\\wrpd19p.exe" "D:\\2018-06\\極洋電機\K電機\\050.受領資料\\10.日付\\20180620\\{}"'.format(sys.argv[1])
    #app_path = u'"C:\\Program Files\\photron\\WRPD19P_SMP\\wrpd19p.exe" "D:\\2018-06\\極洋電機\K電機\\050.受領資料\\10.日付\\%s"'.(sys.argv[1])
    #app_path = u'"C:\\Program Files\\photron\\WRPD19P_SMP\\wrpd19p.exe" "D:\\2018-06\\極洋電機\K電機\\050.受領資料\\10.日付\\DST37326LKWITHPLUG.ZRD"'
    print(app_path)
    app = application.Application()
    app.start(app_path)
    time.sleep(3)

    pyautogui.hotkey('ctrl', 'j')
    pyautogui.typewrite('160')
    time.sleep(3)
    pyautogui.press('tab')
    pyautogui.typewrite( '30')
    time.sleep(3)
    pyautogui.press('return')

    pyautogui.hotkey('ctrl', 'w')
    pyautogui.typewrite('160')
    time.sleep(3)
    pyautogui.press('tab')
    pyautogui.typewrite( '30')
    time.sleep(3)
    pyautogui.press('return')

    pyautogui.typewrite('211')
    time.sleep(3)
    pyautogui.press('tab')
    pyautogui.typewrite( '54')
    time.sleep(3)
    pyautogui.press('return')
    
    drawing_path = "cadimg\\drawing.png"
    #x,y = pyautogui.locateCenterOnScreen(drawing_path, confidence=0.6)
    #print(x,y)
    #x1,y1, x2, y2 = pyautogui.locateOnScreen(drawing_path, confidence=0.6)
    #print(x1,y1, x2,y2)
    
    # x1, y1, x2, y2 = x座標, y座標, x幅, y高さ
    #ImageGrab.grab(bbox=(x1, y1, x1+x2, y1+y2)).save('tmp.png')
    time.sleep(1)
    ImageGrab.grab(bbox=(300, 200, 1400, 950)).save('tmp.png')
    time.sleep(5)

    tools = pyocr.get_available_tools()
    if len(tools) == 0:
    	print("No OCR tool found")
    	sys.exit(1)
    tool = tools[0]
    a = pyocr.builders.TextBuilder(tesseract_layout=4)
    #a = pyocr.builders.WordBoxBuilder( )
    #a = pyocr.builders.LineBoxBuilder( )

    img_o = Image.open('tmp.png')
    txt = tool.image_to_string(
    	img_o,
    	builder  = a
    )
    print (txt)
    img_o.close()
    
    
    
    #WEIGHT
    pyautogui.hotkey('ctrl', 'j')
    pyautogui.typewrite('137')
    time.sleep(3)
    pyautogui.press('tab')
    pyautogui.typewrite( '58')
    time.sleep(3)
    pyautogui.press('return')

    
    time.sleep(1)
    
    # x1, y1, x2, y2 = x座標, y座標, x幅, y高さ
    ImageGrab.grab(bbox=(300, 200, 1400, 900)).save('tmp2.png')
    time.sleep(5)

    tools = pyocr.get_available_tools()
    if len(tools) == 0:
    	print("No OCR tool found")
    	sys.exit(1)
    tool = tools[0]
    a = pyocr.builders.TextBuilder(tesseract_layout=4)
    #a = pyocr.builders.WordBoxBuilder( )
    #a = pyocr.builders.LineBoxBuilder( )

    img_o = Image.open('tmp2.png')
    txt = tool.image_to_string(
    	img_o,
    	builder  = a
    )
    print (txt)
    img_o.close()

    # シンボル
    # x1, y1, x2, y2 = x座標, y座標, x座標, y座標
    # シンボルの中心へ移動
    pyautogui.hotkey('ctrl', 'j')
    pyautogui.typewrite('183')
    time.sleep(3)
    pyautogui.press('tab')
    pyautogui.typewrite( '266')
    time.sleep(3)
    pyautogui.press('return')

    # 画像の切り取り
    time.sleep(1)
    ImageGrab.grab(bbox=(800, 430, 1130, 680)).save('tmp3.png')
