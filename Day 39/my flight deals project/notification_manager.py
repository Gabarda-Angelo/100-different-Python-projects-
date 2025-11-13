from dotenv import load_dotenv
import os
from twilio.rest import Client

# Load environment variables from .env file
load_dotenv()

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.twilio_sid = os.getenv("TWILIO_ENV_SID")
        self.twilio_token = os.getenv("TWILIO_ENV_AUTH_TOKEN")
        self.message = ""

    def send_notification_message(self,origin, data, destination):
        self.message = (f"-Low price alert! Only £{data.price} to\n"
                     f"fly from {origin} to {destination}, on {data.out_date}\n)"
                     f"until {data.return_date}.")
        try:
            client = Client(self.twilio_sid, self.twilio_token)

            message_obj = client.messages.create(
                from_='whatsapp:+14155238886',  # Twilio sandbox number
                body=self.message,
                to='whatsapp:+639669335611'    # Your WhatsApp number
            )

            # ✅ Print for testing success
            print(f"✅ Message sent successfully! SID: {message_obj.sid}")
            print(f"📩 Message body: {message_obj.body}")
            print(f"📌 Status: {message_obj.status}")

        except Exception as e:
            print(f"❌ Failed to send message: {e}")

# # --------------- TESTING ----------------
# notification_manager = NotificationManager()
# notification_manager.send_notification_message("from LHR","informations","Hello! This is a test from Twilio ✅")