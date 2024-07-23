#pylint: disable=redefined-outer-name
import pytest
from sqlalchemy import text
from src.infra.db.repositories.session.session_repository import SessionRepository
from src.domain.models.session import Session
from src.infra.db.settings.connection import DBConnectionHandler

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.fixture
def mock_session():
    return Session(username='Test1',
                   session_id='session_idkmadmadada',
                   device='esp8266_01',
                   group_id='a1a9f26c-514f-41f0-9df0-2c8eff8fd456')

@pytest.mark.skip(reason="sensive test")
def test_register_session(mock_session):
    repository = SessionRepository()
    repository.register_session(session_id=mock_session.session_id,
                                device=mock_session.device,
                                group_id=mock_session.group_id,
                                username=mock_session.username)

    sql = '''SELECT * FROM sessions
        WHERE session_id = '{}' 
    '''.format(mock_session.session_id)
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.session_id == mock_session.session_id
    assert registry.group_id == mock_session.group_id
    assert registry.device == mock_session.device
    assert registry.username == mock_session.username

    connection.execute(text(f'''
        DELETE FROM sessions WHERE session_id = '{registry.session_id}';                      
    '''))
    connection.commit()
    connection.close()


@pytest.mark.skip(reason="sensive test")
def test_list_sessions(mock_session):
    repository = SessionRepository()
    sql = '''INSERT INTO
            sessions (session_id, group_id, device, username)
            VALUES ('{}', '{}', '{}', '{}')
        '''.format(mock_session.session_id,
                   mock_session.group_id,
                   mock_session.device,
                   mock_session.username)

    connection.execute(text(sql))
    connection.commit()

    response = repository.list_sessions()

    assert response is not None

    connection.execute(text(f'''
        DELETE FROM sessions WHERE session_id = '{mock_session.session_id}'
    '''))
    connection.commit()
    connection.close()
