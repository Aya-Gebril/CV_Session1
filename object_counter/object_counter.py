import cv2 as cv
from .image_processor import ImageProcessor
from .color_detector import ColorDetector
from .contour_detector import ContourDetector

WINDOW_NAME = "Object Counter"


class ObjectCounter:
    def __init__(self, image_processor, color_detector, contour_detector):
        self.image_processor = image_processor
        self.color_detector = color_detector
        self.contour_detector = contour_detector

    def load_image(self, image_path):
        self.image = self.image_processor.load_image(image_path)
        self.hsv_image = self.image_processor.convert_to_hsv(self.image)

    def count_objects(self, color):
        lower_bound, upper_bound = self.color_detector.get_color_bounds(color)
        mask = self.image_processor.create_mask(
            self.hsv_image, lower_bound, upper_bound
        )

        contours = self.contour_detector.find_contours(mask)
        result_image = self.image.copy()
        count = self.contour_detector.draw_objects(result_image, contours)
        cv.putText(
            result_image,
            f"Color: {color} | Count: {count}",
            (10, 30),
            cv.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2,
        )

        return result_image, count

    def run(self):
        cv.namedWindow(WINDOW_NAME)
        cv.imshow(WINDOW_NAME, self.image)
        while True:
            key = cv.waitKey(1) & 0xFF
            match chr(key):
                case "q":
                    break
                case "1":
                    color = "red"
                case "2":
                    color = "green"
                case "3":
                    color = "blue"
                case _:
                    continue

            result_image, count = self.count_objects(color)
            print(f"{color.capitalize()} objects: {count}")
            cv.imshow(WINDOW_NAME, result_image)

        cv.destroyAllWindows()
