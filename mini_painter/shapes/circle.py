import cv2 as cv
from .shape import Shape

CIRCLE_RADIUS = 50

class Circle(Shape):
    def draw(self, image, center, color):
        cv.circle(image, center, CIRCLE_RADIUS, color, -1)
