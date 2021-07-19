class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        result = ""
        for i in range(self.height):
            line = ""
            for j in range(self.width):
                line = line + "*"
            line += "\n"
            result += line
        return result

    def get_amount_inside(self, shape: "Rectangle"):
        self_area = self.get_area()
        shape_area = shape.get_area()
        return int(self_area/shape_area)

    def __repr__(self):
        return self.__class__.__name__+"(width={}, height={})".format(self.width, self.height)


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, width):
        self.side = width
        self.width = width

    def set_height(self, height):
        self.side = height
        self.height = height

    def __repr__(self):
        return self.__class__.__name__+"(side={})".format(self.side)