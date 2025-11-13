import urllib

import requests
from  datetime import datetime, timedelta

USERNAME ="muffz"
TOKEN = "2adsfasff234fdg34452452sf113123"
DATE_TODAY = datetime.now().strftime("%Y%m%d")
DATE_YESTERDAY = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
GRAPH_ID = "graph3"
TIME_ZONE = "Asia/Manila"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
#creating graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Buboy Running Graph",
    "unit":"Km",
    "type": "float",
    "color":"ajisai",
    "timezone": TIME_ZONE,

}
headers = {
    "X-USER-TOKEN": TOKEN,
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#creating pixels
pixel_creating_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": DATE_TODAY,
    "quantity": input("how many kilometers did you run today? "),

}

response = requests.post(url=pixel_creating_endpoint, json=pixel_data, headers=headers)
print(response.text)



#updating existing pixel

# pixel_updating_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE_YESTERDAY}"
# pixel_update_data = {
#     "quantity": "10.24",
#
# }

# response = requests.put(url=pixel_updating_endpoint,json=pixel_update_data, headers=headers)
# print(response.txt)

#deleting existing pixel

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20250824"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
#
# print(response.text)


