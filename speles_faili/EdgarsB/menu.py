import tkinter

main = tkinter.Tk()

mframe = tkinter.Frame(main)
mframe.pack()

def clearwin(event=None):
    '''Clear the main windows frame of all widgets'''
    for child in mframe.winfo_children():
        child.destroy()

def win1(event=None):
    '''Create the main window'''
    clearwin()
    b1 = tkinter.Button(mframe, command=win2, text='Window 2')
    b1.pack()
    b2 = tkinter.Button(mframe, command=win3, text='Window 3')
    b2.pack()

def win2(event=None):
    '''Create the second sub window'''
    clearwin()
    entry1 = tkinter.Entry(mframe)
    entry1.pack()
    back = tkinter.Button(mframe, command=win1, text='Back')
    back.pack()

def win3(event=None):
    '''Create the third sub window'''
    clearwin()
    label1 = tkinter.Label(mframe, text='This is the third window!')
    label1.pack()
    back = tkinter.Button(mframe, command=win1, text='Back')
    back.pack()

win1()

main.mainloop()