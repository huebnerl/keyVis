from gui import KeyDisplay
from keyMap import key_map

import pyHook

class KeyListener:
    
    def __init__(self):
        self.key_display = KeyDisplay()

        self.hm = pyHook.HookManager()
        self.hm.KeyDown = self.on_keyboard_event
        self.hm.HookKeyboard()
        print("[Programm is listening.]")

        self.key_display.start()

    def on_keyboard_event(self, event):
        print("[ Key pressed: " + event.Key + " ]")
        
        shown_key = event.Key
        if shown_key in key_map:
            shown_key = key_map[shown_key]

        self.key_display.print(shown_key)
        return True

