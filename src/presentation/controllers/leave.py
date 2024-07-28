from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.actions.leave import LeaveInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class LeaveController(ControllerInterface):

    def __init__(self, use_case: LeaveInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        session_id = http_request.body.get('session_id')

        self.__use_case.user_leave(session_id=session_id)

        return HttpResponse(
            status_code=200,
            body={}
        )
