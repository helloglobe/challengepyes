
correct = ["23","51","98","17","67"]

while True:

    
    ans = input("0から100までの数字を１つ入力してね( q で終了)：\n>>>")

    if ans == "q":

        print("終了します。またね！")

        break

    try:

        answer = int(ans)

    except ValueError:

        print("数字を入力するか、qで終了します")


    if answer in correct:
 
        print("大当たり！")

    else:

        print("不正解")


""" # 模範コード　全角で入力しても整数にして対応。

    # 数字ではないものを入れても、メッセージのあとに「不正解」は出る。
　　　　　　　　　

numbers = [11, 32, 33, 15, 1]



while True:

    answer = input("Guess a number or type q to quit.")

    if answer == "q":

        break

    try:

        answer = int(answer)

    except ValueError:

        print("please type a number or q to quit.")

    if answer in numbers:

        print("You guessed correctly!")

    else:

        print("You guessed incorrectly!")

"""
