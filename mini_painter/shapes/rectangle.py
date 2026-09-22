import cv2 as cv
from .shape import Shape

RECTANGLE_SIZE = 50

class Rectangle(Shape):
    def draw(self, image, center, color):
        x, y = center
        top_left = (x - RECTANGLE_SIZE, y - RECTANGLE_SIZE)
        bottom_right = (x + RECTANGLE_SIZE, y + RECTANGLE_SIZE)
        cv.rectangle(image, top_left, bottom_right, color, -1)
