#pylint: disable=redefined-outer-name
import pytest
from src.data.use_cases.messages.message_manager import MessageManager
from src.test.infra.db.mocks.message_repository import MessageRepositorySpy
from src.test.data.mocks.message_publish_mock import MessagePublishSpy
from src.domain.models.session import Session


@pytest.fixture
def mock_session():
    return Session(session_id="5259d7df-c0f7-4729-879f-17d1f91c6100",
                   group_id="a1a9f26c-514f-41f0-9df0-2c8eff8fd456",
                   device="esp8266_01",
                   username="Test1")


def test_inbox(mock_session):
    message_publish = MessagePublishSpy()
    repository = MessageRepositorySpy()
    use_case = MessageManager(message_repository=repository, message_publish=message_publish)
    use_case.inbox(mock_session)
