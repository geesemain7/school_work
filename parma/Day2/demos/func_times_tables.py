def print_row(y: int, size: int):
    for x in range(1, size + 1):
        print(x * y, end="\t")
    print()

def print_table(size: int):
    for y in range(1, size + 1):
        print_row(y, size)

print_table(7)