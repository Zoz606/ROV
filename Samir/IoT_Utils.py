import paho.mqtt.client as mqtt
#
#
###callback functions
#
#
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Client Connected\n")
        client.publish("Status/HQ", "Connected")
    else:
        print("Client isn't Connected")
        #exit()

def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + "\t" + "Payload: " + str(msg.payload))



def main():
    return

if __name__ == '__main__':
    main()
    
