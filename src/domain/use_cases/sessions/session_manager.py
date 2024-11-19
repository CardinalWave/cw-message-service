from abc import ABC, abstractmethod
from src.domain.models.session import Session


class SessionManagerInterface(ABC):

    @abstractmethod
    def find_session(self, session_id: str) -> Session: pass

    @abstractmethod
    def register_session(self, session: Session): pass

    @abstractmethod
    def delete_session(self, session: Session): pass

    @abstractmethod
    def list_current_sessions(self, group_id: str) -> list[Session]: pass
