import random

print("heeelooo")

senumasivs = [0,5]

xkoordinates = []
ykoordinates = []
senes =[0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    xkoordinates.append(random.randrange(100, 800, 150))
    ykoordinates.append(random.randrange(100, 800, 150))
    

for i in range(10):
senes[i] = logs.create_image(xkoordinates[i], ykoordinates[i], image=sene)

print(senes)
print(xkoordinates)
print(ykoordinates)

