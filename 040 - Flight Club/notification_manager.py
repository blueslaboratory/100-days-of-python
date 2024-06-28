# 27/06/2024
# Day - 040

# This class is responsible for sending notifications 
# with the deal flight details.

##################################################
# DAY 40 PROJECT: SOLUTION


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
        """
        # Retrieve environment variables only once
        self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
        self.email = os.environ["MY_EMAIL"]
        self.email_password = os.environ["MY_EMAIL_PASSWORD"]
        self.twilio_virtual_number = os.environ["TWILIO_VIRTUAL_NUMBER"]
        self.twilio_verified_number = os.environ["TWILIO_VERIFIED_NUMBER"]
        self.whatsapp_number = os.environ["TWILIO_WHATSAPP_NUMBER"]
        
        # Set up Twilio Client and SMTP connection
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])
        self.connection = smtplib.SMTP(os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"])
        """
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


    def send_email(self, email_list, message_body):

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=sender, password=pw)
            
            for email in email_list:
                # Create a MIMEText object for each email
                msg = MIMEMultipart()
                msg['From'] = sender
                msg['To'] = email
                msg['Subject'] = "Low price alert!"

                msg.attach(MIMEText(message_body, 'plain', 'utf-8'))

                connection.sendmail(
                    from_addr=sender,
                    to_addrs=email,
                    msg=msg.as_string()
                )