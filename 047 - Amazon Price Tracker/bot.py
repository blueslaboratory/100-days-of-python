# 23/07/2024
# Day - 047



######################################
# DAY 47 PROJECT: AMAZON PRICE TRACKER

print("\n*** Welcome to the Amazon Price Tracker Bot! ***")

from bs4 import BeautifulSoup
import requests

# Email
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



# STEP 1: Scraping the product price (doesn't work with live_url)
# STEP 3: Add headers to your request

practice_URL = "https://appbrewery.github.io/instant_pot/"
live_URL = "https://www.amazon.com/Funko-Articulated-Rick-Morty-Mr-Poopy/dp/B01MY7YTNR"

# https://httpbin.org/headers
# all_headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "es-ES,es",
#     "Host": "httpbin.org",
#     "Priority": "u=0, i",
#     "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Brave\";v=\"126\"",
#     "Sec-Ch-Ua-Mobile": "?0",
#     "Sec-Ch-Ua-Platform": "\"Windows\"",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "cross-site",
#     "Sec-Fetch-User": "?1",
#     "Sec-Gpc": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
#     "X-Amzn-Trace-Id": "Root=1-669f9710-36f194065132d2735aa56ee5"
#   }

# response = requests.get(practice_URL, verify=False, headers=all_headers)
response = requests.get(practice_URL, verify=False, headers={"Accept-Language":"en-US"})

# This line of code does our parsing  
soup = BeautifulSoup(response.text, "html.parser")

dollars = soup.find(name="span", class_="a-price-whole").getText().split(".")[0]
cents = soup.find(name="span", class_="a-price-fraction").getText()
full_price = float(f"{dollars}.{cents}")
print(full_price)

# price_to_pay = float(soup.find(name="span", class_="priceToPay").getText().split("$")[1])
# print(price_to_pay)

product_title = soup.find(name="span", id="productTitle").getText().strip()
product_title = re.sub(r'\s+', ' ', product_title)
print(product_title)



# STEP 2 - Email alert when the price is below preset value

def send_email():
    
    sender = "titiritest@gmail.com"
    receiver = sender
    pw = "pknf dczx zfpd qleg"
    
    message_body = "PRODUCT: " +product_title +"\nPRICE: $" +str(full_price) +"\nURL: " +practice_URL

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=sender, password=pw)
        
        # Create a MIMEText object for each email
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = "Amazon Price Alert!"

        msg.attach(MIMEText(message_body, 'plain', 'utf-8'))

        connection.sendmail(
            from_addr=sender,
            to_addrs=receiver,
            msg=msg.as_string()
        )
        
        print("Email sent successfully!")



NOTIFICATION_PRICE = 100

if (full_price < NOTIFICATION_PRICE):
    send_email()