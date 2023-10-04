import requests
from twilio.rest import Client

ONW_Endpoint = "https://api.openwathermap.org/data/2.5/onecall"
api_key = ""

account_sid = ""
auth_token = ""

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(ONW_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella",
        from="+245.....",
        to="+254...........",
    )
    







