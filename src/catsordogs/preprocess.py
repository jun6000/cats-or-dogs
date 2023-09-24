import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import numpy as np


def preprocess(img):
    img = tf.image.rgb_to_grayscale(img)
    img = tf.image.resize(img, (256, 256))
    img /= 255.0
    img = np.expand_dims(img, 0)
    return img
