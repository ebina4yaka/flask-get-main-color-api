import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64

from src.get_main_colors import get_main_colors

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def it_works():
    return "it works!"


@app.route('/api/upload', methods=['POST'])
def upload():
    img_stream: bytes = base64.b64decode(request.json['image'])
    return jsonify({"colors": get_main_colors(img_stream)})


@app.route('/api/upload/clusters/<clusters>', methods=['POST'])
def upload_with_clusters(clusters):
    img_stream: bytes = base64.b64decode(request.json['image'])
    return jsonify({"colors": get_main_colors(img_stream, clusters)})


if __name__ == '__main__':
    app.run(debug=False, threaded=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
