from tkinter import * #import Tkinter for GUI App
from tkinter.ttk import Combobox



#Functions
def printOne(self):
    return print("This is the number one")

#Tkinter Variables
diagwindow = Tk()
var = StringVar()
var.set("one")
data = ["one", "two", "three", "four"]
btn = Button(diagwindow, text = "This is a button widget", fg = 'blue')
lbl = Label(diagwindow, text = "Diskspace Available:", fg = 'black' )
txtfld = Entry(diagwindow, text = "Entry Widget", bg = 'white', fg = 'black', bd = 5)
cb = Combobox(diagwindow, values = data)
lb = Listbox(diagwindow, height = 5, selectmode = 'multiple')



#For loop to insert data from (data) into Listbox
for num in data:
    lb.insert(END, num)


#Placement of widgets
btn.place(x = 80, y = 30)
lbl.place(x = 80, y = 70)
txtfld.place(x = 80, y = 110)
cb.place(x = 80, y = 150)
lb.place(x = 350, y = 110)

#binds to run functions on eventPress
#btn.bind('<Button-1>', printOne )


#Build Tkinter Window
diagwindow.title("RPi System Diag")
diagwindow.geometry("600x400+10+20")
diagwindow.mainloop()