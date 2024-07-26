def check_equal(numbers: tuple) -> int:
    a, b, c = numbers
    res = sum((a == b, b == c, a == c))
    return res + 1 if res == 1 else res


x, y, z = (123, 456, 789), (42, 69, 42), (2, 2, 2)
for e in (x, y, z):
    print(check_equal(e))
