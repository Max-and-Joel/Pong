import Objects
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

    def add_object(self, block: Objects.Objecttype , columns_right=0, lines_down=0):
        for y_of_block in range(block.height):
            for x_of_block in range(block.width):
                ispixel = block.get_field()[y_of_block][x_of_block]
                if ispixel > 0:
                    if not self.is_inside_field(x_of_block + columns_right, y_of_block + lines_down):
                        break
                    self.set_pixel(x_of_block + columns_right, y_of_block + lines_down, block.color.get_color())