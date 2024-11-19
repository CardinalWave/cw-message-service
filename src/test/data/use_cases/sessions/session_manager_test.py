#pylint: disable=unidiomatic-typecheck,redefined-outer-name
import pytest
from src.test.infra.db.mocks.session_repository import SessionRepositorySpy
from src.data.use_cases.sessions.session_manager import SessionManager
from src.data.erros.domain_errors import NotFoundError
from src.domain.models.session import Session
from src.test.main.logs import LogSpy


@pytest.fixture
def mock_session():
    return Session(username='Test1',
                   session_id='session_idkmadmadada',
                   device='esp8266_01',
                   group_id='a1a9f26c-514f-41f0-9df0-2c8eff8fd456')


def test_register_session(mock_session):
    repository = SessionRepositorySpy()
    logger_spy = LogSpy()

    use_case = SessionManager(session_repository=repository, logger=logger_spy)

    use_case.register_session(mock_session)


def test_find_session(mock_session):
    repository = SessionRepositorySpy()
    logger_spy = LogSpy()

    use_case = SessionManager(session_repository=repository, logger=logger_spy)

    response = use_case.find_session(mock_session.session_id)

    assert response is not None
    assert type(response) is Session


def test_find_session_not_found(mock_session):
    mock_session.session_id = "session_idiotic_found"
    repository = SessionRepositorySpy()
    logger_spy = LogSpy()

    use_case = SessionManager(session_repository=repository, logger=logger_spy)

    try:
        use_case.find_session(mock_session.session_id)
    except Exception as e:
        assert type(e) is NotFoundError
