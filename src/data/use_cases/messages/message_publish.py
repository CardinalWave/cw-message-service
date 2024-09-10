import json
from src.main.mqtt.mqtt_conn import MQTTClient
from src.domain.use_cases.messages.message_publish import MessagePublishInterface
from src.domain.models.message import Message
from src.domain.models.session import Session
from src.main.logs.logs import log_session


class MessagePublish(MessagePublishInterface):

    def __init__(self, mqtt_client: MQTTClient):
        self.__mqtt_client = mqtt_client

    def handle_message(self, session: Session, message: Message):
        topic = "/{}/{}/{}".format("server", session.device, session.session_id)

        params = json.dumps({
            "device_id": session.device,
            "session_id": session.session_id,
            "action": "send",
            "payload": {
                "message_id": str(message.message_id),
                "group_id": message.group_id,
                "author": message.author,
                "send_time": str(message.send_time),
                "payload": message.payload
            }
        })
        if self.__mqtt_client:
            self.__mqtt_client.publish_message(topic=topic, message=params)
            log_session(session=f'{params} - {topic}', action="publish_message")
