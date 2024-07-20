#pylint: disable=redefined-builtin
import json
import datetime


class Message:
    def __init__(self, message_id: str, group_id: str, author: str, send_time: datetime, payload: str) -> None:
        self.message_id = message_id
        self.group_id = group_id
        self.author = author
        self.send_time = send_time
        self.payload = payload

    def to_dict(self):
        return {
            "message_id": self.message_id,
            "group_id": self.group_id,
            "author": self.author,
            "send_time": self.send_time,
            "payload": self.payload
        }

    def to_json(self):
        return json.dumps(self.to_dict())
