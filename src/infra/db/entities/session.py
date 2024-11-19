from sqlalchemy import Column, String
from src.infra.db.settings.base import Base


class Sessions(Base):
    __tablename__ = "sessions"

    session_id = Column(String, primary_key=True)
    device = Column(String, nullable=False)
    username = Column(String, nullable=False)
    group_id = Column(String, nullable=False)
