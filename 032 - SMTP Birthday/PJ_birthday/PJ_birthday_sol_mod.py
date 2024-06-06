# 6/6/2024

# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

############################
### works for >=1 person ###
############################


from datetime import datetime
import pandas as pd
import random
import smtplib

MY_EMAIL = "titiritest@gmail.com"
MY_PASSWORD = "pknf dczx zfpd qleg"
CSV_DIRECTORY = ".\\032 - SMTP Birthday\\PJ_birthday\\birthdays.csv"
LETTERS_DIRECTORY = ".\\032 - SMTP Birthday\\PJ_birthday\\letter_templates\\letter_"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv(CSV_DIRECTORY)
birthdays_dict = {}

# Populate the dictionary with lists of people
for (index, data_row) in data.iterrows():
    key = (data_row["month"], data_row["day"])
    if key not in birthdays_dict:
        birthdays_dict[key] = []
    birthdays_dict[key].append(data_row)
    
# print("Birthdays Dictionary:", birthdays_dict)

if today_tuple in birthdays_dict:
    for person in birthdays_dict[today_tuple]:
        
        file_path = LETTERS_DIRECTORY + str(random.randint(1,3)) + ".txt"
        
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )