import re

text = input()
pattern = "([a-z]*_[a-z]*)+"

if re.match(pattern, text):
    print(re.search(pattern, text).group())
else:
    print("Not found")
