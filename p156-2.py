

import math

class Circle:

    def __init__(self, r):

        self.radius = r

        print("Created!")


    def area(self):

        return self.radius ** 2 * math.pi


circle = Circle(6)

print(circle.area())


"""


import math

class Circle():

    def __init__(self, radius):

        self.radius = radius



    def calculate_area(self):

        return self.radius ** 2 * math.pi



a_circle = Circle(4)

print(a_circle.calculate_area())


"""
