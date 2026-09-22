class ColorManager:
    COLORS = {
        "1": ("White", (255, 255, 255)),
        "2": ("Red", (0, 0, 255)),
        "3": ("Green", (0, 255, 0)),
        "4": ("Blue", (255, 0, 0)),
        "5": ("Yellow", (0, 255, 255))
    }

    def __init__(self):
        self.current_color_name = "White"
        self.current_color = self.COLORS["1"][1]

    def select_color(self, key):
        if key in self.COLORS:
            self.current_color_name = self.COLORS[key][0]
            self.current_color = self.COLORS[key][1]
            return True

        return False

    def get_color(self):
        return self.current_color

    def get_color_name(self):
        return self.current_color_name