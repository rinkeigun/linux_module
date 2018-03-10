# -*- coding: utf-8 -*-
# windowsの列挙
import ctypes
import array
 
def enum_child_windows_proc(handle, list):
    list.append(handle)
    return 1
 
if __name__ == "__main__":
    parent_handle = ctypes.windll.user32.FindWindowW(0, "無題 - メモ帳")
    print(hex(parent_handle))
 
    child_handles = array.array("i")
    ENUM_CHILD_WINDOWS = ctypes.WINFUNCTYPE(\
            ctypes.c_int,\
            ctypes.c_int,\
            ctypes.py_object)
    ctypes.windll.user32.EnumChildWindows(\
            parent_handle,\
            ENUM_CHILD_WINDOWS(enum_child_windows_proc),\
            ctypes.py_object(child_handles))
    for i in range(len(child_handles)):
        print(hex(child_handles[i]))
