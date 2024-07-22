from abc import ABC, abstractmethod


class LeaveInterface(ABC):

    @abstractmethod
    def user_leave(self, session_id: str): pass
