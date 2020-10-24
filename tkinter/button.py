from tkinter import *

root = Tk()

root.geometry("655x333")

def hello():
    print("Hello Tkinter buttons")

def name():
    print("My Name is Chelsi Jain")

frame = Frame(root, borderwidth = 6, bg = "grey", relief = SUNKEN)
frame.pack(side = LEFT, anchor = "nw")


b1 = Button(frame, fg = "red", text = "print now",command = hello)
b1.pack(side = LEFT,padx = 23)

b2 = Button(frame, fg = "red", text = "Tell me your name now",command = name)
b2.pack(side = LEFT,padx = 23)

b3 = Button(frame, fg = "red", text = "print now")
b3.pack(side = LEFT,padx = 23)

b4 = Button(frame, fg = "red", text = "print now")
b4.pack(side = LEFT,padx = 23)

root.mainloop()