from abc import ABC
from src.domain.models.session import Session
from src.domain.models.message import Message


class SendInterface(ABC):

    def user_send(self, session_id: str, message_payload: str): pass
