import smtplib
import datetime as dt

SENDER_ADDRESS = "python.program@email.com"
USER = ""
PASSWORD = ""


def send_mail(receiver_address, message):
    connection = smtplib.SMTP("smtp.mailtrap.io", 2525)
    connection.starttls()
    connection.login(user=user, password=password)
    connection.sendmail(
        from_addr=SENDER_ADDRESS,
        to_addrs=receiver_address,
        msg=message)
    connection.close()
