import pytest
from uuid import uuid1
from datetime import datetime
from src.data.use_cases.actions.send import Send
from src.test.data.mocks.message_manager_mock import MessageManagerSpy
from src.test.data.mocks.session_manager_mock import SessionManagerSpy
from src.domain.models.session import Session
from src.domain.models.message import Message


@pytest.fixture
def mock_session():
    return Session(session_id="session_idkmadmadada",
                   device="esp8266_01",
                   username="Test",
                   group_id="a1a9f26c-514f-41f0-9df0-2c8eff8fd456")


@pytest.fixture
def mock_message():
    time = datetime.now()
    return Message(
        message_id=str(uuid1()),
        group_id="a1a9f26c-514f-41f0-9df0-2c8eff8fd456",
        author="Test1",
        send_time=time, payload="Ola Mundo!")


def test_send(mock_session, mock_message):
    message_manager = MessageManagerSpy()
    session_manager = SessionManagerSpy()

    use_case = Send(message_manager=message_manager,
                    session_manager=session_manager)
    response = use_case.user_send(message=mock_message, session=mock_session)

    assert response is None

def test_send_not_found_session(mock_session, mock_message):
    mock_session.username = "Test2"
    message_manager = MessageManagerSpy()
    session_manager = SessionManagerSpy()

    use_case = Send(message_manager=message_manager,
                    session_manager=session_manager)

    try:
        use_case.user_send(message=mock_message, session=mock_session)
    except Exception as e:
        assert str(e) == 'Not found'
