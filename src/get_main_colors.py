import cv2
from sklearn.cluster import KMeans
from numpy import ndarray

from src.rgb_tuple_to_color_hex_string import rgb_tuple_to_color_hex_string

CHANNEL = 3
THREE_CHANNEL_COLOR_IMAGE = 1
CLUSTER_SIZE = 5


def get_main_colors(img_array: ndarray) -> list:
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
        response.append(rgb_tuple_to_color_hex_string(tuple(rgb_arr)))

    return response