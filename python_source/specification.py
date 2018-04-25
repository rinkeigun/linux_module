#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import sys
import os
from time import time
import datetime
from pywinauto import application
import time

app_path = "notepad.exe"
app = application.Application()
app.start(app_path)
time.sleep(2)
spec_app = app.top_window()
#app.Notepad.wait('visible')
#app1 = app.Notepad.wait('visible')

print(type(spec_app.wrapper_object()))
print(spec_app.print_control_identifiers(depth=1))
# ダメ？
print(app.Properties.print_control_identifiers(depth=1))

#print(type(spec_app))
#print(type(app["Notepad"].print_control_identifiers()))
#spec_app.print_control_specifications()

'''
#print(app1[1])
print(type(spec_app.wrapper_object()))
print(type(app))
spec_app = app.top_window()

spec_app.print_control_identifiers()
'''