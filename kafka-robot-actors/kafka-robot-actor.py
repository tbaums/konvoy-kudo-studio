import os, sys
import socket
import logging
import time
import random
import json
import urllib
import requests
import gc
from flask import (
    Flask,
    Response,
    request,
    render_template,
    jsonify,
    stream_with_context,
    json,
)
from flask_executor import Executor

if sys.version_info[0] == 3:
    os.environ["PYTHONUNBUFFERED"] = "1"


logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
executor = Executor(app)
robots = []
future = ""


class Robot:

    url = "http://" + os.environ["KAFKA_CLIENT_API"] + "/kafka-client-api/write"

    def __init__(self, name):
        self.name = name
        self.x = random.randint(0, 90)
        self.y = random.randint(0, 90)

    def update(self):
        self.x = str(int(self.x) + random.randint(-1, 1))
        self.y = str(int(self.y) + random.randint(-1, 1))

        querystring = {
            "topic": "actors",
            "payload": json.dumps({"actor": self.name, "x": self.x, "y": self.y}),
            "repetitions": "1",
        }
        # print(querystring)
        headers = {
            "User-Agent": "PostmanRuntime/7.15.0",
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Postman-Token": "4fcd9769-4416-4e67-80df-6023108d452f,b6563b7c-4354-4921-a8e4-e24ea0c6c4fc",
            # 'Host': "a56a94e80947142019796ff050b0605a-515129060.us-west-2.elb.amazonaws.com",
            "accept-encoding": "gzip, deflate",
            "content-length": "",
            "Connection": "keep-alive",
            "cache-control": "no-cache",
        }
        try:
            response = requests.request(
                "POST", self.url, headers=headers, params=querystring, verify=False
            )
            # print("*****POST to ",response.url)
            # print(response.text)
        except Exception as e:
            print("failed post request with error: ", str(e))


@app.route("/robot-api/increment", methods=["GET"])
def increment(robots=robots):
    print(f"Increment request received. Current robot count: {len(robots) + 1}")
    robot = Robot(f"Davis-{random.randint(0,1000)}")
    robots = robots.append(robot)

    return Response(
        f"Increment request received.",
        # f"Increment request received. Current robot count: {len(robots)}",
        mimetype="text/plain",
    )


@app.route("/robot-api/decrement", methods=["GET"])
def decrement(robots=robots):
    robots.pop()

    print(f"*******")
    print(f"Current robot list: {get_robots()}")
    print(f"*******")
    return Response(
        f"Decrement request received. Current robot count: {len(get_robots())}",
        mimetype="text/plain",
    )


@app.route("/robot-api/list", methods=["GET"])
def list_robots(robots=robots):
    print(f"*******")
    print(f"Current robot list: {robots}")
    print(f"*******")
    return Response(f"Current robot count: {len(robots)}", mimetype="text/plain")


@app.route("/robot-api/start", methods=["GET"])
def start(robots=robots):
    def update_loop():
        while True:
            if len(get_robots()) > 0:
                for robot in get_robots():
                    print(f"Updating robot: {robot}")
                    robot.update()
        time.sleep(1)

    if not future:
        future = executor.submit(update_loop)
    return Response(f"Job with ID: {future} kicked off..", mimetype="text/plain")


def get_robots(robots=robots):
    return robots


###################################
#             RUN                 #
###################################
if __name__ == "__main__":

    app.run(host="0.0.0.0", port=float(os.getenv("DW_PORT", "8080")))
