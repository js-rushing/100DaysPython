import requests
import datetime as dt
from config import USER_TOKEN, USER_NAME

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPHS_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

graph_id = "graph1"
new_value_endpoint = f"{GRAPHS_ENDPOINT}/{graph_id}"

user_params = {
    "token": USER_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_params = {
    "id": graph_id,
    "name": "Pushups",
    "unit": "reps",
    "type": "int",
    "color": "ajisai",
}

new_value_params = {
    "date": dt.datetime.now().strftime("%Y%m%d"),
    "quantity": "30"
}

update_value_params = {
    "date": dt.datetime(year=2021, month=5, day=23).strftime("%Y%m%d"),
    "quantity": "25"
}

update_pixel_endpoint = f"{new_value_endpoint}/{update_value_params['date']}"

headers = {
    "X-USER-TOKEN": USER_TOKEN
}

# Create user
# res = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(res.text)

# Create graph
# graphs_res = requests.post(url=GRAPHS_ENDPOINT, json=graph_params, headers=headers)
# print(graphs_res.text)

# Post New Pixel to Graph
# val_res = requests.post(url=new_value_endpoint, headers=headers, json=new_value_params)
# print(val_res.text)

# Update Pixel
# update_res = requests.put(url=update_pixel_endpoint, headers=headers, json=update_value_params)
# print(update_res.text)

# Delete Pixel
delete_res = requests.delete(url=update_pixel_endpoint, headers=headers)
print(delete_res.text)
