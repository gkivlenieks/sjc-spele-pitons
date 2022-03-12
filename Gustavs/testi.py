from ast import While
import threading, time

def xx():
    time.sleep(5)
    i = 0
    while True:
        print(f'i: {i}')
        i += 1
x = threading.Thread(target=xx, daemon=False)

x.start()
h = 0
print('yo')
time.sleep(1)
while True:
    print(f'h: {h}')
    h += 1

