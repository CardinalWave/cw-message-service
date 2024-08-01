from datetime import datetime
from uuid import uuid1
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.models.session import Session
from src.domain.models.message import Message
from src.domain.use_cases.actions.send import SendInterface


class SendController(ControllerInterface):

    def __init__(self, use_case: SendInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        session_id = http_request.body.get('session_id')
        payload = http_request.body.get('payload')
        send_time = datetime.now()
        message_id = str(uuid1())
        message = Message(message_id=message_id,
                          group_id='',
                          send_time=send_time,
                          payload=payload,
                          author='')
        self.__use_case.user_send(session_id=session_id, message=message)

        return HttpResponse(
            status_code=200,
            body={}
        )
