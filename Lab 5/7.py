import re

text = input()
pattern = r"_[a-z]"

print(re.sub(pattern, lambda x: x.group(0)[1].upper(), text))