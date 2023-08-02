import paho.mqtt.client as mqtt

#This is for testing code!!!!!!!!!!!

class MQTTClient:
    def __init__(self, broker_address, broker_port, username=None, password=None):
        self.client = mqtt.Client()
        self.client.username_pw_set(username, password)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.broker_address = broker_address
        self.broker_port = broker_port

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")

    def on_message(self, client, userdata, msg):
        print(f"Message received on {msg.topic}: {msg.payload.decode()}")

    def connect(self):
        self.client.connect(self.broker_address, self.broker_port, 60)
        self.client.loop_start()

    def disconnect(self):
        self.client.disconnect()

class Broker(MQTTClient):
    def __init__(self, broker_address, broker_port):
        super().__init__(broker_address, broker_port)

    def run(self):
        self.connect()
        while True:
            pass

class Publisher(MQTTClient):
    def __init__(self, broker_address, broker_port, username=None, password=None):
        super().__init__(broker_address, broker_port, username, password)

    def publish_message(self, topic, message):
        self.client.publish(topic, message)

class Subscriber(MQTTClient):
    def __init__(self, broker_address, broker_port, username=None, password=None):
        super().__init__(broker_address, broker_port, username, password)

    def subscribe_to_topic(self, topic):
        self.client.subscribe(topic)

    def run(self):
        self.connect()
        while True:
            pass

if __name__ == "__main__":
    broker_address = "192.168.2.10"
    broker_port = 1883
    username = "your_username"
    password = "your_password"

    broker = Broker(broker_address, broker_port)
    publisher = Publisher(broker_address, broker_port, username, password)
    subscriber = Subscriber(broker_address, broker_port, username, password)

    print("Choose an option:")
    print("1. Run broker")
    print("2. Publish message")
    print("3. Subscribe to topic")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        broker.run()
    elif choice == "2":
        topic = input("Enter the topic: ")
        message = input("Enter the message: ")
        publisher.publish_message(topic, message)
    elif choice == "3":
        topic = input("Enter the topic to subscribe: ")
        subscriber.subscribe_to_topic(topic)
        subscriber.run()
    else:
        print("Invalid choice. Exiting...")