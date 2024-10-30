from src.domain.models.message import Message
from src.infra.db.entities.message import Messages as MessagesEntity
from src.infra.db.interfaces.message_repository import MessageRepositoryInterface
from src.infra.db.settings.connection import DBConnectionHandler
from src.data.erros.domain_errors import InternalServerError


class MessageRepository(MessageRepositoryInterface):

    def select_group(self, group_id: str) -> list[MessagesEntity]:
        with DBConnectionHandler() as database:
            try:
                message_entity = (
                    database.session
                    .query(MessagesEntity)
                    .filter(MessagesEntity.group_id == group_id)
                    .all()
                )
                return message_entity
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e

    def save_message(self, message: Message):
        with DBConnectionHandler() as database:
            try:
                new_register = MessagesEntity(
                    message_id=message.message_id,
                    group_id=message.group_id,
                    author=message.author,
                    payload=message.payload,
                    send_time=message.send_time
                )
                database.session.add(new_register)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e
