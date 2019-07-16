FROM python:3.7.3-alpine3.10
WORKDIR /usr/src/app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir requests
COPY kafka-dummy-actor.py ./
CMD [ "python", "-u", "kafka-dummy-actor.py"]
