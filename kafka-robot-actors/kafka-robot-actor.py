import os, sys
import socket
import logging
import time
import random
import json
import urllib
import requests


# from kafka import KafkaProducer

if sys.version_info[0] == 3:
    os.environ["PYTHONUNBUFFERED"] = "1"


logging.basicConfig(level=logging.INFO)


# ###################################
# #      KAFKA PRODUCER CLIENT      #
# ###################################
# def get_producer():
#     try:
#         producer_client = KafkaProducer(
#             bootstrap_servers=[os.environ["BROKER_SERVICE"]],
#             value_serializer=lambda x: json.dumps(x).encode("utf-8"),
#             acks=1,
#         )
#     except Exception as e:
#         sys.stderr.write("Could not create producer_client with error " + str(e))
#     return producer_client

# def write_to_kafka(topic, payload, repetitions):
#     producer_client = get_producer()
#     for _ in range(repetitions):
#         try:
#             producer_client.send(topic, payload)
#             sys.stdout.write(
#                 "Sent to Kafka. Topic: " + topic + " Value: " + str(payload)
#             )

#         except Exception as e:
#             sys.stderr.write(
#                 "could not send message to " + topic + " with payload " + str(payload)
#             )
#             sys.stderr.write("send message failed with error: " + str(e))
#     producer_client.close()
#     return


###################################
#             RUN                 #
###################################
if __name__ == "__main__":
    x = random.randint(0, 90)
    y = random.randint(0, 90)
    while True:
        x = str(int(x) + random.randint(-1, 1))
        y = str(int(y) + random.randint(-1, 1))
        # get only the 5 unique digits at the end of the pod name
        actor = socket.gethostname()[-5:len(socket.gethostname())]
        # TODO: move this to env var passed in YAML. Also, use an internal cluster IP rather than going to the public internet and back.
        url = 'http://' + os.environ['KAFKA_CLIENT_API_SVC_SERVICE_HOST'] + ":" + os.environ['KAFKA_CLIENT_API_SVC_SERVICE_PORT'] + "/kafka-client-api/write"

        querystring = {"topic":"actors","payload": json.dumps({'actor': actor, 'x': x, 'y': y}),"repetitions":"1"}
        print(querystring)
        headers = {
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "4fcd9769-4416-4e67-80df-6023108d452f,b6563b7c-4354-4921-a8e4-e24ea0c6c4fc",
            # 'Host': "a56a94e80947142019796ff050b0605a-515129060.us-west-2.elb.amazonaws.com",
            'accept-encoding': "gzip, deflate",
            'content-length': "",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }
        try:
            response = requests.request("POST", url, headers=headers, params=querystring, verify=False)
        except Exception as e:
            print('failed post request with error: ', str(e))

        print("*****POST to ",response.url)
        print(response.text)
        time.sleep(.25)
