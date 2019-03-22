
# Thanks so much for reading my book.
# Feel free to contact me at cory[at]theselftaughtprogrammer.io.


def hangman(word):

    wrong = 0

    stages = ["\n",   #1

             "________        \n", #2

             "|               \n", #3

             "|        |      \n", #4

             "|        0      \n", #5

             "|       /|⧵     \n", #6

             "|       / ⧵     \n", #7

             "|               \n"  #8 負けを表示する。
              
              ]

    rletters = list(word)

    board = ["__"] * len(word)

    win = False

    print("Welcome to Hangman\n")



#　ループ処理（ゲーム本体）

    while wrong < len(stages) - 1: #7回目まで

        print("\n")

        msg = "Guess a letter >>> "

        char = input(msg)

        if char in rletters:

            cind = rletters \
                   .index(char)

            board[cind] = char #あたった文字で置き換える

            rletters[cind] = '$'  #あたった文字を伏せる

        else:

            wrong += 1   #失敗：まちがい数をインクリメント

        print((" ".join(board)))    #現状ボードを表示

        e = wrong + 1    #ハングマンをどこまで表示するか指定
                     #eの手前までしか表示されないので＋１
    
        print("\n".join(stages[0: e]))
        

        if "__" not in board:    #置き換えたボードが完成していたら

            print("You win!")

            print(" ".join(board))

            win = True

            break

    if not win:

        print("\n".join(stages[0:wrong+1]))  #もう１度ハングマンを表示

        print("You lose! It was {}.".format(word))


anslist = ["cat","book","express","charity","plane",
               "monday","giant","cookie","club","flower"]

import random

hangman(anslist[random.randint(0,9)])  #ランダムに出題する



