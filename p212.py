
import re

t = "__one__ __two__ __three__"

found = re.findall("__.*?__", t)   #　非貪欲な正規表現（*?）を使う

for match in found:
    print(match)
