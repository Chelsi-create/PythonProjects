from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("Radiobutton Tutorial")

def order():
    tmsg.showinfo("Amount Received", f"We have received your order for {var.get()}. Thanks for ordering")

#var = IntVar()
var = StringVar()
var.set("Radio")
#var.set(1)
Label(root, text = "What would you like to have sir?", font = "lucida 19 bold", justify = LEFT, padx = 14).pack()
radio = Radiobutton(root, text = "Dosa", padx = 14, font = "lucida 12 bold", variable = var, value = "Dosa").pack(anchor = "w")
radio = Radiobutton(root, text = "Idli", padx = 14, font = "lucida 12 bold", variable = var, value = "Idli").pack(anchor = "w")
radio = Radiobutton(root, text = "Aloo Paratha", padx = 14, font = "lucida 12 bold", variable = var, value = "Aloo Paratha").pack(anchor = "w")
radio = Radiobutton(root, text = "Samosa", padx = 14, font = "lucida 12 bold", variable = var, value = "Samosa").pack(anchor = "w")

Button(root, text = "Order Now", command = order).pack()

root.mainloop()