import datetime
from uuid import uuid1
from abc import ABC
from typing import Dict
from src.domain.models.message import Message
from src.domain.use_cases.messages.message_manager import MessageManagerInterface
from src.infra.db.interfaces.message_repository import MessageRepositoryInterface
from src.data.erros.domain_errors import BadRequestError, InternalServerError, NotFoundError


class MessageManager(MessageManagerInterface, ABC):

    def __init__(self, message_repository: MessageRepositoryInterface):
        self.__message_repository = message_repository

    def inbox(self, group_id: str) -> list[Dict]:
        try:
            messages_entity = self.__message_repository.select_group(group_id)
            messages = [
                Message(message_id=message.message_id, group_id=message.group_id, send_time=message.send_time, payload=message.payload, author=message.author)
                for message in
                messages_entity]
            last_messages = self.__filter_time(messages)
            return last_messages
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e

    def forward_message(self, message: Message) -> Message:
        try:
            self.__archive_message(message)
            return message
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e

    @staticmethod
    def __filter_time(messages: list[Message]) -> list[Dict]:
        filter_messages = [
            message.to_dict() for message in messages
        ]
        order_messages = sorted(filter_messages, key=lambda x: x['send_time'], reverse=True)
        return order_messages

    def __archive_message(self, message: Message):
        try:
            message.message_id = uuid1()
            self.__message_repository.save_message(message)
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
