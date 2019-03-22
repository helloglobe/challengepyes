
class Rectangle:

    def __init__(self, b, h):

        self.base = b
        self.hight = h

    def calculate_perimeter(self):

        return (self.base + self.hight) * 2


class Square:

    def __init__(self, s):

        self.side = s

    def calculate_perimeter(self):

        return self.side * 4

my_rectangle = Rectangle(5,7)
my_square = Square(8)


print("長方形の外周は {} センチ".format(my_rectangle.calculate_perimeter()))

print("正方形の外周は {} センチ".format(my_square.calculate_perimeter()))

