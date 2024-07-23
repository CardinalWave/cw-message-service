#pylint: disable=redefined-outer-name
from datetime import datetime
import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.repositories.message.message_repository import MessageRepository
from src.domain.models.message import Message

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.fixture
def mock_message():
    message = Message(message_id="1fb1bfaa-45e6-11ef-89a3-8dcb94dccac7",
                      group_id="a1a9f26c-514f-41f0-9df0-2c8eff8fd456",
                      send_time=datetime.now(),
                      payload="Bom Di@1",
                      author="Test1")
    return message


@pytest.mark.skip(reason="sensive test")
def test_select_group(mock_message):
    repository = MessageRepository()
    sql = '''INSERT INTO
            messages (message_id, group_id, payload, author, send_time)
            VALUES ('{}', '{}', '{}', '{}', '{}')
        '''.format(mock_message.message_id,
                   mock_message.group_id,
                   mock_message.payload,
                   mock_message.author,
                   mock_message.send_time)
    connection.execute(text(sql))
    connection.commit()

    response = repository.select_group(group_id=mock_message.group_id)
    registry = response[0]

    assert registry.message_id == mock_message.message_id
    assert registry.group_id == mock_message.group_id
    assert registry.author == mock_message.author
    assert registry.payload == mock_message.payload
    assert registry.send_time == mock_message.send_time

    connection.execute(text(f'''
        DELETE FROM messages WHERE message_id = '{mock_message.message_id}';
    '''))
    connection.commit()


@pytest.mark.skip(reason="sensive test")
def test_save_message(mock_message):
    repository = MessageRepository()
    repository.save_message(mock_message)

    sql = '''SELECT * FROM messages
       WHERE message_id = '{}' 
       '''.format(mock_message.message_id)

    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.message_id == mock_message.message_id
    assert registry.group_id == mock_message.group_id
    assert registry.author == mock_message.author
    assert registry.payload == mock_message.payload
    assert registry.send_time == mock_message.send_time

    connection.execute(text(f'''
        DELETE FROM messages WHERE message_id = '{mock_message.message_id}';
       '''))
    connection.commit()
