from tkinter import *
root = Tk()

root.geometry("655x333")
f1 = Frame(root,bg = "grey",borderwidth = 6,relief = SUNKEN)
f1.pack(side = LEFT,fill = "y")

f2 = Frame(root,borderwidth = 8,bg = "grey",relief = SUNKEN)
f2.pack(side = TOP,fill = X)

# Label is a widget that user just views but not interact with
l = Label(f1,text = "Project Tkinter - PyCharm")
l.pack(pady = 42)

l = Label(f2,text = "Welcome to sublime text")
l.pack()
root.mainloop()