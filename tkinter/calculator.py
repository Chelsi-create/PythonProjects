from tkinter import *

def click(event):
    global scvalue
    #We use cget function to retrieve text from a buttom widget
    text = event.widget.cget("text")
    
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        
        scvalue.set(value)
        screen.update()
    
    elif text == "C":
        scvalue.set(" ")
        screen.get()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()

root.geometry("460x710")
root.title("Calculator By Chelsi Jain")
root.wm_iconbitmap("2.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable = scvalue, font = "lucida 40 bold")
screen.pack(fill = X, ipadx = 8, padx = 10, pady = 10)

f = Frame(root, bg = "black")
b = Button(f, text = "9", padx = 28, pady = 18, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "8", padx = 28, pady = 18, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "7", padx = 28, pady = 18, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg = "black")
b = Button(f, text = "6", padx = 28, pady = 18, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "5", padx = 28, pady = 18, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "4", padx = 28, pady = 18, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg = "black")
b = Button(f, text = "3", padx = 28, pady = 18, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "2", padx = 28, pady = 18, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "1", padx = 28, pady = 18, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg = "black")
b = Button(f, text = "0", padx = 30, pady = 18, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "-", padx = 30, pady = 18, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "*", padx = 30, pady = 18, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg = "black")
b = Button(f, text = "/", padx = 33, pady = 18, font = "lucida 23 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "%", padx = 28, pady = 18, font = "lucida 19 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "=", padx = 28, pady = 18, font = "lucida 19 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg = "black")
b = Button(f, text = "C", padx = 28, pady = 18, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "+", padx = 28, pady = 18, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = ".", padx = 28, pady = 18, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 11, pady = 5)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()