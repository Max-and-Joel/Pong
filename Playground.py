class Playground:
    def __init__(self, hight, width):
        self.height = hight
        self.width = width
        self.list_pixel = []
        for h in range(self.height):
            line = []
            self.list_pixel.append(line)
            for w in range(self.width):
                line.append((0, 0, 0))
        self.clear()

    def clear(self):
        for y in range(self.height):
            for x in range(self.width):
                self.set_pixel(x, y, (0, 0, 0))

    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                print(self.get_pixel(x, y), end=' ')
            print("")

    