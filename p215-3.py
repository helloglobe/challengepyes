
import re

text = "The ghost that says boo haunts the loo."

#  NG!  m = re.findall(".*?oo.*?", text, re.IGNORECASE)

#  >>> ['The ghost that says boo', ' haunts the loo'] となってしまう。

m = re.findall(".oo.*?", text, re.IGNORECASE)

# OK. >>> ['boo', 'loo']　と一致した。

print(m)
