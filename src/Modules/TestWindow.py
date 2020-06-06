import sys

class TestWindow:
    def __init__(self,window,choice):
        self.window = window
        self.window.state("zoomed")
        self.window.grid_rowconfigure(0,weight=0)
        self.window.grid_columnconfigure(0,weight=1)
        self.choice = choice
        self.window.title("Test Window")

        window.protocol("WM_DELETE_WINDOW",self.closing)

    def closing(self):
        sys.exit(0)