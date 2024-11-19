from src.main.logs.logs import Log
from src.presentation.controllers.send import SendController
from src.data.use_cases.actions.send import Send
from src.main.composers.sessions.session_composer import session_composer
from src.main.composers.messages.message_composer import message_composer


def send_composer():
    logger = Log()
    use_case = Send(message_manager=message_composer(),
                    session_manager=session_composer(),
                    logger=logger)
    controller = SendController(use_case, logger)
    return controller.handle
