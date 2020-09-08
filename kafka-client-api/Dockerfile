FROM python:3.7.3
WORKDIR /usr/src/app
RUN mkdir -p /usr/src/app/templates
RUN pip install --upgrade pip
RUN pip install --no-cache-dir flask flask-api kafka-python ifaddr confluent_kafka
COPY kafka-client-api.py ./
CMD [ "python", "-u", "kafka-client-api.py"]
