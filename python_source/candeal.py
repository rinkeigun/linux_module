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
from PIL import ImageGrab
import pyperclip
import csv


def wait_element_view(img, wait_time=1, confidence=0.999):
    for it in range(1, wait_time):
        if pyautogui.locateCenterOnScreen(img, confidence=confidence) is None: 
            time.sleep(1)
            continue
        else:
            break



if __name__ == '__main__':

    time.sleep(1)
    app_path = u"C:\\Program Files\\internet explorer\\iexplore.exe"
    app = application.Application()
    app.start(app_path)
    time.sleep(3)
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
