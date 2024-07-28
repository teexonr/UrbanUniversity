def print_params(a: object = 1, b: object = 'строка', c: object = True) -> None:
    print(a, b, c)


print_params()
print_params(2)
print_params(2, 3)
print_params(2, 3, 4)
print_params(b=25)
print_params(c=[1, 2, 3])

print()
values_list = [2, 'строчка', False]
values_dict = {'a': 3, 'b': 'строчечка', 'c': None}
print_params(*values_list)
print_params(**values_dict)

print()
values_list_2 = [(1, 2, 3), [4, 5, 6]]
print_params(*values_list_2, 42)
