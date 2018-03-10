from PIL import ImageGrab
import pyautogui
import win32gui
import win32ui
import win32con
from PIL import Image
#import win32api
 
#Screen shot
pyautogui.screenshot('screenshot001.png')
 
# = pyautogui.screenshot('screenshot001.png')
img = ImageGrab.grab()
img.save('screenshot002.png')
 
#active window screenshot(GetWindowRect)
hwnd = win32gui.GetForegroundWindow()
w0, h0, w1, h1 = win32gui.GetWindowRect(hwnd)
img = ImageGrab.grab(bbox=(w0, h0, w1, h1))
img.save('screenshot003.png')
 
#active window screenshot(GetClientRect)
hwnd = win32gui.GetForegroundWindow()
w0, h0, w1, h1 = win32gui.GetClientRect(hwnd)
img = ImageGrab.grab(bbox=(w0, h0, w1, h1))
img.save('screenshot004.png')
 
#focused window screenshot
#x, y = win32api.GetCursorPos()
#hwnd = win32gui.WindowFromPoint(win32api.GetCursorPos())
#_, _, (x, y) = win32gui.GetCursorInfo()
#hwnd = win32gui.WindowFromPoint((x, y))
hwnd = win32gui.WindowFromPoint(win32gui.GetCursorPos())
w0, h0, w1, h1 = win32gui.GetWindowRect(hwnd)
img = ImageGrab.grab(bbox=(w0, h0, w1, h1))
img.save('screenshot005.png')


 
hwnd = win32gui.WindowFromPoint(win32gui.GetCursorPos())
w0, h0, w1, h1 = win32gui.GetWindowRect(hwnd)
 
hwndDC = win32gui.GetWindowDC(hwnd)
mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
saveDC = mfcDC.CreateCompatibleDC()
 
saveBitMap = win32ui.CreateBitmap()
saveBitMap.CreateCompatibleBitmap(mfcDC, w1-w0, h1-h0)
saveDC.SelectObject(saveBitMap)
saveDC.BitBlt((0, 0), (w1-w0, h1-h0),  mfcDC,  (0, 0),  win32con.SRCCOPY)
bmpinfo = saveBitMap.GetInfo()
bmpstr = saveBitMap.GetBitmapBits(True)
img = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
img.save('screenshot008.png')