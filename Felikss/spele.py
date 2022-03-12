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
#mainīgie par kustību!!!!
x = 10
y = 10
a = 100
b = 100
direction = None

#def clicked(event):
#    print("pressed")
#    e=30
#    w.create_image(50,400, image = bilde)

#SPĒLES ELEMENTI (8 krāsu maiņas eleemtni / 5 biezuma maiņas)
#b = w.create_line(300, 270, 300, 260, width=10, fill='red')
#w.create_line(300, 240, 300, 230, width=10, fill='yellow')
#w.create_line(300, 150, 300, 160, width=10, fill='green')
#w.create_line(300, 200, 300, 190, width=10, fill='black')
#w.create_line(300, 120, 300, 130, width=10, fill='brown')
#w.create_line(300, 400, 300, 410, width=10, fill='orange')
bilde = PhotoImage(file="SPELES_arhivs\semene.ppm")
pika = PhotoImage(file="SPELES_arhivs\pika.ppm")
#w.create_image(50,400, image = bilde)
player = w.create_image(0,0, image = pika)
w.delete(player)




#def biezums():
#    global g
#    buttonBG = w.create_rectangle(100, 0, 200, 30, fill="grey40", outline="grey60")
#    buttonTXT = w.create_text(150, 15, text= g)
#    w.tag_bind(buttonBG, "<Button-1>", clicked) ## when the square is clicked runs function "clicked".
#    w.tag_bind(buttonTXT, "<Button-1>", clicked) ## same, but for the text.


#iezums()

player =w.create_image(x2,y2, image = pika)

# KUSTĪBU KOORDINĀCIJ!!!!
def move():
    global x_vel
    global y_vel
    global direction
    if direction is not None:
        w.move(player, x_vel,y_vel)
        punkti()
        #after(33,move)

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
    koordinates = w.coords(player)
    print(koordinates)

def on_keyrelease(event):
    global direction
    direction = None

def punkti():
    px = w.coords(player)
    pxx = px[0]
    pxy = px[1]
    ob = random.randrange(50,600)
    oy = random.randrange(50,600)
    print(ob, oy)
    w.create_image(ob,oy, image = bilde)
    if pxx == ob and oy == 250:
        print("uzvara")
        w.create_image(ob,oy, image = bilde)
    if pxx == 300 and pxy == 300:
        w.create_image(200,300, image = bilde)
  # ja spēlētāja koordinātes (pxx un pxy) ir kaut kas - tad varam kaut ko izdarīt...
    



#objekti = w.find_all()
#print(objekti)
#for objekti in objekti:
#    print(w.coords(objekti))
#px = w.coords(player)
#pxx = px[0]
#pxy = px[1]
#print(pxx)
#print(pxy)

master.bind_all('<KeyPress>', on_keypress)
master.bind_all('<KeyRelease>', on_keyrelease)
master.mainloop()