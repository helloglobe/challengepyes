

class Triangle():   # model code

    def __init__(self, base, height):

        self.base = base

        self.height = height



    def calculate_area(self):

        return self.height * self.base / 2



a_triangle = Triangle(20, 30)

print(a_triangle.calculate_area())


"""

class Triangle():   # own code (^^;)

    def __init__(self, long, high):

        self.long = long

        self.high = high

        self.area = 0     # 不要

        print("Created!")


    def cal(self, long, high):

        self.area = long * high * 0.5    # 計算結果だけ返せばOKだった。


triangle = Triangle(10,5)

print(triangle.area)   # 不要

triangle.cal(10,5)    # 冗長

print(triangle.area)  # calモジュールの戻り値を表示したほうがよい。


"""

