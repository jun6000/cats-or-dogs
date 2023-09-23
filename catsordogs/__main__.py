from cv2 import imread
from preprocess import preprocess
from classify import classify


def main():
    img = imread('test2.jpeg')
    img = preprocess(img)
    classify(img)

if __name__ == '__main__':
    main()
