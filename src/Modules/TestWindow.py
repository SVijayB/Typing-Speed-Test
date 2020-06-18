from tkinter import *
import random

window = Tk()
window.title("Test Window")
window.config(bg = "black")
window.geometry("600x400")

colour = ["Red","Blue","Green","Pink","Yellow","Orange","White","Purple","Brown"]
score = 0

current_word = StringVar()
entry_field = Entry(window, textvariable=current_word, font = "Algerian",
    bg = "black", insertbackground = "red", fg='white')

board = Label(window,text="Press enter to start",width=600,height=400,
        font="Algerian 25",fg = "green",bg = "black")
board.pack()

question = Label(window,font = "Algerian",bg = "black")
question.place(x=230,y=50)

time_up_message = Label(window)

score_label = Label(window,text = "Score : 0", font = "Agency",fg = "green", bg = "black")

time = 61

time_label = Label(window)
	
def final_score(score):
    return score
	
def result():
    speed = Label(window,text = "Speed : " + str(round(60/(score))) + "wpm", 
        width = 200, height = 100, fg = "green", font = "Algerian",bg = "back")
    speed.pack()
    time_up_message.forget()
    score_label.forget()
	
def time_decrement():
    global time
    if time>0:
        time = time - 1
        time_label.config(text = "Time Left : " + str(time),font = "Agency", 
            bg = "black", fg = "orange")
        time_label.place(x = 2, y = 2)
        window.after(1000,time_decrement)
    else:
        entry_field.place_forget()
        time_up_message.config(text = "Time's Up", font = "Algerian", bg = "black", 
            fg = "red", width = 600, height = 600)
        time_up_message.pack()
        score_label.place_forget()
        time_label.place_forget()
        window.after(2000,result)

class test():	
    def start(event):
        try:
            board.pack_forget()
            global time
            if (time == 61):
                time_decrement()
            word = random.randint(0,9)
            question.config(text = str("Word"),fg = colour[word])
            entry_field.place(x=120,y=200)
            score_label.place(x=400,y=2)
        
            def correct(event):
                global score
                if (current_word.get() == ("Word").lower()):
                    entry_field.delete(0,END)
                    score = score + 1
                    score_label.config(text = "Score : " + str(score))
                    final_score(score)
                    test.start(event)
                else:
                    entry_field.delete(0,END)
                    test.start(event)
            window.bind("<Return>",correct)
        except:
            pass
    window.bind("<Return>",start)

def closing(): 
    sys.exit(0)

window.protocol("WM_DELETE_WINDOW",closing)
window.mainloop()