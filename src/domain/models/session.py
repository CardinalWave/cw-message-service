#pylint: disable=redefined-builtin
import json


class Session:
    def __init__(self, session_id: str, device: str, username: str, group_id: str) -> None:
        self.session_id = session_id
        self.device = device
        self.username = username
        self.group_id = group_id

    def to_dict(self):
        return {
            "session_id": self.session_id,
            "device": self.device,
            "username": self.username,
            "group_id": self.group_id
        }

    def to_json(self):
        return json.dumps(self.to_dict())
