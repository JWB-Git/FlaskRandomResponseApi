from flask import Flask
import random
import json

app = Flask(__name__)

with open('responses.json') as responseFile:
    responses = json.load(responseFile)


@app.route("/", methods=['POST'])
def index():
    rand_response = random.choice(responses)

    ret_response = {
        'response': rand_response
    }

    return ret_response
