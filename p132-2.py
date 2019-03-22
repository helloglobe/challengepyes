
#何か質問する。

do_list = []

for i in range(5):

     ans = input("今日は何をしましたか？　>>>")

     ans = str(ans)

     do_list.append(ans)

print(do_list)


import csv

#入力された回答をファイルに書き出す。

with open("sst.csv","w", newline="") as f:

    w = csv.writer(f, delimiter=",")

    w.writerow(do_list)


