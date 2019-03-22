
movies = [["Top Gun","Risky Business","Minority Report"],
          ["Titanic","The Revenant","Inception"],
          ["Training Day","Man on Fire","Fight"]]

import csv

with open("movies.csv","w",newline='') as f:

    w = csv.writer(f, delimiter = ",")

    for ml in movies:

        w.writerow(ml)

