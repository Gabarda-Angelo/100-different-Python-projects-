import requests
from datetime import datetime, timedelta

MY_LATITUDE = 14.753738
MY_LONGITUDE = 121.053606

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0,  # Get UTC time
}

# Get sunrise/sunset data from API
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# Extract UTC sunrise/sunset times
sunrise_utc = data["results"]["sunrise"]
sunset_utc = data["results"]["sunset"]

# Convert string → datetime (still in UTC)
sunrise_utc = datetime.fromisoformat(sunrise_utc.replace("Z", "+00:00"))
sunset_utc = datetime.fromisoformat(sunset_utc.replace("Z", "+00:00"))

# Convert UTC → Philippine Time (UTC+8)
philippine_offset = timedelta(hours=8)
sunrise_ph = sunrise_utc + philippine_offset
sunset_ph = sunset_utc + philippine_offset

# Show results
print("Sunrise in PH:", sunrise_ph.strftime("%I:%M %p"))
print("Sunset in PH :", sunset_ph.strftime("%I:%M %p"))

# Get current Philippine time
time_now = datetime.utcnow() + philippine_offset
print("Current PH Time:", time_now.strftime("%I:%M %p"))
z