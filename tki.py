from tkinter import *

root = Tk()

#creating a lable widget
mylabel1 = Label(root, text="Hello world!")
mylabel2 = Label(root, text="My name is Caroline Wanjiku!")
#shoving it in the screen

mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=1)


root.mainloop() 