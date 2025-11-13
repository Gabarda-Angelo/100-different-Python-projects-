#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
from datetime import timedelta, datetime

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_destination_data()


# Set your origin airport
ORIGIN_GENERAL_CITY_IATA = "LON" #LON as the general destination "London"
ORIGIN_SPECIFIC_CITY_IATA = "LHR"  #London Heathrow International Airport (LHR)  LHR is the specific IATA airport code for London Heathrow Airport.
# ==================== Update the Airport IATA Codes in Google Sheet ====================

for row in sheet_data:
    if row["iataCode"] == "":
        print("yes iata code is empty!")
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)

print(f"sheet_data:\n {sheet_data}")

data_manager.update_destination_codes()

# ==================== Search for Flights ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_GENERAL_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    '''
        Try this codes if you want to send you the current cheap price its found.
        but not less than in the google sheets price.

    '''
    # if flights is None or not flights['data']:
    #     #dont send text message
    #      pass
    # else:
    #     '''
    #     If you want you could only send a message if the cheapest flight you find here now
    #     is less than the usual flight price you list on your google sheet Flight Deals.
    #     (make sure it's connected to Sheety API to alter your Google Sheet Flight Deals)
    #     '''
    #     notification_manager.send_notification_message(ORIGIN_SPECIFIC_CITY_IATA,cheapest_flight , destination['iataCode'])
    '''
    if the cheapest flight you find here now
    is less than the usual flight price you list on your google sheet Flight Deals.
    try to change the google sheets price to see it
    '''
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        notification_manager.send_notification_message(
            ORIGIN_SPECIFIC_CITY_IATA, cheapest_flight, destination['iataCode'])

    # Slowing down requests to avoid rate limit
    time.sleep(2)






