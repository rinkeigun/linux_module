# -*- coding: utf-8 -*-

from tkinter import *

#コールバック関数を定義しておく。
def callback():
    print ('called')

#root ウィンドウを作る。
root = Tk()
frame = Frame(root,width=300,height=200)
frame.pack()

menu_top = Menu(root)
menu_file = Menu(menu_top)
menu_open = Menu(menu_top)

root.configure(menu=menu_top)

menu_top.add_cascade (label='FILE(F)',menu=menu_file,under=5)
menu_top.add_command(label=u'ヘルプ(H)',underline=4,command=callback)

menu_file.add_command(label='New Window(N)',under=11)
menu_file.add_cascade(label='Open(O)',under=5,menu=menu_open)

menu_open.add_command(label='Local File(L)',under=11)
menu_open.add_command(label='Network(N)',under=8)

root.mainloop()