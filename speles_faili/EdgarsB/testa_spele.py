from calendar import c
from tkinter import *
import random
canvas_width = 600
canvas_height = 600
master = Tk()


logs = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
master.title("Līnijas spēle")
logs.pack()


sarkG = PhotoImage(file="speles_faili\EdgarsB\sark_maza.ppm")
#logs.create_image(250,250, image= sarkG)

player = logs.create_image(250,250, image = sarkG)

master.mainloop()