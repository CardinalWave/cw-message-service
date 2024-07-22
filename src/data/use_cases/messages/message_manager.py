from uuid import uuid1
from src.domain.models.message import Message
from src.domain.models.session import Session
from src.domain.use_cases.messages.message_manager import MessageManagerInterface
from src.domain.use_cases.messages.message_publish import MessagePublishInterface
from src.infra.db.interfaces.message_repository import MessageRepositoryInterface
from src.data.erros.domain_errors import BadRequestError, InternalServerError


class MessageManager(MessageManagerInterface):

    def __init__(self, message_repository: MessageRepositoryInterface,
                 message_publish: MessagePublishInterface):
        self.__message_repository = message_repository
        self.__message_publish = message_publish

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
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e

    def forward_message(self, session: Session, message: Message):
        try:
            self.__archive_message(message)
            self.__message_publish.handle_message(session=session, message=message)
            return message
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e

    @staticmethod
    def __filter_time(messages: list[Message]) -> list[Message]:
        order_messages = sorted(messages, key=lambda x: x.send_time)
        return messages

    def __archive_message(self, message: Message):
        try:
            message.message_id = uuid1()
            self.__message_repository.save_message(message)
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
