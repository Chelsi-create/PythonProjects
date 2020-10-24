from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("733x566")
root.title("PyCharm")

def myfunc():
    print("Function is working")
    

def help():
    print("I will help you")
    a = tmsg.showinfo("Help", "Chelsi will help you with this GUI")
    print(a)

def rate():
    print("Rate Us")
    value = tmsg.askquestion("Was your experience Good?", "You user this GUI...Was your experience Good?")
    print(value)
    if value == "yes":
        msg = "Great. Rate Us on appstore please"
    else:
        msg = "Tell us what went wrong. We will call you soon"
    tmsg.showinfo("Experience",msg)

mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff = 0)
m1.add_command(label = "New Project", command = myfunc)
m1.add_command(label = "Save", command = myfunc)
m1.add_separator()
m1.add_command(label = "Save As", command = myfunc)
m1.add_command(label = "Print", command = myfunc)
mainmenu.add_cascade(label = "File",menu = m1)

root.config(menu = mainmenu)

m2 = Menu(mainmenu, tearoff = 0)
m2.add_command(label = "Cut", command = myfunc)
m2.add_command(label = "Copy", command = myfunc)
m2.add_command(label = "Paste", command = myfunc)
m2.add_separator()
m2.add_command(label = "Undo", command = myfunc)
mainmenu.add_cascade(label = "Edit",menu = m2)
root.config(menu = mainmenu)

m3 = Menu(mainmenu, tearoff = 0)
m3.add_command(label = "Help", command = help)
m3.add_command(label = "Rate Us", command = rate)

mainmenu.add_cascade(label = "Help",menu = m3)
root.config(menu = mainmenu)

root.mainloop()