from src.data.use_cases.messages.message_manager import MessageManager
from src.infra.db.repositories.message.message_repository import MessageRepository
from src.main.composers.messages.message_publish import message_publish_composer
from src.main.logs.logs import Log


def message_composer():
    repository = MessageRepository()
    logger = Log()
    message_publish = message_publish_composer()
    use_case = MessageManager(message_repository=repository,
                              message_publish=message_publish,
                              logger=logger)

    return use_case
