from tkinter import *
r = Tk()

redy = IntVar()

mainw = Canvas(
    r,
    width=500,
    height=500
)
mainw.pack()

def func():
    print('whaaaaaaaat')

kkas = mainw.create_rectangle(0, 0, 500, 200, fill='grey')

mainw.tag_bind(kkas, "<Button-1>", func)

r.mainloop()