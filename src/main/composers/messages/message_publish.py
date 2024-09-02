from src.data.use_cases.messages.message_publish import MessagePublish
from src.main.mqtt.mqtt_conn import MQTTClient
from src.config.config import Config


def message_publish_composer():
    ip = Config.MQTT_BROKER_IP
    port = Config.MQTT_BROKER_PORT
    mqtt_c = MQTTClient(ip=ip, port=port)
    use_case = MessagePublish(mqtt_c)

    return use_case
