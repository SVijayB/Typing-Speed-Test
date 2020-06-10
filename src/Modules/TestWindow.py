import sys
from tkinter import *
import random

class TestWindow():
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

        self.score_label = Label(window,text = "Score : 0", font = "Agency",fg = "green", bg = "black")

        self.time = 61

        self.time_label = Label(window)

    def re(event):
        self.score = 0
        self.time = 20
        start(event)
	
    def final_score(self,score):
    	return self.score
	
    def result(self):
        self.speed = Label(window,text = "Speed : " + str(round(60/(score))) + "wpm", 
        width = 200, height = 100, fg = "green", font = "Algerian",bg = "back")
        self.speed.grid()
        self.time_up_message.grid_forget()
        self.score_label.grid_forget()
	
    def time_decrement(self):
        if(self.time>0):
            self.time = self.time - 1
            self.time_label.config(text = "Time Left : " + str(time),font = "Agency", 
            bg = "black", fg = "orange")
            self.time_label.place(x = 2, y = 2)
            self.window.after(1000,time)
        else:
            self.entry_field.place_forget()
            self.time_up_message.config(text = "Time's Up", font = "Algerian", bg = "black", 
            fg = "red", width = 600, height = 600)
            self.time_up_message.grid()
            self.score_label.place_forget()
            self.time_label.place_forget()
            window.after(2000,result)
	
    def start(self,event):
        try:
            self.board.pack_forget()
            if (self.time == 61):
                time_decrement()
            self.word = random.randint(0,9)
            self.question.config(text = str("Word"),fg = self.colour[self.word])
            self.entry_field.place(pady = (0,10))
            self.score_label.place(pady = (0,10))
	
            def correct(self,event):
                if (self.current_word.get() == ("Word").lower()):
                    self.entry_field.delete(0,END)
                    self.score = self.score + 1
                    self.score_label.config(text = "Score : " + str(self.score))
                    self.final_score(score)
                    start(event)
                else:
                    self.entry_field.delete(0,END)
                    start(event)
            window.bind("<Return>",correct)
        except:
            pass
    window.bind("<Return>",start)

    def closing(self):
        sys.exit(0)

    window.protocol("WM_DELETE_WINDOW",closing)