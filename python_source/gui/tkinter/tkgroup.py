import tkinter

root = tkinter.Tk()
root.title("Frame")
frame = tkinter.Frame(root)
frame.pack()

bottomframe = tkinter.Frame(root)
bottomframe.pack(side=tkinter.BOTTOM)

redbutton = tkinter.Button(frame, text="1")
redbutton.pack(side=tkinter.LEFT)

greenbutton = tkinter.Button(frame, text="2")
greenbutton.pack(side=tkinter.LEFT)

bluebutton = tkinter.Button(frame, text="3")
bluebutton.pack(side=tkinter.LEFT)

blackbutton = tkinter.Button(bottomframe, text="Go")
blackbutton.pack(side=tkinter.BOTTOM)

root.mainloop()