from src.domain.models.session import Session
from src.domain.use_cases.sessions.session_manager import SessionManagerInterface


class SessionManagerSpy(SessionManagerInterface):

    def register_session(self, session: Session): pass

    def find_session(self, session_id: str) -> Session:
        if session_id == "session_idkmadmadada":
            return Session(session_id="session_idkmadmadada",
                           username="Test1",
                           group_id="a1a9f26c-514f-41f0-9df0-2c8eff8fd456",
                           device="esp8266_01")
        return Session(session_id="", group_id="", username="", device="")

    def list_current_sessions(self, group_id: str) -> list[Session]:
        sessions = [Session(session_id="session_idkmadmadada",
                            username="Test2",
                            group_id="a1a9f26c-514f-41f0-9df0-2c8eff8fd456",
                            device="esp8266_01"),
                    Session(session_id="session_karmadata3",
                            username="Test1",
                            group_id="a1a9f26c-514f-41f0-9df0-2c8eff8fd456",
                            device="esp8266_01")
                    ]
        return sessions

    def delete_session(self, session: Session): pass
