# 04/03/2024
# Day - 030

# https://tkdocs.com/tutorial/canvas.html
# https://tkdocs.com/tutorial/widgets.html#entry
# https://www.w3schools.com/python/python_file_write.asp

# pip install pyperclip

"""
l. Add a "Search" button next to the website entry field. 
2. Adjust the layout and the other widgets as needed to get the 
desired look. 
3. Create a function called find_password() that gets 
triggered when the "Search" button is pressed. 
4. Check if the user's text entry matches an item in the data .json 
5. If yes, show a messagebox with the website's name and password. 
6. Catch an exception that might occur trying to access the 
data .json showing a messagebox with the text: "No Data File Found". 
7. If the user's website does not exist inside the data.json, 
show a messagebox that reads "No details for the website exists". 
"""

##################################################
# DAY 30 PROJECT: MYPASS (simplified) --> JSON

print("\n*** Welcome to MyPass JSON! ***")

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json



# ---------------------------- CONSTANTS ------------------------------- #
DIRECTORY_JSON = ".\\030 - Exceptions & JSON\\PJ_PW_Manager\\data.json"




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
    
    new_data = {
            web: {
                "username":  username,
                "password": pw
            }
        }
    
    if len(web)==0 or len(username)==0 or len(pw)==0:
        messagebox.showwarning(title="Oops", message="Please don't leave empty fields")
    else:
        # write mode --> mode="w" --> json.dump()
        # read mode  --> mode="r" --> json.load()
        # with open(DIRECTORY_JSON, mode="r") as file:
            # writing:
            # json.dump(new_data, file, indent=4)
            
            # reading:
            # data = json.load(file)
            # print(data)

        # appending (updating) --> r + w --> json.update()
        try:
            with open(DIRECTORY_JSON, mode="r") as file:
                # 1. reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open(DIRECTORY_JSON, mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open(DIRECTORY_JSON, mode="w") as file:
                # 2. updating old data with new data
                data.update(new_data)
                # 3. writing updated data
                json.dump(data, file, indent=4)
                # closes automatically
            
    erase_fields()

def erase_fields():
    entry_website.delete(0, END)
    # entry_username.delete(0, END)
    entry_password.delete(0, END)



# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    web = entry_website.get()
    # read mode  --> mode="r" --> json.load()
    try:
        with open(DIRECTORY_JSON, mode="r") as file:
            
            # reading:
            data = json.load(file)
            username = data[web]["username"]
            pw = data[web]["password"]
            
            messagebox.showinfo(title="Search Results", message=f"username: {username}\n"
                                                                f"password: {pw}")
    
    except FileNotFoundError:
        messagebox.showwarning(title="Oops", message="File Not Found")
        
    except KeyError:
        messagebox.showwarning(title="Oops", message="Password Not Found")



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

button_search = Button(text="Search", width=30, command=find_password)
button_search.grid(column=1, row=6)



window.mainloop()