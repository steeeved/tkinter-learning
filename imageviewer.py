from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap('download.ico')

my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/Steve/Documents/code/Python/learn/tkinter/img/carol(17).png"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/Steve/Documents/code/Python/learn/tkinter/img/carol(18).png"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/Steve/Documents/code/Python/learn/tkinter/img/carol(19).png"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/Steve/Documents/code/Python/learn/tkinter/img/carol(20).png"))
my_img5 = ImageTk.PhotoImage(Image.open("C:/Users/Steve/Documents/code/Python/learn/tkinter/img/carol(21).png"))
my_img6 = ImageTk.PhotoImage(Image.open("C:/Users/Steve/Documents/code/Python/learn/tkinter/img/carol(22).png"))
my_img7 = ImageTk.PhotoImage(Image.open("C:/Users/Steve/Documents/code/Python/learn/tkinter/img/carol(23).png"))
my_img8 = ImageTk.PhotoImage(Image.open("C:/Users/Steve/Documents/code/Python/learn/tkinter/img/carol(24).png"))
my_img9 = ImageTk.PhotoImage(Image.open("C:/Users/Steve/Documents/code/Python/learn/tkinter/img/carol(25).png"))
my_img10 = ImageTk.PhotoImage(Image.open("C:/Users/Steve/Documents/code/Python/learn/tkinter/img/carol(26).png"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5,my_img6,my_img7,my_img8,my_img9,my_img10]

status = Label(root, text="Image 1 of "+ str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image = my_img1)
my_label.grid(row=2, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back


    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root,text=">>", comman=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    my_label.grid(row=2, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    if image_number == 10:
        button_forward = Button(root, text=">>", state=DISABLED)
        button_forward.grid(row=1,column=2)

    status = Label(root, text="Image " +str(image_number)+ " of "+ str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=0, column=0, columnspan=3, sticky=W+E)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root,text=">>", comman=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    my_label.grid(row=2, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    status = Label(root, text="Image " +str(image_number)+ " of "+ str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=0, column=0, columnspan=3, sticky=W+E)
    
button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="Exit program", command=root.quit)
button_forward = Button(root, text=">>", comman=lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)
status.grid(row=0, column=0, columnspan=3, sticky=W+E)

root.mainloop() 