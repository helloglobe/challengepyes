x = input("what odd number do you like? : ")
x = int(x)

def a(x):

    """
    Returns x // 2.
    :param x: int.
    :return int xを2で割った商.
    """
    return x // 2

def b(y):
    """
    Returns y * 4.
    :param y: int.
    :return float yの4倍.
    """
    
    print("roughly half your favorite number, multiplied by 4 is ...")
    return float(y * 4)

y = a(x)
print(a)

print(b(y))


#model code ^^
"""

def divide(x):

    return x / 2



def multiply(x):

    return x * 4



y = divide(4)

z = multiply(y)



print(z)
    

"""
