import requests
import datetime as dt
import smtplib
import time
from not_for_git import MY_LAT, \
    MY_LNG, \
    UTC_OFFSET, \
    MAILTRAP_USER, \
    MAILTRAP_PASS, \
    SENDER_ADDRESS, \
    RECIPIENT_ADDRESS

time_now = dt.datetime.now()

params = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "date": time_now,
    "formatted": "0"
}


def get_iss_position():
    iss_res = requests.get(url="http://api.open-notify.org/iss-now.json")

    iss_res.raise_for_status()

    iss_data = iss_res.json()
    longitude = float(iss_data["iss_position"]["longitude"])
    latitude = float(iss_data["iss_position"]["latitude"])
    iss_position = (latitude, longitude)
    print(iss_position)
    print(f"({MY_LAT}, {MY_LNG})")
    return iss_position


def is_overhead(position):
    if float(MY_LAT) - 5 < float(position[0]) < float(MY_LAT) + 5 \
            and float(MY_LNG) - 5 < float(position[1]) < float(MY_LNG) + 5:
        return True
    else:
        return False


def get_sun_times():
    sun_res = requests.get("https://api.sunrise-sunset.org/json", params=params)
    sun_data = sun_res.json()

    sunrise = sun_data['results']['sunrise']
    sunset = sun_data['results']['sunset']

    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])

    sunrise_hour = convert_to_local(sunrise_hour)
    sunset_hour = convert_to_local(sunset_hour)
    sun_times = (sunrise_hour, sunset_hour)
    return sun_times


def convert_to_local(hour):
    if hour <= 5:
        hour += 12
    hour += UTC_OFFSET
    return hour


def is_dark(sun_time_tuple):
    sunrise = sun_time_tuple[0]
    sunset = sun_time_tuple[1]
    if time_now.hour < sunrise or time_now.hour > sunset + 12:
        return True
    else:
        return False


def send_email():
    message = "Subject: ISS\n\nLook Up!"
    connection = smtplib.SMTP("smtp.mailtrap.io", 2525)
    connection.starttls()
    connection.login(user=MAILTRAP_USER, password=MAILTRAP_PASS)
    connection.sendmail(
        from_addr=SENDER_ADDRESS,
        to_addrs=RECIPIENT_ADDRESS,
        msg=message
    )
    connection.close()


while True:
    if is_dark(get_sun_times()) and is_overhead(get_iss_position()):
        print("Email Sent")
        send_email()
    else:
        print("Conditions not met.")
    time.sleep(60)
