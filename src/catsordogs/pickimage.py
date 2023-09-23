from tkinter.filedialog import Tk, askopenfilename
from cv2 import imread


def pickimage():
    Tk().withdraw()
    filepath = askopenfilename(
        title='Select an image file',
        filetypes=[
            ('Image files', '*.jpg *.jpeg *.png *.bmp'),
        ],
        multiple=False
    )
    if not filepath:
        return None
    img = imread(filepath)
    return img
