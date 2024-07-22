from src.domain.models.session import Session
from src.domain.use_cases.actions.join import JoinInterface
from src.domain.use_cases.messages.message_manager import MessageManagerInterface
from src.domain.use_cases.sessions.session_manager import SessionManagerInterface


class Join(JoinInterface):

    def __init__(self, message_manager: MessageManagerInterface,
                 session_manager: SessionManagerInterface):
        self.__message_manager = message_manager
        self.__session_manager = session_manager

    def user_join(self, session: Session):
        self.__session_manager.register_session(session)
        self.__message_manager.inbox(session=session)
