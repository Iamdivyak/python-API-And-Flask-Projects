import requests
from datetime import datetime
import os
APP_ID = os.environ.get("API_ID")
API_KEY = os.environ.get("API_KEY")
GENDER = "female"
WEIGHT_KG = 66.00
HEIGHT_CM = 165
AGE = 20
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}
sheety_endpoint = os.environ.get("sheety_endpoint")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
params = {
    "query": input("Tell which exercise you did today?: "),
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE,
    # "x-app-id": APP_ID,
    # "x-app-key": API_KEY,
}

response = requests.post(exercise_endpoint, headers=headers, json=params)
response.raise_for_status()
result = response.json()
print(result)

exercise = result["exercises"][0]["name"].title()
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheety_header = {"Authorization":f"Bearer {os.environ.get('token')}"}

sheet_inputs = {
    "workout": {
        "Date": today_date,
        "Time": now_time,
        "Exercise": exercise,
        "Duration": duration,
        "Calories": calories
    }
}

sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=sheety_header)
sheet_response.raise_for_status()
print(sheet_response.text)







