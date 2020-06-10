from tkinter import *

class TestWindow():
    def __init__(self,root,choice):
        self.root = root
        self.root.state("zoomed")
        self.root.grid_rowconfigure(0,weight=0)
        self.root.grid_columnconfigure(0,weight=1)
        self.root.configure(bg="black")
        self.root.title("Test Window")
        self.choice = choice
        
        self.colour = ["Red","Blue","Green","Pink","Yellow","Orange","White","Purple","Brown"]
        self.score = 0

        self.type = StringVar()
        self.entry_field = Entry(root,textvariable=type,
        font = "Algerian", bg = "black", insertbackground = "red")
        self.entry_field.focus()
        self.entry_field.place()

        self.board = Label(root,text="Press enter to start",width=600,height=400,
        font="Algerian",fg = "green",bg = "black")
        self.board.grid(pady = (0,10))

        self.question = Label(root,font = "Algerian",bg = "black")
        self.question.grid(pady = (0,10))

        self.time_up_message = Label(root)

        self.score_label = Label(root,text = "Score : 0", font = "Agency",fg = "green", bg = "black")

        self.time = 61

        self.time_label = Label(root)

    def re(self,event):
        self.score = 0
        self.time = 20
        start(event)
	
    def final_score(self,score):
    	return self.score

    def result(self):
        self.speed = Label(root,text = "Speed : " + str(round(60/(score))) + "wpm", 
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
            self.root.after(1000,time)
        else:
            self.entry_field.place_forget()
            self.time_up_message.config(text = "Time's Up", font = "Algerian", bg = "black", 
            fg = "red", width = 600, height = 600)
            self.time_up_message.grid()
            self.score_label.place_forget()
            self.time_label.place_forget()
            root.after(2000,result)

    
