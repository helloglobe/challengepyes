
import cubed

x = input("数字を一つ入力 >> ")
x = int(x)        # 引数として渡すときはintにしないとダメらしい。

result = cubed.cubed(x)    #引数を指定して関数を呼び出す。

print(result)
