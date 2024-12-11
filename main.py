from datetime import *

import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
USER_NAME = "schatzmaster"
TOKEN = "aopiduh24362oiwt"
GRAPH_ID = "graph1"
today = datetime.now()

QUANTITY = "15"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": QUANTITY,
}


response = requests.delete(url=pixel_endpoint, headers=headers)

print(response.text)
