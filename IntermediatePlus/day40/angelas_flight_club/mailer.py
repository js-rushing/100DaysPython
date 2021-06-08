import smtplib
from pprint import pprint
from config import MAILTRAP_USER, MAILTRAP_PASS, SHEETY_PRICES_ENDPOINT, ENVIRONMENT

class Mailer:
    def __init__(self, message):
        self.message = message
        self.users = self.get_users()

    def get_users(self):
        if ENVIRONMENT == "Production":
            response = requests.get(url=f"{SHEETY_PRICES_ENDPOINT}/users")
            data = response.json()
            self.users = data["users"]
        else:
            self.users = [
                {'firstName': 'John', 'lastName': 'Doe', 'email': 'jdoe@email.com', 'id': 2},
                {'firstName': 'Wanda', 'lastName': 'Jones', 'email': 'wjones@email.com', 'id': 3},
                {'firstName': 'Dario', 'lastName': 'Smith', 'email': 'dsmith@email.com', 'id': 4},
            ]
        return self.users

    def send_mail(self):
        sender_address = "Private Person <from@example.com"

        for user in self.users:
            message = f"Subject: Cheap Flights!\n\nHello, {user['firstName']}\n\n{self.message}"
            receiver_address = "A Test User <to@example.com>"
            connection = smtplib.SMTP("smtp.mailtrap.io", 2525)
            connection.starttls()
            connection.login(user=MAILTRAP_USER, password=MAILTRAP_PASS)
            connection.sendmail(
                from_addr=sender_address,
                to_addrs=receiver_address,
                msg=message
            )
            connection.close()

