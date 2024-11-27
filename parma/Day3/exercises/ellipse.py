import math


class Ellipse:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def area(self):
        return math.pi * self._a * self._b

    def foci(self):
        return math.sqrt(abs(self._a**2 - self._b**2))


def main():
    a = float(input("Insert length of semi axis a: "))
    b = float(input("Insert length of semi axis b: "))
    obj = Ellipse(a, b)
    area = obj.area()
    foci = obj.foci()
    print("The area is:", area)
    print("The foci is: +-", foci)


main()
