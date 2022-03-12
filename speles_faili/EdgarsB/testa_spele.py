from calendar import c
from tkinter import *
import random

from numpy import true_divide
canvas_width = 900
canvas_height = 900
master = Tk()

#mainīgie - kas svarīgi

direction = None

rezultats = 0

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

# SĒNES 
sene = PhotoImage(file="speles_faili\EdgarsB\semene.ppm") 

# UZTAISĪT sēnes (mainot masīva izmēru var veidot vairāk sēnes)!!!!
xkoordinates = []
ykoordinates = []
senesst = []
senes = []

for i in range(10):
    xkoordinates.append(random.randrange(100, 800, 150))
    ykoordinates.append(random.randrange(100, 800, 150))
    senesst.append(0)  
    senes.append(i)

for i in range(10):
    senes[i] = logs.create_image(xkoordinates[i], ykoordinates[i], image=sene)
    

print(senesst)
print(senes)
print(xkoordinates)
print(ykoordinates)


#print(sx1, sy1, sx2, sy2)

#punktu skaitīšana....
def punkti():
    # global sx1, sy1, sx2, sy2, sx3, sy3, rezultats, sene1status, sene2status, sene3status
    global rezultats, senesst, senes, xkoordinates, ykoordinates
    
    px = logs.coords(player)
    pxx = int(px[0])
    pxy = int(px[1])
    #print(pxx, pxy, sx1, sy1 )
    # pirmā sēne noķerta... 
    # print(rezultats)
    rezultatutablo()

    for i in range(10):
        if (xkoordinates[i]-30)<pxx<(xkoordinates[i]+30) and (ykoordinates[i]-30)<pxy<(ykoordinates[i]+30) and senesst[i]==0:
            logs.delete(senes[i])
            print(i)
            print(px)
            rezultats = rezultats +1
            senesst[i]= senesst[i] + 1
            print(rezultats)


 #   if pxx==sx1 and pxy==sy1 and sene1status==0:
 #       logs.delete(sene1)
 #       print("seeeneee 1")
 #       rezultats = rezultats +1
 #       sene1status = sene1status + 1
        
 #   if pxx==sx2 and pxy==sy2:
 #       logs.delete(sene2)
 #       print("seeeneee 2")
 #       rezultats = rezultats +1
    
 #   if pxx==sx3 and pxy==sy3:
 #       logs.delete(sene3)
 #       print("seeeneee 3")
 #       rezultats = rezultats +1
    
    if rezultats == 5 :
        uzvarteksts = logs.create_text(450, 450,  font=(None, 50), text="SPēle uzvarēta!!!!")
        
# REZULTATU TABLO

def rezultatutablo():
    buttonBG = logs.create_rectangle(100, 0, 200, 30, fill="red", outline="grey60")
    buttonTXT = logs.create_text(150, 15,  font=(None, 25), text=rezultats)



#KUSTĪBA _ staigājam apkārt...
player = logs.create_image(250,250, image = sarkG)
# vilks = .... (333???)
def move():
    global x_vel
    global y_vel
    global direction
    if direction is not None:
        logs.move(player, x_vel,y_vel)
        punkti()
        #kustināt vilku... 
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
    #print(koordinates)

def on_keyrelease(event):
    global direction
    direction = None







#Master mainloops - izmaiņas un notikumi
master.bind_all('<KeyPress>', on_keypress)
master.bind_all('<KeyRelease>', on_keyrelease)
master.mainloop()