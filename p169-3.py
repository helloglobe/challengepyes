
class Shape:

    def __init__(self, b, h):

        self.base = b
        self.hight = h

    def what_am_i(self):

        if self.base == self.hight:

            return "square"

        else:

            return "rectangle"

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

a_shape = Rectangle(4,7)

b_shape = Square(5,5)

print("１つのオブジェクトは")
print(a_shape.what_am_i())
print("です。")

print("もう１つのオブジェクトは")
print(b_shape.what_am_i())
print("です。")

x = input("底辺を入力>>> ")
y = input("高さを入力>>> ")
c_shape = Shape(x, y)

print("そのオブジェクトは")
print(c_shape.what_am_i())
print("です。")
