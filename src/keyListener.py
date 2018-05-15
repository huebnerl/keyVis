from gui import KeyDisplay

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
        self.key_display.print(event.Key)
        return True

