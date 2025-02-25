# 1
import math 

some_list = [1, 2, -12, 123, -3939, 88, 73.5]
print(math.prod(some_list))

# 2
some_string = input()

uppers = sum(map(str.isupper, some_string))
lowers = sum(map(str.islower, some_string))

print(f"uppers - {uppers}, lowers - {lowers}")

# 3
some_string = input()
print(some_string == "".join(list(reversed(some_string))))

# 4
import time

num = int(input("Sample Input:\n"))
milliseconds = int(input("Milliseconds: "))

time.sleep(milliseconds / 1000)
print(f"Square root of {num} after {milliseconds} miliseconds is {math.sqrt(num)}")

# 5
some_tuple = (0, 1, 0, 2, False, True, "some sentence")
print(all(some_tuple))
