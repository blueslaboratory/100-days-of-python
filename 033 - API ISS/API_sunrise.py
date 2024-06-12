# 06/06/2024
# Day - 033

# https://www.latlong.net/Show-Latitude-Longitude.html
# https://sunrise-sunset.org/api#limits

##################################################
print("\n\n*** API - Sunrise ***")

import requests
from datetime import datetime

MY_LAT = 40.412772
MY_LONG = -3.679655

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T"))
print(sunrise.split("T")[1].split(":")[0])

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)