import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT Broker!")
        print("⌛️ Waiting For File Data From Writer")
    else:
        print("❌ Failed to connect, return code %d\n", rc)

def on_message(client, userdata, message):
    print("✅ Status received " ,str(message.payload.decode("utf-8")))

client = mqtt.Client("aniruddha-mqtt-reader")
client.on_connect = on_connect
client.on_message=on_message
print('⌛️ Trying to Connect')
client.connect("broker.hivemq.com")

# client.loop_start()
client.subscribe("file/status")
client.loop_forever()
# time.sleep(5)