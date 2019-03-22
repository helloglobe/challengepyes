
class Square:

    def __init__(self, s):

        self.side = s

    def calculate_perimeter(self):

        return self.side * 4

    def change_size(self, d):

        self.side = self.side + d

    def print_size(self):

        print("It's {}, for sure.".format(self.side))
    


my_square = Square(8)

print(my_square.calculate_perimeter())

my_square.change_size(5)

print(my_square.calculate_perimeter())

my_square.change_size(-2)

print(my_square.calculate_perimeter())

my_square.change_size(-18)

print(my_square.calculate_perimeter())

print(my_square.side)   #  この時点での辺の長さは？

my_square.print_size()




