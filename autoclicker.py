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


while True:
    if click == 1:
        mouse.press(button)
        mouse.release(button)
        time.sleep(delay)
    else :
        pass
