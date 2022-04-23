from twilio.rest import Client
import smtplib

TWILIO_SID = "AC6761d771f927f7cedd19c74f38fc9ec8"
TWILIO_AUTH_TOKEN = "b90dfb1eb19d9e11754de8b507393dde"
TWILIO_VIRTUAL_NUMBER = "+16204989396"
TWILIO_VERIFIED_NUMBER = "+16478839992"
# MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
# MY_EMAIL = YOUR EMAIL
# MY_PASSWORD = YOUR PASSWORD


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    # def send_emails(self, emails, message, google_flight_link):
    #     with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
    #         connection.starttls()
    #         connection.login(MY_EMAIL, MY_PASSWORD)
    #         for email in emails:
    #             connection.sendmail(
    #                 from_addr=MY_EMAIL,
    #                 to_addrs=email,
    #                 msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
    #             )