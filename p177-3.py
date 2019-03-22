
def compare(obj1, obj2):   # 同じオブジェクトかを調べる関数でisの動作をみる

    return obj1 is obj2


ab = "abc"

print(compare("a", "b"))  # F

print(compare(ab,ab))  # T

print(compare(2,1))  # F

"""# p.175のコードを試す

class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()  # 括弧内のselfは空白
same_bob = bob  # 同じbobを代入

print(bob is same_bob)  # True

another_bob = Person()
print(bob is another_bob)  # False
"""

