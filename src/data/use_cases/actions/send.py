from datetime import datetime
from src.main.logs.logs import log_error, log_session
from src.domain.models.message import Message
from src.domain.models.session import Session
from src.domain.use_cases.actions.send import SendInterface
from src.domain.use_cases.sessions.session_manager import SessionManagerInterface
from src.domain.use_cases.messages.message_manager import MessageManagerInterface
from src.data.erros.domain_errors import NotFoundError, BadRequestError


class Send(SendInterface):

    def __init__(self, session_manager: SessionManagerInterface,
                 message_manager: MessageManagerInterface):
        self.__session_manager = session_manager
        self.__message_manager = message_manager

    def user_send(self, session_id: str, message_payload: str):
        try:
            session = self.__find_session(session_id=session_id)
            self.__send_message(session=session, message_payload=message_payload)
            log_session(session.to_dict(), "send")
        except BadRequestError as e:
            log_error(e, e.message)
            raise BadRequestError('Falha no envio') from e

    def __find_session(self, session_id: str) -> Session:
        session = self.__session_manager.find_session(session_id=session_id)
        if session is None:
            raise NotFoundError
        return session

    def __send_message(self, session: Session, message_payload: str):
        try:
            message = Message(message_id="",
                              group_id=session.group_id,
                              author=session.username,
                              send_time=str(datetime.now()),
                              payload=message_payload)
            for _ in self.__session_manager.list_current_sessions(session.group_id):
                self.__message_manager.forward_message(session=_, message=message)
        except BadRequestError as e:
            raise BadRequestError(str(e)) from BadRequestError
