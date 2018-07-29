import win32com.client
control = win32com.client.Dispatch("AgControl.AgControl")
print (control.IsVersionSupported('5.0'))