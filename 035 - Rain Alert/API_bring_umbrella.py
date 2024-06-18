# 18/06/2024
# Day - 035

# Check if it will rain in the next 12 hours and tell the user
# to bring an umbrella

##################################################
print("\n\n*** Bring Umbrella API Challenge ***")

import requests


api_key = "792672e5944ad05554ae1fa26aefb1d7"
MY_LAT = 40.416930
MY_LONG = -3.703399

URL_3_hour_forecast = f"https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=URL_3_hour_forecast, params=parameters)

print(response.status_code)
print(response)

weather_data = response.json()
# print(data)
# Online JSON viewer:
# https://jsonviewer.stack.hu/

# print("Weather id:", weather_data["list"][0]["weather"][0]["id"])



# List to store weather IDs
weather_ids = []
rain_flag = False



# Storing the id's in a list
for forecast in weather_data["list"]:
    
    # print(forecast["weather"][0]["id"])
    
    for weather in forecast["weather"]:
        weather_ids.append(weather["id"])



for id in weather_ids:
    if id <= 699 and rain_flag == False:
        rain_flag = True
        
if rain_flag:
    print("Bring an umbrella")