from email.mime import image
from tkinter import *
import random

master = Tk()

CW = 600
CH = 600
pstep = 5

logs = Canvas (
    master,
    width=CW,
    height=CH
)
logs.pack()
ma = PhotoImage(file="Gustavs/assets/marijo.ppm")
playah = logs.create_image(CW // 2, CH // 2, image = ma)
master.title("Linijas spēle")
px = CW // 2
py = CH // 2
master.resizable(False, False)

def playahmove(way):
    global px, py, playah
    if way == 'right':
        px += pstep
    elif way == 'left':
        px -= pstep
    elif way == 'up':
        py -= pstep
    elif way == 'down':
        py += pstep
    logs.delete(playah)
    playah = logs.create_image(px, py, image = ma)


def on_keypress(event):
    if event.keysym == "w":
        playahmove('up')
    if event.keysym == "a":
        playahmove('left')
    if event.keysym == "s":
        playahmove('down')
    if event.keysym == "d":
        playahmove('right')

def on_keyrelease(event):
    global direction
    direction = None

master.bind_all('<KeyPress>', on_keypress)
master.bind_all('<KeyRelease>', on_keyrelease)
master.mainloop()