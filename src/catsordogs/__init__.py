from .pickimage import pickimage
from .preprocess import preprocess
from .classify import classify
from .logfatal import logfatal


def main():
    img = pickimage()
    if img is None:
        logfatal("Image file not chosen.")
    img = preprocess(img)
    classify(img)
