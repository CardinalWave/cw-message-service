from abc import ABC, abstractmethod
from src.domain.models.session import Session


class JoinInterface(ABC):

    @abstractmethod
    def user_join(self, session: Session): pass
