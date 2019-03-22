
class Hexagon:

    def __init__(self, s1, s2, s3, s4, s5, s6):

        self.s1 = s1    # 6辺の長さを個別に保持する（正六角形ではない！）
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def cal(self):

         return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

a_hexagon = Hexagon(1,2,3,4,5,6)

print(a_hexagon.cal())


"""
class Hexagon:      # クラス（オブジェクト）の中で変数を定義する方法

    def __init__(self, r):

        self.ra = r

        self.le = 0

        print("Created!")


    def cal(self, x):

        self.le = x * 6

    def change_size(self, r):

        self.ra = r

hexa = Hexagon(10)

print(hexa.le)

hexa.cal(hexa.ra)   # calを指定されたhexaで呼び出す

print(hexa.le)      #　外周計算結果を表示する

hexa.change_size(8)   # サイズを変える（もう１回始めからではなくて）

hexa.cal(hexa.ra)

print(hexa.le)   # サイズが変わった外周を表示する

"""
