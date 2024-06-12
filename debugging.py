# debugging shit sheet

# refactor a variable: F2


import requests


MY_LAT = 40.416930
MY_LONG = -3.703399

parameters = {
    "key": "12bd8ddde9d0435eb3c4e7e6cb15c167",
    "q": f"{MY_LAT}+{MY_LONG}",
}

response = requests.get("https://api.opencagedata.com/geocode/v1/json", params=parameters)
response.raise_for_status()

data = response.json()

continent = data["results"][0]["components"]["continent"]
country = data["results"][0]["components"]["country"]
city = data["results"][0]["components"]["city"]


print("Continent:", continent)
print("Country:", continent)
print("City:", city)

