# 1st program
print(9 ** 0.5 * 5)

# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)

# 3rd program
print(int(str(1234)[1:3]) + int(str(5678)[1:3]))
other3 = 1234 % 1000 // 10 + 5678 % 1000 // 10

# 4th program
a, b = 13.42, 42.13
c, d = 54.39, 37.54


def check_equal(x, y):
    check1 = str(x).split('.')[0] == str(y).split('.')[1]
    check2 = str(y).split('.')[0] == str(x).split('.')[1]
    return check1 or check2


def check_equal2(x, y):
    x, y = [int(e * 100) for e in (x, y)]
    check1 = x // 100 == y % 100
    check2 = y // 100 == x % 100
    return check1 or check2


print(check_equal(a, b))
