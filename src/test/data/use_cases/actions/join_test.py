#pylint: disable=redefined-outer-name
import pytest
from src.data.use_cases.actions.join import Join
from src.test.data.mocks.message_manager_mock import MessageManagerSpy
from src.test.data.mocks.session_manager_mock import SessionManagerSpy
from src.domain.models.session import Session
from src.test.main.logs import LogSpy


@pytest.fixture
def mock_session():
    return Session(session_id="session_idkmadmadada",
                   device="esp8266_01",
                   username="Lua",
                   group_id="a1a9f26c-514f-41f0-9df0-2c8eff8fd456")


def test_join(mock_session):
    message_manager = MessageManagerSpy()
    session_manager = SessionManagerSpy()
    logger_spy = LogSpy()
    join = Join(message_manager=message_manager,
                session_manager=session_manager,
                logger=logger_spy)
    join.user_join(session=mock_session)
