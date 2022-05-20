# Author: Tristan Brigham (TristanB22) 

# this script is meant to move the mouse every few seconds to keep the screen
# on while other scripts are being run
import pyautogui
import time

while True:
    pyautogui.moveTo(0, 0, 1)
    time.sleep(5)
    pyautogui.moveTo(10, 10, 1)
    time.sleep(5)
