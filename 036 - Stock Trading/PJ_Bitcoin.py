# 18/06/2024
# Day - 036

##################################################
# DAY 36 PROJECT: BITCOIN STOCK TRADING SOLUTION
# LOL, DON'T DAYTRADE

print("\n*** Welcome to the BITCOIN HODL DON'T DAYTRADE LOL Price Alert Rollercoaster! ***")

import requests
import smtplib
import json

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "titiritest@gmail.com"
receiver = sender
pw = "pknf dczx zfpd qleg"

SYMBOL = "BTC"
COMPANY_NAME = "Bitcoin"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY_STOCK = "EQFNKTFSIXEB2KTO"
API_KEY_NEWS = "3b3e4f3bdaf0454f8f7288897b3555d5"



## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#TODO 2. - Get the day before yesterday's closing stock price

stock_params = {
    "apikey": API_KEY_STOCK,
    "symbol": SYMBOL,
    "market": "USD",
    "function": "DIGITAL_CURRENCY_DAILY",
}

############################################
# Uncomment this if the STOCK API is working
# response = requests.get(STOCK_ENDPOINT, params=stock_params)
# btc_data = response.json()

##########################################
# Comment this if the STOCK API is working
# read the JSON:
with open('.\\036 - Stock Trading\\json\\btc_data.json', 'r') as file:
    btc_data = json.load(file)

# print(btc_data)

time_series = btc_data["Time Series (Digital Currency Daily)"]
data_list = [value for (key, value) in time_series.items()]

# print(data_list)

before_yesterday_price = float(data_list[1]["4. close"])
yesterday_price = float(data_list[0]["4. close"])

print(f"BTC before yesterday: ${before_yesterday_price}")
print(f"BTC yesterday: ${yesterday_price}")


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = round(abs(yesterday_price - before_yesterday_price),2)
print(f"Absolute Difference: ${difference}")


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percent = round((difference / yesterday_price)*100,5)
print(f"Difference between yesterday & today: {diff_percent}%")


#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if diff_percent > 0.07:
    print("\nGet News Agent 007:")



## STEP 2: https://newsapi.org/ 
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

if diff_percent > 0.07:
    
    news_params = {
        "apiKey": API_KEY_NEWS,
        "qInTitle": COMPANY_NAME,
    }
    
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    # print(articles)


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

three_articles = articles[:3]
# print(three_articles)


## STEP 3: Use twilio.com/docs/sms/quickstart/python (SMTP)
#to send a separate message with each article's title and description to your phone number. 


#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]


#TODO 9. - Send each article as a separate message via Twilio. 

message = "\n\n".join(f"Headline: {article['title']} \nBrief: {article['content']}" for article in three_articles)
print(message)

# Encode the message in UTF-8
message = message.encode('utf-8')

# Create a MIMEText object to represent the email
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = sender
msg['Subject'] = f"BTC {diff_percent}%"

msg.attach(MIMEText(message, 'plain', 'utf-8'))

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=sender, password=pw)
    connection.sendmail(
        from_addr=msg['From'], 
        to_addrs=msg['To'], 
        msg=msg.as_string()
    )

print("\n--> Message sent successfully!")


#Optional TODO: Format the message like this: 
"""
BTC: 🔺2%
Headline: ...
Brief: ...
BTC: 🔻5%
Headline: ...
Brief: ...
"""


############################################
# Uncomment this if the NEWS API is working    
# Write the JSON data to a text file
# with open(".\\036 - Stock Trading\\json\\btc_news_data.json", "w") as file:
#     json.dump(articles, file, indent=4)

# print("Data has been written to news_data.json")


############################################
# Uncomment this if the STOCK API is working
# Write the JSON data to a text file
# with open(".\\036 - Stock Trading\\json\\btc_data.json", "w") as file:
#     json.dump(btc_data, file, indent=4)

# print("Data has been written to btc_data.json")