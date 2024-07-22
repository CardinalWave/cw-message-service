import paho.mqtt.client as mqtt


class MQTTClient:
    def __init__(self, ip: str, port: int):
        self.broker_ip = ip
        self.broker_port = port
        self.client = mqtt.Client()
        self.client_connect()

    def client_connect(self):
        self.client.connect(self.broker_ip, self.broker_port)

    def publish_message(self, topic, message):

        self.client.publish(topic, message)

    def close_connection(self):
        self.client.disconnect()
