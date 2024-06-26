# 26/06/2024
# Day - 039

# This file will need to use the DataManager, FlightSearch, 
# FlightData, NotificationManager classes to achieve the program 
# requirements.

##################################################
# DAY 39 PROJECT: SOLUTION

print("\n*** Welcome to the Flight Deal Finder! ***")

from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
import time


# ==================== Set up the Flight Search ====================
# Create an instance of DataManager
data_manager = DataManager()
# Fetch the sheet data
sheet_data = data_manager.get_destination_data()
# Print the sheet data
pprint(sheet_data)
flight_search = FlightSearch()



# ==================== Update the Airport Codes in Google Sheet ====================

#  In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the API.
#  You should use the code you get back to update the sheet_data dictionary.

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()