import os, sys
import socket
import logging
import time
import random
import json
import requests
import ssl

from flask import (
    Flask,
    Response,
    request,
    render_template,
    jsonify,
    stream_with_context,
    json,
)

if sys.version_info[0] == 3:
    os.environ["PYTHONUNBUFFERED"] = "1"


logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

prediction_endpoint = os.environ["KF_SERVING_ENDPOINT"]

# prediction_endpoint = "http://mnist-predictor-default.mt.svc.cluster.local/v1/models/mnist:predict"

###################################
#              API                #
###################################


@app.route("/prediction-api", methods=["POST"])
def predict():
    # hit prediction endpoint http://mnist-predictor-default.mt.svc.cluster.local/v1/models/mnist:predict
    input = request.get_json(force = True)
    print(input)
    
    response = requests.post(prediction_endpoint, data=json.dumps(input), verify=False)
    print(response.text)

    return Response(response, mimetype="application/json")


###################################
#             RUN                 #
###################################
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=float(os.getenv("DW_PORT", "8080")))
