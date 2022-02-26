from calendar import c
from tkinter import *
import random
canvas_width = 900
canvas_height = 900
master = Tk()

#mainīgie - kas svarīgi

direction = None



#Izveidojam spelēs laukumu!!! neaizmirstam komandu .pack()
logs = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
master.title("Līnijas spēle")
logs.pack()

#Izveidojam spēlētāju (bilde)
sarkG = PhotoImage(file="speles_faili\EdgarsB\sark_videja.ppm")
#logs.create_image(250,250, image= sarkG)
player = logs.create_image(250,250, image = sarkG)
logs.delete(player)

#Fona attēla iestatīšana... (svarīgs izmērs - der PNG)
fons = PhotoImage(file="speles_faili\EdgarsB\mezs_sss.png")
logs.create_image(0,0, image=fons)

#KUSTĪBA _ staigājam apkārt...
player = logs.create_image(250,250, image = sarkG)
def move():
    global x_vel
    global y_vel
    global direction
    if direction is not None:
        logs.move(player, x_vel,y_vel)
        #punkti()
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
    koordinates = logs.coords(player)
    print(koordinates)

def on_keyrelease(event):
    global direction
    direction = None




#Master mainloops - izmaiņas un notikumi
master.bind_all('<KeyPress>', on_keypress)
master.bind_all('<KeyRelease>', on_keyrelease)
master.mainloop()