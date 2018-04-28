#!/usr/bin/python
# -*- encoding: utf-8 -*-

import win32evtlog
import win32evtlogutil
import winerror

#logType = "System"
logType = "Application"
h = win32evtlog.OpenEventLog(None, logType)

flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
objects = win32evtlog.ReadEventLog(h,flags, 0)
while objects:
  for ev_obj in objects:
    #appname, eventid, vnetcategory, eventtype, strings = win32evtlogutil.SafeFormatMessage(ev_obj, logType)
    appname = win32evtlogutil.FormatMessage(ev_obj, logType)
    print( type(appname))
    print( appname )
    '''
    if winerror.HRESULT_CODE(ev_obj.EventID) == 6005:
      print ("%s %s" % ("start", ev_obj.TimeGenerated.Format()))
      print (win32evtlogutil.SafeFormatMessage(ev_obj, logType))
      # print (win32evtlogutil.SafeFormatMessage(ev_obj, logType).encode("mbcs"))
    if winerror.HRESULT_CODE(ev_obj.EventID) == 7001:
      print ("%s %s" % ("start", ev_obj.TimeGenerated.Format()))
      print (win32evtlogutil.SafeFormatMessage(ev_obj, logType))
    if winerror.HRESULT_CODE(ev_obj.EventID) == 6006:
      print ("%s %s" % ("end", ev_obj.TimeGenerated.Format()))
      print (win32evtlogutil.SafeFormatMessage(ev_obj, logType))
    if winerror.HRESULT_CODE(ev_obj.EventID) == 7002:
      print ("%s %s" % ("end", ev_obj.TimeGenerated.Format()))
      print (win32evtlogutil.SafeFormatMessage(ev_obj, logType))
      # print (win32evtlogutil.SafeFormatMessage(ev_obj, logType).encode("mbcs"))
    if winerror.HRESULT_CODE(ev_obj.EventID) == 10005:
      print ("%s %s" % ("restart", ev_obj.TimeGenerated.Format()))
      print (win32evtlogutil.SafeFormatMessage(ev_obj, logType))
    if winerror.HRESULT_CODE(ev_obj.EventID) == 10010:
      print ("%s %s" % ("restart", ev_obj.TimeGenerated.Format()))
      print (win32evtlogutil.SafeFormatMessage(ev_obj, logType))
    '''
  objects = win32evtlog.ReadEventLog(h,flags, 0)

win32evtlog.CloseEventLog(h)