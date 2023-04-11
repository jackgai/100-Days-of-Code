from datetime import datetime

import requests
import time
import smtplib
import config

MY_LAT = 35.181446  # Your latitude
MY_LONG = 136.906403  # Your longitude


def iss_is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if abs(MY_LAT - iss_latitude) > 5:
        return False
    if abs(MY_LONG - iss_longitude) > 5:
        return False
    return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour
    return hour_now <= sunrise or hour_now >= sunset


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    if iss_is_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(config.MY_EMAIL, config.MY_PASSWORD)
        connection.sendmail(
            from_addr=config.MY_EMAIL,
            to_addrs=config.MY_EMAIL,
            msg="Subject:Look Up☝️\n\nThe ISS is above you in the sky!"
        )
    time.sleep(60)
