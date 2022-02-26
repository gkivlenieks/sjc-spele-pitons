from calendar import c
from tkinter import *
import random
canvas_width = 900
canvas_height = 900
master = Tk()

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

#Fona attēla iestatīšana... (svarīgs izmērs - der PNG)
fons = PhotoImage(file="speles_faili\EdgarsB\mezs_sss.png")
logs.create_image(0,0, image=fons)



#Master mainloops - izmaiņas un notikumi
master.mainloop()