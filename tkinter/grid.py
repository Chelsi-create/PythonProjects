from tkinter import *
def getval():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")


root = Tk()
root.geometry("655x333")

user = Label(root,text = "UserName")
password = Label(root,text = "Password")
user.grid()
password.grid(row = 1)

# variable classes in tkinter
#BooleanVar,DoubleVar,IntVar,StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root,textvariable = uservalue)
passentry = Entry(root,textvariable = passvalue)

userentry.grid(row = 0, column = 1)
passentry.grid(row = 1, column = 1)

b1 = Button(text = "Submit",command = getval)
b1.grid()

root.mainloop()