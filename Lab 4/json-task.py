import json

with open("sample-data.json", "r", encoding="UTF-8") as json_file:
    data = json.load(json_file)

HEADER = '''
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------ 
'''

print(HEADER)

for el in data["imdata"]:
    el = el["l1PhysIf"]["attributes"]
    print(el["dn"].ljust(51), end="")
    print(el["descr"].ljust(21), end="")
    print(el["speed"].ljust(10), end="")
    print(el["mtu"].ljust(8), end="")

    print()
