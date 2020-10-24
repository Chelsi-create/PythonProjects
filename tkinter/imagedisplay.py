from tkinter import *
from PIL import Image, ImageTk

x_root = Tk()
x_root.geometry("455x244")

#photo = PhotoImage(file = "D:\JS\Images\a.jpg")

#For jpg images
image = Image.open("D:\JS\Images\a.jpg")
photo = ImageTk.PhotoImage(image)


image_label = Label(image=photo)
image_label.pack()

x_root.mainloop()
