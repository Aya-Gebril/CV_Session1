import cv2 as cv
import numpy as np
from .shape import Shape

POLYGON_WIDTH = 60
POLYGON_TOP_HEIGHT = 60
POLYGON_BOTTOM_HEIGHT = 50

class Polygon(Shape):
    def draw(self, image, center, color):
        x, y = center
        points = np.array(
            [
                [x, y - POLYGON_TOP_HEIGHT],
                [x - POLYGON_WIDTH, y + POLYGON_BOTTOM_HEIGHT],
                [x + POLYGON_WIDTH, y + POLYGON_BOTTOM_HEIGHT],
            ]
        )
        cv.fillPoly(image, [points], color)
