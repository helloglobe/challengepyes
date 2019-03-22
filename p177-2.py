

class Square:

    square_list = []   # クラス変数を追加

    def __init__(self, w, l):

        self.wid = w
        self.len = l
        self.square_list.append([self.wid, self.len])  # 2個セットの追加

    def __repr__(self):  # repr という名前を変更すると×（特殊メソッド？）。

        return "{} by {}の四角形が追加されました".format(self.wid, self.len)

    def __add__(self):   # add は計算用の特殊メソッド

        return (self.wid + self.len)*2

        
import random

for i in range(10):

    x = random.randint(1,50)
    y = random.randint(1,50)
    my_square = Square(x, y)
    print(my_square)   # 作られたオブジェクトの説明
    print((x + y)*2)   # その外周を計算
    
print(Square.square_list)


