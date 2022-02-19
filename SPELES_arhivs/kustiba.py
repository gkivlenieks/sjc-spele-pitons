from tkinter import *

x = 10
y = 10
a = 100
b = 100
direction = None

def move():
    global x_vel
    global y_vel
    global direction
    if direction is not None:
        canvas1.move(rect, x_vel,y_vel)
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


window = Tk()
window.geometry("400x200")

#canvas and drawing
canvas1=Canvas(window, height = 200, width = 400)
canvas1.grid(row=0, column=0, sticky=W)
coord = [x, y, a, b]
rect = canvas1.create_rectangle(*coord, outline="#fb0", fill="#fb0")

#capturing keyboard inputs and assigning to function
window.bind_all('<KeyPress>', on_keypress)
window.bind_all('<KeyRelease>', on_keyrelease)
window.mainloop()