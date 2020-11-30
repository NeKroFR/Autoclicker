'''
Created by NeKro
'''


#import
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


#init
delay = float(input("delay :"))
printdelay = str(delay)
print("\ndelay = " + printdelay)

click = Button.left
activate = KeyCode(char='²')
