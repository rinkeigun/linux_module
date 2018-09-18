import tkinter

root = tkinter.Tk()

labelframe = tkinter.LabelFrame(root, text="This is a left LabelFrame")
labelframe.pack(side=tkinter.LEFT, fill="both", expand="yes")

left = tkinter.Label(labelframe, text="Inside the left LabelFrame")
left.pack()

labelframe = tkinter.LabelFrame(root, text="This is a right LabelFrame")
labelframe.pack(side=tkinter.RIGHT, fill="both", expand="yes")

right = tkinter.Label(labelframe, text="Inside the right LabelFrame")
right.pack()

root.mainloop()