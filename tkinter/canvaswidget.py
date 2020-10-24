from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Chelsi's GUI")
can_widget = Canvas(root, width = canvas_width, height = canvas_height)
can_widget.pack()

# The line goes from the point x1, y1 to x2, y2
can_widget.create_line(0,50,10000,50, fill = "dark blue")
can_widget.create_line(0,50,10000,50, fill = "dark blue")

#Creating a rectangle and specifying parameters in this order
can_widget.create_rectangle(2, 2, 800, 400)

# Writing text
can_widget.create_text(200, 200, text = "python")

# Creating an oval
can_widget.create_oval(344,233,244,355)
# Creating a circle
can_widget.create_oval(344,344,355,355)

root.mainloop()