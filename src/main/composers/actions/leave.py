from src.data.use_cases.actions.leave import Leave
from src.main.composers.sessions.session_composer import session_composer
from src.presentation.controllers.leave import LeaveController


def leave_composer():
    composer = session_composer()
    use_case = Leave(session_manager=composer)
    controller = LeaveController(use_case)

    return controller.handle
