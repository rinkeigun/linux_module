import win32gui
import time

while(1):
    hwnd = win32gui.WindowFromPoint(win32gui.GetCursorPos())
    w0, h0, w1, h1 = win32gui.GetWindowRect(hwnd)
    print( w0, h0, w1, h1 )
    print(win32gui.GetWindowText( hwnd ))
    time.sleep(1)
