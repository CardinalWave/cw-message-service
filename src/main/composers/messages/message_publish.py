from src.data.use_cases.messages.message_publish import MessagePublish
from src.main.logs.logs import Log
from src.main.mqtt.mqtt_conn import MQTTClient
from src.config.config import Config


def message_publish_composer():
    logger = Log()
    ip = Config.MQTT_BROKER_IP
    port = Config.MQTT_BROKER_PORT
    mqtt_c = MQTTClient(ip=ip, port=port)
    use_case = MessagePublish(mqtt_c, logger)

    return use_case
