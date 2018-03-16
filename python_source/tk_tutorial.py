## 動作しないなぁ
from tkinter import *
import subprocess

window = Tk()
count = 0
def click():
    global count
    count += 1
    if count % 10 == 0:
        print(count, u"回")
click1=Button(window, text=u"クリック", command = click)
click1.pack()


def func1():
    print("クリック")


def func2():
    subprocess.run(("start", "timeout", "/T", "10"), shell=True)

root = Tk()
Button(root, text="ボタン1", command=func1).pack()
Button(root, text="ボタン2", command=func2).pack()
mainloop()