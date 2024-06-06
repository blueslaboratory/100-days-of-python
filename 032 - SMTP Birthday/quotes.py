# 5/06/2024
# Day - 032
# Daily Motivational Quotes

'''
Objective:
send a motivational quote via email on the current weekday 
(you can change it to monday afterwards)

Hints
1. Use the datetime module to obtain the current day of the week
2. Open the quotes.txt file and obtain a list of quotes
3. Use the random module to pick a random quote from your list of quotes
4. Use the smtplib to send the email to yourself
'''


print("\n*** Welcome to Daily Motivational Quotes! ***")


import datetime as dt
import random
import smtplib


def get_quote():
    # closes automatically
    with open(".\\032 - SMTP Birthday\\quotes.txt") as file:
        # separates in an array
        contents = file.readlines()    
        # chooses a random quote
        random_quote = random.choice(contents)
    
    print(random_quote)
    return random_quote
    

def send_email(message):
    sender = "titiritest@gmail.com"
    receiver = "titiritest@yahoo.com"
    pw = "pknf dczx zfpd qleg"
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender, password=pw)
        connection.sendmail(
            from_addr=sender, 
            to_addrs=receiver, 
            msg=f"Subject: Happy Birthday!!\n\n {message}"
        )


# now = dt.datetime.now()
# today = now.weekday()

today = dt.datetime(year=2024, month=6, day=21, hour=7).weekday()

# 0: Monday, 4: friday 6: Sunday
print(f'\nToday: {today}')
print(f'Type: {type(today)}')

if today == 4:
    print("\nToday is Friday! Yay!")
    
    quote = get_quote()
    send_email(quote)