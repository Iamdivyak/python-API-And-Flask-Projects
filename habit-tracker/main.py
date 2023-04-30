import requests
from datetime import datetime
import os
TOKEN = os.environ.get("habit_tracker_token")
USERNAME = "iamdivya"
# print(TOKEN)
API_ENDPOINT = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(API_ENDPOINT, json=user_params)
# data = response.text
#
# print(data)

graph_endpoint = f"{API_ENDPOINT}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name":"PROGRASS",
    "unit": "kilometre",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN,

}

# graph_response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# data = graph_response.text
# print(data)

today = datetime.now()


graph_value_endpoint = f"{graph_endpoint}/graph1"
graph_value_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many kilometers did you cicled today?: ")
}

graph_value_header={
    "X-USER-TOKEN": TOKEN,
}
# print(today.strftime("%Y%m%d"))
graph_value_response = requests.post(graph_value_endpoint, json=graph_value_params, headers=graph_value_header)
data = graph_value_response.text
print(data)
update_endpoint = f"{graph_value_endpoint}/{today.strftime('%Y%m%d')}"
update_params = {
    # "date": today.strftime("%Y%m%d"),
    "quantity": "2.00",
    # "color":"sora",
}

delete_endpoint = update_endpoint

# delete_response = requests.delete(delete_endpoint, headers=headers, json=delete_params)
# print(delete_response.text)

