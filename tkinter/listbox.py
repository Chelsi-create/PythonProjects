from tkinter import *

# ACTIVE means jo bhi select kiya hai uske baad add hoga

i = 0
def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1

root  =Tk()
root.geometry("455x233")
root.title("Tkinter Listbox Tutorial")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item of a listbox")

Button(root, text = "Add Item", command = add).pack()

root.mainloop()