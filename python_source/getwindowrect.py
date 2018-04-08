import win32gui
import win32gui_struct
import win32con
from win32com.shell import shell, shellcon
import time
import pywintypes

while(1):
    pt = win32gui.GetCursorPos()
    hwnd = win32gui.WindowFromPoint(pt)
    w0, h0, w1, h1 = win32gui.GetWindowRect(hwnd)
    focus = win32gui.GetFocus()
    #win32gui.DrawFocusRect( hwnd, (w0, h0, w1, h1))
    #win32gui.DrawEdge( hwnd, (w0, h0, w1, h1), win32con.BDR_INNER, win32con.BF_ADJUST)
    print( "my point:",w0, h0, w1, h1 )
    print( "client point:", win32gui.GetClientRect(hwnd))
    parent = win32gui.GetParent( hwnd )
    active = win32gui.GetActiveWindow()
    print("window placement: ", win32gui.GetWindowPlacement(hwnd))
    childwindow = win32gui.ChildWindowFromPoint(hwnd, win32gui.GetCursorPos())
    print( "capture : ", win32gui.GetCapture())
    window = win32gui.GetWindow(hwnd, 1)
    win32gui.SendMessage( hwnd, 1, None, None)
    desktop = win32gui.GetDesktopWindow()
    menu = win32gui.GetMenu(hwnd)
    cursorinfo = win32gui.GetCursorInfo()
    foreground = win32gui.GetForegroundWindow()
    hdc = win32gui.GetDC(hwnd)
    #win32gui.PolylineTo(hdc, ((w0, h0), (w1, h0), (w1, h1), (w0, h1), (w0,h0)))
    obj = win32gui.GetCurrentObject(hdc, win32con.OBJ_BITMAP)
    stockobj = win32gui.GetStockObject(obj)
    sysmenu  = win32gui.GetSystemMenu(hwnd, 1)





    print("1. desktop     : ", desktop)
    print("2. window      : ", window)
    print("3. hwnd        : ", hwnd )
    print("4. parent      : ", parent)
    print("5. child       : ", childwindow)
    print("6. active      : ", active)
    print("7. focus       : ", focus)
    print("8. getMenu     : ", menu)
    print("9. CursorInfo  : ", cursorinfo)
    print("10. Foreground : ", foreground)
    print("11. hdc        : ", hdc  )
    print("12. obj        : ", obj  )
    print("13. stockobj   : ", stockobj  )
    print("14. sysmenu    : ", sysmenu  )
    print("================================================")
    print("1. desktop class: ", win32gui.GetClassName(desktop))
    print("2. window  class: ", win32gui.GetClassName(window ))
    print("3. hwnd    class: ", win32gui.GetClassName(hwnd   ))
    if parent != 0:
        print("4. parent  class: ", win32gui.GetClassName(parent ))
    if childwindow != 0:
        print("5. child   class: ", win32gui.GetClassName(childwindow  ))
    if active != 0:
        print("6. active  class: ", win32gui.GetClassName(active ))
    #print("7. focus   class: ", win32gui.GetClassName(focus   ))
    #print("8. menu    class: ", win32gui.GetClassName(menu   ))
    #print("9. cursor  class: ", win32gui.GetClassName(cursorinfo   ))
    print("10.fore    class: ", win32gui.GetClassName(foreground))
    #print("11.hdc     class: ", win32gui.GetClassName(hdc    ))
    #print("12.obj     class: ", win32gui.GetClassName(obj    ))
    #print("13.stockobjclass: ", win32gui.GetClassName(stockobj  ))
    #print("14.sysmenu class: ", win32gui.GetClassName(sysmenu))
    print("================================================")
    print("1. desktop text : ", win32gui.GetWindowText(desktop))
    print("2. window  text : ", win32gui.GetWindowText(window ))
    print("3. hwnd    text : ", win32gui.GetWindowText(hwnd   ))
    print("4. parent  text : ", win32gui.GetWindowText(parent ))
    print("5. child   text : ", win32gui.GetWindowText(childwindow  ))
    print("6. active  text : ", win32gui.GetWindowText(active ))
    print("7. focus   text : ", win32gui.GetWindowText(focus  ))
    print("8. getMenu text : ", win32gui.GetWindowText(menu   ))
    #print("9. CursorIntext : ", win32gui.GetWindowText(cursorinfo ))
    print("10.foregro text : ", win32gui.GetWindowText(foreground ))
    print("11.hdc     text : ", win32gui.GetWindowText(hdc   ))
    print("12.obj     text : ", win32gui.GetWindowText(obj    ))
    print("13.stockobjtext : ", win32gui.GetWindowText(stockobj))
    print("14.sysmenu text : ", win32gui.GetWindowText(sysmenu))
    print("15.menu         : ", win32gui.GetMenuItemRect(hwnd, menu, 2))

    buf, extras = win32gui_struct.EmptyMENUITEMINFO()
    #print(type(buf))
    #print("buf 0 : ", buf[0])
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    try:
        #print(type( menu ))
        for i in range( win32gui.GetMenuItemCount(menu) ):
            win32gui.GetMenuItemInfo( menu, 
                i, 
                True, 
                buf)
            #win32gui.GetMenuInfo( menu, 
            #    buf )
            #print( "menu :" , buf[0] )
            _, rect = win32gui.GetMenuItemRect(hwnd, menu, i)
            #print( rect )
            if win32gui.PtInRect( rect, pt ):
                print(win32gui_struct.UnpackMENUITEMINFO(buf))

    except pywintypes.error :
        pass
    win32gui.DrawMenuBar(hwnd)
    #time.sleep(1)
    
    #print("menu count : ", win32gui.GetMenuItemCount(menu))
    
    #print("layout:", win32gui.GetLayout())
    #print("Message:", win32gui.GetMessage(hwnd, 0, 10))
    
    time.sleep(1)
