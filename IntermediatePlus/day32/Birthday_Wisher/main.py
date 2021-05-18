# Extra Hard Starting Project #

import smtplib
import datetime as dt
import pandas
from random import randint
from not_for_git import MAILTRAP_USER, MAILTRAP_PASS

SENDER_ADDRESS = "Private Person <from@example.com>"
USER = MAILTRAP_USER
PASSWORD = MAILTRAP_PASS

birthdays = pandas.read_csv("birthdays.csv")
today = dt.datetime.now()


def prepare_letter(recipient):
    with open(f"./letter_templates/letter_{randint(1, 3)}.txt") as file:
        content = file.read()
        letter_content = content.replace("[NAME]", recipient)
        return letter_content


def send_email(email, content):
    message = content
    connection = smtplib.SMTP("smtp.mailtrap.io", 2525)
    connection.starttls()
    connection.login(user=USER, password=PASSWORD)
    connection.sendmail(
        from_addr=SENDER_ADDRESS,
        to_addrs=email,
        msg=f"Subject: Happy Birthday!\n\n{message}")
    connection.close()


for (index, row) in birthdays.iterrows():
    if row["month"] == today.month and row["day"] == today.day:
        letter = prepare_letter(row["name"])
        send_email(row["email"], letter)
