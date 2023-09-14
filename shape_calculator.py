class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_width(self) -> float:
        return self.width

    def get_height(self) -> float:
        return self.height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        width_line = f'{"*" * self.width}\n'

        return width_line * self.height

    def get_amount_inside(self, rectangle: 'Rectangle') -> int:
        return int(self.get_area() // rectangle.get_area())


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        super().set_height(side)
        super().set_width(side)

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)