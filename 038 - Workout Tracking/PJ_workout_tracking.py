# 25/06/2024
# Day - 038



##################################################
# DAY 38 PROJECT: WORKOUT TRACKING

print("\n*** Welcome to Workout Tracking! ***")

import requests
import json
from datetime import datetime


APP_ID = "10d33fb2"
API_KEY = "548e21b466f0cfc9dd6d66ce34948cb1"

host_domain = "https://trackapi.nutritionix.com"
exercise_endpoint = f"{host_domain}/v2/natural/exercise"

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

exercise_query = input("Tell me which exercises you did: ")
# cycling 2 hours, yoga 1 hour, pilates 30 minutes

data = {
    "query": exercise_query
    # "query": "swam for 1 hour and ran 2 miles"
}


###################################################
# Comment this if the NUTRITIONIX API isn't working
response = requests.post(url=exercise_endpoint, headers=headers, json=data)
exercise_data = response.json()

print("Status Code:", response.status_code)
print("JSON Response:", response.json())


################################################
# Comment this if the NUTRITIONIX API is working
# read the JSON:
# with open('.\\038 - Workout Tracking\\json\\exercise_data.json', 'r') as file:
#     exercise_data = json.load(file)



sheety_endpoint = "https://api.sheety.co/011da807f98f271a5006c9f3feb4bf0b/workoutsTracking/workouts"

headers = {
    "Authorization": "Bearer tokensito"
}

date = datetime.now().strftime('%Y/%m/%d')
time = datetime.now().strftime('%H:%M:%S')
# exercise = exercise_data["exercises"][0]["name"]
exercise_names = []
exercise_duration = []
exercise_calories = []
exercise_json = {}

for exercise in exercise_data["exercises"]:
    exercise_names.append(exercise["name"].title())
    exercise_duration.append(exercise["duration_min"])
    exercise_calories.append(exercise["nf_calories"])
    
for i in range(len(exercise_names)):
    exercise_json = {
        "workout":{
            "date": date,
            "time": time,
            "exercise": exercise_names[i],
            "duration": exercise_duration[i],
            "calories": exercise_calories[i]
        }
    }
    
    print(exercise_json)
    
    response = requests.post(url=sheety_endpoint, json=exercise_json, headers=headers)
    data_json = response.json()

    print("Status Code:", response.status_code)
    print("JSON Response:", data_json)




############################################
# Uncomment this if the NUTRITIONIX API is working
# Write the JSON data to a text file
# with open(".\\038 - Workout Tracking\\json\\exercise_data.json", "w") as file:
#     json.dump(exercise_data, file, indent=4)

# print("Data has been written to exercise_data.json")