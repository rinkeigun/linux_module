import tkinter

root = tkinter.Tk()
root.title("Status bar")
root.geometry("300x300")
status = tkinter.Label(root, text="Now processing..",
                           borderwidth=2, relief="groove")
status.pack(side=tkinter.BOTTOM, fill=tkinter.X)
root.mainloop()