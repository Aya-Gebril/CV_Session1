from canvas import Canvas
from color_manager import ColorManager
from painter import Painter

def main():
    try:
        canvas = Canvas()
        color_manager = ColorManager()
        painter = Painter(canvas, color_manager)
        painter.run()
        
    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
