from src.presentation.controllers.join import JoinController
from src.data.use_cases.actions.join import Join
from src.main.composers.messages.message_composer import message_composer
from src.main.composers.sessions.session_composer import session_composer


def join_composer():
    use_case = Join(message_manager=message_composer(),
                    session_manager=session_composer())
    controller = JoinController(use_case)
    return controller.handle
