from datetime import datetime
from src.domain.models.message import Message
from src.infra.db.entities.message import Messages as MessagesEntity
from src.infra.db.interfaces.message_repository import MessageRepositoryInterface


class MessageRepositorySpy(MessageRepositoryInterface):

    def select_group(self, group_id: str) -> list[MessagesEntity]:
        messages = [MessagesEntity(group_id="a1a9f26c-514f-41f0-9df0-2c8eff8fd456",
                                   send_time=datetime.now(),
                                   author="Test1",
                                   payload={"message": "Ola"}),
                    MessagesEntity(group_id="a1a9f26c-514f-41f0-9df0-2c8eff8fd456",
                                   send_time=datetime.now(),
                                   author="Test1",
                                   payload={"message": "Bom Dia"})
                    ]
        return messages

    def save_message(self, message: Message): pass
