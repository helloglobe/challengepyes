
import re

string = "Two too."

m = re.findall("T[ow]o", string, re.IGNORECASE)

print(m)

