FROM python:3.7.3-alpine3.10
WORKDIR /usr/src/app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir requests flask flask-api flask-executor
COPY kafka-robot-actor.py ./
CMD [ "python", "-u", "kafka-robot-actor.py"]
