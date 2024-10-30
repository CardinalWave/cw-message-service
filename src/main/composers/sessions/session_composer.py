from src.data.use_cases.sessions.session_manager import SessionManager
from src.infra.db.repositories.session.session_repository import SessionRepository


def session_composer():
    repository = SessionRepository()
    use_case = SessionManager(session_repository=repository)

    return use_case
