from tkinter import *
from tkinter import ttk

def spin_changed(*args):
    print('value = %s' % spinval.get())
    if spinval.get().isnumeric():
        s = spinval.get()
        i = int(s)
        spinval.set(i)
    else:
        spinval.set("0")
    
if __name__ == '__main__':
    
    root = Tk()
    root.title('Spinbox')
    root.columnconfigure(0, weight=1);
    root.rowconfigure(0, weight=1);
    
    # Frame
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid(sticky=(N,W,S,E))
    frame1.columnconfigure(0, weight=1);
    frame1.rowconfigure(0, weight=1);
    
    # スピンボックス
    spinval = StringVar()
    spinval.trace("w", spin_changed)
    
    sp = Spinbox(
        frame1,
        textvariable=spinval,
        from_=0,
        to=10)
    sp.grid(row=0, column=0, sticky=(N, W))
        
    root.mainloop()