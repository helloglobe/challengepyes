
list_1 = [8, 19, 148, 4]

list_2 = [9, 1, 33, 83]


# 結果を格納するリストを準備　　4 * 4 = 16 個のリスト。

result = []

for i in list_1:

    for j in list_2:

        result.append(i * j)

# for j in list_2:     二重掛け合わせになるので不要だった。

#    for i in list_1:

#        result.append(j * i)


print(result)


