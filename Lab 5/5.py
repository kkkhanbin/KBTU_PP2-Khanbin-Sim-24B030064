import re

text = input()
pattern = r"a.*b$"

found = re.findall(pattern, text)
if found is not None:
    print(found)
else:
    print("Not found")
