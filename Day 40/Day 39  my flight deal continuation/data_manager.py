import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv


load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = os.getenv("MY_ENV_SHEETY_USER")
        self._password = os.getenv("MY_ENV_SHEETY_PASSWORD")
        self._sheety_endpoint = os.getenv("MY_ENV_SHEETY_PRICES_ENDPOINT")
        self.users_endpoint = os.getenv("MY_ENV_SHEETY_USERS_ENDPOINT")
        self.authentication = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customer_data = {}



    def get_destination_data(self):
        sheety_response = requests.get(url=self._sheety_endpoint, auth=self.authentication)
        data = sheety_response.json()
        print("DEBUG RESPONSE:", data)  # <-- Add this for debugging
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):

        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city["iataCode"],
                }
            }
            sheety_response = requests.put(
                 url=f"{self._sheety_endpoint}/{city["id"]}",
                 json=new_data,
                 auth=self.authentication
            )

            print(sheety_response.text)
    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint, auth=self.authentication)
        data = response.json()
        # See how Sheet data is formatted so that you use the correct column name!
        # pprint(data)
        # Name of spreadsheet 'tab' with the customer emails should be "users".
        self.customer_data = data["users"]
        print("DEBUG RESPONSE in customer data:", data)  # <-- Add this for debugging
        return self.customer_data








