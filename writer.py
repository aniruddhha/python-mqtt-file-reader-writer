import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT Broker!")
        print('⌛️ Sending Data To Reader')
        data = readFileData()
        client.publish("file/status",data)
       
    else:
        print("❌ Failed to connect, return code %d\n", rc)

def on_publish(client, userdata, qos):
    print('✅ File Data Sent To Reader')

def connectAndStart():
    client = mqtt.Client("aniruddha-mqtt-writer")
    client.on_connect = on_connect
    print('⌛️ Trying to Connect')
    client.connect("broker.hivemq.com")
    client.on_publish = on_publish
    client.loop_forever()

def readFileData():
    print('⌛️ Reading File')
    file = open('file.txt',mode='r')
    data = file.readline()
    print(f'👉 File Data: {data}')
    return data

def main():
    connectAndStart()

if __name__ == "__main__":
    main()
    

