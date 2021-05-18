import requests
import datetime as dt
from not_for_git import MY_LAT, MY_LNG, UTC_OFFSET

time_now = dt.datetime.now()

params = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "date": time_now,
    "formatted": "0"
}


def convert_to_local(hour):
    if hour <= 5:
        hour += 12
    hour += UTC_OFFSET
    return hour


def is_dark():
    if time_now.hour > sunset_hour + 12:
        return True
    else:
        return False


res = requests.get("https://api.sunrise-sunset.org/json", params=params)
data = res.json()

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
sunset_hour = int(sunset.split("T")[1].split(":")[0])

sunrise_hour = convert_to_local(sunrise_hour)
sunset_hour = convert_to_local(sunset_hour)

print(sunrise_hour)
print(sunset_hour)
print(time_now.hour)

if is_dark():
    print("dark")
else:
    print("not dark")
