def main():
    random_histogram()

def population_density():
    def density(population, land_area):
        return population / land_area

    test1 = density(10, 1)
    expected_result1 = 10
    print(f"Expected: {expected_result1}, Actual: {test1}")

    test2 = density(864816, 121.4)
    expected_result2 = 7123.6902801
    print(f"Expected {expected_result2}, Actual: {test2}")

def readable_timedelta():
    def calc(days):
        week_count = days // 7
        day_count = days % 7
        return f"{week_count} week(s) and {day_count} day(s)."

    print(calc(10))

def lambda_with_map():
    numbers = [
                [34, 63, 88, 71, 29],
                [90, 78, 51, 27, 45],
                [63, 37, 85, 46, 22],
                [51, 22, 34, 11, 18]
    ]

    averages = list(map(lambda x: sum(x) / len(x), numbers))

    print(averages)

def lambda_with_filter():
    cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]
    max_len = 10

    short_cities = list(filter(lambda x: len(x) < max_len, cities))
    print(short_cities)

def random_histogram():
    from random import randint
    i, max_lines = 0, int(input("Max lines: "))

    while i < max_lines:
        print("*" * randint(1, 10))
        i += 1

def perfect_number():
    def check(n):
        sum1 = 0

        for i in range(1, n):
            if n % i == 0:
                sum1 += i
        if sum1 == n:
            return f"{n} is a perfect number."
        else:
            return f"{n} isn't a perfect number."

    print(check(int(input("Insert number for check: "))))

main()
