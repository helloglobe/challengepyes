
import re

line = "I love $"

m = re.findall("\\$", line, re.IGNORECASE)

# "$"で検索すると、['']になってしまう。

# "\$"なら['$']となり、OK。エラーもなし。
# さらに、"\\$"としても結果は['$']と同じ。なぜ\\と重ねるのか謎！

print(m)


