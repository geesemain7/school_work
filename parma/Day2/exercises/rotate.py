from math import sin, cos, radians

def rotate(pt: (float, float), a: float) -> (float, float):

    x, y = pt

    rx = x * cos(a) - y * sin(a)
    ry = x * sin(a) + y * cos(a)

    return rx, ry

def main():

    a = float(input("Insert x: "))
    b = float(input("Insert y: "))
    angle = float(input("Insert angle: "))

    c = rotate((a, b), angle)

    print("Rotated coordinates:", c)

main()