# Imagem base do Python na versao 3.11
FROM cardinal_wave-python-base-image

#COPY requirements.txt .

#RUN apk add git build-base libffi-dev

#RUN pip install -r requirements.txt

COPY  . /app

WORKDIR /app

ENV MQTT_BROKER_IP=mqtt-mosquitto
ENV MQTT_BROKER_PORT=1883
ENV CW_CENTRAL_SERVICE=cw-central-service
ENV CW_CENTRAL_SERVICE_IP=cw-central-service
ENV CW_CENTRAL_SERVICE_PORT=5001
ENV CW_LOG_TRACE=cw-log-trace
ENV CW_LOG_TRACE_IP=cw-log-trace
ENV CW_LOG_TRACE_PORT=5050
ENV CW_MESSAGE_SERVICE=cw-message-service
ENV CW_MESSAGE_SERVICE_URL=http://cw-message-service:5003
ENV CW_MESSAGE_SERVICE_IP=cw-message-service
ENV CW_MESSAGE_SERVICE_PORT=5003
ENV CW_MESSAGE_DB=postgresql+psycopg2://postgres:postgres@cw_message_db:5432/cw_message_db
ENV CW_MESSAGE_DB_PASS=postgres
ENV CW_MESSAGE_DB_USER=postgres
ENV CW_MESSAGE_DB_HOST=cw_message_db
ENV CW_MESSAGE_DB_PORT=5431
ENV CW_MESSAGE_DB_NAME=postgres

EXPOSE 5003

CMD [ "python", "run.py" ]
