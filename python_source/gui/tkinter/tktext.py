from tkinter import *
from tkinter import ttk
from tkinter.font import Font

def button_click():
    print('TEXT = %s' % txt.get(1.0, END))
    

if __name__ == '__main__':
    root = Tk()
    root.title('Text 1')
    root.minsize(100, 100)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    # Frame
    frame1 = ttk.Frame(root, padding=10)
    frame1.rowconfigure(1, weight=1)
    frame1.columnconfigure(0, weight=1)
    frame1.grid(sticky=(N,W,S,E))
    
    #Button
    button1 = ttk.Button(frame1, text='OK', command=button_click)
    button1.grid(row=0, column=0, columnspan=2, sticky=(N,E))
    
    # Text
    f = Font(family='Helvetica', size=11)
    v1 = StringVar()
    txt = Text(frame1)
    txt.configure(font=f)
    txt.insert(1.0, "Hello!")
    txt.grid(row=1, column=0, sticky=(N,W,S,E))
    
     # Scrollbar
    scrollbar = ttk.Scrollbar(
        frame1, 
        orient=VERTICAL, 
        command=txt.yview)
    txt['yscrollcommand'] = scrollbar.set
    scrollbar.grid(row=1,column=1,sticky=(N,S))
    
    root.mainloop()