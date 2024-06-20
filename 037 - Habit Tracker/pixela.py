# 20/06/2024
# Day - 037



##################################################
################# Create User ####################
##################################################

print("\n\n*** Create User ***")

import requests
from datetime import datetime

USERNAME = "titiritest"
TOKEN = "pipiripython"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "username": USERNAME,
    "token": "P1X3L444",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# POST request: Create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)



##################################################
################# Change Token ###################
##################################################

print("\n\n*** Change token ***")

# Define the endpoint URL
url = "https://pixe.la/v1/users/titiritest"

# Define the headers
headers = {
    "X-USER-TOKEN": "P1X3L444"
}

# Define the JSON payload (new password)
data = {
    "newToken": TOKEN
}

# PUT request: Change Token
# response = requests.put(url, headers=headers, json=data)
# print(response.text)



##################################################
################# Create Graph ###################
##################################################

# https://docs.pixe.la/entry/post-graph
# https://pixe.la/v1/users/titiritest/graphs/graph1
# https://pixe.la/v1/users/titiritest/graphs/graph1.html

print("\n\n*** Create Graph ***")

GRAPH_ID = "graph1"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "100-days-of-python",
    "unit": "commit",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# POST request: Create Graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)



##################################################
############### Posting a Pixel ##################
##################################################

# https://docs.pixe.la/entry/post-pixel

print("\n\n*** Posting a pixel ***")

# /v1/users/<username>/graphs/<graphID>
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# https://www.w3schools.com/python/python_datetime.asp
today = datetime.now()
today_new_format = today.strftime("%Y%m%d")

yesterday = datetime(year=2024, month=6, day=19)
yesterday_new_format = yesterday.strftime("%Y%m%d")

# print(today)
# print(today_new_format)

pixel_creation_config = {
    "date": today_new_format,
    "quantity": input("How many commits did you did today?"),
    "optionalData": "{\"very optional key\":\"very optional value\"}",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# POST request: Posting a Pixel
# response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_config, headers=headers)
# print(response.text)



##################################################
############### Put a Pixel ######################
##################################################

# https://docs.pixe.la/entry/put-pixel

print("\n\n*** Putting a pixel ***")

# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

yyyyMMdd = 20240609
pixel_putting_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yyyyMMdd}"


print(today)
print(today_new_format)

pixel_putting_config = {
    "quantity": "17",
    "optionalData": "{\"very optional key\":\"very optional value\"}",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# PUT request: Put a Pixel
# response = requests.put(url=pixel_putting_endpoint, headers=headers, json=pixel_putting_config)
# print(response.text)



##################################################
############### Delete a Pixel ###################
##################################################

# https://docs.pixe.la/entry/delete-pixel

print("\n\n*** Deleting a pixel ***")

# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

yyyyMMdd = 20240609
pixel_deleting_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yyyyMMdd}"

headers = {
    "X-USER-TOKEN": TOKEN
}

# DELETE request: Delete a pixel
response = requests.delete(url=pixel_deleting_endpoint, headers=headers, json=pixel_deleting_endpoint)
print(response.text)