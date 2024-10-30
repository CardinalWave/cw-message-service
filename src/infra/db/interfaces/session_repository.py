from abc import ABC, abstractmethod
from src.infra.db.entities.session import Sessions as SessionsEntity


class SessionRepositoryInterface(ABC):

    @abstractmethod
    def register_session(self, session_id: str, device: str, username: str, group_id: str): pass

    @abstractmethod
    def delete_session(self, session_id: str): pass

    @abstractmethod
    def list_sessions(self) -> list[SessionsEntity]: pass

    @abstractmethod
    def select_session(self, session_id: str) -> SessionsEntity: pass
