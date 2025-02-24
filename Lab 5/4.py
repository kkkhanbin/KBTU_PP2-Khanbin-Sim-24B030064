import re

text = input()
pattern = "[A-Z][a-z]+"

found = re.findall(pattern, text)
if found is not None:
    print(found)
else:
    print("Not found")
