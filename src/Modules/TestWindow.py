import sys
from tkinter import *

class TestWindow:
    def __init__(self,window,choice):
        self.window = window
        self.window.state("zoomed")
        self.window.grid_rowconfigure(0,weight=0)
        self.window.grid_columnconfigure(0,weight=1)
        self.choice = choice
        self.window.title("Test Window")
        self.window.config(bg = "black")
        self.colour = ["Red","Blue","Green","Pink","Yellow","Orange","White","Purple","Brown"]
        self.score = 0

        self.current_word = StringVar()
        self.entry_field = Entry(window,textvariable=current_word ,
        font = "Algerian", bg = "black", insertbackground = "red")
        self.entry_field.focus()

        self.board = Label(window,text="Press enter to start",width=600,height=400,
        font="Algerian",fg = "green",bg = "black")
        self.board.grid(pady = (0,10))

        self.question = Label(window,font = "Algerian",bg = "black")
        self.question.grid(pady = (0,10))

        self.time_up_message = Label(window)

        self.score = Label(window,text = "Score : 0", font = "Agency",fg = "green", bg = "black")

        self.time = 61

        self.time_label = Label(window)

        window.protocol("WM_DELETE_WINDOW",self.closing)

    def closing(self):
        sys.exit(0)