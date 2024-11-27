def hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c

def main():
    l1 = float(input("1st side? "))
    l2 = float(input("2nd side? "))
    hp = hypotenuse(l1, l2)
    print("3rd side:", hp)

main()