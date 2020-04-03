#!/usr/bin/env python3

from datetime import datetime
import time
import os
from SimpleEmailer import Emailer
import socket

filename = "$HOME/Development/Python/MQTTClient/" + datetime.today().strftime('%d_%m_%Y') + ".csv"
print(filename)
# with open(filename, 'r') as csv_file:
#     data = csv_file.readlines()
#     last_string = data[-1]

last_string = os.popen('tail -n 1 %s' % filename).read()

print(last_string)

epochTime, topic, value = last_string.split(",")
currentEpochTime = time.time()
print("Current EpochTime", currentEpochTime)
timeDifference = float(currentEpochTime)-float(epochTime)
print("Time difference between last value:", timeDifference)

if (timeDifference > 600):
    print("Long since I got an update...")
    sender = Emailer()
    emailSubject = "Inverter Update outdated"
    emailContent = "Hi<br>\
    It's been %5.2f seconds since MQTT delivered\
    an update to the Raspberry Pi. <br>\
    Regards, Raspberry Pi Emailer %s" % (timeDifference, socket.gethostname())
    sender.sendmail(emailSubject, emailContent)

from os.path import expanduser
home = expanduser("~")

outfile = open(home + "/Development/Python/MQTTClient/watchdogtimer_lastupdate.log", 'a')
currentDatetime = datetime.today().strftime('%d_%m_%Y %H:%M:%S')
outfile.write(currentDatetime + ",diff: %f" % timeDifference + "\n")

