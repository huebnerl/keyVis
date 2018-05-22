from gui import KeyDisplay
from keyMap import *

import time
import pyHook

class KeyListener:
    
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

        self.hm = pyHook.HookManager()
        self.hm.KeyDown = self.on_keyboard_event
        self.hm.HookKeyboard()
        print("[Programm is listening.]")

        self.key_display = KeyDisplay()
        self.key_display.start()

    def on_keyboard_event(self, event):
        print("[ Key pressed: " + event.Key + " ]")
        self.update_time()

        shown_key = event.Key
        if shown_key in key_map:
            shown_key = key_map[shown_key]
        
        if (self.t1 - self.t2) > 500:
            self.key_display.print(shown_key)
        else:
            self.key_display.append(shown_key)
        return True

    def update_time(self):
        self.t2 = self.t1
        self.t1 = int(round(time.time() * 1000))

