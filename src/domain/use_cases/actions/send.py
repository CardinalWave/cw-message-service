from abc import ABC
from src.domain.models.session import Session
from src.domain.models.message import Message


class SendInterface(ABC):

    def user_send(self, session: Session, message: Message): pass
