from tkinter import *

root = Tk()
root.geometry("744x433")
root.title("Code with Chelsi - Title of my GUI")
root.wm_iconbitmap("1.ico")

root.configure(background = "grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f"{width}x{height}")
Button(text = "Close", command = root.destroy).pack()


root.mainloop()
