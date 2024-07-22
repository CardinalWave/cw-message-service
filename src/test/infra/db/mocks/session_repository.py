from src.infra.db.entities.session import Sessions as SessionsEntity
from src.infra.db.interfaces.session_repository import SessionRepositoryInterface


class SessionRepositorySpy(SessionRepositoryInterface):

    def select_session(self, session_id: str) -> SessionsEntity:
        if session_id == 'session_idkmadmadada':
            return SessionsEntity(username='Test1',
                                  session_id='session_idkmadmadada',
                                  device='esp8266_01',
                                  group_id='a1a9f26c-514f-41f0-9df0-2c8eff8fd456')

    def register_session(self, session_id: str,
                         device: str,
                         username: str,
                         group_id: str): pass

    def delete_session(self, session_id: str): pass

    def list_sessions(self) -> list[SessionsEntity]:
        return [SessionsEntity(username='Test1',
                               session_id='session_idkmadmadada',
                               device='esp8266_01',
                               group_id='a1a9f26c-514f-41f0-9df0-2c8eff8fd456'),
                SessionsEntity(username='Test2',
                               session_id='session_idkmadmadava',
                               device='esp8266_01',
                               group_id='a1a9f26c-514f-41f0-9df0-2c8eff8fd456')
                ]
