# 23/07/2024
# Day - 047



###############################################
# DAY 47 PROJECT: AMAZON PRICE TRACKER SOLUTION

print("\n*** Welcome to the Amazon Price Tracker Bot! ***")

from bs4 import BeautifulSoup
import requests
import smtplib
import os
# pip install dotenv
# from dotenv import load_dotenv


# Load environment variables from .env file
# load_dotenv()



# STEP 1: Scraping the product price (doesn't work with live_url)
# STEP 3: Add headers to your request

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Full headers would look something like this
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

# A minimal header would look like this:
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }

response = requests.get(practice_url, verify=False, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

# Find the HTML element that contains the price
price = soup.find(name="span", class_="priceToPay").get_text()

# Remove the dollar sign using split
price_without_currency = price.split("$")[1]

# Convert to floating point number
price_as_float = float(price_without_currency)
print(price_as_float)



# STEP 2 - Email alert when the price is below preset value

SMTP_ADDRESS = "smtp.gmail.com"
EMAIL = "titiritest@gmail.com"
PASSWORD = "pknf dczx zfpd qleg"

# Get the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{practice_url}".encode("utf-8")
        )
        
    print("Email sent successfully!")