import requests
from datetime import datetime, timedelta
import smtplib
import time

# ---------------------- CONFIGURATION ---------------------- #
MY_LAT = 14.753738  # Your latitude
MY_LONG = 121.053606  # Your longitude
MY_EMAIL = "agabarda451@gmail.comm"
MY_PASSWORD = "zjkx unua ivup ejbz"

# ---------------------- CHECK ISS POSITION ---------------------- #
def is_iss_overhead():
    """Check if the ISS is within ±5° of your location."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if ISS is close to your location(This code could create rectangular curvature that if ISS enter to it you could see it
    return (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and \
           (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5)

# ---------------------- CHECK IF IT'S DARK ---------------------- #
def is_night():
    """Check if it's currently dark at your location."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

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


    # Get current Philippine time
    time_now = datetime.utcnow() + philippine_offset


    return time_now >= sunset_ph or time_now <= sunrise_ph

# ---------------------- SEND EMAIL ---------------------- #
def send_email():
    """Send yourself an email when ISS is visible."""
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="gelo.gabarda@gmail.com",
            msg="Subject: Look Up 👆\n\nThe ISS is above you in the sky! 🚀"
        )

# ---------------------- MAIN LOOP ---------------------- #
while True:
    time.sleep(60)  # Check every 60 seconds
    if is_iss_overhead() and is_night():
        send_email()
        print("Email sent! The ISS is overhead 🌌")
    else:
        print("No ISS visible right now.")
