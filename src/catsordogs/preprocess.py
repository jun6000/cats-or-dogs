import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.image import rgb_to_grayscale, resize
from numpy import expand_dims


def preprocess(img):
    img = rgb_to_grayscale(img)
    img = resize(img, (256, 256))
    img /= 255.0
    img = expand_dims(img, 0)
    return img
