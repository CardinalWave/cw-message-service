from datetime import datetime
from uuid import uuid1
from src.domain.models.message import Message
from src.domain.use_cases.messages.message_manager import MessageManagerInterface


class MessageManagerSpy(MessageManagerInterface):

    def inbox(self, group_id: str) -> list[Message]:
        messages = [Message(message_id=str(uuid1()),
                            group_id="a1a9f26c-514f-41f0-9df0-2c8eff8fd456",
                            send_time=datetime.now(),
                            author="Test1",
                            payload="Ola Mundo!"),

                    Message(message_id=str(uuid1()),
                            group_id="a1a9f26c-514f-41f0-9df0-2c8eff8fd456",
                            send_time=datetime.now(),
                            author="Test1",
                            payload="Ola Mundo!231")
                    ]
        return messages

    def forward_message(self, message: Message):
        return message
