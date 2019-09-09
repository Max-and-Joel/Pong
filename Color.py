class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def get_color(self):
        return self.red, self.green, self.blue


class ObjectColor:
    yellow =Color(255, 255, 0)

    red =   Color(255, 0, 0)