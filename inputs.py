from tkinter import *

root = Tk()

e = Entry(root, width=50, bg ="Black", fg = "White", borderwidth=5)
e.pack()
e.insert(0, "Enter your name: ")

def myclick():
    hello = "Hello " + e.get()
    mylabel = Label(root, text=hello)
    mylabel.pack()

myButton = Button(root, text="Enter your name", command=myclick)
myButton.pack()

root.mainloop()