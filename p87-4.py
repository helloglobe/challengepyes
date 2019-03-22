my_dic = {"身長": 172, "体重": 56, "出身": "仙台", "趣味": "音楽・ゲーム", \
          "特技": "フィギュアスケート"}

print("羽生結弦について")

qu = input("聞きたいことを日本語で入力してください：")

print(my_dic[qu])

print("追加情報はありますか？")

key = input("何を知っていますか？：")

answer = input("答えを入力してください：")

my_dic [key] = answer

print(my_dic)   #追加されたことを確認
