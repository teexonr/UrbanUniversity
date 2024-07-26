# Словари и множества

my_dict = {'Имя': 'Владислав', 'Год рождения': 1999}
print('Dict:', my_dict)
print('Existing value:', my_dict['Имя'])
print('Not existing value: ', my_dict.get('Фамилия'))
my_dict['Страна'] = 'Россия'
my_dict.update({'Город': 'Ленинск-Кузнецкий'})
print('Deleted value:', my_dict.pop('Год рождения'))
print('Modified dictionary:', my_dict)

print()

my_set = {1, 1, 2, '3', 3, '3'}
print('Set:', my_set)
[my_set.add(e) for e in (4, '5')]
my_set.remove(3)
print('Modified set:', my_set)
