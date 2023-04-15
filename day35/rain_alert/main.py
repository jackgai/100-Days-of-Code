import requests
import config
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv("/Users/yizhigai/Desktop/python_environment_variables/.env")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": float(os.getenv("MY_LAT")),
    "lon": float(os.getenv("MY_LONG")),
    "appid": os.getenv("OWM_API_KEY"),
    "units": "metric",
    "cnt": 30
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]

weather = []
will_rain = False
for each_weather in weather_data[:min(len(weather_data), 10)]:
    weather_list = each_weather["weather"]
    for condition in weather_list:
        weather.append(condition["id"])

for weather_code in weather:
    if weather_code < 700:
        will_rain = True
        break

# if will_rain:
#     print("it will rain")

if will_rain:
    client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔︎.",
        from_=os.getenv("FROM_PHONE_NUMBER"),
        to=os.getenv("TO_PHONE_NUMBER")
    )
    print(message.status)
