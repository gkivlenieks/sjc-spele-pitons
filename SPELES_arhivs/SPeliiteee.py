from calendar import c
from tkinter import *
import random
canvas_width = 900
canvas_height = 900
master = Tk()
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
master.title("Līnijas spēle")


# KOMENTĀRI!!! 
w.pack()
c
x1=300
y1=300
x2=150
y2=250
e=5
f='blue'
teksts=30
g=100
def clicked(event):
    print("pressed")
    e=30
    w.create_image(50,400, image = bilde)

#SPĒLES ELEMENTI (8 krāsu maiņas eleemtni / 5 biezuma maiņas)
b = w.create_line(300, 270, 300, 260, width=10, fill='red')
w.create_line(300, 240, 300, 230, width=10, fill='yellow')
w.create_line(300, 150, 300, 160, width=10, fill='green')
w.create_line(300, 200, 300, 190, width=10, fill='black')
w.create_line(300, 120, 300, 130, width=10, fill='brown')
w.create_line(300, 400, 300, 410, width=10, fill='orange')
bilde = PhotoImage(file="SPELES_arhivs\pika.ppm")
pika = PhotoImage(file="SPELES_arhivs\semene.ppm")
w.create_image(50,400, image = bilde)
player = w.create_image(0,0, image = pika)
w.delete(player)
def punkti():
    global teksts
    buttonBG1 = w.create_rectangle(0, 0, 100, 30, fill="grey40", outline="grey60")
    buttonTXT1 = w.create_text(50, 15, text=teksts)
    if teksts==40:
        teksts="GAME OVER"



def biezums():
    global g
    buttonBG = w.create_rectangle(100, 0, 200, 30, fill="grey40", outline="grey60")
    buttonTXT = w.create_text(150, 15, text= g)
    w.tag_bind(buttonBG, "<Button-1>", clicked) ## when the square is clicked runs function "clicked".
    w.tag_bind(buttonTXT, "<Button-1>", clicked) ## same, but for the text.

punkti()
biezums()
#w variants (uz augsu)
def uzaugsu():
    global x1, y1, x2, y2, e, f, c, player
    w.delete(player)
    x2=x1+0
    y2=y1-10
    c = w.create_line(x1, y1, x2, y2, width=e, fill=f )
    player =w.create_image(x2,y2, image = pika)
    x1=x2
    y1=y2
    print(x1)
    print(y1)
#d variants (pa labi)
def palabi():
    global x1, y1, x2, y2, e, f, c, player
    w.delete(c)
    w.delete(player)
    x2=x1+10
    y2=y1+0
    w.create_line(x1, y1, x2, y2, width=e, fill=f )
    player = w.create_image(x2,y2, image = pika)
    x1=x2
    y1=y2
    print(x1)
    print(y1)
#a variants (pa kreisi)
def pakreisi():
    global x1, y1, x2, y2, e, f, player
    x2=x1-10
    y2=y1+0
    w.delete(player)
    w.create_line(x1, y1, x2, y2, width=e, fill=f )
    player = w.create_image(x2,y2, image = pika)
    x1=x2
    y1=y2
    print(x1)
    print(y1)
#s variants (uz leju)
def uzleju():
    global x1, y1, x2, y2, e, f, player
    x2=x1+0
    y2=y1+10
    w.delete(player)
    w.create_line(x1, y1, x2, y2, width=e, fill=f )
    player = w.create_image(x2,y2, image = pika)
    x1=x2
    y1=y2
    print(x1)
    print(y1)

def salidzinam():
    global x2,y2, e, f, teksts
    print(x2)
    print(y2)
    if (x2==300 and y2==260):
        e=20
        print('palielinam')  
        teksts = teksts -5 
        punkti()
    if (x2==300 and y2==240):
        f='black'
        print('krasojam')
        teksts = teksts + 5
        punkti()
    if (x2==300 and y2==190):
        #if ( 30 < x2 < 100 and y2=21220 ) >>> dzīvības -1 
        if f=='black':
            e=e+15
            teksts = teksts + 10
            punkti()
        else: 
            e=e    
    print('lielaks ar krasu')


while g>0:
    k = input('virziens')
    if k=='w':
        uzaugsu()
        salidzinam()
        punkti()
        g=g-1
        biezums()
    if g==0:
        break    
    if k =='s':
        uzleju()
        punkti()
        g=g-1
    if g==0:
        break 
    if k =='a':
        pakreisi()
        punkti()
        w.delete(b)
        g=g-1
    if g==0:
        break 
    if k =='d':
        palabi()    
        g=g-1
    if g==0:
        break 






mainloop()