import requests
from twilio.rest import Client
from not_for_git import API_KEY, \
    MY_LAT, \
    MY_LNG, \
    ACCOUNT_SID, \
    AUTH_TOKEN, \
    TWILIO_NUMBER, \
    PERSONAL_NUMBER

OWM_URL = "https://api.openweathermap.org/data/2.5/onecall"
PARAMS = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "exclude": "current,minutely,daily",
    "units": "imperial",
    "appid": API_KEY
}

rain_in_forecast = False

res = requests.get(OWM_URL, params=PARAMS)
res.raise_for_status()
weather_data = res.json()['hourly']

for weather_id in range(0, 11):
    if weather_data[weather_id]['weather'][0]['id'] < 700:
        rain_in_forecast = True

if rain_in_forecast:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(body="Rain is in the forecast.  Bring your umbrella.",
                                     from_=TWILIO_NUMBER,
                                     to=PERSONAL_NUMBER)
