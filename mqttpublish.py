#!/usr/bin/env python
import paho.mqtt.client as mqtt
import time
import random

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

client = mqtt.Client("myclient")
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.username_pw_set("daniel", password="12312415q23413")
client.connect("localhost") #connect to broker
client.loop_start() #start the loop
# print("Subscribing to topic #")
# client.subscribe("#")
print("Publishing message to topic","house/bulbs/bulb1")

randint = random.randint(0,10)
client.publish("house/bulbs/bulb1", str(randint))
time.sleep(1) # wait
# try:
# 	while(True):
# 		pass
# except KeyboardInterrupt:
# 	pass
client.loop_stop() #stop the loop