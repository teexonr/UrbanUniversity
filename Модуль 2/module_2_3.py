my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = -1

while (i := i + 1) < len(my_list):
    if my_list[i] == 0:
        continue
    if my_list[i] < 0:
        break

    print(my_list[i])
