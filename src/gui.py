import tkinter as tk
import time


class KeyDisplay:

    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(self.root, font=("Helvetica", 100, "bold"),  fg="grey", bg='white')

        self.root.config(background='white')
        self.root.overrideredirect(True)
        self.root.geometry("%dx%d+%d+%d" % (self.root.winfo_screenwidth(),
            self.root.winfo_screenheight(), 0, 0))
        self.root.lift()
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-disabled", True)
        self.root.wm_attributes("-transparentcolor", "white")
        self.label.place(rely=1.0, relx=1.0, x=-10, y=-20, anchor='se')

    def start(self):
        self.root.mainloop()

    def print(self, print_text):
        self.label.config(width=len(print_text))
        self.label.config(text=print_text)
        self.label.update()

    def append(self, append_text):
        width = self.label.cget("width") + len(append_text)
        self.label.config(width = width)

        text = self.label.cget("text") + append_text
        self.label.config(text=text)

        self.label.update()
        
    def __del__(self):
        self.root.destroy()
