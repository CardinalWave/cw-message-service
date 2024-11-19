from src.main.logs.logs import Log
from src.presentation.controllers.join import JoinController
from src.data.use_cases.actions.join import Join
from src.main.composers.messages.message_composer import message_composer
from src.main.composers.sessions.session_composer import session_composer


def join_composer():
    logger = Log()
    use_case = Join(message_manager=message_composer(),
                    session_manager=session_composer(),
                    logger=logger)
    controller = JoinController(use_case, logger)
    return controller.handle
