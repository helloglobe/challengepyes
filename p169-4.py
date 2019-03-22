
class Horse:

    def __init__(self, color, name, rider):

        self.color = color
        self.name = name
        self.rider = rider

class Rider:

    def __init__(self, name):

        self.name = name

paul = Rider("Paul McDonald")

lala = Horse("white", "LaLa", paul)  # コンポジションを使用
# Horseオブジェクトを作り、その騎手としてRiderオブジェクトを渡している。

print(lala.rider.name)  # lala.rider　の nameは？
