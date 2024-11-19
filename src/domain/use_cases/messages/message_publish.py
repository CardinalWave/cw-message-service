from abc import ABC, abstractmethod
from src.domain.models.message import Message
from src.domain.models.session import Session


class MessagePublishInterface(ABC):

    @abstractmethod
    def handle_message(self, session: Session, message: Message): pass
