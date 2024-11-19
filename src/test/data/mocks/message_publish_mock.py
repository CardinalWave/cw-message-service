from src.domain.models.message import Message
from src.domain.models.session import Session
from src.domain.use_cases.messages.message_publish import MessagePublishInterface


class MessagePublishSpy(MessagePublishInterface):

    def handle_message(self, session: Session, message: Message): pass
