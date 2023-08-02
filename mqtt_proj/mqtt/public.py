import paho.mqtt.client as mqtt
import time

def read_temp(sensor_id):
    with open("/sys/devices/w1_bus_master1/{}/temperature".format(sensor_id),"r") as f :
        data = f.read().strip()
    temp_c = int(data)/1000.0
    return temp_c

def on_publish(client,userdata,result):
    print("Data published")

client = mqtt.Client()
client.on_publish = on_publish
client.connect("192.168.2.10",1883,60)

while True:
    temperature = read_temp("10-000803312a8d")
    if temperature is not None:
        client.publish("czujnik1/DS","t={}".format(temperature))
    time.sleep(1)
