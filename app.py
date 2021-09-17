from flask import Flask
from flask_cors import CORS, cross_origin
import random

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

responses = [
    "How much would a wood chuck chuck if a wood chuck could chuck wood",
    "Your team will win this weekend!",
    "BJSS will rule the world!",
    "This is certainly a well trained model",
    "O Romeo, Romeo, wherefore art thou Romeo?",
    "Pub? Pub!",
    "There are only 10 types of people in the world – those who understand binary, and those who don’t.",
    "Today shall be sunny, or rainy idk",
    "LOL ROFL",
    "Go get a Greggs, you deserve it"
]


@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def index():
    rand_response = random.choice(responses)

    ret_response = {
        'response': rand_response
    }

    return ret_response
