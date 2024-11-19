from src.data.use_cases.actions.leave import Leave
from src.main.composers.sessions.session_composer import session_composer
from src.main.logs.logs import Log
from src.presentation.controllers.leave import LeaveController


def leave_composer():
    composer = session_composer()
    logger = Log()
    use_case = Leave(session_manager=composer, logger=logger)
    controller = LeaveController(use_case, logger)

    return controller.handle
