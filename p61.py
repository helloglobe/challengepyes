x = 1
y = 2
z = 3

print("1,2,3を指定倍すると...")

def f():
    a = input("ところで何倍にしますか？：　")
    a = int(a)  #整数化しないとなぜか変な動きをするので注意！！

    print(x * a)
    print(y * a)
    print(z * a)

f()

print("になります！")
