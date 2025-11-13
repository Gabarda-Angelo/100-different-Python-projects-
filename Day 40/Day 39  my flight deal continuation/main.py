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

# data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# ==================== Retrieve your customer emails ====================

customer_data = data_manager.get_customer_emails()
print("DEBUG RESPONSE in customer data:", customer_data)  # <-- Add this for debugging
# Verify the name of your email column in your sheet. Yours may be different from mine
customer_email_list = [row["whatIsYourEmail?"] for row in customer_data]
# print(f"Your email list includes {customer_email_list}")

# ==================== Search for direct flights ====================

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
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    # ==================== Search for indirect flight if N/A ====================

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_GENERAL_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: £{cheapest_flight.price}")

    # ==================== Send Notifications and Emails  ====================
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
    # ==================== Send Notifications and Emails  ====================
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly direct " \
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly " \
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                      f"with {cheapest_flight.stops} stop(s) " \
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

        #send notification via whatsap
        notification_manager.send_notification_message(message)

        # Send emails to everyone on the list
        notification_manager.send_emails(email_list=customer_email_list, email_body=message)








