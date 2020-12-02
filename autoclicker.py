'''
Created by NeKro
'''

#import
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

#init
delay = float(input("delay(s) :"))
printdelay = str(delay)
print("\ndelay = " + printdelay)

button = Button.left
mouse = Controller()
click = int(0)
start = int(1)

while True:
    if start == 0:
        if click == 1:
            click = 0
            print(str(click))
        if click == 0:
            pass

    elif start == 1:
        if click == 1:
            pass
        if click == 0:
            click = 1
            print(str(click))
        
    elif click == 1:
        mouse.press(button)
        mouse.release(button)
        time.sleep(delay)
    
    else :
        pass
