import requests
import config
from twilio.rest import Client

parameters = {
    "lat": config.my_lat,
    "lon": config.my_long,
    "appid": config.api_key,
    "units": "metric",
    "cnt": 30
}

response = requests.get(url=config.OWM_Endpoint, params=parameters)
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
    client = Client(config.account_sid, config.auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔︎.",
        from_=config.from_phone_number,
        to=config.to_phone_number
    )
    print(message.status)
