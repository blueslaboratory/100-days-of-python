# 01/03/2024
# Day - 027

# https://docs.python.org/3/library/tkinter.html#the-packer
# https://tcl.tk/man/tcl8.6/TkCmd/pack.htm


##################################################
print("\n\n*** GUI: Tkinter 1 ***")

import tkinter
from tkinter import *



window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)



# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "italic"))
my_label.pack()

# my_label.pack(side="left")
# my_label.pack(side="bottom")
# my_label.pack(side="right")

# my_label.pack(expand="true")

# change label text (either works):
my_label["text"] = "New Text"
my_label.config(text="New Text")



# Button
def button_clicked():
    print("I got clicked")
    # my_label["text"] = "Oo wee, i got clicked"
    
    # change the label to the input box text:
    # print(input.get())
    my_label.config(text=input.get())

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()



# Entry
input = Entry(width=10)
input.pack()



window.mainloop()