import re

text = input()
pattern = r"[A-Z]"

print(re.sub(pattern, lambda x: "_" + x.group(0)[0].lower(), text))