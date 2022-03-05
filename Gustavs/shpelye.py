from tkinter import *
from PIL import Image, ImageTk, ImageOps
import random

master = Tk()
punkti = 0

# canvas augstums, platums
CW = 600
CH = 600

#main logs
logs = Canvas (
    master,
    width=CW,
    height=CH
)
logs.pack()

# player step length
pstep = 5

# bg
grass = PhotoImage(file='Gustavs/assets/graaas.ppm')

#fons
bukgronds = logs.create_image(CW // 2, CH // 2, image= grass)

# pa cik pikseļiem playeris pārvietojas
pstep = 5

# backgrounds
grass = PhotoImage(file='Gustavs/assets/graaas.ppm')

#fons
bukgronds = logs.create_image(CW // 2, CH // 2, image= grass)

#sēne bildes izmēri, pa cik bilde tiks uztaisīta mazāka, tās uzlikšana
mushM = 12
mushroom = Image.open('gustavs/assets/Mushroom.png')
MushSiz = mushroom.size
mushroom = mushroom.resize((MushSiz[0] // mushM, MushSiz[1] // mushM))
seene = ImageTk.PhotoImage(mushroom)
sx = random.randrange(20, CW - 20, 5)
sy = random.randrange(20, CH - 20, 5)
sene = logs.create_image(sx, sy, image= seene)
def mushrum():
    global sx, sy, sene
    logs.delete(sene)
    sx = random.randrange(20, CW - 20, 5)
    sy = random.randrange(20, CH - 20, 5)
    sene = logs.create_image(sx, sy, image= seene)

#mario
ImgM = 10
marijo = Image.open('Gustavs/assets/BMario-NoBG.png')
MarioSiz = marijo.size
marijo = marijo.resize((MarioSiz[0] // ImgM, MarioSiz[1] // ImgM))
ma = ImageTk.PhotoImage(marijo)
playah = logs.create_image(CW // 2, CH // 2, image = ma)

#score
score = logs.create_rectangle(0, 0, 100, 50, fill='grey60', outline='black')
tscore = logs.create_text(50, 25, font=(None, 20), text=punkti)
def scoore(points):
    global tscore
    logs.delete(tscore)
    tscore = logs.create_text(50, 25, font=(None, 20), text=punkti)

#loga title
master.title("Linijas spēle")

#sākuma spēlētaja atrašanās vieta
px = CW // 2
py = CH // 2

#resizability
master.resizable(False, False)

#facing right
m = True

#player move
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

#logs ir/nav resizable
master.resizable(False, False)

#vai spēlētājs skatās pa labi
m = True

#speletāja kustības funkcija
def playahmove(way):
    global px, py, playah, marijo, ma, m, punkti, sx, sy
    #vai būs jāmirroro bilde
    w = False
    #pārbauda kurā virziena tas jāpārvieto
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
    if px <= sx and px + marijo.size[0] >= sx + mushroom.size[1] and py <= sy and py + marijo.size[1] >= sy + mushroom.size[1]:
        punkti += 1
        scoore(punkti)
        print('l')
        mushrum()
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