from src.main.server.server import app
from src.config.config import Config


if __name__ == "__main__":
    ip = Config.CW_MESSAGE_SERVICE_IP
    port = Config.CW_MESSAGE_SERVICE_PORT
    app.run(host=ip, port=port)
