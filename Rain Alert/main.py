import requests
import os
from twilio.rest import Client

API_KEY = os.environ.get("MY_API_KEY")
LAT = 55.756540
LNG = 37.614920

account_sid = os.environ.get("MY_ACCOUNT_SID")
auth_token = os.environ.get("MY_AUTH_TOKEN")

weather_params = {
    "lat": LAT,
    "lon": LNG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts"

}

end_point = "https://api.openweathermap.org/data/2.5/onecall"

# 1st method
# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LNG}&exclude=hourly,daily&appid={API_KEY}")

# 2nd method
response = requests.get(end_point, params=weather_params)
response.raise_for_status()

weather_data = response.json()

# 1st method to code a Bring an umbrella if weather id is < 700
# weather_id = []
# weather_hourly = weather_data["hourly"]
#
# for i in range(12):
#     code = weather_hourly[i]["weather"][0]["id"]
#     weather_id.append(code)
#
# for i in weather_id:
#     if i < 700:
#         print("Bring a Umbrella")
#         break


# 2nd method
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code < 700):
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Its going to rain⛈️ today.Remember to bring an Umbrella☔.",
        from_='+16073176928',
        to='+91620210****'
    )
    print(message.status)
