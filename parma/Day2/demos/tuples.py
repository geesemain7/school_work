def divmod_(a, b):
    quotient = a // b
    reminder = a % b
    return (quotient, reminder)

result = divmod_(5, 2)
q, r = result