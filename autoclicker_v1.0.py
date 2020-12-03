'''
Created by NeKro
'''

#import
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

#init
delay = float(input("delay(s) :"))
print("\ndelay = " + str(delay))

button = Button.left
mouse = Controller()
click = int(0)

while True:
    mouse.press(button)
    mouse.release(button)
    time.sleep(delay)