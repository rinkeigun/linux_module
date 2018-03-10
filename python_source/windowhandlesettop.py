# windowsのサイズ設定

import win32gui
import win32con


def set_window_top():
    hwnd = win32gui.GetForegroundWindow()
    (left, top, right, bottom) = win32gui.GetWindowRect(hwnd)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, left+50, top+50, right - left+50, bottom - top+50, 0)
    
if __name__=='__main__':
    set_window_top()
    