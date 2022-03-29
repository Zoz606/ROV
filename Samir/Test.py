import paho.mqtt.client as imqtt
import time
from IoT_Utils import *
from AI_Motion import *

# Global Variables
connected = False
port = 1883
broker_addr = "127.0.0.1"
#broker_addr = "192.168.8.101"
#broker_addr = "192.168.43.206"
#broker_addr = "192.168.8.103"
#broker_addr = "192.168.1.9"

# client init
client = mqtt.Client("HQ")
client.on_connect = on_connect
client.on_message = on_message

# connect client
print("Client Connecting")
client.connect(broker_addr, port=port)
client.loop_start()
time.sleep(2)
    
# client subscribe
client.subscribe("status")
client.subscribe("x")
client.subscribe("y")
client.subscribe("z")

client.publish("status", "1")


done = False
x1, y1, z1 = 0, 0, 0

while not done:
    motion = get_motion()
    if motion[0] == x1:
        client.publish("x", str(motion[0]))
        x1 = -(~x1)

    if motion[1] == y1:
        client.publish("y", str(motion[1]))
        y1 = -(~y1)

    if motion[2] == z1:
        client.publish("z", str(motion[2]))
        z1 = -(~z1)
