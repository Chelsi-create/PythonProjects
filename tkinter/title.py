from tkinter import *
root = Tk()

root.geometry("444x233")
root.title("Chelsi's GUI")

# Important Label options
# text - adds the text
# bd - background
# fg - foreground
# font - font = ("comicsansms",12,"bold") 
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN , RAISED , GROOVE , RIDGE

title_label = Label(text = '''Google LLC is an American multinational technology company that specializes in Internet-related services and 
\nproducts, which include online advertising technologies, search engine, cloud computing, software, and hardware. It is considered one of the
\nBig Four technology companies, alongside Amazon, Apple and Facebook.''',bg = "red",fg = "white",padx = 23,pady = 94, font = ("comicsansms",12,"bold"),borderwidth = 10,relief = SUNKEN)


#Important pack options
#anchor = nw
#side = top,bottom,left,right
#fill
#padx
#pady

#title_label.pack(side = BOTTOM , anchor = "sw" , fill = X)
title_label.pack(side = LEFT , fill = Y,padx = 34,pady = 34)

root.mainloop()