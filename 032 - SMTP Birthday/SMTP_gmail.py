# 5/06/2024
# Day - 032

import smtplib

sender = "titiritest@gmail.com"
receiver = "titiritest@yahoo.com"
pw = "pknf dczx zfpd qleg"

message = "Hello cara hielow"


# 1st WAY
# smtp.gmail.com is the email provider
connection = smtplib.SMTP("smtp.gmail.com")
# TLS (Transport Layer Security)
connection.starttls()

# it is sent to the spam inbox lol
connection.login(user=sender, password=pw)
connection.sendmail(
    from_addr=sender, 
    to_addrs=receiver, 
    msg=f"Subject: 1st WAY - Hell_O_Kitty\n\n {message}"
)


# 2nd WAY
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=sender, password=pw)
    connection.sendmail(
        from_addr=sender, 
        to_addrs=receiver, 
        msg=f"Subject: 2nd WAY - Hell_O_Kitty\n\n {message}"
    )