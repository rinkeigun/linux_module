# -*- coding: utf-8 -*-
import ctypes
 
if __name__ == "__main__":
    handle = ctypes.windll.user32.FindWindowW("Notepad", 0)
    #handle = ctypes.windll.user32.FindWindowW("wechat", 0)
    print(hex(handle))
    