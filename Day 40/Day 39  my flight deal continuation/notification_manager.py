from dotenv import load_dotenv
import os
from twilio.rest import Client
import smtplib

# Load environment variables from .env file
load_dotenv()

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        # Retrieve environment variables only once
        self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
        self.email = os.environ["MY_EMAIL"]
        self.email_password = os.environ["MY_EMAIL_PASSWORD"]
        self.twilio_sid = os.getenv("TWILIO_ENV_SID")
        self.twilio_token = os.getenv("TWILIO_ENV_AUTH_TOKEN")
        self.twilio_virtual_number = os.environ["TWILIO_VIRTUAL_NUMBER"]
        self.whatsapp_number = os.environ["TWILIO_WHATSAPP_NUMBER"]


        self.connection = smtplib.SMTP(os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"], 587)

    def send_notification_message(self, message):
        try:
            client = Client(self.twilio_sid, self.twilio_token)

            message_obj = client.messages.create(
                from_=f'whatsapp:{self.twilio_virtual_number}',  # Twilio virtual number
                body=message,
                to=f'whatsapp:{self.whatsapp_number}'    # Your WhatsApp number
            )

            # ✅ Print for testing success
            print(f"✅ Message sent successfully! SID: {message_obj.sid}")
            print(f"📩 Message body: {message_obj.body}")
            print(f"📌 Status: {message_obj.status}")

        except Exception as e:
            print(f"❌ Failed to send message: {e}")

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )
