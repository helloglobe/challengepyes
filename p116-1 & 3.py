
shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for index, show in enumerate(shows):

    print(index)

    print(show)



"""
下のは自作。enumerateを使ってない。2変数を同時にenumerateできるよ♪

"""

list = ["ウォーキング・デッド","アントラージュ",
        "ザ・ソプラノズ","ヴアンパイア・ダイアリーズ"]

i = 1

for show in list:

    print("{}. {}".format(i, show))

    i += 1

    
for index, show in enumerate(list):

    print (index + 1)

    print (show)
    
