def convert(string):

    try:

        return float(string)

    except ValueError:

        print("Could not convert the string to a float.")
        #returnがないのでNoneを返す。

        #0を返すようにしてみる。
        return 0



c = convert("abcdefg")

print(c)

c = convert("4.5")

print(c)
