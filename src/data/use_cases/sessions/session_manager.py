from src.main.logs.logs import log_warning
from src.domain.models.session import Session
from src.domain.use_cases.sessions.session_manager import SessionManagerInterface
from src.infra.db.interfaces.session_repository import SessionRepositoryInterface
from src.data.erros.domain_errors import BadRequestError, InternalServerError, NotFoundError


class SessionManager(SessionManagerInterface):

    def __init__(self, session_repository: SessionRepositoryInterface):
        self.__session_repository = session_repository

    def register_session(self, session: Session):
        try:
            self.__session_repository.register_session(session_id=session.session_id,
                                                       group_id=session.group_id,
                                                       username=session.username,
                                                       device=session.device)
        except BadRequestError as e:
            log_warning(e, "Error to register session")
            raise BadRequestError() from e
        except InternalServerError as e:
            log_warning(e, "Error to register session")
            raise InternalServerError() from e

    def delete_session(self, session: Session):
        try:
            self.__session_repository.delete_session(session.session_id)
        except BadRequestError as e:
            log_warning(e, "Error to delete session")
            raise BadRequestError(str(e)) from e
        except InternalServerError as e:
            log_warning(e, "Error to delete session")
            raise InternalServerError(str(e)) from e

    def list_current_sessions(self, group_id: str) -> list[Session]:
        sessions_entity = self.__session_repository.list_sessions()
        try:
            group_current_sessions = [
                Session(session_id=session.session_id,
                        group_id=session.group_id,
                        username=session.username,
                        device=session.device)
                for session in sessions_entity if session.group_id == group_id
            ]
            return group_current_sessions
        except BadRequestError as e:
            log_warning(e, "Error to return list")
            raise BadRequestError(str(e)) from e

    def find_session(self, session_id: str) -> Session:
        try:
            session_entity = self.__session_repository.select_session(session_id)
            session = Session(session_id=session_entity.session_id,
                              group_id=session_entity.group_id,
                              username=session_entity.username,
                              device=session_entity.device)
            return session
        except Exception as e:
            log_warning(e, "Error to find session")
            raise NotFoundError() from e
