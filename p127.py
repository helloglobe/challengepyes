
    # http://tinyurl.com/jt9guu2

    # ファイルを丸ごと書き換える（置き換える）

with open("st.txt", "w", encoding = "utf-8") as f:

    f.write("hi from python!")


my_list = []


    # readメソッドはファイルを開いて1回だけ使えるので、毎度開き直す。(^^;)>

with open("st.txt","r", encoding = "utf-8") as f:
    
    print(f.read())

with open("st.txt","r", encoding = "utf-8") as f:
    
    my_list.append(f.read())


print(my_list)

