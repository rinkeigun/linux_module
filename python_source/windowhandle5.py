# -*- coding: utf-8 -*-
import ctypes
 
WM_CHAR = 0x0102
 
if __name__ == "__main__":
    ctypes.windll.user32.SendMessageW(0x000205F8, WM_CHAR, 0x61, 0)
