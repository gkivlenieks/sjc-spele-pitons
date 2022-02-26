from email.mime import image
from tkinter import *
from PIL import Image, ImageTk, ImageOps

master = Tk()

CW = 600
CH = 600
pstep = 5
grass = PhotoImage(file='Gustavs/assets/graaas.ppm')
ImgW = 426
ImgH = 586
ImgM = 10

logs = Canvas (
    master,
    width=CW,
    height=CH
)
bukgronds = logs.create_image(CW // 2, CH // 2, image= grass)
logs.pack()
marijo = Image.open('Gustavs/assets/BMario-NoBG.png')
marijo = marijo.resize((ImgW // ImgM, ImgH // ImgM))
ma = ImageTk.PhotoImage(marijo)
playah = logs.create_image(CW // 2, CH // 2, image = ma)
master.title("Linijas spēle")
px = CW // 2
py = CH // 2
master.resizable(False, False)
m = True

def playahmove(way):
    global px, py, playah, marijo, ma, m
    w = False
    if way == 'right':
        mm = True
        px += pstep
        w = True
    elif way == 'left':
        mm = False
        px -= pstep
        w = True
    elif way == 'up':
        py -= pstep
    elif way == 'down':
        py += pstep
    logs.delete(playah)
    if w and mm == False and m == True:
        m = False
        marijo = ImageOps.mirror(marijo)
        ma = ImageTk.PhotoImage(marijo)
    elif w and mm and m == False:
        m = True
        marijo = ImageOps.mirror(marijo)
        ma = ImageTk.PhotoImage(marijo)
    playah = logs.create_image(px, py, image = ma)
    w = False


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