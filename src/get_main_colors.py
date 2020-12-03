import cv2
from sklearn.cluster import KMeans
from numpy import ndarray, uint8, asarray

from src.rgb_tuple_to_color_hex_string import rgb_tuple_to_color_hex_string

DEFAULT_CLUSTER_SIZE = 5
CHANNEL = 3
THREE_CHANNEL_COLOR_IMAGE = 1


def get_main_colors(img_stream: bytes, cluster_size=DEFAULT_CLUSTER_SIZE) -> list:
    response = []
    img_array: ndarray = asarray(bytearray(img_stream), dtype=uint8)
    cv2_img = cv2.imdecode(img_array, THREE_CHANNEL_COLOR_IMAGE)
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    cv2_img = cv2_img.reshape(
        (cv2_img.shape[0] * cv2_img.shape[1], CHANNEL))
    cluster = KMeans(n_clusters=cluster_size)
    cluster.fit(X=cv2_img)
    cluster_centers_arr = cluster.cluster_centers_.astype(
        int, copy=False)

    for rgb_arr in cluster_centers_arr:
        response.append(rgb_tuple_to_color_hex_string(tuple(rgb_arr)))

    return response
