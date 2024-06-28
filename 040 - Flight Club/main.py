# 27/06/2024
# Day - 040

# This file will need to use the DataManager, FlightSearch,
# FlightData, NotificationManager classes to achieve the program
# requirements.

##################################################
# DAY 40 PROJECT: SOLUTION

print("\n*** Welcome to the Flight Deal Finder! ***")

import time
from datetime import datetime, timedelta
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager



# ==================== Set up the Flight Search ====================

# Create an instance of DataManager
data_manager = DataManager()
# Fetch the sheet data
sheet_data = data_manager.get_destination_data()
# Print the sheet data
pprint(sheet_data)
# Flight Search
flight_search = FlightSearch()
# Set your origin airport
ORIGIN_CITY_IATA = "MAD"
# Notification Manager
notification_manager = NotificationManager()



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



# ==================== Retrieve your customer emails ====================

customer_data = data_manager.get_customer_emails()
# Verify the name of your email column in your sheet. Yours may be different from mine
customer_email_list = [row["whatIsYourEmail?"] for row in customer_data]
# print(f"Your email list includes {customer_email_list}")



# ==================== Search for Flights ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:

    print(f"Getting flights for {destination['city']}...")

    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: {cheapest_flight.price}€")

    # Slowing down requests to avoid rate limit
    time.sleep(2)



    # ==================== Search for indirect flight if N/A ====================

    if cheapest_flight.price == "N/A":
        
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: {cheapest_flight.price}€")



    # ==================== Send SMS/Whatsapp/Email ====================

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        
        print(f"Check your email. Lower price flight found to {destination['city']}!")
        
        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only {cheapest_flight.price}€ to fly direct "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only {cheapest_flight.price}€ to fly "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"with {cheapest_flight.stops} stop(s) "\
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

        # Send SMS
        # notification_manager.send_sms(message_body=message)

        # SMS not working? Try whatsapp instead.
        # notification_manager.send_whatsapp(message_body=message)

        # Whatsapp not working? Try email, email never fails.
        notification_manager.send_email(email_list=customer_email_list, message_body=message)