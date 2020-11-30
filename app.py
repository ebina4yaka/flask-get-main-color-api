import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
from numpy import asarray, ndarray, uint8
import cv2
from sklearn.cluster import KMeans

app = Flask(__name__)
CORS(app)

CHANNEL = 3
THREE_CHANNEL_COLOR_IMAGE = 1
CLUSTER_SIZE = 5


def convert_rgb_tuple_to_color_hex_string(rgb_tuple: tuple) -> str:
    return '#%02x%02x%02x' % rgb_tuple


def get_main_colors(img_array: ndarray) -> list[str]:
    response = []
    cv2_img = cv2.imdecode(img_array, THREE_CHANNEL_COLOR_IMAGE)
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    cv2_img = cv2_img.reshape(
        (cv2_img.shape[0] * cv2_img.shape[1], CHANNEL))
    cluster = KMeans(n_clusters=CLUSTER_SIZE)
    cluster.fit(X=cv2_img)
    cluster_centers_arr = cluster.cluster_centers_.astype(
        int, copy=False)

    for rgb_arr in cluster_centers_arr:
        response.append(convert_rgb_tuple_to_color_hex_string(tuple(rgb_arr)))

    return response


@app.route('/api/upload', methods=['POST'])
def upload():
    img_stream: bytes = base64.b64decode(request.json['image'])
    img_array: ndarray = asarray(bytearray(img_stream), dtype=uint8)
    return jsonify({"colors": get_main_colors(img_array)})


if __name__ == '__main__':
    app.run(debug=False, threaded=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
