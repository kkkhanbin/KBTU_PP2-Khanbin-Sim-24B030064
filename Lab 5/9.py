import re

text = input()
pattern = "(?=[A-Z])"

print(re.sub(pattern, " ", text))
