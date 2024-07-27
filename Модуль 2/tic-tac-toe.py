def draw_area(area):
    for e in area:
        print(*e)


def transpose_area(area):
    area_t = ['*']
    for i in range(len(area)):
        area_t.append([])
        for j in range(len(area[i])):
            area_t[-1].append(area[j][i])
    return area_t


def diagonal_area(area):
    area_d = ['', '']
    for i in range(len(area)):
        for j in range(len(area)):
            if i == j:
                area_d[0] += area[i][i]
                area_d[1] += area[i][-i-1]
    return area_d


def check_win(area):
    area_t = transpose_area(area)
    area_d = diagonal_area(area)
    for a in (area, area_t, area_d):
        for row in a:
            if '*' in row:
                continue
            line = set(''.join(row))
            if len(line) == 1:
                print('-' * 10, f'{list(line)[0]} win', '-' * 10)
                return 0
    if '*' not in ''.join(''.join(x) for x in area):
        print('-' * 10, 'Ничья!', '-' * 10)
        return 1
    return 2


def make_step(area, player):
    while True:
        coord = input('Введите координаты клетки (через пробел) (1, 2, 3): ')
        x, y = [int(e) - 1 for e in coord.split()]
        if area[x][y] == '*':
            break
        else:
            print('Клетка занята! Попробуйте ещё раз.')
    area[x][y] = player
    return area


def main():
    area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
    print('-' * 10, 'Крестики-нолики', '-' * 10)
    step = int(input('Кто ходит первым? (Крестики - 1, Нолики - 2): '))
    draw_area(area)
    while check_win(area):
        player = ['X', 'O'][(step - 1) % 2]
        print('\nХод', player)
        step += 1
        make_step(area, player)
        draw_area(area)


if __name__ == '__main__':
    main()
