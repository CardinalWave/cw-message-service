from abc import ABC, abstractmethod
from src.domain.models.message import Message
from src.infra.db.entities.message import Messages as MessagesEntity


class MessageRepositoryInterface(ABC):

    @abstractmethod
    def select_group(self, group_id: str) -> list[MessagesEntity]: pass

    @abstractmethod
    def save_message(self, message: Message): pass
