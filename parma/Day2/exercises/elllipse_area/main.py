import calc

def main():
    sem1 = float(input("Insert semi-axis 1: "))
    sem2 = float(input("Insert semi-axis 2: "))
    area = calc.area_calc(sem1, sem2)
    print("The area is:", area)

main()