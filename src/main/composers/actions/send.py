from src.presentation.controllers.send import SendController
from src.data.use_cases.actions.send import Send
from src.main.composers.sessions.session_composer import session_composer
from src.main.composers.messages.message_composer import message_composer


def send_composer():
    use_case = Send(message_manager=message_composer(), session_manager=session_composer())
    controller = SendController(use_case)
    return controller.handle
