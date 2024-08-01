from src.main.mqtt.mqtt_conn import MQTTClient
from src.domain.use_cases.messages.message_publish import MessagePublishInterface
from src.domain.models.message import Message
from src.domain.models.session import Session


class MessagePublish(MessagePublishInterface):

    def __init__(self, mqtt_client: MQTTClient):
        self.__mqtt_client = mqtt_client

    def handle_message(self, session: Session, message: Message):
        topic = "/{}/{}/{}".format("server", session.device, session.session_id)
        self.__mqtt_client.publish_message(topic=topic, message=message.to_json())
