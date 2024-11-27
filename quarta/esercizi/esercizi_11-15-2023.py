def main():
    for_loop()

def for_loop():
    num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
    count, odd_sum = 0, 0
    limit = 5

    for num in num_list:
        if num % 2 != 0:
            odd_sum += num
            count += 1
        if count == limit:
            break

    print(f"The number of odd numbers is: {count}")
    print(f"The sum of the odd numbers is: {odd_sum}")

def while_loop():
    num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
    count, odd_sum, i = 0, 0, 0

    while count < 5:
        if num_list[i] % 2 != 0:
            odd_sum += num_list[i]
            count += 1
        i += 1

    print(f"The number of odd numbers is: {count}")
    print(f"The sum of the odd numbers is: {odd_sum}")

main()
