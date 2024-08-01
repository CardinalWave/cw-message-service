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

    def user_send(self, session: Session, message: Message):
        try:
            session = self.__find_session(session_id=session.session_id)
            message.group_id = session.group_id
            message.author = session.username
            self.__send_message(session=session, message=message)
            log_session(session, "send")
        except BadRequestError as e:
            log_error(e, e.message)
            raise BadRequestError('Falha no envio') from e

    def __find_session(self, session_id: str) -> Session:
        session = self.__session_manager.find_session(session_id=session_id)
        if session is None:
            raise NotFoundError
        return session

    def __send_message(self, session: Session, message: Message):
        try:
            self.__message_manager.forward_message(session=session, message=message)
        except BadRequestError as e:
            raise BadRequestError(str(e)) from BadRequestError
