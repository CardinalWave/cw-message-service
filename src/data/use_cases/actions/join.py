from typing import Dict
from src.domain.models.session import Session
from src.domain.use_cases.actions.join import JoinInterface
from src.domain.use_cases.messages.message_manager import MessageManagerInterface
from src.domain.use_cases.sessions.session_manager import SessionManagerInterface


class Join(JoinInterface):

    def __init__(self, message_manager: MessageManagerInterface, session_manager: SessionManagerInterface):
        self.__message_manager = message_manager
        self.__session_manager = session_manager

    def user_join(self, session: Session) -> list[Dict]:
        group_id = session.group_id
        self.__session_manager.register_session(session)
        inbox_message = self.__message_manager.inbox(group_id=group_id)
        return inbox_message
