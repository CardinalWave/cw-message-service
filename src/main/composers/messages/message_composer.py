from src.data.use_cases.messages.message_manager import MessageManager
from src.infra.db.repositories.message.message_repository import MessageRepository


def message_composer():
    repository = MessageRepository()
    use_case = MessageManager(message_repository=repository)

    return use_case
