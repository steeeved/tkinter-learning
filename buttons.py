from tkinter import *

root = Tk()

def myclick():
    mylabel = Label(root, text="Look! I clicked a button")
    mylabel.pack()

myButton = Button(root, text="Click me!", padx=10, pady=10, command=myclick, fg="Blue", bg="red")
myButton.pack()

root.mainloop()