from abc import ABC


class SendInterface(ABC):

    def user_send(self, session_id: str, message_payload: str): pass
