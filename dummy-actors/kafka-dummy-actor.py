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
        actor = socket.gethostname()[-5:-1]
        # payload = {"payload": {"actor": str(actor), "x": x, "y": y}}
        url = "http://aa88ee6c922d84faba50b571b841e45d-593314138.us-west-2.elb.amazonaws.com/kafka-client-api/write"

        # http://aa88ee6c922d84faba50b571b841e45d-593314138.us-west-2.elb.amazonaws.com/kafka-client-api/write?topic=actors&payload={"actor":"actor2", "x": "80", "y":"48"}&repetitions=100

        # querystring = {"topic":"actors","payload":"{'actor':'actor2', 'x': '80', 'y':'48'}","repetitions":"100"}
        querystring = {"topic":"actors","payload": json.dumps({'actor': actor, 'x': x, 'y': y}),"repetitions":"1"}
        print(querystring)
        headers = {
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "4fcd9769-4416-4e67-80df-6023108d452f,b6563b7c-4354-4921-a8e4-e24ea0c6c4fc",
            'Host': "aa88ee6c922d84faba50b571b841e45d-593314138.us-west-2.elb.amazonaws.com",
            'accept-encoding': "gzip, deflate",
            'content-length': "",
            # 'referer': "http://aa88ee6c922d84faba50b571b841e45d-593314138.us-west-2.elb.amazonaws.com/kafka-client-api/write?topic=actors&payload=%7B%22actor%22:%22{actor}%22,%20%22x%22:%20%22{x}%22,%20%22y%22:%22{y}%22%7D&repetitions=1",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("POST", url, headers=headers, params=querystring, verify=False)

        print("*****POST to ",response.url)
        print(response.text)
        # r = requests.post(
        #     "http://aa88ee6c922d84faba50b571b841e45d-593314138.us-west-2.elb.amazonaws.com/kafka-client-api/write",
        #     params={
        #         "topic": "actors",
        #         "payload": {"actor": str(actor), "x": x, "y": y}'',
        #         "repetitions": "1",
        #     },
        #     verify=False,
        # )
        # print(r.url)
        # requests.post("http://aa88ee6c922d84faba50b571b841e45d-593314138.us-west-2.elb.amazonaws.com/kafka-client-api/write?topic=actors&payload={'actor':{actor}, 'x': {x}, 'y':{y}}&repetitions=1", verify=False)
        # write_to_kafka("actors", {'actor':  str(actor),'x': x, 'y': y}, 1)
        time.sleep(.5)
