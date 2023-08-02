import paho.mqtt.client as mqtt

# Callbacks
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("czujnik1/DS") # Replace with your topic

def on_message(client, userdata, msg):
    print(f"Message received on {msg.topic}: {msg.payload.decode()}")

# Create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("pi", "raspberr")
# Connect to the broker
client.connect("192.168.2.10", 1883, 60)  # Replace with your broker address and port

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()