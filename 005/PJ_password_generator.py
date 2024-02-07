# 07/02/2024
# Day - 005



##################################################
# DAY 5 PROJECT: PASSWORD GENERATOR

print("\n*** Welcome to the PyPassword Generator! ***")

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("How many letters would you like in your password?")
n_letters = int(input("> "))

print("How many symbols would you like?")
n_symbols = int(input("> "))

print("How many numbers would you like?")
n_numbers = int(input("> "))

eazy_password = ""



#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for i in range(0, n_letters):
    n_random = random.randint(0, n_letters) - 1
    eazy_password += letters[n_random]

for i in range(0, n_symbols):
    n_random = random.randint(0, n_symbols) - 1
    eazy_password += symbols[n_random]

for i in range(0, n_numbers):
    eazy_password += random.choice(numbers)

print("\nEazy Level")
print("Here is your password:", eazy_password)



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password = ""

list_password = list(eazy_password)
print("Here is your password as a list:", list_password)

for i in range(len(list_password), 0, -1):
    n_random = random.randint(0, len(list_password)-1)
    hard_password += list_password[n_random]
    list_password.pop(n_random)

print("\nHard Level")
print("Here is your password:", hard_password)



#Hard Level 2 - Order of characters randomised: SOLUTION
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password2 = ""

list_password = list(eazy_password)
random.shuffle(list_password)

for char in list_password:
    hard_password2 += char

print("\nHard Level 2")
print("Here is your password:", hard_password2)