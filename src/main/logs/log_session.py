from src.main.logs.log_handler import logger
from src.domain.models.session import Session


def log_session(session: Session, action: str):
    log_payload = session.to_dict()
    log_payload['action'] = action
    log_payload['service'] = "cw-message-service:ip_service:0000"

    logger.info(log_payload)
