import cv2 as cv
from canvas import Canvas, WINDOW_NAME
from color_manager import ColorManager
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.polygon import Polygon


STATUS_POSITION = (10, 30)
STATUS_FONT = cv.FONT_HERSHEY_SIMPLEX
STATUS_SCALE = 0.7
STATUS_THICKNESS = 2
STATUS_COLOR = (255, 255, 255)

class Painter:
    def __init__(self, canvas, color_manager):
        self.canvas = canvas
        self.color_manager = color_manager
        self.shapes = {
            "c": Circle(),
            "r": Rectangle(),
            "p": Polygon()
        }
        self.current_shape_name = "Circle"
        self.current_shape = self.shapes["c"]

    def set_shape(self, key):
        if key in self.shapes:
            self.current_shape = self.shapes[key]
            shape_names = {
                "c": "Circle",
                "r": "Rectangle",
                "p": "Polygon"
            }
            self.current_shape_name = shape_names[key]

    def handle_mouse(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            self.current_shape.draw(
                self.canvas.image,
                (x, y),
                self.color_manager.get_color()
            )

    def draw_status(self, image):
        status = (
            f"Shape: {self.current_shape_name} | "
            f"Color: {self.color_manager.get_color_name()}"
        )

        cv.putText(
            image,
            status,
            STATUS_POSITION,
            STATUS_FONT,
            STATUS_SCALE,
            STATUS_COLOR,
            STATUS_THICKNESS
        )

    def handle_key(self, key):
        key = chr(key)
        match key:
            case "c":
                self.set_shape("c")

            case "r":
                self.set_shape("r")

            case "p":
                self.set_shape("p")

            case "1" | "2" | "3" | "4" | "5":
                self.color_manager.select_color(key)

    def run(self):
        cv.namedWindow(WINDOW_NAME)
        cv.setMouseCallback(WINDOW_NAME, self.handle_mouse)
        
        while True:
            display_image = self.canvas.image.copy() 
            self.draw_status(display_image) 
            self.canvas.show(display_image)
            
            key = cv.waitKey(1) & 0xFF
            match chr(key):
                case "q":
                    break
                case "w": 
                    self.canvas.save("mini_painter_output.png") 
                case _: 
                    self.handle_key(key)

        cv.destroyAllWindows()
