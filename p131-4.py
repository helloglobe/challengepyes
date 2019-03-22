
movies = [["トップ・ガン","Risky Business","Minority Report"],
          ["Titanic","The Revenant","インセプション"],
          ["トレーニング・デイ","Man on Fire","Fight"]]

import csv

with open("movies_jp.csv","w",newline='', encoding="utf-8") as f:

    w = csv.writer(f, delimiter = ",")

    for ml in movies:

        w.writerow(ml)



with open("movies_jp.csv","r",encoding="utf-8") as f:


    print(f.read())
