from tkinter import *

def chelsi(event):
    print(f"You clicked on the button at {event.x}, {event.y}")

root = Tk()

root.title("Tkinter Events")
root.geometry("644x334")

widget = Button(root, text = 'Click me Please')
widget.pack()

widget.bind('<Button-1>', chelsi)
widget.bind('<Double-1>', quit)

root.mainloop()
