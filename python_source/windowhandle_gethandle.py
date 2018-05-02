# -*- coding: utf-8 -*-
import ctypes
 
if __name__ == "__main__":
    handle = ctypes.windll.user32.FindWindowW(0, "無題 - メモ帳")
    print(hex(handle))
