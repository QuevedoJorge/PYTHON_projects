import requests
from twilio.rest import Client

# OWM
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "b9e6785820f8f9d4f9de56a88bb43126"
# Twilio
account_sid = "ACbec987c87aa8182d54d36ad8bb22e90a"
auth_token = '686b046163117f5f941661f9505375b3'

# Params
weather_params = {
    "lat": "-12.189961",
    "lon": "-77.012028",
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

general_list = weather_data["list"]
will_rain = False

for list_item in general_list:
    for weather in list_item["weather"]:
        if weather["id"] < 700:
            will_rain = True
            break

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today, take care!",
        to="whatsapp:+51965423871"
    )
else:
    print("It won't be rain😎")
