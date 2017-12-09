import json
from flask import Flask, jsonify, abort
from flask import request
import http.client
from service import getTags
app = Flask(__name__)


@app.route('/post/data/', methods=['POST'])
def postData():
    """
    POST: json payload which contains paragraph text.
    RESPONSE: json payload which contains list of tags.
    """
    # value = request.json["text"]
    value = request.json
    data = getTags(value)
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug = True )