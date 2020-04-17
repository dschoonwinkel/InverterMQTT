#!/usr/bin/env python3

import smtplib
import time
import configparser
 
config = configparser.ConfigParser()
config.read('/home/pi/Development/Python/InverterMQTT/emailcredentials.conf')
email = config['credentials']['email']
password = config['credentials']['password']
to_email = config['credentials']['to_email']

# 
# Based on tutorial: https://www.bc-robotics.com/tutorials/sending-email-using-python-raspberry-pi/
#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = email #change this to match your gmail account
GMAIL_PASSWORD = password  #change this to match your gmail password

class Emailer:
    def sendmail(self, subject, content, recipient=to_email):
         
        #Create Headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)
 
        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
 
        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
 
        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit
 
def main():
    sender = Emailer()
    emailSubject = "Hello World!"
    emailContent = "This is a test of my emailer class on Linux"
    sender.sendmail(emailSubject, emailContent)

if __name__ == '__main__':
    main()



