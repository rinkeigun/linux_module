from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Frame Test')

frame1 = ttk.Frame(
    root,
    height=200,
    width=300,
    relief='sunken',
    borderwidth=5)
frame1.grid()

root.mainloop()