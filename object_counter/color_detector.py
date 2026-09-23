import numpy as np

class ColorDetector:
    def get_color_bounds(self, color):
        color_bounds = {
            "red": (np.array([0, 100, 100]), np.array([10, 255, 255])),
            "green": (np.array([40, 100, 100]), np.array([80, 255, 255])),
            "blue": (np.array([100, 100, 100]), np.array([130, 255, 255])),
        }
        if color not in color_bounds:
            raise ValueError("Unsupported color.")

        return color_bounds[color]
