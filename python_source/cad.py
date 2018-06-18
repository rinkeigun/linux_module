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
    app_path = u'"C:\\Program Files\\photron\\WRPD19P_SMP\\wrpd19p.exe" "D:\\2018-06\\極洋電機\K電機\\050.受領資料\\10.日付\\20180615\\{}"'.format(sys.argv[1])
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

    pyautogui.typewrite('208')
    time.sleep(3)
    pyautogui.press('tab')
    pyautogui.typewrite( '53')
    time.sleep(3)
    pyautogui.press('return')
    
    drawing_path = "cadimg\\drawing.png"
    #x,y = pyautogui.locateCenterOnScreen(drawing_path, confidence=0.6)
    #print(x,y)
    x1,y1, x2, y2 = pyautogui.locateOnScreen(drawing_path, confidence=0.6)
    print(x1,y1, x2,y2)
    
    # x1, y1, x2, y2 = x座標, y座標, x幅, y高さ
    #ImageGrab.grab(bbox=(x1, y1, x1+x2, y1+y2)).save('tmp.png')
    ImageGrab.grab(bbox=(x1, 200, 1400, y1+y2)).save('tmp.png')
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
    
    '''
    pyautogui.typewrite(u'asia.centiro.ikea.com/c3neo/ui/shell/')
    pyautogui.press('return')
    login_path = "ikeaimg\\login.png"
    wait_element_view( login_path, wait_time=10, confidence=0.6)
    time.sleep(3)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    
    #login
    print('login')
    pyautogui.typewrite('spec@ikea.com')
    pyautogui.press('tab')
    pyautogui.typewrite('cdt2018!')
    time.sleep(3)
    x,y = pyautogui.locateCenterOnScreen(login_path, confidence=0.6)
    pyautogui.click(x,y)
    
    #order
    print('Order')
    order_path = "ikeaimg\\order.png"
    #time.sleep(5)
    wait_element_view( order_path, wait_time=5, confidence=0.6)
    x,y = pyautogui.locateCenterOnScreen(order_path, confidence=0.6)
    pyautogui.click(x,y)

    #serviceorder
    print('Service Order')
    serviceorder_path = "ikeaimg\\serviceorder.png"
    time.sleep(1)
    x,y = pyautogui.locateCenterOnScreen(serviceorder_path, confidence=0.6)
    pyautogui.click(x,y)

    #serviceorders
    print('Service Orders')
    serviceorders_path = "ikeaimg\\serviceorders.png"
    time.sleep(1)
    x,y = pyautogui.locateCenterOnScreen(serviceorders_path, confidence=0.6)
    pyautogui.click(x,y)
    
    #search
    print('search')
    search_path = "ikeaimg\\search.png"
    wait_element_view( search_path, wait_time=10, confidence=0.8)
    time.sleep(3)
    x,y = pyautogui.locateCenterOnScreen(search_path, confidence=0.8)
    pyautogui.click(x,y)


    #search
    print('status')
    status_path = "ikeaimg\\status.png"
    time.sleep(10)
    wait_element_view( status_path, wait_time=10, confidence=0.8)
    x,y = pyautogui.locateCenterOnScreen(status_path, confidence=0.8)
    first_line_y = y + 30
    pyautogui.click(x,first_line_y)
    
    #search
    print('cntl+a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'A')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'C')

    #silverlight_OK
    print('silverlight_OK')
    silverlight_path = "ikeaimg\\silverlight_OK.png"
    #time.sleep(10)
    wait_element_view( silverlight_path, wait_time=10, confidence=0.8)
    x,y = pyautogui.locateCenterOnScreen(silverlight_path, confidence=0.8)
    pyautogui.click(x,y)
    
    #clipboard
    print( pyperclip.paste() )
    clipboard_list = pyperclip.paste().split("\r\n")
    #clipboard_list.insert(0, '	ステータス	チーム	サービス	開始日	開始時間	キャパシティ	郵便番号	お客様氏名	サービスオーダー番号	配送オーダー番号	作成日	サービスプロバイダ	SP Sublevel\r\n')
    #clipboard_list.insert(0, '	ステータス	チーム	サービス	開始日	開始時間	キャパシティ	郵便番号	お客様氏名	サービスオーダー番号	配送オーダー番号	作成日	サービスプロバイダ	SP Sublevel	商品	サービス情報	質問事項	添付	オーダー情報	アラート	StatusEvents\r\n')
    clipboard_len = len(clipboard_list)

    f = open('data.csv', 'a') #ファイルが無ければ作る、の'a'を指定します

    csvWriter = csv.writer(f)

    for n in range(0, clipboard_len):
       print(clipboard_list[n])
       split_str = clipboard_list[n].split('\t')
       clip_str = []
       for a_str in split_str:
            clip_str.append( a_str.replace('\xa0',''))
       print( n, clip_str )
       csvWriter.writerow(clip_str)          #1行書き込み

    f.close()
    '''
