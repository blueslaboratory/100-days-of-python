# 25/06/2024
# Day - 038



##################################################
# DAY 38 PROJECT: WORKOUT TRACKING

print("\n*** Welcome to Workout Tracking! ***")

import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 69
HEIGHT_CM = 183
AGE = 31

# APP_ID = os.environ["NT_APP_ID"]
# API_KEY = os.environ["NT_API_KEY"]
APP_ID = "10d33fb2"
API_KEY = "548e21b466f0cfc9dd6d66ce34948cb1"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# sheet_endpoint = os.environ["SHEET_ENDPOINT"]
sheet_endpoint = "https://api.sheety.co/011da807f98f271a5006c9f3feb4bf0b/workoutsTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    # "Authorization": f"Bearer {os.environ['TOKEN']}"
    "Authorization": "Bearer tokensito"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)