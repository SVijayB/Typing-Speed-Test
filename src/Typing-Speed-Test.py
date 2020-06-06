from tkinter import *
from Modules.SelectionWindow import SelectionWindow

if __name__ == "__main__":
    window = Tk()
    window.state("zoomed")
    app = SelectionWindow(window)
    window.mainloop()