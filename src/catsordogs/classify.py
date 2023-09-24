from tensorflow.keras.models import load_model
from pkg_resources import resource_filename


def classify(img):
    model = load_model(resource_filename(__name__, 'model.h5'))
    result = model.predict(img)
    result = result[0][0]
    if result < 0.5:
        print('Found a cat!')
    else:
        print('Found a dog!')
