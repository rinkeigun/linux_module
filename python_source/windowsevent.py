import ctypes
import array

def get_window_text_w(handle):
    length = get_window_text_length_w(handle)
    if length == 0:
        return ""
    buffer = ctypes.create_unicode_buffer(length+1)
    if ctypes.windll.user32.GetWindowTextW(
            ctypes.c_int(handle), buffer, ctypes.sizeof(buffer)) == 0:
        raise WindowsError()
    return buffer.value


def set_window_text_w(handle, text):
    if not ctypes.windll.user32.SetWindowTextW(
            ctypes.c_int(handle), ctypes.c_wchar_p(text)):
        raise WindowsError()


def get_window_text_length_w(handle):
    l = ctypes.windll.user32.GetWindowTextLengthW(ctypes.c_int(handle))
    if l == 0:
        raise WindowsError()
    return l
    

def enum_top_level_windows():
    ENUM_WINDOWS_FUNC = ctypes.WINFUNCTYPE(
        ctypes.c_int, ctypes.c_int, ctypes.py_object)
    handles = array.array("i")
    if not ctypes.windll.user32.EnumWindows(
            ENUM_WINDOWS_FUNC(_enumtopwindows_enumproc),
            ctypes.py_object(handles)):
        raise WindowsError()
    return handles


def enum_child_windows(handle):
    ENUM_WINDOWS_FUNC = ctypes.WINFUNCTYPE(
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.py_object)
    handles = array.array("i")
    if not ctypes.windll.user32.EnumChildWindows(
            ctypes.c_int(handle),
            ENUM_WINDOWS_FUNC(_enumtopwindows_enumproc),
            ctypes.py_object(handles)):
        raise WindowsError()
    return handles


def enum_thread_windows(thread_id):
    ENUM_WINDOWS_FUNC = ctypes.WINFUNCTYPE(
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.py_object)
    handles = array.array("i")
    if not ctypes.windll.user32.EnumThreadWindows(
            ctypes.c_uint32(thread_id),
            ENUM_WINDOWS_FUNC(_enumtopwindows_enumproc),
            ctypes.py_object(handles)):
        raise WindowsError()
    return handles


def _enumtopwindows_enumproc(handle, list):
    list.append(handle)
    return 1


if __name__ == "__main__":
#    handles = windowhandleenumerator.enum_top_level_windows()
    handles = enum_top_level_windows()
    for handle in handles:
        print("\"{text}\" ({handle:0>8X})".format(
            handle=handle,
#            text=windowtext.get_window_text_w(handle)))
            text=get_window_text_w(handle)))
