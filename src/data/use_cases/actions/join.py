from src.main.logs.logs import log_error, log_session
from src.domain.models.session import Session
from src.domain.use_cases.actions.join import JoinInterface
from src.domain.use_cases.messages.message_manager import MessageManagerInterface
from src.domain.use_cases.sessions.session_manager import SessionManagerInterface
from src.data.erros.domain_errors import BadRequestError


class Join(JoinInterface):

    def __init__(self, message_manager: MessageManagerInterface,
                 session_manager: SessionManagerInterface):
        self.__message_manager = message_manager
        self.__session_manager = session_manager

    def user_join(self, session: Session):
        try:
            self.__session_manager.register_session(session)
            self.__message_manager.inbox(session=session)
            log_session(session, 'join')
        except Exception as e:
            log_error(e, 'Usuario ja logado')
            raise BadRequestError('Usuario ja logado') from e
