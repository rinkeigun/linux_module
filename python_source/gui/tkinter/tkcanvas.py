import tkinter

root = tkinter.Tk()
root.title("Canvas")
C = tkinter.Canvas(root, bg="white", height=300, width=300)
C.create_polygon(10, 10, 50, 170, 130, 140, 180, 40, fill="red")
C.create_line(10, 10, 200, 200, fill='black')
C.pack()
root.mainloop()