def get_matrix(n: int, m: int, value: int) -> list:
    matrix = []
    if n < 1 or m < 1:
        return matrix

    for _ in range(n):
        matrix.append([])
        for _ in range(m):
            matrix[-1].append(value)

    return matrix


print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))
