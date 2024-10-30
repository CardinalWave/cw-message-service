from abc import ABC, abstractmethod
from src.domain.models.message import Message
from src.domain.models.session import Session


class MessageManagerInterface(ABC):

    @abstractmethod
    def inbox(self, session: Session): pass

    @abstractmethod
    def forward_message(self, session: Session, message: Message): pass

    @abstractmethod
    def save_message(self, message: Message): pass
