
a = input("type a number:")    
b = input("type a number:")


try:
    a = int(a)
    b = int(b)
    print(a/b)
except (ZeroDivisionError,ValueError):    #各単語の頭を大文字にしないとエラーになる。
    print("Invalid input!")


