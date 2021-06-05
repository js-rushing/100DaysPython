from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER, PERSONAL_NUMBER


class NotificationManager:
    def __init__(self, data):
        self.data = data
        self.message = f"Hot Travel Deal!\n" \
                       f"{str(self.data['nights'])} nights in {str(self.data['arrCity'])}\n" \
                       f"Flight from {str(self.data['depCity'])} to {str(self.data['arrCity'])} " \
                       f"for only £{str(self.data['price'])}\n" \
                       f"Leaves {str(self.data['outDate'])} returns {str(self.data['inDate'])}"

    def send_text(self):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(body=self.message, from_=TWILIO_NUMBER, to=PERSONAL_NUMBER)
        print(self.message)
