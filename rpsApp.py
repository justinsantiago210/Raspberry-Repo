from tkinter import *

class rpsApp:
    def __init__(self, win):
        #Create Widgets
        self.rockbtn = Button(win, text = "Rock")
        self.paperbtn = Button(win, text = "Paper")
        self.scissorbtn = Button(win, text = "scissors")
        self.emptylbl = Label(win, text = "Test Text")
        #Place Widgets
        self.rockbtn.place(x = 100, y = 100)
        self.paperbtn.place(x = 100, y = 130)
        self.scissorbtn.place(x = 100, y = 160)
        self.emptylbl.place(x = 100, y = 190)
        #Bind Widgets
        self.rockbtn.bind()#('<Button-1>, self.class')
        #Functions
        def playRock(rockbtn):
#Initialize Tkinter
win = Tk()
myWindow = rpsApp(win)
win.title("Rock, Paper, Scisors!")
win.geometry("500x500+10+10")
win.mainloop()
