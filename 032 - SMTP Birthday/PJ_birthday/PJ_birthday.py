# 6/6/2024
##################### Extra Hard Starting Project ######################

# [X] 1. Update the birthdays.csv

# [X] 2. Check if today matches a birthday in the birthdays.csv

# [X] 3. If step 2 is true, pick a random letter from letter templates and 
#        replace the [NAME] with the person's actual name from birthdays.csv

# [X] 4. Send the letter generated in step 3 to that person's email address.


########################################################################
# DAY 32 PROJECT: 

import datetime as dt
import csv
import random
import smtplib


def birthday_matches():
    DIRECTORY_CSV = ".\\032 - SMTP Birthday\\PJ_birthday\\birthdays.csv"
    data = []
    
    # closes automatically
    with open(DIRECTORY_CSV) as file:
        reader = csv.reader(file)
        # Convierte el iterador a una lista
        data = list(reader) 
        # print(data)
    
    now = dt.datetime.now()
    today_day = now.day
    today_month = now.month
    
    matches = []
    
    # data is an iterator: once you do 1 for loop, it is exhausted
    for row in data[1:]:
        # print(row)
        
        if int(row[3]) == today_month and int(row[4]) == today_day:
            matches.append(row)
    
    return matches



def select_letter():
    letter = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    random_letter = random.choice(letter)
    
    DIRECTORY_TXT = f".\\032 - SMTP Birthday\\PJ_birthday\\letter_templates\\{random_letter}"
    
    with open(DIRECTORY_TXT, 'r') as file:
        data = file.read()
        
    return data


def customize_letter(name):
    letter = select_letter()
    string_to_replace = "[NAME]"
    
    custom_letter = letter.replace(string_to_replace, name)
    
    return custom_letter


def send_email(letter, email):
    sender = "titiritest@gmail.com"
    receiver = email
    pw = "pknf dczx zfpd qleg"
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender, password=pw)
        connection.sendmail(
            from_addr=sender, 
            to_addrs=receiver, 
            msg=f"Subject: Happy Birthday!!\n\n {letter}"
        )



birthday_matches = birthday_matches()

if len(birthday_matches) != 0:
    
    print("Today's Birthdays:")
    
    for birthday in birthday_matches:
        print(birthday)
        name = birthday[0]
        email = birthday[1]
        
        custom_letter = customize_letter(name)
        send_email(custom_letter, email)
        print(f'Happy Birthday email sent to: {name}')