# 18/06/2024
# Day - 036

##################################################
# DAY 36 PROJECT: TESLA STOCK TRADING
# LOL, DON'T DAYTRADE

print("\n*** Welcome to the TESLA HODL DON'T DAYTRADE LOL Price Alert Rollercoaster! ***")

import requests
import smtplib
import json

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "titiritest@gmail.com"
receiver = sender
pw = "pknf dczx zfpd qleg"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_KEY_STOCK = "EQFNKTFSIXEB2KTO"
API_KEY_NEWS = "3b3e4f3bdaf0454f8f7288897b3555d5"

STOCK_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"

stock_parameters = {
    "apikey": API_KEY_STOCK,
    "symbol": STOCK,
    "function": "TIME_SERIES_DAILY",
}


############################################
# Uncomment this if the STOCK API is working
# response = requests.get(url=STOCK_URL, params=stock_parameters)
# stock_data = response.json()


##########################################
# Comment this if the STOCK API is working
# read the JSON:
with open('.\\036 - Stock Trading\\json\\stock_data.json', 'r') as file:
    stock_data = json.load(file)

# STOCK
# print(stock_data)

time_series = stock_data["Time Series (Daily)"]
dates = list(time_series.keys())

print(time_series[dates[1]])

before_yesterday_price = float(time_series[dates[1]]["4. close"])
yesterday_price = float(time_series[dates[0]]["4. close"])

print(f"{dates[1]} - Before yesterday: ${before_yesterday_price}")
print(f"{dates[0]} - Yesterday: ${yesterday_price}")

porcentage_change = round(((yesterday_price - before_yesterday_price)/yesterday_price)*100, 2)


if (porcentage_change > 5):
    print(f"--> The % change between before yesterday and yesterday is: {porcentage_change}%")
    print("\nGet News:")
    
    news_parameters = {
        "apiKey": API_KEY_NEWS,
        "q": COMPANY_NAME,
        "from": dates[0],
        "sortBy": "popularity",
        # "category": "business",
        # "language": "en",
        # "country": "us",
    }
    response = requests.get(url=NEWS_URL, params=news_parameters)
    news_data = response.json()
    # print(news_data)
    
    top_articles_headlines = []
    message = ""
    
    for i in range(3):
        print(news_data["articles"][i]["title"])
        top_articles_headlines.append(news_data["articles"][i])
        message += f"{news_data["articles"][i]["title"]}\n"
        
    # Encode the message in UTF-8
    message = message.encode('utf-8')
    
    # Create a MIMEText object to represent the email
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = sender
    msg['Subject'] = f"Tesla {porcentage_change}%"
    
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



############################################
# Uncomment this if the NEWS API is working    
#    Write the JSON data to a text file
#    with open(".\\036 - Stock Trading\\json\\news_data.json", "w") as file:
#        json.dump(news_data, file, indent=4)

# print("Data has been written to news_data.json")

############################################
# Uncomment this if the STOCK API is working
# Write the JSON data to a text file
# with open(".\\036 - Stock Trading\\json\\stock_data.json", "w") as file:
#     json.dump(stock_data, file, indent=4)

# print("Data has been written to stock_data.json")