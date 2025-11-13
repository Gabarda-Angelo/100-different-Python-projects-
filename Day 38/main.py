'''
Notes:
-the only reason we’re using Nutritionix API is to process natural language input
from the user and return structured exercise data in JSON format.

-The Sheety API is included in your code only so that the structured exercise data we get from Nutritionix
can be sent automatically to Google Sheets for logging and tracking purposes.

'''


import requests
from datetime import datetime
import os

# Nutritionix API details
APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]

GENDER = "male"
WEIGHT = 63
HEIGHT = 162   # in centimeters
AGE = 24

SHEETY_TOKEN = os.environ["ENV_SHEETY_TOKEN"]

# Sheety endpoint (use your actual link)
sheety_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]


# Ask user what they did
exercise_activity = input("Tell me which exercises you did: ")

# Nutritionix headers & request body
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": exercise_activity,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

# Send request to Nutritionix
response = requests.post(
    url="https://trackapi.nutritionix.com/v2/natural/exercise",
    json=exercise_params,
    headers=headers
)
result = response.json()

# Prepare current date & time
today = datetime.now().strftime("%Y-%m-%d")
time_now = datetime.now().strftime("%H:%M:%S")

# Sheety headers
sheety_headers = {
    # "Content-Type": "application/json",
    "Authorization":f"Bearer {SHEETY_TOKEN}",
}
# Loop through each exercise returned by Nutritionix
for exercise in result["exercises"]:
    workout_data = {
        "workout": {
            "date": today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Send workout to Sheety
    sheety_response = requests.post(url=sheety_endpoint,json=workout_data,headers=sheety_headers)

    # Show confirmation
    print(response.text)
    print(sheety_response.text)






