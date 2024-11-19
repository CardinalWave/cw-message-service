from src.data.use_cases.sessions.session_manager import SessionManager
from src.infra.db.repositories.session.session_repository import SessionRepository
from src.main.logs.logs import Log


def session_composer():
    repository = SessionRepository()
    logger = Log()

    use_case = SessionManager(session_repository=repository,
                              logger=logger)

    return use_case
