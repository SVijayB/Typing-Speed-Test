from tkinter import *
from tkinter import ttk
import time
from Modules.SelectionPage import SelectionPage

class SecondPage:
    def __init__(self,window,choice):
        self.window = window
        self.window.state("zoomed")
        self.window.grid_rowconfigure(0,weight=0)
        self.window.grid_columnconfigure(0,weight=1)
        self.choice = choice

        window.protocol("WM_DELETE_WINDOW",self.closing)

    def closing(self):
        sys.exit(0)

if __name__ == "__main__":
    window = Tk()
    window.state("zoomed")
    app = SelectionPage(window)
    window.mainloop()