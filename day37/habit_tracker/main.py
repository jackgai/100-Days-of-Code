import requests
import os
from dotenv import load_dotenv
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

load_dotenv("/Users/yizhigai/Desktop/python_environment_variables/.env")
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = "graph1"

# set up a user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

# create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN.encode("utf-8")
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# create a pixel
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2023, month=4, day=1).strftime("%Y%m%d")

pixel_config = {
    "date": today,
    "quantity": "5.3"
}

# post_pixel_response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
# print(post_pixel_response.text)

# update pixel
put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

put_pixel_config = {
    "quantity": "30.5"
}

# put_pixel_response = requests.put(url=put_pixel_endpoint, json=put_pixel_config, headers=headers)
# print(put_pixel_response.text)

# delete a pixel
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(delete_pixel_response.text)
