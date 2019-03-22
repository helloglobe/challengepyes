# http://tinyurl.com/go9wepf

import csv



with open("st.csv", "w", newline='') as f:

    write = csv.writer(f, delimiter=",")

    write.writerow(["one",

                    "two",

                    "three"])

    write.writerow(["four",

                    "five",

                    "six"])
    
    write.writerow(["pooh",

                    "tooh",

                    "hooh"])
