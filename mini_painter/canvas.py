import cv2 as cv
import numpy as np

C_WIDTH = 800
C_HEIGHT = 600
C_CHANNELS = 3
WINDOW_NAME = "Mini Painter"

class Canvas:
    def __init__(self):
        self.image = np.zeros(
            (C_HEIGHT, C_WIDTH, C_CHANNELS),
            dtype=np.uint8
        )

    def show(self, image = None):
        if image is None:
            image = self.image
        cv.imshow(WINDOW_NAME, image)

    def save(self, filename):
        cv.imwrite(filename, self.image)
