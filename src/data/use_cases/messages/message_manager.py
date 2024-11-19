from uuid import uuid1
from src.domain.models.message import Message
from src.domain.models.session import Session
from src.domain.use_cases.messages.message_manager import MessageManagerInterface
from src.domain.use_cases.messages.message_publish import MessagePublishInterface
from src.infra.db.interfaces.message_repository import MessageRepositoryInterface
from src.data.erros.domain_errors import BadRequestError, InternalServerError
from src.main.logs.logs_interface import LogInterface


class MessageManager(MessageManagerInterface):

    def __init__(self, message_repository: MessageRepositoryInterface,
                 message_publish: MessagePublishInterface,
                 logger: LogInterface):
        self.__message_repository = message_repository
        self.__message_publish = message_publish
        self.__logger = logger

    def inbox(self, session: Session):
        try:
            messages_entity = self.__message_repository.select_group(session.group_id)
            messages = [
                Message(message_id=message.message_id,
                        group_id=message.group_id,
                        send_time=message.send_time,
                        payload=message.payload,
                        author=message.author)
                for message in
                messages_entity]
            for message in messages:
                self.__message_publish.handle_message(session=session, message=message)
            self.__logger.log_session(session=session.to_dict(), action='message_inbox')
        except BadRequestError as e:
            self.__logger.log_error(error=e, message=e.message)
            raise BadRequestError(str(e)) from e
        except Exception as e:
            self.__logger.log_critical(error=e, message="[Error] -"
                                                        "Inbox Action -"
                                                        "session_id:" + session.session_id)
            raise InternalServerError(str(e)) from e

    def forward_message(self, session: Session, message: Message):
        try:
            self.__message_publish.handle_message(session=session, message=message)
            self.__logger.log_session(session=session.to_dict(), action='message_forward_message')
            return message
        except BadRequestError as e:
            self.__logger.log_critical(error=e, message="[Error] -"
                                                        "Forward Message Action -"
                                                        "session_id:" + session.session_id)
            raise BadRequestError(str(e)) from e

    def save_message(self, message: Message):
        try:
            message.message_id = uuid1()
            self.__logger.log_session(session=message.to_dict(), action='message_save')
            self.__message_repository.save_message(message)
        except BadRequestError as e:
            self.__logger.log_critical(error=e, message="[Error] - Forward Message Action -"
                                                        "message_id:" + message.payload +
                                                        " author:" + message.author +
                                                        " group_id:" + message.group_id)
            raise BadRequestError(str(e)) from e
