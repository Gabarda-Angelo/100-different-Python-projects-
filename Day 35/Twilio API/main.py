
import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()  # Loads .env from project root

MY_LATITUDE = float(os.getenv("MY_LATITUDE"))
MY_LONGITUDE = float(os.getenv("MY_LONGITUDE"))
MAX_RAINY_RANGE_CODE = int(os.getenv("MAX_RAINY_RANGE_CODE"))
OWM_Endpoint = os.getenv("OWM_Endpoint")
api_key = os.getenv("OWM_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid":api_key,
    "cnt":4,  #cnt, a number of time stamps, read the documentation of API for more info

}
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()



# def raining():
number_of_timestamps = len(data['list'])
will_rain = False
for i in range(number_of_timestamps):
    weather_condition_code = data["list"][i]["weather"][0]["id"]
    date_time = data["list"][i]["dt_txt"]
    description = data["list"][i]["weather"][0]["description"]
    if weather_condition_code < MAX_RAINY_RANGE_CODE:
        will_rain = True


client = Client(account_sid, auth_token)
if will_rain:

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's going to rain today, don't forget to bring umbrella ☂️",
        to='whatsapp:+639669335611'
    )
else:
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's not going to rain today",
        to='whatsapp:+639669335611'
    )







