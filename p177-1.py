

class Square:

    square_list = []   # クラス変数を追加

    def __init__(self, w, l):

        self.wid = w
        self.len = l
        self.square_list.append([self.wid, self.len])  # 2個セットの追加

        
import random

for i in range(10):

    x = random.randint(1,50)
    y = random.randint(1,50)
    my_square = Square(x, y)
    
print(Square.square_list)


