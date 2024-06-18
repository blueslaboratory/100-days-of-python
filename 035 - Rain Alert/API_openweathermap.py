# 18/06/2024
# Day - 035


##################################################
print("\n\n*** Openweathermap API Challenge ***")

import requests
import json

api_key = "792672e5944ad05554ae1fa26aefb1d7"
MY_LAT = 40.416930
MY_LONG = -3.703399

# https://home.openweathermap.org/api_keys

# https://api.openweathermap.org/data/2.5/weather?q=Madrid&appid=792672e5944ad05554ae1fa26aefb1d7

# https://www.latlong.net/
# https://openweathermap.org/current
# https://api.openweathermap.org/data/2.5/weather?lat=40.416930&lon=-3.703399&appid=792672e5944ad05554ae1fa26aefb1d7

# https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
# https://api.openweathermap.org/data/2.5/forecast?lat=40.416930&lon=-3.703399&appid=792672e5944ad05554ae1fa26aefb1d7

URL_3_hour_forecast = f"https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key
}

response = requests.get(url=URL_3_hour_forecast, params=parameters)

print(response.status_code)
print(response)

weather_data = response.json()
# print(data)
# Online JSON viewer:
# https://jsonviewer.stack.hu/

print("Weather description:", weather_data["list"][0]["weather"][0]["description"])


# Write the JSON data to a text file
with open(".\\035 - Rain Alert\\txt\\3_hour_forecast.txt", "w") as file:
    json.dump(weather_data, file, indent=4)

print("Data has been written to 3_hour_forecast.txt")