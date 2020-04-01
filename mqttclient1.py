#!/usr/bin/env python
import paho.mqtt.client as mqtt
import time
import csv
import configparser

fieldnames = ["epochTime", "topic", "value"]

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        epoch_count = time.time()

        info = {
            "epochTime": epoch_count,
            "topic" : message.topic,
            "value": str(message.payload.decode("utf-8"))
        }
        print(info)
        csv_writer.writerow(info)

    print("message topic=",message.topic)
    # print("message qos=",message.qos)
    # print("message retain flag=",message.retain)

# with open('data.csv', 'w') as csv_file:
#     csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     csv_writer.writeheader()

config = configparser.ConfigParser()
config.read('credentials.conf')
username = config['credentials']['username']
password = config['credentials']['password']
host = config['credentials']['host']

print(username)
print(password)
print(host)

client = mqtt.Client("receiver")
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.username_pw_set(username, password=password)
client.connect(host) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic ")
# client.subscribe("Inverter/GridWatts")
client.subscribe("Inverter/LoadWatts")
try:
    while(True):
        pass
except KeyboardInterrupt:
    pass
client.loop_stop() #stop the loop