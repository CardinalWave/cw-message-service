#pylint: disable=no-else-return
import time
import paho.mqtt.client as mqtt


class MQTTClient:
    def __init__(self, ip: str, port: int):
        self.broker_ip = ip
        self.broker_port = port
        self.client = mqtt.Client()
        self.client_connect()
        self.client.loop_start()

    def client_connect(self):
        self.client.connect(self.broker_ip, self.broker_port)

    def publish_message(self, topic, message):
        retries = 0
        max_retries = 3
        retry_delay = 5
        while retries < max_retries:
            result = self.client.publish(topic, message)
            if result.rc == mqtt.MQTT_ERR_SUCCESS:
                print(f"Success: {topic} - {message}")
                return True
            else:
                self.client_connect()
                print(f"Failed - {result.rc} - Tryin:  {retries + 1}")
                retries += 1
                if retries < max_retries:
                    self.client.reconnect()
                    time.sleep(retry_delay)
        print(f"Failed to publish - {topic} : {message}")
        return False

    def close_connection(self):
        self.client.disconnect()
