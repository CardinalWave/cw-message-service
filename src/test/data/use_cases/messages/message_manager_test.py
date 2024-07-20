from datetime import datetime
from typing import Dict
from src.data.use_cases.messages.message_manager import MessageManager
from src.test.infra.db.mocks.message_repository import MessageRepositorySpy


def test_inbox():
    mock_group_id = "a1a9f26c-514f-41f0-9df0-2c8eff8fd456"

    repository = MessageRepositorySpy()
    use_case = MessageManager(message_repository=repository)
    response = use_case.inbox(group_id=mock_group_id)

    assert response is not None
    assert len(response) > 0
    assert type(response) is list
    assert response.__getitem__(0).get('group_id') is not None
    assert response.__getitem__(0).get('send_time') is not None

