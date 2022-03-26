from tkinter import *
from PIL import Image, ImageTk, ImageOps
import random
from playsound import *
import threading
import time

from setuptools import Command

master = Tk()
punkti = 0
mushcnt = 10

kkas = False

redy = IntVar()

sterp = 1
slep = .05

def sound():
    playsound("Gustavs/assets/CoinSE.mp3")

# canvas augstums, platums
CW = 600
CH = 600

# main logs
logs = Canvas(
    master,
    width=CW,
    height=CH
)
logs.pack()

# player step length
pstep = 5

def mushrum(m):
    global slep
    # globals()[f'mush{m}x'] = random.randrange(20, CW - 20, 5)
    # globals()[f'mush{m}y'] = random.randrange(20, CH - 20, 5)
    # globals()[f"mush{m}"] = logs.create_image(globals()[f'mush{m}x'], globals()[f'mush{m}y'], image=seene)
    logs.delete(globals()[f"mush{m}"])
    globals()[f'mush{m}x'] = -1
    globals()[f'mush{m}y'] = -1
    nx = threading.Thread(target=sound, daemon=True)
    nx.start()
    slep /= 1.2
    print(f'slep: {slep}')

titel_bg = logs.create_rectangle(0, 0, CW, 50, fill='grey70')
titel = logs.create_text(CW // 2, 25, text='Kaut kāds speles nosaukums', font=('Ubuntu Medium', 20))
sakt_poga = logs.create_rectangle(0, CH - 50, CW, CH, fill='grey70')
sakt_poga_teksts = logs.create_text(CW // 2, CH - 25, text='Sākt Spēli', font=("Ubuntu Medium", 20))

logs.tag_bind(sakt_poga, "<Button-1>", lambda n: redy.set(1))
logs.tag_bind(sakt_poga_teksts, "<Button-1>", lambda n: redy.set(1))

logs.wait_variable(redy)

# fons
grass = PhotoImage(file='Gustavs/assets/graaas.ppm')
bukgronds = logs.create_image(CW // 2, CH // 2, image=grass)

# sēne bildes izmēri, pa cik bilde tiks uztaisīta mazāka, tās uzlikšana
mushM = 12
mushroom = Image.open('gustavs/assets/Mushroom.png')
MushSiz = mushroom.size
mushroom = mushroom.resize((MushSiz[0] // mushM, MushSiz[1] // mushM))
seene = ImageTk.PhotoImage(mushroom)
# mario
px = CW // 2
py = CH // 2
ImgM = 10
marijo = Image.open('Gustavs/assets/BMario-NoBG.png')
MarioSiz = marijo.size
marijo = marijo.resize((MarioSiz[0] // ImgM, MarioSiz[1] // ImgM))
ma = ImageTk.PhotoImage(marijo)
playah = logs.create_image(px, py, image=ma)
print(f'px: {px}; py: {py}')
# kaut kas
slx = 0
sly = 0
slimeeM = 10
slimee = Image.open('Gustavs/assets/sss.png')
slimee = slimee.resize((slimee.size[0] // slimeeM, slimee.size[1] // slimeeM))
slime = ImageTk.PhotoImage(slimee)
slim = logs.create_image(slx, sly, image=slime)
# score
score = logs.create_rectangle(0, 0, 100, 50, fill='grey60', outline='black')
tscore = logs.create_text(50, 25, font=(None, 20), text=punkti)

for x in range(mushcnt):
    globals()[f"mush{x}x"] = random.randrange(20, CW - 20, 5)
    globals()[f"mush{x}y"] = random.randrange(20, CW - 20, 5)
    globals()[f"mush{x}"] = logs.create_image(
        globals()[f'mush{x}x'], globals()[f'mush{x}y'], image=seene)
    print(
        f'generated mushroom{x} at {globals()[f"mush{x}x"]}; {globals()[f"mush{x}y"]}')


def smove():
    global slx, sly, slim, slep, sterp, slep
    j = True
    while 1:
        if slx == px and sly == py:
            print('hehe')
        if (slx < px or sly > py) and (slx < px or sly > py):
            if slx < px and j:
                j = False
                slx += sterp
            elif sly < py and j == False:
                j = True
                sly += sterp
            elif slx > px and j:
                j = False
                slx -= sterp
            elif sly > py and j == False:
                j = True
                sly -= sterp

        elif slx < px:
            slx += sterp
        elif slx > px:
            slx -= sterp
        elif sly < py:
            sly += sterp
        elif sly > py:
            sly -= sterp
        logs.delete(slim)
        slim = logs.create_image(slx, sly, image=slime)
        time.sleep(slep)


slm = threading.Thread(target=smove, daemon=False)

slm.start()


def scoore(points):
    global tscore
    logs.delete(tscore)
    tscore = logs.create_text(50, 25, font=(None, 20), text=punkti)


# loga title
master.title("Maaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaarioo")

# resizability
master.resizable(False, False)

# facing right
m = True

# player move


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


# logs ir/nav resizable
master.resizable(False, False)

# vai spēlētājs skatās pa labi
m = True
# speletāja kustības funkcija


def playahmove(way):
    global px, py, playah, marijo, ma, m, punkti, i
    # vai būs jāmirroro bilde
    w = False
    # pārbauda kurā virziena tas jāpārvieto
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
    playah = logs.create_image(px, py, image=ma)
    for i in range(mushcnt):
        if px <= globals()[f"mush{i}x"] and px + marijo.size[0] >= globals()[f"mush{i}x"] + mushroom.size[1] and py <= globals()[f"mush{i}y"] and py + marijo.size[1] >= globals()[f"mush{i}y"] + mushroom.size[1]:
            punkti += 1
            scoore(punkti)
            # globals()[f"mush{i}x"] = -1
            # globals()[f"mush{i}y"] = -1
            logs.delete(globals()[f"mush{i}"])
            mushrum(i)
            print(f'just hit mushroom number {i}')
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
