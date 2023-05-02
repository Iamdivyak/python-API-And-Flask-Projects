import requests
import os
import datetime

API_ID = os.environ["api_id"]
API_KEY = os.environ["api_key"]

nutritionix_header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    # "x-remote-user-id": 0,
}

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_params = {
    "query": input("Tell me which exercises you did Today?: "),
    "gender": "female",
    "weight_kg": 66,
    "height_cm": 167,
    "age": 22
}

nutritionix_response = requests.post(url=nutritionix_endpoint, headers=nutritionix_header, json=nutritionix_params)
result = nutritionix_response.json()
print(result)

sheety_endpoint = os.environ["sheety_endpoint"]

now = datetime.datetime.now()
date = now.date().strftime("%d/%m/%Y")
time = now.time().strftime("%X")
# print(date, time)

for exercise in result["exercises"]:
    sheety_params = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheety_endpoint, json=sheety_params)
print(sheet_response.text)
