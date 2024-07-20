import datetime
from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models.message import Message


class MessageManagerInterface(ABC):

    @abstractmethod
    def inbox(self, group_id: str) -> list[Dict]: pass

    @abstractmethod
    def forward_message(self, message: Message) -> Message: pass
