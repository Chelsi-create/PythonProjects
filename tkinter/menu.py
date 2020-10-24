from tkinter import *

root = Tk()
root.geometry("733x566")
root.title("PyCharm")

def myfunc():
    print("Function is working")

# Creating a widget - mymenu is a widget
#Use these to create on drop down  menu
mymenu = Menu(root)
mymenu.add_command(label = "File",command = myfunc)
mymenu.add_command(label = "Exit",command = quit)

root.config(menu = mymenu)

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

root.mainloop()