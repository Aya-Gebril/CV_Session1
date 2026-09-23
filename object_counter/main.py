from .image_processor import ImageProcessor
from .color_detector import ColorDetector
from .contour_detector import ContourDetector
from .object_counter import ObjectCounter

IMAGE_PATH = "test_images/image.png"

def main():
    try:
        image_processor = ImageProcessor()
        color_detector = ColorDetector()
        contour_detector = ContourDetector()

        object_counter = ObjectCounter(
            image_processor, color_detector, contour_detector
        )

        object_counter.load_image(IMAGE_PATH)
        object_counter.run()

    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
