from tkinter import *

root = Tk()
root.geometry("344x233")
root.title("GUI window by user input")

def update():
    print("Updating the GUI")
    root.geometry(f"{widthentry.get()}x{heightentry.get()}")

width = Label(root, text = "Width")
height = Label(root, text = "Height")
width.grid(row = 1, column = 2)
height.grid(row = 2, column = 2)




width = StringVar()
height = StringVar()

widthentry = Entry(root, textvariable = width)
heightentry = Entry(root, textvariable = height)
widthentry.grid(row = 1, column = 3)
heightentry.grid(row = 2, column = 3)
Button(root, text = "Apply", command = update).pack()


root.mainloop()