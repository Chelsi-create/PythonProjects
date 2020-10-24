from tkinter import *
import messagebox
import tkinter

top = tkinter.Tk()

def p_h():
    print("Hello")
mb = Menubutton(top, text = "condiments", )
mb.grid()
mb.menu = Menu(mb, tearoff = 0)
mb["menu"] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton(label = "mayo", variable = mayoVar, command = p_h)
mb.menu.add_checkbutton(label = "ketchup", variable = ketchVar, command = p_h)

top.mainloop()