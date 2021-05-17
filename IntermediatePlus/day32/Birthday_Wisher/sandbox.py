# ANGELA'S EXAMPLE MODIFIED TO WORK WITH mailtrap.io
import smtplib

user = "8ddd5f8e14c4a5"
password = "13b8b3ca446469"
sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"


connection = smtplib.SMTP("smtp.mailtrap.io", 2525)
connection.starttls()
connection.login(user=user, password=password)
connection.sendmail(
    from_addr=sender,
    to_addrs=receiver,
    msg="Subject:Hello\n\nThis is the body of my email.")
connection.close()


# THE WAY mailtrap.io SUGGESTS USING smtplib
# import smtplib
#
# sender = "Private Person <from@example.com>"
# receiver = "A Test User <to@example.com>"
#
# message = f"""\
# Subject: Hi Mailtrap
# To: {receiver}
# From: {sender}
#
# This is a test e-mail message."""
#
# with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
#     server.login("8ddd5f8e14c4a5", "13b8b3ca446469")
#     server.sendmail(sender, receiver, message)

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()
# minute = now.minute
# second = now.second
# microsecond = now.microsecond
# print(year)
# print(month)
# print(day)
# print(day_of_week)
# print(minute)
# print(second)
# print(microsecond)
#
# date_of_birth = dt.datetime(year=1975, month=8, day=24, hour=4)
# print(date_of_birth)
