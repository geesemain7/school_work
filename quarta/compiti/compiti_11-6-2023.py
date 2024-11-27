def main():
    nearest_square()

def fruit_basket_task_2():
    # Example 1
    result = 0
    basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
    fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

    for fruit, num in basket_items.items():
        if fruit in fruits:
            result += num

    print(f"There are {result} fruits.")
    print(result)

    # Example 2
    result = 0
    basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
    fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

    for fruit, num in basket_items.items():
        if fruit in fruits:
            result += num

    print(f"There are {result} fruits.")
    print(result)

    # Example 3
    result = 0
    basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
    fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

    for fruit, num in basket_items.items():
        if fruit in fruits:
            result += num

    print(f"There are {result} fruits.")
    print(result)

def fruit_basket_task_3():
    fruit_num, not_fruit_num = 0, 0
    basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
    fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

    for fruit, num in basket_items.items():
        if fruit in fruits:
            fruit_num += num
        else:
            not_fruit_num += num

    print(fruit_num, not_fruit_num)

def count_by_check():
    start, end = 0, 10
    inc = 1
    brk = start

    if start < end:
        while brk < end:
            brk += inc
        result = brk
    else:
        result = "Oops! Looks like your start value is greater than the end value. Please try again."

    print(result)

def nearest_square():
    import math

    limit = 40
    num = limit

    while limit > 0:
        if math.sqrt(num) % 1 == 0:
            result = num
            break
        else:
            num -= 1

    print(result)

main()