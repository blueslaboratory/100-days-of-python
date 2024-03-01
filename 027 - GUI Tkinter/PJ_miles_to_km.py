# 01/03/2024
# Day - 027

# https://docs.python.org/3/library/tkinter.html#the-packer
# https://tcl.tk/man/tcl8.6/TkCmd/pack.htm


##################################################
# DAY 27 PROJECT: MILES TO KM

print("\n*** Welcome to tkinter: miles to km! ***")


from tkinter import *



def miles_to_km():
    print("miles_to_km() got clicked")
    miles = float(input.get())
    km = miles*1.60934
    my_label_result.config(text=f"{km}")



window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=240, height=100)
window.config(padx=20, pady=20)



# Label
my_label_miles = Label(text="Miles", font=("Arial", 10))
my_label_miles.grid(column=2, row=0)

my_label_equal = Label(text="is equal to", font=("Arial", 10))
my_label_equal.grid(column=0, row=1)

my_label_result = Label(text="0", font=("Arial", 10))
my_label_result.grid(column=1, row=1)

my_label_km = Label(text="Km", font=("Arial", 10))
my_label_km.grid(column=2, row=1)



# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)



# Entry
input = Entry(width=10)
input.grid(column=1, row=0)



window.mainloop()