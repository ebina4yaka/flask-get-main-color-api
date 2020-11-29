import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import numpy as np
import cv2
from sklearn.cluster import KMeans

app = Flask(__name__)
CORS(app)


def get_main_colors(img_array):
    response = []
    cv2_img = cv2.imdecode(img_array, 1)
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    cv2_img = cv2_img.reshape(
        (cv2_img.shape[0] * cv2_img.shape[1], 3))
    cluster = KMeans(n_clusters=5)
    cluster.fit(X=cv2_img)
    cluster_centers_arr = cluster.cluster_centers_.astype(
        int, copy=False)

    for rgb_arr in cluster_centers_arr:
        color_hex_str = '#%02x%02x%02x' % tuple(rgb_arr)
        response.append(color_hex_str)

    return response


@app.route('/api/upload', methods=['POST'])
def upload():
    img_stream = base64.b64decode(request.json['image'])
    img_array = np.asarray(bytearray(img_stream), dtype=np.uint8)
    return jsonify({"colors": get_main_colors(img_array)})


if __name__ == '__main__':
    app.run(debug=False, threaded=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
