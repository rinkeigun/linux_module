from tkinter import font
import tkinter

root = tkinter.Tk()
root.title("Label")
root.geometry("300x300+1500+10")
label1 = tkinter.Label(root, text="Hallo")
label1.pack(side="top")
font1 = font.Font(family='Helvetica', size=20, weight='bold')
label2 = tkinter.Label(root, text="Bye", bg="blue", font=font1)
label2.pack(side="top")
font2 = font.Font(family='Times', size=40)
label2 = tkinter.Label(root, text="See you", fg="red", font=font2)
label2.pack(side="top")

root.mainloop()