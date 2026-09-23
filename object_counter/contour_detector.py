import cv2 as cv

MIN_CONTOUR_AREA = 500

class ContourDetector:
    def find_contours(self, mask):
        contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        return contours

    def draw_objects(self, image, contours):
        count = 0
        for contour in contours:
            area = cv.contourArea(contour)
            if area >= MIN_CONTOUR_AREA:
                x, y, width, height = cv.boundingRect(contour)
                cv.rectangle(image, (x, y), (x + width, y + height), (0, 0, 0), 2)
                count += 1

        return count
