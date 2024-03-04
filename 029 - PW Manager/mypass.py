# 04/03/2024
# Day - 029

# https://tkdocs.com/tutorial/canvas.html
# https://tkdocs.com/tutorial/widgets.html#entry
# https://www.w3schools.com/python/python_file_write.asp

# pip install pyperclip

##################################################
# DAY 29 PROJECT: MYPASS

print("\n*** Welcome to MyPass! ***")

from tkinter import *
from tkinter import messagebox
import random
import pyperclip




# ---------------------------- CONSTANTS ------------------------------- #
DIRECTORY_TXT = ".\\029 - PW Manager\\data.txt"




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# DAY 5: PW GENERATOR
# Password Generator Project
def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    """
    for char in range(nr_letters):
    password_list.append(random.choice(letters))

    for char in range(nr_symbols):
    password_list += random.choice(symbols)

    for char in range(nr_numbers):
    password_list += random.choice(numbers)
    """

    random.shuffle(password_list)

    password = "".join(password_list)
    print(f"Your password is: {password}")
    
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    # when you generate the pw, it's on the clipboard: CTRL+V
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = entry_website.get()
    username = entry_username.get()
    pw = entry_password.get()
    
    if len(web)==0 or len(username)==0 or len(pw)==0:
        messagebox.showwarning(title="Oopsie", message="Please don't leave empty fields")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered:"
                                                          f"\nusername: {username}"
                                                          f"\npassword: {pw}"
                                                          f"\nIs it ok to save?")
        
        if is_ok:
            # if the file does not exist, mode="a" creates the file
            with open(DIRECTORY_TXT, mode="a") as file:
                file.write(f"web: {web}\n")
                file.write(f"username: {username}\n") 
                file.write(f"pw: {pw}\n") 
                file.write("_____________________________________________\n")
                # closes automatically
            
    erase_fields()

def erase_fields():
    entry_website.delete(0, END)
    # entry_username.delete(0, END)
    entry_password.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)



# canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=".\\029 - PW Manager\\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=2)



# Label
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_username = Label(text="Email/Username:")
label_username.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)



# Entry
entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

entry_username = Entry(width=35)
entry_username.grid(column=1, row=2, columnspan=2)
entry_username.insert(0, "blueslaboratory")

entry_password = Entry(width=35)
entry_password.grid(column=1, row=3)



# Button
button_generate_pw = Button(text="Generate Password", width=30, command=generate_password)
button_generate_pw.grid(column=1, row=4)

button_add = Button(text="Add", width=30, command=save)
button_add.grid(column=1, row=5)



window.mainloop()