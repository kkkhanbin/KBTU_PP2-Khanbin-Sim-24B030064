import re

text = input()
pattern = r"[., ]"
print(re.sub(pattern, ";", text))
