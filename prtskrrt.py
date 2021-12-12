import time
import random
from typing import KeysView
from pynput.keyboard import Key, Controller

keyboard = Controller()

a = input("strt (Y/N)")
if a == "Y":
    time.sleep(1)
    for i in range(999):
        keyboard.type("&prntsc")
        keyboard.press(Key.enter)
        time.sleep(11)
else:
    print("bruv")
    quit()
