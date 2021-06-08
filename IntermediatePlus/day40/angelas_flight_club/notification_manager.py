from twilio.rest import Client
from config import ENVIRONMENT, \
    TWILIO_SID, \
    TWILIO_AUTH_TOKEN, \
    TWILIO_VIRTUAL_NUMBER, \
    TWILIO_VERIFIED_NUMBER


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        if ENVIRONMENT == "Production":
            message = self.client.messages.create(
                body=message,
                from_=TWILIO_VIRTUAL_NUMBER,
                to=TWILIO_VERIFIED_NUMBER,
            )
            # Prints if successfully sent.
            print(f"Text sent: {message.sid}")
        else:
            print(f"Dev Mode: {message}")
