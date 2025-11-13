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
        self._sheety_endpoint = os.getenv("MY_ENV_SHEETY_ENDPOINT")
        self.authentication = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}



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






