
import csv

with open("C:/Users/Inoue Mari/Desktop/py/st.csv","r") as f:

    r = csv.reader(f, delimiter = ",")

    for count in r:

        print(",".join(count))

with open ("C:/Users/Inoue Mari/Desktop/py/st.txt","r") as f:

    r = csv.reader(f, delimiter = ",")

    for count in r:            # ふつうのテキストファイルでもできた！

        print(",".join(count))

"""join されて出力される様子：

hi from python!,oi from python.,yay from python!
lalaland, yeyeland, hoholand
one, two, three!

"""

with open ("C:/Users/Inoue Mari/Desktop/py/st.txt","r") as f:

    r = csv.reader(f, delimiter = ",")

    for count in r:            # ふつうのテキストファイルでもできた！

        print(count)

# ↑ joinしないと、カンマ区切りでリストになって出力される。
"""
['hi from python!', 'oi from python.', 'yay from python!']
['lalaland', ' yeyeland', ' hoholand']
['one', ' two', ' three!']

"""
