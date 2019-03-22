
str1 = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"

no = str1.index("、")  #「、」の前までを取り出す。

print(str1[:no])

no2 = str1.index("ど")

     
print(str1[no+1:no2])

print(str1[no2:])

print(str1[:-1])  #最後の。をとって表示する

str2 = str1[:-1]  #最後の。のない文字列を新しく作る

print(str2)

