import requests
MY_LATITUDE = 14.7514
MY_LONGITUDE = 121.0517
MAX_RAINY_RANGE_CODE = 700
APP_ID = "OWM_KEY_REDACTED"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid":APP_ID,
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


if will_rain:
    print("it will rain on the next 12 hours")







