import win32gui
import re

class WindowMgr:
    #set the wildcard string you will search for
    def find_window_wildcard(self, wildcard):
        self._handle = None
        win32gui.EnumWindows(self.window_enum_callback, wildcard)

    #enumurate through all the windows until you find the one you need
    def window_enum_callback(self, hwnd, wildcard):
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) != None:
            self._handle = hwnd ##pass back the id of the window

    #as a separate function, set the window to the foreground
    def set_foreground(self):
        win32gui.SetForegroundWindow(self._handle)

    #extra function to get all child window handles
    def get_child_handles(self):
        win32gui.EnumChildWindows(self._handle, add_to_list, None)

    #final function to send the commands in
    def flash_window(self):
        for c_hwnd in child_list:
            print((self._handle),(c_hwnd),(win32gui.GetWindowText(c_hwnd))) #prove correct child window found
            #send command1#
            #send command2#
            #send command3#

#seprate fundction to collect the list of child handles
def add_to_list(hwnd, param):
    if win32gui.GetWindowText(hwnd)[:3] == "IWD":
        child_list.append(hwnd)

child_list=[]
w = WindowMgr()

w.find_window_wildcard(".*s*")
w.set_foreground()
w.get_child_handles()
w.flash_window()