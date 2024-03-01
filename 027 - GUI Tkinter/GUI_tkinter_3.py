# 01/03/2024
# Day - 027

# https://docs.python.org/3/library/tkinter.html#the-packer
# https://tcl.tk/man/tcl8.6/TkCmd/pack.htm


##################################################
print("\n\n*** GUI: Tkinter Layout Managers 3 ***")


from tkinter import *



def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)



# 3 Tkinter Layout Managers: pack, place and grid
# "Grid is my preferred way of working with tkinter:"
# You can't mix grid and pack in the same program



window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)



# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")

# my_label.pack(side="left")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

my_label.config(padx=50, pady=50)



# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)



# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)



window.mainloop()