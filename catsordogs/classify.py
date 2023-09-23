from tensorflow.keras.models import load_model


def classify(img):
    model = load_model('model.h5')
    result = model.predict(img)
    result = result[0][0]
    if result < 0.5:
        print('Found a cat!')
    else:
        print('Found a dog!')
