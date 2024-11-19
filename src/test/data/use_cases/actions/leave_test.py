from src.data.use_cases.actions.leave import Leave
from src.test.data.mocks.session_manager_mock import SessionManagerSpy
from src.test.main.logs import LogSpy


def test_leave():
    session_manager = SessionManagerSpy()
    logger_spy = LogSpy()

    leave = Leave(session_manager, logger_spy)
    leave.user_leave(session_id="session_idkmadmadada")
