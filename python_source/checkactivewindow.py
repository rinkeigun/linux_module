# windowsのハンドル、名前を取得

from time import sleep
import ctypes
import win32gui
import win32process

def funWin():
    handle = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(handle)
    thread_process = win32process.GetWindowThreadProcessId(handle)
    # 1:process, 0:thread
    print(str(handle) + ":" + title+ ":" + str(thread_process[1])+ ":" + str(thread_process[0]))

# 下記関数がうまく実行できない
def onForeground():
    """Detect if SC2-Client is the foreground window (only Windows)."""
    try:
        forewindow = ctypes.windll.user32.GetForegroundWindow()
        print(forewindow)
        fg_window_name = ctypes.windll.user32.GetWindowText(forewindow)
        print(fg_window_name)
        print("3")
        #fg_window_name = GetWindowText(GetForegroundWindow()).lower()
        print( u"1:" )
        #note = "NotePad".lower()
        #return fg_window_name == "無題 - メモ帳"
        return true
    except Exception as e:
        #module_logger.exception("message")
        return False
if __name__ == '__main__':
    while(1):
    	#print(onForeground())
    	funWin()
    	sleep(1)
