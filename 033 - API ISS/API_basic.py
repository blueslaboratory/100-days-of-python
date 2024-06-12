# 06/06/2024
# Day - 033

# Terminal:
# > pip install requests

##################################################
print("\n\n*** API - requests - response ***")

import requests


# 404: request fails
response = requests.get(url="http://api.open-notify.org/is-now.json")
print(response.status_code)


# 200: successful
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)


if response.status_code == 404:
    raise Exception("That resource does not exist.")
elif response.status_code == 401:
    raise Exception("You are not authorised to access this data.")


data = response.json()["iss_position"]
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
