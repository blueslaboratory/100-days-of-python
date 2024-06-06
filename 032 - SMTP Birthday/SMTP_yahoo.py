# 5/06/2024
# Day - 032

import smtplib


sender = "titiritest@yahoo.com"
receiver = "titiritest@gmail.com"
# pw = "pknf dczx zfpd qleg"
# Video 290 - Esta función no está disponible en este momento.

message = "Hello cara hielow"


# 2nd WAY
with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=sender, password=pw)
    connection.sendmail(
        from_addr=sender, 
        to_addrs=receiver, 
        msg=f"Subject: 2nd WAY - Hell_O_Kitty\n\n {message}"
    )