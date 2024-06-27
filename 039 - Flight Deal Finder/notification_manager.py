# 26/06/2024
# Day - 039

# This class is responsible for sending notifications 
# with the deal flight details.

##################################################
# DAY 39 PROJECT: SOLUTION


import os
from twilio.rest import Client
# pip install twilio

# Email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "titiritest@gmail.com"
receiver = sender
pw = "pknf dczx zfpd qleg"

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        # self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])
        pass

    def send_sms(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.
        
        Parameters:
        message_body (str): The text content of the SMS message to be sent.
        
        Returns:
        None
        
        Notes:
        - Ensure that `TWILIO_VIRTUAL_NUMBER` and `TWILIO_VERIFIED_NUMBER` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VIRTUAL_NUMBER"]
        )
        # Prints if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)


    def send_email(self, message_body):
        # Encode the message in UTF-8
        message = message_body.encode('utf-8')

        # Create a MIMEText object to represent the email
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = sender
        msg['Subject'] = "Low price alert!"

        msg.attach(MIMEText(message, 'plain', 'utf-8'))

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender, password=pw)
            connection.sendmail(
                from_addr=msg['From'],
                to_addrs=msg['To'],
                msg=msg.as_string()
            )