# 07/06/2024
# Day - 033


# https://www.latlong.net/

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up
# BONUS: run the code every 60 seconds

# NOTE: Your position is within +5 or -5 degrees 
# of the ISS position

##################################################
# DAY 33 PROJECT: ISS CHALLENGE


print("\n*** Welcome to the ISS, look-out! ***")


import requests
from datetime import datetime
import smtplib

MY_LAT = 40.416930
MY_LONG = -3.703399

EMAIL_RECEIVER = "titiritest@yahoo.com"



def sun():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    
    sunset_hour = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise_hour = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    
    return sunrise_hour, sunset_hour



def iss_position():
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        
        iss_latitude = float(response.json()["iss_position"]["latitude"])
        iss_longitude = float(response.json()["iss_position"]["longitude"])
        
        return iss_latitude, iss_longitude
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching ISS position: {e}")
        # return -75.5814, -75.5814
        # return 9.691724, -120.743497
        return None, None



def where_am_i(latitude, longitude):

    parameters = {
        "key": "12bd8ddde9d0435eb3c4e7e6cb15c167",
        "q": f"{latitude}+{longitude}",
    }
    
    response = requests.get("https://api.opencagedata.com/geocode/v1/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    
    # print(data)
    
    if not data["results"]:
        return "No results found", "N/A", "N/A"
    
    components = data["results"][0]["components"]

    if "continent" not in components:
        return "No continent data", "N/A", "N/A"
    
    continent = components.get("continent", "N/A")
    country = components.get("country", "N/A")
    city = components.get("city", "N/A")
    
    # Check for ocean location
    if "body_of_water" in components:
        continent = "We are in the OCEAN BABY: " + components["body_of_water"]

    return continent, country, city
    


def send_email(letter, email):
    sender = "titiritest@gmail.com"
    receiver = email
    pw = "pknf dczx zfpd qleg"
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender, password=pw)
        connection.sendmail(
            from_addr=sender, 
            to_addrs=receiver, 
            msg=f"Subject: ISS - CHECK OUT THE SKY!!\n\n {letter}"
        )



print("\n*** SUN ***")

sunrise_hour, sunset_hour = sun()

print("-> The sunrise hour is:", sunrise_hour)
print("-> The sunset hour is:", sunset_hour)

print(f"\nThere will be LIGHT:")
print(f"-> From {sunrise_hour} to {sunset_hour}: {sunset_hour-sunrise_hour} hours")



print("\n\n*** YOU ***")

print("Q: Where am I?")
print(f"\nLatitude: {MY_LAT}")
print(f"Longitude: {MY_LONG}")

continent, country, city = where_am_i(MY_LAT, MY_LONG)
print("\n- Continent:", continent)
print("- Country:", country)
print("- City:", city)



print("\n\n*** ISS ***")

print("Q: Where is it?")
iss_latitude, iss_longitude = iss_position()

if iss_latitude == None or iss_longitude == None:
    print("Can't fetch the ISS latitude or longitude")
else:
    print(f"\nLatitude: {iss_latitude}")
    print(f"Longitude: {iss_longitude}")

    continent, country, city = where_am_i(iss_latitude, iss_longitude)
    print("\n- Continent:", continent)
    print("- Country:", country)
    print("- City:", city)


    print("\n\nQ: Can i see the ISS in the sky?")
    now_hour = datetime.now().hour

    if now_hour < sunrise_hour or now_hour > sunset_hour:
        print("\nIt is: DARK")
        
        if (iss_latitude > MY_LAT-5) and (iss_latitude < MY_LAT+5) and (iss_longitude > MY_LONG-5) and (iss_longitude < MY_LONG+5):
            message = "*** Look up! You can see the ISS in the sky ***"
            
            send_email(message, EMAIL_RECEIVER)
            print()
            
        else:
            print("A: Nope")
    else:
        print("A: Nope, it is sunny")