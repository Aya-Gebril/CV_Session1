import cv2 as cv

class ImageProcessor:
    def load_image(self, image_path):
        image = cv.imread(image_path)
        if image is None:
            raise ValueError("Could not load image.")

        return image

    def convert_to_hsv(self, image):
        return cv.cvtColor(image, cv.COLOR_BGR2HSV)

    def create_mask(self, hsv_image, lower_bound, upper_bound):
        return cv.inRange(hsv_image, lower_bound, upper_bound)
