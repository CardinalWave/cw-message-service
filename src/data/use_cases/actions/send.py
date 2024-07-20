from typing import Dict
from src.domain.models.message import Message
from src.domain.models.session import Session
from src.domain.use_cases.actions.send import SendInterface
from src.domain.use_cases.sessions.session_manager import SessionManagerInterface
from src.domain.use_cases.messages.message_manager import MessageManagerInterface
from src.data.erros.domain_errors import NotFoundError, BadRequestError


class Send(SendInterface):

    def __init__(self, session_manager: SessionManagerInterface, message_manager: MessageManagerInterface):
        self.__session_manager = session_manager
        self.__message_manager = message_manager

    def user_send(self, session: Session, message: Message) -> Dict:
        session = self.__find_session(session.session_id)
        message.group_id = session.group_id
        message_sent = self.__message_manager.forward_message(message=message)
        return message_sent.to_dict()

    def __find_session(self, session_id: str) -> Session:
        session = self.__session_manager.find_session(session_id=session_id)
        if session is None:
            raise NotFoundError
        return session

    def __send_message(self, message: Message, group_id: str):
        try:
            self.__message_manager.forward_message(message=message)
        except BadRequestError as e:
            raise BadRequestError(str(e)) from BadRequestError
