import re

text = input()
pattern = "[A-Z]"
print(re.split(pattern, text))
