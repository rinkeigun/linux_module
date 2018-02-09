import win32evtlog
import win32evtlogutil
from pprint import pprint
from time import sleep
computer = "MyHost"
computer = "DESKTOP-9MI30R1"
logType = "Application"
h = win32evtlog.OpenEventLog(computer, logType)
objects = win32evtlog.ReadEventLog(h, win32evtlog.EVENTLOG_BACKWARDS_READ|
win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)
while objects:
    for object in objects:
        dir(object)
        #msg = win32evtlogutil.SafeFormatMessage(object, logType).encode("mbcs")
        msg = win32evtlogutil.SafeFormatMessage(object, logType)
        #if (object.EventType==1):
        if (1==1):
            # エラーのみ表示
            print (msg)
        objects = win32evtlog.ReadEventLog(h, win32evtlog.EVENTLOG_BACKWARDS_READ|
win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)
        sleep(1)
print (u'完了')
