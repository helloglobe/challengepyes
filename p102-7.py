
name = "Hemingway"

letter = input("どの文字を探しますか：\n>>>")

try:
    answer = name.index("letter")
    print(answer)
except:
    print("Not found.")
    answer = "?"


sentence = "{}の{}番目の文字が'{}'です".format(name, answer, letter)

print(sentence)
