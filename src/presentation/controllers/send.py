from src.main.logs.logs_interface import LogInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.actions.send import SendInterface


class SendController(ControllerInterface):

    def __init__(self, use_case: SendInterface,
                 logger: LogInterface):
        self.__use_case = use_case
        self.__logger = logger

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        session_id = http_request.body.get('session_id')
        payload = http_request.body.get('payload')
        message = payload
        self.__use_case.user_send(session_id=session_id, message_payload=message)
        self.__logger.log_session(session=[session_id], action="chat_send_controller")
        return HttpResponse(
            status_code=200,
            body={}
        )
