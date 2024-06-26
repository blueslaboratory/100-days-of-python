# 26/06/2024
# Day - 039

# This class is responsible for talking to the Google Sheet.

##################################################
# DAY 39 PROJECT: SOLUTION

from pprint import pprint
import os
import requests
from requests.auth import HTTPBasicAuth

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/011da807f98f271a5006c9f3feb4bf0b/flightDeals/prices"


class DataManager:
    
    def __init__(self):
        # self._user = os.environ["SHEETY_USRERNAME"]
        # self._password = os.environ["SHEETY_PASSWORD"]
        # self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.headers = {
            "Authorization": "Bearer tokensito"
        }

    def get_destination_data(self):
        
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data, headers=self.headers)
            print(response.text)
    
    
    
    
    # COMMENTED
    # sheety_endpoint = "https://api.sheety.co/011da807f98f271a5006c9f3feb4bf0b/flightDeals/prices"

    # headers = {
    #     "Authorization": "Bearer tokensito"
    # }

    # def get_sheet_data(self):
    #     response = requests.get(url=self.sheety_endpoint, headers=self.headers)
    #     data_json = response.json()
        
    #     if response.status_code == 200:
    #         return data_json
    #     else:
    #         return None