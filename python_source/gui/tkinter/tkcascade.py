from tkinter import *
import tkinter.messagebox as tkmsg
 
 
root = Tk()
root.option_add('*font', ('FixedSys', 14))
 
var = StringVar()
var.set('normal')
 
def dummy(): pass
 
# 状態の変更
def change_state():
    m1.entryconfigure('Menu1', state = var.get())
    m1.entryconfigure('Menu2', state = var.get())
    m1.entryconfigure('Menu3', state = var.get())
    m0.entryconfigure('SingleMenu', state = var.get())
 
def tandoku():
    res=tkmsg.askquestion( title = 'about', message = '単独メニューが選ばれました')
    print('戻り値：',res)
# メニューの設定
m0 = Menu(root)
root.configure(menu = m0)
 
m1 = Menu(m0, tearoff = False)
 
 
m0.add_cascade(label = 'カスケードMenu', under = 0, menu = m1)
m1.add_command(label = 'Menu1', command = dummy)
m1.add_command(label = 'Menu2', command = dummy)
m1.add_command(label = 'Menu3', command = dummy)
 
m0.add_command(label = 'SingleMenu', command = tandoku)
 
 
# ラジオボタンの設定
for x in ('normal', 'active', 'disabled'):
    Radiobutton(root, text = x, value = x,
                variable = var, command = change_state).pack(anchor = W)
 
root.mainloop()