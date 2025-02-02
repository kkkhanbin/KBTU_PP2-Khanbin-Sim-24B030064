from math import sqrt, pow

from abc import abstractmethod


class Std:
    @staticmethod
    def get_string() -> str:
        return input()

    @staticmethod
    def print_string(output: str) -> None:
        print(output)


class Shape:
    @abstractmethod
    def area() -> None:
        pass


class Square(Shape):
    def __init__(self, length: float, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.length = length
    
    def area(self) -> None:
        area = pow(self.length, 2)

        Std.print_string(area)


class Rectangle(Shape):
    def __init__(self, length: float, width: float, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.length = length
        self.width = width
    
    def area(self) -> None:
        area = self.length * self.width

        Std.print_string(area)



class Point:
    def __init__(self, coords: tuple) -> None:
        self.coords = coords

    def show(self) -> None:
        Std.print_string(self.coords)

    def move(self, new_coords: tuple) -> None:
        self.coords = new_coords
    
    def dist(self, point) -> float:
        x1, y1 = self.coords
        x2, y2 = point.coords

        distance = sqrt(pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2))

        return distance


class Account:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.balance = 0

    def deposit(self, amount: float) -> tuple:
        self.balance += amount

        return 0, 'Successful deposit'
    
    def withdraw(self, amount: float) -> tuple:
        if amount > self.balance:
            return -1, 'Insufficient funds'

        self.balance -= amount

        return 0, 'Successful withdrawal'


def main():
    square = Square(10)
    square.area()

    rec = Rectangle(10, 20)
    rec.area()

    point1 = Point((1, 4))
    point2 = Point((5, 0))
    Std.print_string(point1.dist(point2))

    account = Account('Khanbin')
    print(account.deposit(450))
    print(account.withdraw(700))
    print(account.withdraw(100))

    nums = range(10000)
    print(list(filter(lambda x: all([x % i != 0 for i in range(2, round(sqrt(x) + 1))]), nums)))


if __name__ == '__main__':
    main() 
