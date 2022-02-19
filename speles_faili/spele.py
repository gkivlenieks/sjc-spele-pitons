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
x = 10
y = 10
a = 100
b = 100
direction = None
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
bilde = PhotoImage(file="sjc-spele-pitons\SPELES_arhivs\semene.ppm")
pika = PhotoImage(file="sjc-spele-pitons\SPELES_arhivs\pika.ppm")
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

player =w.create_image(x2,y2, image = pika)

def move():
    global x_vel
    global y_vel
    global direction
    if direction is not None:
        w.move(player, x_vel,y_vel)
        after(33,move)

def on_keypress(event):
    global direction
    global x_vel
    global y_vel
    if event.keysym == "Left":
        direction = "left"
        x_vel = -5
        y_vel = 0
    if event.keysym == "Right":
        direction = "right"
        x_vel = 5
        y_vel = 0
    if event.keysym == "Down":
        direction = "down"
        x_vel = 0
        y_vel = 5
    if event.keysym == "Up":
        direction = "up"
        x_vel = 0
        y_vel = -5
    
    move()

def on_keyrelease(event):
    global direction
    direction = None

master.bind_all('<KeyPress>', on_keypress)
master.bind_all('<KeyRelease>', on_keyrelease)
master.mainloop()
