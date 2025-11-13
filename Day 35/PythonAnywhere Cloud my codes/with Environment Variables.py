#Notes this code is for PythonEverywhere Clouds, it might not work it here,
#Environment Variables - Hiding the codes values into the virtual environment so it will be secured and easy to use of team

import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import requests
from dotenv import load_dotenv   # <-- add this line

load_dotenv()                     # <-- load .env locally (optional on PythonAnywhere)

MY_LATITUDE = 15.37
MY_LONGITUDE = 120.30
MAX_RAINY_RANGE_CODE = 700
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key     = os.getenv("OWM_API_KEY")          # OpenWeather
account_sid = os.getenv("TWILIO_ACCOUNT_SID")  # <-- NEW
auth_token  = os.getenv("TWILIO_AUTH_TOKEN")   # <-- NEW

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


proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}
client = Client(account_sid, auth_token,http_client=proxy_client)
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







