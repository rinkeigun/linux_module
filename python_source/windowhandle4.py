# -*- coding: utf-8 -*-
import ctypes


'''
int MessageBox(
    HWND hWnd,          // オーナーウィンドウのハンドル
    LPCTSTR lpText,     // メッセージボックス内のテキスト
    LPCTSTR lpCaption,  // メッセージボックスのタイトル
    UINT uType          // メッセージボックスのスタイル
);
'''


if __name__ == "__main__":
    ctypes.windll.user32.MessageBoxW(0, "text", "window_text", 0x00000040)
