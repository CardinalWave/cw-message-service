from src.infra.db.entities.session import Sessions as SessionsEntity
from src.infra.db.interfaces.session_repository import SessionRepositoryInterface
from src.infra.db.settings.connection import DBConnectionHandler
from src.data.erros.domain_errors import InternalServerError


class SessionRepository(SessionRepositoryInterface):

    def register_session(self, session_id: str, device: str, username: str, group_id: str):
        with DBConnectionHandler() as database:
            try:
                session_entity = SessionsEntity(
                    session_id=session_id,
                    group_id=group_id,
                    device=device,
                    username=username
                )
                new_registry = session_entity
                database.session.add(new_registry)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise InternalServerError('Duplicate register') from e

    def delete_session(self, session_id: str):
        with DBConnectionHandler() as database:
            try:
                session = (
                    database.session
                    .query(SessionsEntity)
                    .filter(SessionsEntity.session_id == session_id)
                    .first()
                )

                if session:
                    database.session.delete(session)
                    database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e

    def list_sessions(self) -> list[SessionsEntity]:
        with DBConnectionHandler() as database:
            try:
                sessions = (
                    database.session
                    .query(SessionsEntity)
                    .all()
                )
                return sessions
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e

    def select_session(self, session_id: str) -> SessionsEntity:
        with DBConnectionHandler() as database:
            try:
                session_entity = (
                    database.session
                    .query(SessionsEntity)
                    .filter(SessionsEntity.session_id == session_id)
                    .first()
                )
                return session_entity
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e
