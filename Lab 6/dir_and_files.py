import os

# 1
path = "./sample_dir"

print(f"only dirs - {[x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]}")
print(f"only files - {[x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]}")
print(f"all - {os.listdir(path)}")

# 2
path = "./sample_dir/sample_file1.txt"

print(f'''exists - {os.path.exists(path)}
readable - {os.access(path, os.R_OK)}
writable - {os.access(path, os.W_OK)}
executable - {os.access(path, os.X_OK)}''')

# 3
path = "./sample_dir/sample_file1.txt"

if os.path.exists(path):
    print(os.path.abspath(path))
else:
    print("Does not exist")

# 4
path = "./sample_dir/sample_file1.txt"

with open(path, mode="r", encoding="utf-8") as textfile:
    print(len(textfile.readlines()), "lines there")

# 5
path = "./sample_dir/sample_file1.txt"
output_list = ["Some text", "Hmmmmmmmmmmmmmmmmmmm"]

with open(path, mode="a", encoding="utf-8") as textfile:
    print(" ".join(output_list), file=textfile)

    # another way is textfile.write()

# 6
import string

path = "./sample_dir/alphabet"
for sym in string.ascii_uppercase:
    new_file = open(f"{path}/{sym}.txt", "w")
    new_file.close()

    # os.remove(f"{path}/{sym}.txt")

# 7
from_path = "./sample_dir/sample_file1.txt"
to_path = "./sample_dir/copy1.txt"

with open(from_path, mode="r", encoding="utf-8") as fromfile:
    with open(to_path, mode="w+", encoding="utf-8") as tofile:
        tofile.write(fromfile.read())
        
        # another way - using shutil.copyfile

# 8
del_path = "./sample_dir/a.py"

if os.path.exists(del_path):
    if os.access(del_path, os.W_OK):
        os.remove(del_path)
        print("deleted")
    else:
        print("not enough rights")
else:
    print("does not exist")