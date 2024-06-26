# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


###############################
### works for only 1 person ###
###############################

from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "titiritest@gmail.com"
MY_PASSWORD = "pknf dczx zfpd qleg"
CSV_DIRECTORY = ".\\032 - SMTP Birthday\\PJ_birthday\\birthdays.csv"
LETTERS_DIRECTORY = ".\\032 - SMTP Birthday\\PJ_birthday\\letter_templates\\letter_"


today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv(CSV_DIRECTORY)

"""
No vale para multiples personas porque:
Cada clave (month, day) en el diccionario estará asociada a un solo data_row. 
Si hay múltiples personas con el mismo cumpleaños, solo se guardará la última persona 
procesada en el diccionario, porque las claves deben ser únicas y cada asignación 
sobrescribe la anterior.
"""
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

print(birthdays_dict)

if today_tuple in birthdays_dict:
    
    birthday_person = birthdays_dict[today_tuple]
    file_path = LETTERS_DIRECTORY + str(random.randint(1,3)) + ".txt"
    
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )