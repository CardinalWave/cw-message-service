from src.domain.use_cases.actions.leave import LeaveInterface
from src.domain.use_cases.sessions.session_manager import SessionManagerInterface


class Leave(LeaveInterface):

    def __init__(self, session_manager: SessionManagerInterface):
        self.__session_manager = session_manager

    def user_leave(self, session_id: str):
        session = self.__session_manager.find_session(session_id=session_id)
        self.__session_manager.delete_session(session)
