def squares(n: int):
    for i in range(n):
        yield i ** 2


def even(n: int):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


def divisible(n: int):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


def reversed(n: int):
    for i in range(n, -1, -1):
        yield i


# task 2
print(", ".join(map(str, even(int(input("N: "))))))

# task 4
for i in squares(50):
    print(i, end=" ")
print()

print(list(reversed(10)))
