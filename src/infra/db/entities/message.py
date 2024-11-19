from sqlalchemy import Column, String
from src.infra.db.settings.base import Base


class Messages(Base):
    __tablename__ = "messages"

    message_id = Column(String, primary_key=True)
    group_id = Column(String, nullable=False)
    author = Column(String, nullable=False)
    payload = Column(String, nullable=False)
    send_time = Column(String, nullable=False)
