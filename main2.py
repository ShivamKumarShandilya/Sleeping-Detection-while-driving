from tkinter import *
from main import drive

root = Tk()
root.geometry("800x450")
root.wm_iconbitmap("1.ico")
root.title('Sleeping Detection')
root.minsize(700, 437)
root.maxsize(700, 437)
bg = PhotoImage(file="ko.png")

# image show kara raha hai using label
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

# Create Frame
frame1 = Frame(root)
frame1.grid()
button_1 = PhotoImage(file='ll.png')
label_1 = Label(image=button_1)
b1 = Button(root, image=button_1, command=drive, borderwidth=0, bg="#010431", activebackground='#010431')
b1.place(x=322,y=110)


root.mainloop()