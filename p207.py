
import re

l = "Beautidul is better than ugly."

matches = re.findall("beautidul", l, re.IGNORECASE)


print(matches)
