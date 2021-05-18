import smtplib
import datetime as dt
from random import choice
from not_for_git import MAILTRAP_USER, MAILTRAP_PASS

SENDER_ADDRESS = "Private Person <from@example.com>"
USER = MAILTRAP_USER
PASSWORD = MAILTRAP_PASS
MAILING_DAY = 0
TODAY = dt.datetime.now().weekday()
FRIDAY = dt.datetime(year=2021, month=2, day=12).weekday()
WEDNESDAY = dt.datetime(year=2021, month=4, day=14).weekday()


def send_mail(receiver_address, msg):
    connection = smtplib.SMTP("smtp.mailtrap.io", 2525)
    connection.starttls()
    connection.login(user=USER, password=PASSWORD)
    connection.sendmail(
        from_addr=SENDER_ADDRESS,
        to_addrs=receiver_address,
        msg=f"Subject: Hello!\n\n{msg}")
    connection.close()


def get_quote():
    with open("quotes.txt") as file:
        quotes = file.readlines()
        return choice(quotes)


def date_match(date):
    if date == MAILING_DAY:
        return True
    else:
        return False


# Test date_time() function
# print("match") if date_match(TODAY) else print("no match")
# print("match") if date_match(WEDNESDAY) else print("no match")
# print("match") if date_match(FRIDAY) else print("no match")

message = get_quote()
if date_match(TODAY):
    send_mail("A Test User <to@example.com>", message)
