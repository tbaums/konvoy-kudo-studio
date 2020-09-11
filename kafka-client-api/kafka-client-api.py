import os, sys
import socket
import logging
import time
import random
import json
import urllib

from flask import (
    Flask,
    Response,
    request,
    render_template,
    jsonify,
    stream_with_context,
    json,
)
from kafka import KafkaConsumer, KafkaProducer
from confluent_kafka.admin import AdminClient, NewTopic

if sys.version_info[0] == 3:
    os.environ["PYTHONUNBUFFERED"] = "1"


logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

kafka_dns = os.environ["KAFKA_ENDPOINT"]


###################################
#              API                #
###################################

# This API is designed to be extremely simple, testable, and extensible by the widest possible audience.
#
# The API contains only 3 methods, `read`, `write`, and `delete-topic`.


# WRITE_TO_KAFKA ----------------------------------------------
# write (topic: <string>, payload: <JSON object>, repetitions: <int>)
# The `repetitions` parameter indicates the number of times you want the message written to Kafka.
# This allows simulation of high load write behavior to Kafka.


# READ_FROM_KAFKA ----------------------------------------------
# read (topic: <string>, (optional) group_id: <string>)

# NOTE: Messages are passed to the front end as JSON they are read off the Kafka queue.
# Individual JSON objects are separated by '::::' and must be parsed thus on the frontend.


# NOTE: The route below assumes that Ingress provided at /kafka-client-api.
# If you change this Ingress path to something else, you must change the routing below.
@app.route("/kafka-client-api/write", methods=["POST"])
def write():
    query_string = urllib.parse.parse_qs(request.query_string.decode("UTF-8"))
    app.logger.debug("Request query_string: " + str(query_string))
    topic = query_string["topic"][0]
    payload = query_string["payload"][0]
    repetitions = int(query_string["repetitions"][0])

    write_to_kafka(topic, payload, repetitions)
    return Response("WRITE REQUEST RECEIVED", mimetype="text/plain")


@app.route("/kafka-client-api/read", methods=["GET"])
def read():
    query_string = urllib.parse.parse_qs(request.query_string.decode("UTF-8"))
    app.logger.debug("Request query_string: " + str(query_string))
    topic = query_string["topic"][0]
    # TODO: Implement proper UUID for default group_id
    if "group_id" in query_string and len(query_string["group_id"]) > 0:
        group_id = query_string["group_id"][0]
    else:
        group_id = str(socket.gethostname()) + str(random.randint(0, 9999999999))
    # NOTE: read_from_kafka() is included here to facilitate stream_with_context to FE.
    def read_from_kafka():
        try:
            consumer_client = get_consumer(topic, group_id)
        except Exception as e:
            app.logger.error("Could not create consumer_client with error " + str(e))

        for message in consumer_client:
            app.logger.info(message)
            # NB: can only 'yield' a string
            yield str(json.loads(message.value)) + "::::"
        consumer_client.close()

    return Response(stream_with_context(read_from_kafka()), mimetype="application/json")


@app.route("/kafka-client-api/delete-topic", methods=["POST", "GET"])
def delete_topic():
    a = AdminClient({"bootstrap.servers": kafka_dns})

    query_string = urllib.parse.parse_qs(request.query_string.decode("UTF-8"))
    app.logger.debug("Request query_string: " + str(query_string))
    topic = [query_string["topic"][0]]

    print('Topic submitted for deletion: ', topic)

    fs = a.delete_topics(topic, operation_timeout=30)

    # Wait for operation to finish.
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print("Topic {} deleted".format(topic))
        except Exception as e:
            print("Failed to delete topic {}: {}".format(topic, e))
    
    
    new_topic = [NewTopic(topic, num_partitions=3, replication_factor=1)]
    # Call create_topics to asynchronously create topics, a dict
    # of <topic,future> is returned.
    fs = a.create_topics(new_topic)

    # Wait for operation to finish.
    # Timeouts are preferably controlled by passing request_timeout=15.0
    # to the create_topics() call.
    # All futures will finish at the same time.
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print("Topic {} created".format(topic))
        except Exception as e:
            print("Failed to create topic {}: {}".format(topic, e))
    
    return Response(f"DELETE REQUEST RECEIVED for topic: {topic}", mimetype="text/plain")



###################################
#      KAFKA PRODUCER CLIENT      #
###################################
def get_producer():
    try:
        producer_client = KafkaProducer(
            bootstrap_servers=[kafka_dns],
            value_serializer=lambda x: json.dumps(x).encode("utf-8"),
            acks=1,
        )
    except Exception as e:
        app.logger.error("Could not create producer_client with error " + str(e))
    return producer_client


def write_to_kafka(topic, payload, repetitions):
    producer_client = get_producer()
    for _ in range(repetitions):
        try:
            producer_client.send(topic, payload)
            app.logger.debug(
                "Sent to Kafka. Topic: " + topic + " Value: " + str(payload)
            )

        except Exception as e:
            app.logger.error(
                "could not send message to " + topic + " with payload " + str(payload)
            )
            app.logger.error("send message failed with error: " + str(e))
    producer_client.close()
    return


###################################
#      KAFKA CONSUMER CLIENT      #
###################################


def get_consumer(topic, group_id):
    try:
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=[kafka_dns],
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id=str(group_id),
            # connections_max_idle_ms – Close idle connections after the number of milliseconds
            # specified by this config. The broker closes idle connections after
            # connections.max.idle.ms, so this avoids hitting unexpected socket disconnected errors
            # on the client. Default: 540000
            connections_max_idle_ms=305001,
            # request_timeout_ms (int) – Client request timeout in milliseconds. Default: 305000.
            # Must be smaller than connections_max_idle_ms
            # request_timeout_ms=1900,
            # session_timeout_ms (int) – The timeout used to detect failures when using Kafka’s
            # group management facilities. The consumer sends periodic heartbeats to indicate its
            # liveness to the broker. If no heartbeats are received by the broker before the expiration
            #  of this session timeout, then the broker will remove this consumer from the group and
            #  initiate a rebalance. Note that the value must be in the allowable range as configured
            #  in the broker configuration by group.min.session.timeout.ms and
            # group.max.session.timeout.ms. Default: 10000
            # session_timeout_ms=1899,
            # heartbeat_interval_ms (int) – The expected time in milliseconds between heartbeats
            #  to the consumer coordinator when using Kafka’s group management facilities.
            # Heartbeats are used to ensure that the consumer’s session stays active and to
            # facilitate rebalancing when new consumers join or leave the group.
            # The value must be set lower than session_timeout_ms, but typically
            # should be set no higher than 1/3 of that value. It can be adjusted even lower
            #  to control the expected time for normal rebalances. Default: 3000
            # heartbeat_interval_ms=1000,
        )
        return consumer
    except Exception as e:
        app.logger.error("failed to connect KafkaConsumer with error: " + str(e))


###################################
#             RUN                 #
###################################
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=float(os.getenv("DW_PORT", "8080")))
