from src.data.use_cases.messages.message_publish import MessagePublish
from src.main.mqtt.mqtt_conn import MQTTClient


def message_publish_composer():
    mqtt_c = MQTTClient(ip="192.168.15.69", port=1883)
    use_case = MessagePublish(mqtt_c)

    return use_case
