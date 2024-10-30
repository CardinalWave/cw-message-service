from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.models.session import Session
from src.domain.use_cases.actions.join import JoinInterface


class JoinController(ControllerInterface):

    def __init__(self, use_case: JoinInterface):
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        group_id = http_request.body.get('group_id')
        username = http_request.body.get('username')
        session_id = http_request.body.get('session_id')
        device = http_request.body.get('device')
        session = Session(session_id=session_id,
                          device=device,
                          username=username,
                          group_id=group_id)
        self.__use_case.user_join(session=session)

        return HttpResponse(
            status_code=200,
            body={}
        )
