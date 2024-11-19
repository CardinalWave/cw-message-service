from src.domain.use_cases.actions.leave import LeaveInterface
from src.domain.use_cases.sessions.session_manager import SessionManagerInterface
from src.data.erros.domain_errors import BadRequestError
from src.main.logs.logs_interface import LogInterface


class Leave(LeaveInterface):

    def __init__(self, session_manager: SessionManagerInterface,
                 logger: LogInterface):
        self.__session_manager = session_manager
        self.__logger = logger

    def user_leave(self, session_id: str):
        try:
            session = self.__session_manager.find_session(session_id=session_id)
            self.__session_manager.delete_session(session)
            self.__logger.log_session(session.to_dict(), "leave")
        except BadRequestError as e:
            self.__logger.log_error(e, e.message)
            raise BadRequestError('Usuario nao encontrado') from e
